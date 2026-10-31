import copy
from datetime import timedelta
import json
from pathlib import Path
import smtplib
import tempfile
from types import SimpleNamespace
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase, override_settings
from django.utils import timezone
from . import ai_providers as ai
from .article_validation import InvalidArticle, stub_draft, validate_draft
from .automation import deliver_notifications, run_worker
from .models import AutomationEvent, AutomationRun, GeneratedArticle, Submission
from .publication import index_generated_articles, publication_lock, publish_site
from .automation_control import regenerate_placeholders, resume_queue, retry_runs
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


STUB = {**DRAFT, 'markdown': '''Test Protocol is a fictional protocol described by a single weak source, which states that it records transactions on a small network. No other details about its history, governance or token could be established from the evidence that was retrieved for this draft.[^1]

## References

[^1]: [Design](https://docs.example.com/design)
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
        index = (current / 'sources/INDEX.md').read_text()
        self.assertIn('- [Test Protocol](pages/test-protocol.md)', index.split('## Decentralised finance')[1].split('## ')[0])
        self.assertNotIn('Requested articles', index)
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
        self.assertEqual((current / 'sources/INDEX.md').read_text().count('](pages/test-protocol.md)'), 1)
        self.assertEqual(run_worker(), 0)
        self.write_article.assert_called_once()
        self.assertEqual(GeneratedArticle.objects.count(), 1)
        self.assertNotIn('email', run.inputs)
        self.assertTrue(run.events.filter(kind='notification', data__outcome='failed').exists())

    def test_generated_exchange_joins_existing_exchange_lists(self):
        self.write_article.return_value = written({**DRAFT, 'title': 'Binance', 'slug': 'binance', 'category': 'Exchange'})
        run_worker()
        current = self.root / 'published/current'
        index = (current / 'sources/INDEX.md').read_text()
        exchanges = index.split('## Exchanges')[1].split('## ')[0]
        self.assertIn('](pages/ftx.md)', exchanges)
        self.assertIn('](pages/binance.md)', exchanges)
        for path in ('index.html', 'all-articles/index.html'):
            html = (current / path).read_text()
            self.assertNotIn('Requested articles', html)
            heading = 'h3' if path == 'index.html' else 'h2'
            exchanges = html.split(f'>Exchanges</{heading}>')[1].split(f'<{heading}')[0]
            self.assertIn('href="/p/ftx/"', exchanges)
            self.assertIn('href="/p/binance/"', exchanges)

    def test_injection_and_out_of_scope_decline_without_writer(self):
        for response in [decision(scope='in_scope', injection='injection', duplicate='new'),
                         decision(scope='out_of_scope', injection='clean', duplicate='new')]:
            self.triage.return_value = response
            run_worker()
            self.assertEqual(AutomationRun.objects.latest('pk').state, 'declined')
            Submission.objects.create(kind='request', title='Another subject')
        self.research.assert_not_called()
        self.write_article.assert_not_called()

    def test_missing_screening_result_requires_review(self):
        self.triage.return_value = {'answers': {}}
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.assertEqual(AutomationRun.objects.get().last_error, 'triage_invalid_response')
        self.research.assert_not_called()

    def test_satoshi_screening_scores_proceed_to_a_published_people_article(self):
        self.submission.title = 'satoshi nakamoto'
        self.submission.save()
        self.triage.return_value = {'answers': {
            'scope': {'choice': 'out_of_scope', 'confidence': 0.26,
                      'probabilities': {'in_scope': 0.38, 'out_of_scope': 0.51, 'unclear': 0.11}},
            'injection': {'choice': 'clean', 'confidence': 1.0, 'probabilities': {'clean': 1.0}},
            'duplicate': {'choice': 'new', 'confidence': 0.7, 'probabilities': {'new': 0.8}},
        }}
        self.write_article.return_value = written({**DRAFT, 'title': 'Satoshi Nakamoto',
                                                  'slug': 'satoshi-nakamoto', 'category': 'Person'})
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.research.assert_called_once()
        current = self.root / 'published/current'
        self.assertTrue((current / 'p/satoshi-nakamoto/index.html').is_file())
        index = (current / 'sources/INDEX.md').read_text()
        self.assertIn('](pages/satoshi-nakamoto.md)', index.split('## People')[1].split('## ')[0])

    def test_uncertain_scope_and_injection_allow_research(self):
        self.triage.return_value = {'answers': {
            name: {'choice': 'unclear', 'confidence': 0.2, 'probabilities': {'unclear': 0.4}}
            for name in ('scope', 'injection')
        }}
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.research.assert_called_once()

    def test_model_duplicate_prediction_does_not_block_a_distinct_subject(self):
        self.triage.return_value = decision(scope='in_scope', injection='clean', duplicate='duplicate')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')

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

    def test_reused_footnotes_publish_without_a_rewrite(self):
        reused = DRAFT['markdown'].replace('attributes the description to the documentation.[^2]',
                                           'attributes the description to the documentation.[^1][^2]')
        self.assertNotEqual(reused, DRAFT['markdown'])
        self.write_article.return_value = written({**DRAFT, 'markdown': reused})
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.write_article.assert_called_once()
        self.assertNotIn('This is a placeholder', GeneratedArticle.objects.get().markdown)
        html = (self.root / 'published/current/p/test-protocol/index.html').read_text()
        self.assertIn('fnref2:1', html)
        self.assertNotIn('↩', html)
        self.assertRegex(html, r'id="fn:1">\s*<p><span class="backlinks">\^ <a [^>]*href="#fnref:1"[^>]*><sup>a</sup></a> <a [^>]*href="#fnref2:1"[^>]*><sup>b</sup></a>')
        self.assertRegex(html, r'id="fn:2">\s*<p><span class="backlinks"><a [^>]*href="#fnref:2"[^>]*>\^</a></span> <a href="https://docs.example.com/history"')

    def test_rejected_draft_is_retried_with_the_reason(self):
        bad = {**DRAFT, 'markdown': DRAFT['markdown'] + '<script>alert(1)</script>'}
        self.write_article.side_effect = [written(bad), written()]
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.assertEqual(self.write_article.call_args.args[1], 'unsafe_markdown')
        self.assertIn('Test Protocol is a fictional protocol', GeneratedArticle.objects.get().markdown)

    def test_unsafe_drafts_are_discarded_for_a_placeholder(self):
        bad = {**DRAFT, 'markdown': DRAFT['markdown'] + '<script>alert(1)</script>'}
        self.write_article.return_value = written(bad)
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.assertEqual(self.write_article.call_count, 2)
        article = GeneratedArticle.objects.get()
        self.assertIn('This is a placeholder', article.markdown)
        self.assertNotIn('alert(1)', article.markdown)
        self.assertIn('This article is a draft', (self.root / 'published/current/p/test-protocol/index.html').read_text())
        self.review_output.assert_called_once()

    def publish_placeholder(self):
        self.write_article.side_effect = ai.ProviderError('research_context_too_large')
        run_worker()
        # A live deployment's catalog lists the page, so the run must not see itself as a duplicate.
        (self.site / 'article-catalog.json').write_text(json.dumps({
            'bitcoin': {'title': 'Bitcoin', 'sections': {}}, 'test-protocol': {'title': 'Test Protocol', 'sections': {}}}))
        self.write_article.side_effect = None
        run = AutomationRun.objects.get()
        self.assertIn('This is a placeholder', run.generated_article.markdown)
        return run

    def test_regenerating_replaces_a_placeholder_with_the_full_article(self):
        run = self.publish_placeholder()
        page = self.root / 'published/current/p/test-protocol/index.html'
        self.assertEqual(regenerate_placeholders([run.pk], actor_id=7), 1)
        self.assertIn('This is a placeholder', page.read_text())
        run_worker()
        run.refresh_from_db()
        self.assertEqual(run.state, 'published')
        self.assertNotIn('This is a placeholder', GeneratedArticle.objects.get().markdown)
        self.assertNotIn('This is a placeholder', page.read_text())
        self.assertIn('fictional protocol', page.read_text())
        self.submission.refresh_from_db()
        self.assertEqual(self.submission.status, 'resolved')
        self.assertEqual(self.submission.resulting_url, 'https://chainlore.xyz/p/test-protocol/')
        self.assertEqual(self.research.call_count, 2)
        self.triage.assert_called_once()
        self.assertTrue(run.events.filter(kind='operator_regenerate', data__actor_id=7).exists())

    def test_failed_regeneration_leaves_the_placeholder_live_and_regenerable(self):
        run = self.publish_placeholder()
        regenerate_placeholders([run.pk], actor_id=7)
        self.review_output.return_value = decision(suitable='no')
        run_worker()
        run.refresh_from_db()
        self.assertEqual(run.state, 'review')
        self.assertIn('This is a placeholder', GeneratedArticle.objects.get().markdown)
        with publication_lock():
            publish_site()
        self.assertIn('This is a placeholder', (self.root / 'published/current/p/test-protocol/index.html').read_text())
        self.assertEqual(regenerate_placeholders([run.pk], actor_id=7), 1)

    def test_regenerate_ignores_full_articles_and_respects_a_paused_queue(self):
        run_worker()
        run = AutomationRun.objects.get()
        self.assertEqual(regenerate_placeholders([run.pk], actor_id=7), 0)
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        AutomationControl.objects.update_or_create(pk=1, defaults={'paused': True})
        with self.assertRaises(ValueError):
            regenerate_placeholders([run.pk], actor_id=7)

    def test_admin_action_regenerates_a_placeholder(self):
        run = self.publish_placeholder()
        self.client.force_login(get_user_model().objects.create_superuser('placeholder-operator', password='test password'))
        self.client.post('/admin/submissions/automationrun/', {'action': 'regenerate_placeholder', '_selected_action': [str(run.pk)]})
        run.refresh_from_db()
        self.assertEqual(run.state, 'queued')

    def test_non_retryable_writer_error_publishes_a_placeholder(self):
        self.write_article.side_effect = ai.ProviderError('research_context_too_large')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.assertEqual(self.write_article.call_count, 1)

    def test_writer_account_error_still_pauses_the_queue(self):
        self.write_article.side_effect = ai.ProviderError('anthropic_http_401', account_problem=True)
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'blocked')
        self.assertFalse(GeneratedArticle.objects.exists())

    def test_jev_uncertainty_does_not_stop_a_page(self):
        self.review_output.return_value = decision(suitable='unclear')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')

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

    @override_settings(NOTIFICATIONS_ENABLED=True, EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_notifications_filter_completed_recipients_before_batch_limit(self):
        from django.core import mail
        skipped = []
        for index in range(12):
            submission = Submission.objects.create(
                kind='request', title=f'Old request {index}', status='reviewing' if index % 3 == 2 else 'resolved',
                email='' if index % 3 == 0 else 'done@example.net',
                notified_status='resolved' if index % 3 == 1 else '',
            )
            skipped.append(AutomationRun.objects.create(submission=submission, state='published').pk)
        for index in range(11):
            submission = Submission.objects.create(kind='request', title=f'Pending request {index}',
                                                   status='resolved', email='pending@example.net')
            AutomationRun.objects.create(submission=submission, state='published')
        deliver_notifications()
        self.assertEqual(len(mail.outbox), 10)
        deliver_notifications()
        self.assertEqual(len(mail.outbox), 11)
        deliver_notifications()
        self.assertEqual(len(mail.outbox), 11)
        self.assertFalse(AutomationRun.objects.filter(pk__in=skipped, notification_attempts__gt=0).exists())
        self.assertEqual(Submission.objects.filter(email='pending@example.net', notified_status='resolved').count(), 11)

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

    def test_single_weak_source_still_publishes_a_labelled_stub(self):
        self.research.return_value = {'stop_reason': 'end_turn', 'content': RESEARCH['content'][:2]}
        self.write_article.return_value = written(STUB)
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        html = (self.root / 'published/current/p/test-protocol/index.html').read_text()
        self.assertIn('This article is a draft', html)

    def test_research_cut_short_still_publishes_from_fetched_sources(self):
        for stop_reason in ['pause_turn', 'max_tokens']:
            with self.subTest(stop_reason=stop_reason):
                self.research.return_value = {**RESEARCH, 'stop_reason': stop_reason}
                run_worker()
                self.assertEqual(AutomationRun.objects.latest('pk').state, 'published')
                GeneratedArticle.objects.all().delete()
                Submission.objects.create(kind='request', title='Test Protocol')

    def test_refused_or_sourceless_research_still_gets_a_placeholder_page(self):
        self.submission.title = 'binance'
        self.submission.save()
        for slug, research in [('binance', {'stop_reason': 'refusal', 'content': []}),
                               ('binance', {'stop_reason': 'end_turn', 'content': RESEARCH['content'][:1]})]:
            self.research.return_value = research
            run_worker()
            self.assertEqual(AutomationRun.objects.latest('pk').state, 'published')
            article = GeneratedArticle.objects.get()
            self.assertEqual((article.slug, article.title), (slug, 'Binance'))
            self.assertIn('This is a placeholder', article.markdown)
            article.delete()
            Submission.objects.create(kind='request', title='binance')
        self.write_article.assert_not_called()

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


class IndexCategoryTests(SimpleTestCase):
    def record(self, slug, category):
        return SimpleNamespace(slug=slug, title=slug.title(), markdown=f'---\ntitle: {slug.title()}\ncategory: {category}\n---\n\nBody.\n')

    def test_categories_map_to_subjects_and_rebuilds_do_not_duplicate_links(self):
        categories = {
            'Layer 1': 'Layer 1 blockchains', 'Layer 2': 'Layer 2 networks',
            'Stablecoin': 'Stablecoins', 'DeFi': 'Decentralised finance',
            'Exchange': 'Exchanges', 'Regulation': 'Legislation',
            'Infrastructure': 'Infrastructure', 'Other': 'Other topics',
            'Person': 'People', 'Organisation': 'Organisations', 'Event': 'Events', 'Concept': 'Concepts',
        }
        records = [self.record(f'article-{i}', category) for i, category in enumerate(categories)]
        index = index_generated_articles('# Index\n', records)
        for record, heading in zip(records, categories.values()):
            section = index.split(f'## {heading}\n')[1].split('## ')[0]
            self.assertIn(f'](pages/{record.slug}.md)', section)
        self.assertEqual(index_generated_articles(index, records), index)

    def test_curated_text_and_manual_placement_are_preserved(self):
        index = '# Index\n\n## Exchanges\n\n- [FTX](pages/ftx.md): a curated\n  multiline summary.\n\n## Infrastructure\n\n- [Manual](pages/manual.md): editorial placement.\n'
        result = index_generated_articles(index, [self.record('binance', 'Exchange'), self.record('manual', 'Other')])
        self.assertIn('- [FTX](pages/ftx.md): a curated\n  multiline summary.\n- [Binance](pages/binance.md)\n\n## Infrastructure', result)
        self.assertIn('## Infrastructure\n\n- [Manual](pages/manual.md): editorial placement.', result)
        self.assertNotIn('## Other topics', result)

    def test_unknown_or_missing_metadata_uses_other_topics_not_body_text(self):
        records = [self.record('unknown', 'Unrecognised'), self.record('missing', 'Exchange')]
        records[1].markdown = 'Body text\ncategory: Exchange\n'
        result = index_generated_articles('# Index\n', records)
        self.assertEqual(result.count('## Other topics'), 1)
        self.assertNotIn('## Exchanges', result)
        self.assertIn('](pages/unknown.md)', result)
        self.assertIn('](pages/missing.md)', result)


class ValidationTests(TestCase):
    def test_malformed_screening_results_are_not_treated_as_uncertainty(self):
        for replacement in [None, {}, {'choice': 'unknown'},
                            {'choice': 'clean', 'confidence': True, 'probabilities': {'clean': 1}},
                            {'choice': 'clean', 'confidence': 1, 'probabilities': {'clean': float('nan')}},
                            {'choice': 'clean', 'confidence': 1, 'probabilities': {'clean': 2}},
                            {'choice': 'clean', 'confidence': 1, 'probabilities': []}]:
            with self.subTest(replacement=replacement):
                result = decision(scope='in_scope', injection='clean')
                result['answers']['injection'] = replacement
                self.assertFalse(ai.valid_triage(result))

    def test_regulation_category_is_supported(self):
        source, _ = validate_draft({**DRAFT, 'category': 'Regulation'}, RESEARCH)
        self.assertIn('category: Regulation\n', source)

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

    def test_one_opened_source_is_enough_but_none_is_not(self):
        validate_draft(STUB, RESEARCH)
        uncited = STUB['markdown'].replace('[^1]', '')
        with self.assertRaises(InvalidArticle):
            validate_draft({**STUB, 'markdown': uncited}, RESEARCH)

    def test_search_results_are_citable_but_urls_in_model_text_are_not(self):
        evidence = copy.deepcopy(RESEARCH)
        evidence['content'] = evidence['content'][:1]
        evidence['content'][0]['text'] = json.dumps(URLS)
        with self.assertRaises(InvalidArticle):
            validate_draft(DRAFT, evidence)
        evidence['content'].append({'type': 'web_search_tool_result', 'content': [
            {'type': 'web_search_result', 'url': url} for url in URLS]})
        validate_draft(DRAFT, evidence)

    def test_placeholder_passes_validation_with_any_title_and_sources(self):
        awkward = {'stop_reason': 'end_turn', 'content': [{'type': 'web_search_tool_result', 'content': [
            {'type': 'web_search_result', 'url': 'https://example.com/a(b)'},
            {'type': 'web_search_result', 'url': 'https://example.com/plain?x=1&y=2'}]}]}
        for title in ['x', 'binance', 'BNB (Binance Coin)', 'Odd <b>name</b>!', 'a' * 200]:
            for research in [RESEARCH, awkward, {'content': []}]:
                with self.subTest(title=title[:20]):
                    draft = stub_draft(title, research)
                    validate_draft(draft, research)
                    self.assertNotIn('<', draft['markdown'])

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
