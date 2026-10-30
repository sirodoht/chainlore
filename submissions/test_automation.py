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

URLS = ['https://docs.example.com/design', 'https://docs.example.com/history', 'https://news.example.org/report']
RESEARCH = {'stop_reason': 'end_turn', 'content': [
    {'type': 'text', 'text': 'Research evidence for the fictional test protocol.'},
    {'type': 'web_search_tool_result', 'content': [
        {'type': 'web_search_result', 'url': url, 'title': 'Test source'} for url in URLS]}]}
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

    def test_only_search_results_count_as_evidence(self):
        evidence = copy.deepcopy(RESEARCH)
        evidence['content'][-1]['content'] = []
        evidence['content'][0]['text'] = json.dumps(URLS)
        with self.assertRaises(InvalidArticle):
            validate_draft(DRAFT, evidence)

    def test_confidence_requires_valid_probability_and_confidence(self):
        for answer in [{}, {'choice': 'yes', 'confidence': 0.99},
                       {'choice': 'yes', 'confidence': '1', 'probabilities': {'yes': 1}},
                       {'choice': 'yes', 'confidence': 0.99, 'probabilities': {'yes': float('nan')}}]:
            self.assertFalse(ai.confident({'answers': {'suitable': answer}}, 'suitable', 'yes'))
