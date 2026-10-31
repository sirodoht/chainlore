import copy
from datetime import timedelta
import json
from pathlib import Path
import smtplib
import tempfile
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.utils import timezone
from . import ai_providers as ai
from .article_validation import InvalidArticle, validate_draft
from .automation import run_worker
from .models import AutomationEvent, AutomationRun, GeneratedArticle, Submission
from .publication import publication_lock, publish_site
from .automation_control import resume_queue, retry_runs
from .models import AutomationControl

URLS = ['https://docs.example.com/design', 'https://docs.example.com/history', 'https://news.example.org/report']
RESEARCH = {'stop_reason': 'end_turn', 'content': [
    {'type': 'text', 'text': 'Research evidence for the fictional test protocol.'},
    *[{'type': 'web_fetch_tool_result', 'content': {
        'type': 'web_fetch_result', 'url': url, 'content': {'title': 'Test source', 'source': {'type': 'text', 'data': 'Example evidence'}}}} for url in URLS]]}
DRAFT = {'title': 'Test Protocol', 'slug': 'test-protocol', 'ticker': 'TEST', 'category': 'DeFi', 'markdown': '''Test Protocol is a fictional protocol used to test the publishing process. Its documentation describes a network and a set of rules for recording transactions. The example article includes references so that the validator can check their relationship with the research evidence.[^1]

| Fact | Value |
|---|---|
| Name | Test Protocol |

## History

The documentation describes the history of Test Protocol, including its initial launch and subsequent development. This paragraph is deliberately long enough to represent a short encyclopedia entry rather than an empty fixture, and attributes the description to the documentation.[^2]

## Technology

The research report describes the protocol's technical design and its limitations. This paragraph records a neutral summary of that report, with an explicit reference attached. The test verifies that citations survive rendering and that private submission fields do not appear in generated public files.[^3]

## References

[^1]: [Design](https://docs.example.com/design)
[^2]: [History](https://docs.example.com/history)
[^3]: [Report](https://news.example.org/report)
'''}


def decision(**values):
    return {'model': 'jev-test', 'answers': {key: {'choice': value, 'confidence': 0.99, 'probabilities': {value: 0.999}}
                                          for key, value in values.items()}}


def written(draft=None):
    return {'stop_reason': 'end_turn', 'content': [{'type': 'text', 'text': json.dumps(draft or DRAFT)}]}


