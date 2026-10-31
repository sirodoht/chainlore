import copy
import io
import json
import os
from pathlib import Path
import tempfile
import urllib.error
from unittest.mock import patch
from django.test import TestCase, override_settings
from . import ai_providers as ai
from .article_validation import evidence_urls
from .models import AutomationEvent, AutomationRun, Submission


def fetched(url):
    return {'type': 'web_fetch_tool_result', 'tool_use_id': 'tool-' + url.rsplit('/', 1)[-1], 'content': {
        'type': 'web_fetch_result', 'url': url, 'content': {'title': 'Source', 'source': {'type': 'text', 'data': 'Full evidence'}}}}


class ProviderTests(TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        override = override_settings(DATA_DIR=self.root)
        override.enable()
        self.addCleanup(override.disable)
        self.run = AutomationRun.objects.create(submission=Submission.objects.create(kind='request', title='Example'), inputs={'title': 'Example'})
        self.pause = {'id': 'part-1', 'model': 'claude-haiku-5-5', 'stop_reason': 'pause_turn',
                      'content': [fetched('https://docs.example.com/first'),
                                  {'type': 'server_tool_use', 'id': 'pending', 'name': 'web_fetch', 'input': {'url': 'https://docs.example.com/second'}}],
                      'container': {'id': 'container-1'},
                      'usage': {'input_tokens': 100, 'output_tokens': 20, 'server_tool_use': {'web_search_requests': 6, 'web_fetch_requests': 4}}}
        self.end = {'id': 'part-2', 'model': 'claude-haiku-5-5', 'stop_reason': 'end_turn',
                    'content': [fetched('https://docs.example.com/second'), fetched('https://news.example.org/third'), {'type': 'text', 'text': 'Completed research.'}],
                    'usage': {'input_tokens': 150, 'output_tokens': 30, 'server_tool_use': {'web_search_requests': 2, 'web_fetch_requests': 2}}}
        self.end['content'][0]['tool_use_id'] = 'pending'

    def test_pause_continues_exact_assistant_content_and_merges_all_evidence(self):
        with patch.object(ai, 'call', side_effect=[self.pause, self.end]) as call:
            result = ai.research(self.run)
        self.assertEqual(call.call_count, 2)
        payload = call.call_args_list[1].args[3]
        self.assertEqual(payload['messages'][-1], {'role': 'assistant', 'content': self.pause['content']})
        self.assertEqual(payload['container'], 'container-1')
        self.assertEqual([tool['max_uses'] for tool in payload['tools']], [2, 2])
        self.assertEqual(call.call_args_list[0].kwargs['timeout'], 300)
        self.assertEqual(result['stop_reason'], 'end_turn')
        self.assertEqual(len(evidence_urls(result)), 3)
        self.assertEqual(len(ai.research_context(result)['opened_sources']), 3)
        self.assertEqual(result['usage']['input_tokens'], 250)
        self.assertEqual(result['usage']['server_tool_use']['web_search_requests'], 8)
        self.run.refresh_from_db()
        self.assertEqual(len(self.run.research_session['responses']), 2)

    def test_failed_continuation_reuses_saved_paid_work_after_restart(self):
        with patch.object(ai, 'call', side_effect=[self.pause, ai.ProviderError('anthropic_network_error', True)]):
            with self.assertRaises(ai.ProviderError):
                ai.research(self.run)
        resumed = AutomationRun.objects.get(pk=self.run.pk)
        self.assertEqual(len(resumed.research_session['responses']), 1)
        with patch.object(ai, 'call', return_value=self.end) as call:
            result = ai.research(resumed)
        call.assert_called_once()
        self.assertEqual(call.call_args.args[3]['messages'][-1]['content'], self.pause['content'])
        self.assertEqual(len(evidence_urls(result)), 3)

    def test_continuation_cap_is_durable_and_tool_budget_never_resets(self):
        second = {**copy.deepcopy(self.end), 'stop_reason': 'pause_turn'}
        with patch.object(ai, 'call', side_effect=[self.pause, second, second]) as call:
            result = ai.research(self.run)
        self.assertEqual(call.call_count, 3)
        self.assertEqual(call.call_args.args[3]['tools'], [])
        self.assertEqual(result['stop_reason'], 'pause_turn')
        self.run.refresh_from_db()
        with patch.object(ai, 'call') as call:
            ai.research(self.run)
        call.assert_not_called()

    def test_unfinished_call_beyond_budget_stops_without_an_invalid_provider_request(self):
        paused = copy.deepcopy(self.pause)
        paused['usage']['server_tool_use']['web_fetch_requests'] = 6
        with patch.object(ai, 'call', return_value=paused) as call:
            result = ai.research(self.run)
        call.assert_called_once()
        self.assertEqual(result['continuation_stop'], 'tool_budget_exhausted')

    def test_exhausted_search_is_removed_while_pending_fetch_continues(self):
        paused = copy.deepcopy(self.pause)
        paused['usage']['server_tool_use']['web_search_requests'] = 8
        with patch.object(ai, 'call', side_effect=[paused, self.end]) as call:
            ai.research(self.run)
        tools = call.call_args.args[3]['tools']
        self.assertEqual([(tool['name'], tool['max_uses']) for tool in tools], [('web_fetch', 2)])

    def test_completed_checkpoint_does_not_repeat_paid_call(self):
        with patch.object(ai, 'call', return_value=self.end):
            ai.research(self.run)
        self.run.refresh_from_db()
        with patch.object(ai, 'call') as call:
            result = ai.research(self.run)
        call.assert_not_called()
        self.assertEqual(result['stop_reason'], 'end_turn')

    def test_auth_billing_and_configuration_errors_are_sanitized_queue_problems(self):
        for status, detail in [(400, 'credit balance too low'), (401, 'bad credential'),
                               (402, 'billing'), (403, 'permission'), (404, 'model missing'),
                               (429, 'monthly spend cap reached')]:
            with self.subTest(status=status):
                error = urllib.error.HTTPError('https://api.anthropic.com/v1/messages', status, 'error', {},
                                               io.BytesIO(json.dumps({'error': {'message': detail + ' secret echoed by provider'}}).encode()))
                with patch.object(ai, 'credential', return_value='not-a-real-secret'), patch.object(ai.urllib.request, 'urlopen', side_effect=error):
                    with self.assertRaises(ai.ProviderError) as raised:
                        ai.call(self.run, 'anthropic', 'research', {'model': 'test'}, timeout=300)
                self.assertTrue(raised.exception.account_problem)
                self.assertFalse(raised.exception.retryable)
                self.assertNotIn('secret', str(raised.exception))
        self.assertNotIn('secret', json.dumps(list(AutomationEvent.objects.values_list('data', flat=True))))

    def test_rate_limit_and_server_errors_remain_retryable(self):
        for status in (429, 500, 529):
            error = urllib.error.HTTPError('https://api.typesafe.ai/v1/systemone', status, 'error', {'retry-after': '10'}, io.BytesIO(b'{"error":"temporarily unavailable"}'))
            with patch.object(ai, 'credential', return_value='test'), patch.object(ai.urllib.request, 'urlopen', side_effect=error):
                with self.assertRaises(ai.ProviderError) as raised:
                    ai.call(self.run, 'jev', 'triage', {})
            self.assertTrue(raised.exception.retryable)
            self.assertFalse(raised.exception.account_problem)

    def test_missing_key_pauses_without_making_a_request(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(ai.urllib.request, 'urlopen') as transport:
            with self.assertRaises(ai.ProviderError) as raised:
                ai.call(self.run, 'jev', 'triage', {})
        self.assertTrue(raised.exception.account_problem)
        transport.assert_not_called()

    def test_research_transport_uses_extended_timeout(self):
        with patch.object(ai, 'credential', return_value='test'), patch.object(ai.urllib.request, 'urlopen') as transport:
            transport.return_value.__enter__.return_value.read.return_value = json.dumps(self.end).encode()
            ai.research(self.run)
        self.assertEqual(transport.call_args.kwargs['timeout'], 300)