class AutomationTests(TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.site = self.root / 'site'
        self.site.mkdir()
        (self.site / 'article-catalog.json').write_text(json.dumps({'bitcoin': {'title': 'Bitcoin', 'sections': {}}}))
        (self.site / 'build-info.json').write_text(json.dumps({'revision': 'a' * 40, 'release': 'test'}))
        override = override_settings(DATA_DIR=self.root, PUBLICATION_ROOT=self.root / 'published',
                                     SITE_ROOT=self.site, ARTICLE_CATALOG=self.site / 'article-catalog.json',
                                     AUTOMATION_ENABLED=True, AUTOMATION_DAILY_LIMIT=10, NOTIFICATIONS_ENABLED=False)
        override.enable()
        self.addCleanup(override.disable)
        self.submission = Submission.objects.create(kind='request', title='Test Protocol', email='private@example.net')
        for name, value in [('triage', decision(scope='in_scope', injection='clean', duplicate='new')),
                            ('research', RESEARCH), ('write_article', written()),
                            ('review_output', decision(suitable='yes'))]:
            mock = patch.object(ai, name, return_value=value)
            setattr(self, name, mock.start())
            self.addCleanup(mock.stop)

    def test_publish_and_deploy_preserve_generated_article_and_exclude_private_data(self):
        self.assertEqual(run_worker(), 1)
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'published')
        self.submission.refresh_from_db()
        self.assertEqual(self.submission.status, 'resolved')
        self.assertEqual(self.submission.resulting_url, 'https://chainlore.xyz/p/test-protocol/')
        current = self.root / 'published/current'
        html = (current / 'p/test-protocol/index.html').read_text()
        self.assertIn('This article is a draft', html)
        self.assertIn('Test Protocol', (current / 'all-articles/index.html').read_text())
        self.assertIn('test-protocol', json.loads((current / 'article-catalog.json').read_text()))
        self.assertTrue((current / 'p/test-protocol.md').is_file())
        self.assertNotIn(self.submission.email, ''.join(path.read_text() for path in current.rglob('*') if path.is_file()))
        first = current.resolve()
        (self.site / 'build-info.json').write_text(json.dumps({'revision': 'b' * 40, 'release': 'new-code'}))
        with publication_lock():
            publish_site(self.site)
        self.assertNotEqual(first, current.resolve())
        self.assertEqual(json.loads((current / 'build-info.json').read_text())['revision'], 'b' * 40)
        self.assertTrue((current / 'p/test-protocol/index.html').is_file())
        self.assertEqual(run_worker(), 0)
        self.write_article.assert_called_once()
        self.assertEqual(GeneratedArticle.objects.count(), 1)
        self.assertNotIn('email', run.inputs)
        self.assertTrue(run.events.filter(kind='notification', data__outcome='failed').exists())

    def test_injection_and_out_of_scope_decline_without_writer(self):
        for response in [decision(scope='in_scope', injection='injection', duplicate='new'),
                         decision(scope='out_of_scope', injection='clean', duplicate='new')]:
            self.triage.return_value = response
            run_worker()
            self.assertEqual(AutomationRun.objects.latest('pk').state, 'declined')
            Submission.objects.create(kind='request', title='Another subject')
        self.research.assert_not_called()
        self.write_article.assert_not_called()

    def test_uncertainty_or_bad_response_never_approves(self):
        self.triage.return_value = {'answers': {}}
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.research.assert_not_called()

    def test_duplicate_resolves_without_spending(self):
        self.submission.title = 'BITCOIN'
        self.submission.save()
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'duplicate')
        self.triage.assert_not_called()

    def test_retries_resume_research_checkpoint_and_are_bounded(self):
        self.write_article.side_effect = ai.ProviderError('anthropic_http_429', True)
        run_worker()
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'retry')
        self.assertEqual(run_worker(), 0)
        for attempt in range(2):
            AutomationRun.objects.update(next_attempt_at=timezone.now() - timedelta(seconds=1))
            run_worker()
        run.refresh_from_db()
        self.assertEqual(run.state, 'failed')
        self.assertEqual(run.attempts, 3)
        self.research.assert_called_once()
        self.assertEqual(self.write_article.call_count, 3)

    def test_validation_failure_never_publishes(self):
        draft = {**DRAFT, 'markdown': DRAFT['markdown'] + '<script>alert(1)</script>'}
        self.write_article.return_value = written(draft)
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.assertFalse(GeneratedArticle.objects.exists())
        self.review_output.assert_not_called()

    def test_unapproved_output_never_publishes(self):
        self.review_output.return_value = decision(suitable='no')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.assertFalse(GeneratedArticle.objects.exists())

    def test_disabled_daily_limit_and_process_lock(self):
        with override_settings(AUTOMATION_ENABLED=False):
            self.assertEqual(run_worker(), 0)
        with override_settings(AUTOMATION_DAILY_LIMIT=0):
            self.assertEqual(run_worker(), 0)
        with publication_lock():
            self.assertEqual(run_worker(), 0)
        self.assertFalse(AutomationRun.objects.exists())

    def test_publication_failure_resumes_without_regenerating(self):
        with patch('submissions.automation.publish_site', side_effect=OSError('disk issue')):
            run_worker()
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'retry')
        self.assertEqual(GeneratedArticle.objects.count(), 1)
        AutomationRun.objects.update(next_attempt_at=timezone.now() - timedelta(seconds=1))
        run_worker()
        run.refresh_from_db()
        self.assertEqual(run.state, 'published')
        self.write_article.assert_called_once()

    def test_failed_rebuild_keeps_active_publication_intact(self):
        run_worker()
        current = self.root / 'published/current'
        previous = current.resolve()
        with patch('submissions.publication.subprocess.run') as build:
            build.return_value.returncode = 1
            with publication_lock(), self.assertRaisesRegex(ValueError, 'site_build_failed'):
                publish_site()
        self.assertEqual(current.resolve(), previous)
        self.assertTrue((current / 'p/test-protocol/index.html').is_file())

    def test_notifications_retry_three_times_without_regenerating(self):
        self.submission.title = 'Bitcoin'
        self.submission.save()
        with override_settings(NOTIFICATIONS_ENABLED=True), patch('submissions.notify.notify', side_effect=smtplib.SMTPException('private failure')) as send:
            for _ in range(5):
                AutomationRun.objects.update(notification_retry_at=timezone.now() - timedelta(seconds=1))
                run_worker()
        self.assertEqual(send.call_count, 3)
        self.assertEqual(AutomationEvent.objects.filter(kind='notification').count(), 3)
        self.triage.assert_not_called()
        self.assertNotIn('private failure', json.dumps(list(AutomationEvent.objects.values_list('data', flat=True))))

    def test_manual_decision_during_generation_prevents_publication(self):
        def review(run):
            Submission.objects.filter(pk=self.submission.pk).update(status='declined')
            return decision(suitable='yes')
        self.review_output.side_effect = review
        run_worker()
        self.assertFalse(GeneratedArticle.objects.exists())
        self.submission.refresh_from_db()
        self.assertEqual(self.submission.status, 'declined')

    def test_audit_is_private_and_read_only_in_admin(self):
        run = AutomationRun.objects.create(submission=self.submission)
        self.assertEqual(self.client.get('/admin/submissions/automationrun/').status_code, 302)
        user = get_user_model().objects.create_superuser('operator', password='test password')
        self.client.force_login(user)
        response = self.client.get(f'/admin/submissions/automationrun/{run.pk}/change/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.post(f'/admin/submissions/automationrun/{run.pk}/change/', {'state': 'published'}).status_code, 403)

    def test_account_failure_pauses_queue_without_spending_attempts_or_advancing(self):
        second = Submission.objects.create(kind='request', title='Another request')
        self.research.side_effect = ai.ProviderError('anthropic_http_401', account_problem=True)
        with override_settings(NOTIFICATIONS_ENABLED=True, ADMIN_NOTIFICATION_EMAIL='admin@example.com'), patch('submissions.automation_control.notify_provider_problem') as alert:
            run_worker()
            for _ in range(3):
                self.assertEqual(run_worker(), 0)
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'blocked')
        self.assertEqual(run.attempts, 0)
        self.assertTrue(run.triage)
        self.assertTrue(AutomationControl.objects.get().paused)
        second.refresh_from_db()
        self.assertEqual(second.status, 'new')
        self.assertEqual(AutomationRun.objects.count(), 1)
        alert.assert_called_once()
        self.triage.assert_called_once()
        self.research.assert_called_once()

        # Recovery continues from the completed triage without a database edit.
        self.research.side_effect = None
        self.assertEqual(resume_queue(actor_id=123), 1)
        run_worker()
        run.refresh_from_db()
        self.assertEqual(run.state, 'published')
        self.assertEqual(run.attempts, 1)
        self.triage.assert_called_once()
        self.assertTrue(run.events.filter(kind='queue_resumed', data__actor_id=123).exists())

    def test_repeated_account_failure_fails_the_run_and_releases_the_queue(self):
        second = Submission.objects.create(kind='request', title='Another request')
        self.research.side_effect = [ai.ProviderError('anthropic_http_400', account_problem=True),
                                     ai.ProviderError('anthropic_http_400', account_problem=True), RESEARCH]
        self.write_article.return_value = written({**DRAFT, 'title': 'Another Request', 'slug': 'another-request'})
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'blocked')
        resume_queue(actor_id=1)
        run_worker()
        first = AutomationRun.objects.get(submission=self.submission)
        self.assertEqual(first.state, 'failed')
        self.assertEqual(first.last_error, 'anthropic_http_400')
        self.assertFalse(AutomationControl.objects.get().paused)
        run_worker()
        self.assertEqual(AutomationRun.objects.get(submission=second).state, 'published')
        self.assertEqual(self.research.call_count, 3)

    def test_failed_queue_alert_is_audited_and_retried_without_provider_calls(self):
        self.triage.side_effect = ai.ProviderError('jev_http_401', account_problem=True)
        with override_settings(NOTIFICATIONS_ENABLED=True, ADMIN_NOTIFICATION_EMAIL='admin@example.com'), patch('submissions.automation_control.notify_provider_problem', side_effect=smtplib.SMTPException('private mail error')) as alert:
            run_worker()
            run_worker()
            self.assertEqual(alert.call_count, 1)
            for _ in range(4):
                AutomationControl.objects.update(alert_retry_at=timezone.now() - timedelta(seconds=1))
                run_worker()
        self.assertEqual(alert.call_count, 3)
        self.triage.assert_called_once()
        self.assertEqual(AutomationEvent.objects.filter(kind='queue_alert', data__outcome='failed').count(), 3)
        self.assertNotIn('private mail error', json.dumps(list(AutomationEvent.objects.values_list('data', flat=True))))

    def test_admin_can_resume_and_retry_but_cannot_edit_audit_records(self):
        from django.contrib.auth.models import Permission
        self.triage.side_effect = ai.ProviderError('jev_http_401', account_problem=True)
        run_worker()
        control = AutomationControl.objects.get()
        reader = get_user_model().objects.create_user('reader', is_staff=True)
        reader.user_permissions.add(Permission.objects.get(codename='view_automationcontrol'))
        self.client.force_login(reader)
        url = '/admin/submissions/automationcontrol/'
        self.client.post(url, {'action': 'resume', '_selected_action': [str(control.pk)]})
        control.refresh_from_db()
        self.assertTrue(control.paused)
        operator = get_user_model().objects.create_superuser('queue-operator', password='test password')
        self.client.force_login(operator)
        self.assertContains(self.client.get(url), 'Resume queue after fixing provider settings')
        self.client.post(url, {'action': 'resume', '_selected_action': [str(control.pk)]})
        control.refresh_from_db()
        self.assertFalse(control.paused)
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'queued')
        run.state = 'failed'
        run.attempts = 3
        run.research_session = {'checkpoint': 'keep'}
        run.save()
        self.client.post('/admin/submissions/automationrun/', {'action': 'retry_failed', '_selected_action': [str(run.pk)]})
        run.refresh_from_db()
        self.assertEqual(run.state, 'queued')
        self.assertEqual(run.attempts, 0)
        self.assertEqual(run.research_session, {'checkpoint': 'keep'})
        self.assertTrue(run.events.filter(kind='operator_retry').exists())

    def test_recovery_respects_lock_and_never_requeues_a_published_article(self):
        run = AutomationRun.objects.create(submission=self.submission, state='published')
        self.assertEqual(retry_runs([run.pk], actor_id=1), 0)
        with publication_lock(), self.assertRaises(BlockingIOError):
            resume_queue(actor_id=1)

    def test_restart_review_explicitly_clears_stages_but_keeps_audit(self):
        run = AutomationRun.objects.create(submission=self.submission, state='review', attempts=3,
                                           triage={'old': True}, research_session={'old': True},
                                           research=RESEARCH, draft={'insufficient_evidence': True})
        AutomationEvent.objects.create(run=run, kind='decision', data={'reason': 'previous_hold'})
        self.assertEqual(retry_runs([run.pk], actor_id=7, restart=True), 1)
        run.refresh_from_db()
        self.assertEqual(run.state, 'queued')
        self.assertEqual(run.attempts, 0)
        self.assertEqual(run.research_session, {})
        self.assertEqual(run.triage, {})
        self.assertTrue(run.events.filter(kind='decision', data__reason='previous_hold').exists())


class ValidationTests(TestCase):
    def test_unsafe_and_unfounded_articles_rejected(self):
        for replacement in [
            {'slug': '../../private'}, {'title': '<img src=x>'}, {'ticker': 'TEST\nstatus: human-reviewed'},
            {'markdown': DRAFT['markdown'] + '\n<script>alert(1)</script>'},
            {'markdown': DRAFT['markdown'].replace(URLS[0], 'javascript:alert(1)')},
            {'markdown': DRAFT['markdown'].replace(URLS[0], 'https://unknown.example.com/source')},
            {'markdown': DRAFT['markdown'] + '\n[click](https://example.com)'},
            {'markdown': DRAFT['markdown'] + '\n![track](https://example.com/pixel)'},
            {'markdown': DRAFT['markdown'].replace('[^3]', '[^4]', 1)},
            {'markdown': DRAFT['markdown'] + '\nsecret@example.com'},
            {'markdown': DRAFT['markdown'].replace('[^1]', '', 1)},
        ]:
            with self.subTest(replacement=list(replacement)):
                with self.assertRaises(InvalidArticle):
                    validate_draft({**DRAFT, **replacement}, RESEARCH)

    def test_only_opened_pages_count_as_evidence(self):
        evidence = copy.deepcopy(RESEARCH)
        evidence['content'] = evidence['content'][:1]
        evidence['content'][0]['text'] = json.dumps(URLS)
        evidence['content'].append({'type': 'web_search_tool_result', 'content': [
            {'type': 'web_search_result', 'url': url} for url in URLS]})
        with self.assertRaises(InvalidArticle):
            validate_draft(DRAFT, evidence)

    def test_confidence_requires_valid_probability_and_confidence(self):
        for answer in [{}, {'choice': 'yes', 'confidence': 0.99},
                       {'choice': 'yes', 'confidence': '1', 'probabilities': {'yes': 1}},
                       {'choice': 'yes', 'confidence': 0.99, 'probabilities': {'yes': float('nan')}}]:
            self.assertFalse(ai.confident({'answers': {'suitable': answer}}, 'suitable', 'yes'))

    def test_failed_fetch_is_not_evidence(self):
        evidence = copy.deepcopy(RESEARCH)
        evidence['content'][-1]['content']['type'] = 'web_fetch_tool_result_error'
        with self.assertRaises(InvalidArticle):
            validate_draft(DRAFT, evidence)

    def test_research_handoff_keeps_fetched_sources_and_discards_encrypted_payloads(self):
        research = copy.deepcopy(RESEARCH)
        research['content'][1]['content']['content']['source']['data'] = 'x' * 7000 + 'Important evidence at the end'
        research['content'].append({'type': 'web_search_tool_result', 'content': [
            {'type': 'web_search_result', 'url': URLS[0], 'encrypted_content': 'opaque ciphertext'}]})
        context = ai.research_context(research)
        self.assertEqual({item['url'] for item in context['opened_sources']}, set(URLS))
        self.assertNotIn('opaque ciphertext', json.dumps(context))
        self.assertTrue(context['opened_sources'][0]['text'].endswith('Important evidence at the end'))

    def test_unreadable_pdf_and_empty_fetch_cannot_count_as_writer_evidence(self):
        for source in [{'type': 'base64', 'data': 'cGRm'}, {'type': 'text', 'data': ''}]:
            evidence = copy.deepcopy(RESEARCH)
            evidence['content'][-1]['content']['content']['source'] = source
            self.assertEqual(len(ai.research_context(evidence)['opened_sources']), 2)
            with self.assertRaises(InvalidArticle):
                validate_draft(DRAFT, evidence)
