import json
import smtplib
import tempfile
import uuid
from io import StringIO
from pathlib import Path
from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.management import call_command
from django.test import Client, TestCase, override_settings
from .forms import new_token
from .models import RateLimit, Submission


class SubmissionsTests(TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        (root / 'assets').mkdir()
        (root / 'assets/site.css').write_text('body { color: black; }')
        (root / 'article-catalog.json').write_text(json.dumps({'bitcoin': {'title': 'Bitcoin', 'sections': {'history': 'History'}}}))
        (root / 'build-info.json').write_text(json.dumps({'revision': 'a' * 40}))
        self.root = root
        override = override_settings(DATA_DIR=root, SITE_ROOT=root, ARTICLE_CATALOG=root / 'article-catalog.json', PRODUCTION=False, SECURE_SSL_REDIRECT=False, ADMIN_NOTIFICATION_EMAIL='', NOTIFICATIONS_ENABLED=True)
        override.enable()
        self.addCleanup(override.disable)

    def data(self, **kwargs):
        return {'article': 'bitcoin', 'details': 'The stated date is incorrect.', 'claim': 'The stated date', 'sources': 'https://example.com/reference', 'form_token': new_token(), **kwargs}

    def test_three_forms_and_prefill(self):
        for kind in ('request', 'correction', 'improvement'):
            response = self.client.get(f'/submit/{kind}/?article=bitcoin&section=history')
            self.assertEqual(response.status_code, 200)
            if kind != 'request':
                self.assertContains(response, '<option value="bitcoin" selected>Bitcoin</option>', html=True)
            if kind != 'request':
                self.assertEqual(response.context['form']['section'].value(), 'History')
        self.assertEqual(self.client.get('/submit/unknown/').status_code, 404)

    def test_improvement_requires_article_and_suggestion_with_optional_sources(self):
        response = self.client.post('/submit/improvement/', {
            'article': 'bitcoin', 'details': 'Add a section on the DAO fork.',
            'section': 'History', 'form_token': new_token()})
        self.assertEqual(response.status_code, 302)
        record = Submission.objects.get()
        self.assertEqual(record.kind, 'improvement')
        self.assertEqual(record.article_revision, 'a' * 40)
        self.assertEqual(record.sources, '')
        self.assertEqual(record.section, 'History')
        self.assertEqual(record.claim, '')
        self.assertNotContains(self.client.get(response.url), record.details)
        response = self.client.post('/submit/improvement/', {'form_token': new_token()})
        self.assertIn('article', response.context['form'].errors)
        self.assertIn('details', response.context['form'].errors)
        response = self.client.post('/submit/improvement/', self.data(article='missing'))
        self.assertIn('article', response.context['form'].errors)

    def test_removed_question_route_rejects_get_and_post(self):
        self.assertEqual(self.client.get('/submit/question/').status_code, 404)
        self.assertEqual(self.client.post('/submit/question/', self.data()).status_code, 404)
        self.assertFalse(Submission.objects.exists())

    def test_correction_without_email_and_private_receipt(self):
        response = self.client.post('/submit/correction/', self.data())
        self.assertEqual(response.status_code, 302)
        record = Submission.objects.get()
        self.assertEqual(record.kind, 'correction')
        self.assertEqual(record.email, '')
        self.assertEqual(record.article_revision, 'a' * 40)
        receipt = self.client.get(response.url)
        self.assertContains(receipt, str(record.reference))
        self.assertNotContains(receipt, record.details)
        self.assertIn('no-store', receipt['Cache-Control'])

    def test_article_request(self):
        response = self.client.post('/submit/request/', self.data(title='A new protocol', email='reader@example.com'))
        self.assertEqual(response.status_code, 302)
        record = Submission.objects.get()
        self.assertEqual(record.title, 'A new protocol')
        self.assertEqual(record.article, '')
        self.assertEqual(record.status, 'new')
        receipt = self.client.get(response.url)
        self.assertNotContains(receipt, record.email)
        self.assertNotContains(self.client.get('/submit/'), record.email)

    def test_article_request_accepts_only_a_title(self):
        response = self.client.post('/submit/request/', {'title': 'A new protocol', 'form_token': new_token()})
        self.assertEqual(response.status_code, 302)
        record = Submission.objects.get()
        self.assertEqual(record.details, '')
        self.assertEqual(record.sources, '')
        self.assertEqual(record.email, '')
        form = self.client.get('/submit/request/').context['form']
        self.assertEqual([field.name for field in form.visible_fields() if field.field.required], ['title'])

    def test_article_request_still_requires_a_title(self):
        response = self.client.post('/submit/request/', {'details': 'Some scope', 'form_token': new_token()})
        self.assertIn('title', response.context['form'].errors)
        self.assertFalse(Submission.objects.exists())

    def test_correction_requires_claim_and_validates_provided_sources(self):
        response = self.client.post('/submit/correction/', self.data(claim='', sources=''))
        self.assertIn('claim', response.context['form'].errors)
        self.assertNotIn('sources', response.context['form'].errors)
        response = self.client.post('/submit/correction/', self.data(claim='Incorrect claim', sources='javascript:alert(1)'))
        self.assertIn('sources', response.context['form'].errors)
        self.assertFalse(Submission.objects.exists())
        response = self.client.post('/submit/correction/', self.data(claim='Incorrect claim', sources='https://example.com/reference', correction='Replacement text', section='History'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Submission.objects.get().section, 'History')

    def test_correction_accepts_missing_or_blank_sources(self):
        form = self.client.get('/submit/correction/').context['form']
        self.assertFalse(form.fields['sources'].required)
        self.assertEqual(form.fields['sources'].label, 'Source links (optional)')
        for sources in (None, '', '   '):
            with self.subTest(sources=sources):
                data = self.data(details=f'Incorrect date: {sources!r}')
                if sources is None:
                    data.pop('sources')
                else:
                    data['sources'] = sources
                response = self.client.post('/submit/correction/', data)
                self.assertEqual(response.status_code, 302)
                record = Submission.objects.get(details=data['details'])
                self.assertEqual(record.sources, '')
                self.assertEqual(record.kind, 'correction')

    def test_invalid_article_and_length_are_rejected(self):
        response = self.client.post('/submit/correction/', self.data(article='../../private'))
        self.assertIn('article', response.context['form'].errors)
        response = self.client.post('/submit/correction/', self.data(details='x' * 5001))
        self.assertIn('details', response.context['form'].errors)
        self.assertFalse(Submission.objects.exists())

    def test_duplicate_post_does_not_duplicate_submission(self):
        data = self.data()
        first = self.client.post('/submit/correction/', data)
        second = self.client.post('/submit/correction/', data)
        self.assertEqual(first.url, second.url)
        self.assertEqual(Submission.objects.count(), 1)

    @override_settings(ADMIN_NOTIFICATION_EMAIL='editor@example.com')
    def test_new_submissions_notify_admin_once_after_commit(self):
        for kind in ('request', 'correction', 'improvement'):
            with self.subTest(kind=kind):
                data = self.data(title='New protocol', email='reader@example.com')
                before = len(mail.outbox)
                with self.captureOnCommitCallbacks(execute=True) as callbacks:
                    response = self.client.post(f'/submit/{kind}/', data)
                    self.assertEqual(len(mail.outbox), before)
                self.assertEqual(response.status_code, 302)
                self.assertEqual(len(callbacks), 1)
                message = mail.outbox[-1]
                record = Submission.objects.get(kind=kind)
                self.assertEqual(message.to, ['editor@example.com'])
                self.assertEqual(message.subject, f'New Chainlore {record.get_kind_display().lower()}')
                self.assertIn(f'https://chainlore.xyz/admin/submissions/submission/{record.pk}/change/', message.body)
                self.assertIn(record.title or record.article, message.body)
                self.assertNotContains(self.client.get(response.url), 'editor@example.com')
                with self.captureOnCommitCallbacks(execute=True) as callbacks:
                    duplicate = self.client.post(f'/submit/{kind}/', data)
                self.assertEqual(duplicate.url, response.url)
                self.assertEqual(callbacks, [])
                self.assertEqual(len(mail.outbox), before + 1)

    @override_settings(ADMIN_NOTIFICATION_EMAIL='editor@example.com')
    def test_spam_and_invalid_submissions_do_not_notify_admin(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            self.client.post('/submit/correction/', self.data(website='https://spam.example'))
            self.client.post('/submit/request/', {'title': '', 'form_token': new_token()})
        self.assertEqual(callbacks, [])
        self.assertEqual(len(mail.outbox), 0)
        self.assertFalse(Submission.objects.exists())

    def test_admin_notification_requires_recipient_and_email_configuration(self):
        for options in ({'ADMIN_NOTIFICATION_EMAIL': ''},
                        {'ADMIN_NOTIFICATION_EMAIL': 'editor@example.com', 'NOTIFICATIONS_ENABLED': False}):
            with override_settings(**options), self.captureOnCommitCallbacks(execute=True):
                response = self.client.post('/submit/correction/', self.data())
            self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(Submission.objects.count(), 2)

    @override_settings(ADMIN_NOTIFICATION_EMAIL='editor@example.com')
    def test_admin_email_failure_preserves_submission_and_private_configuration(self):
        for error in (smtplib.SMTPException('editor@example.com secret-token'), OSError('connection failed')):
            with patch('submissions.notify.send_mail', side_effect=error):
                with self.assertLogs('submissions.notify', level='ERROR') as logs:
                    with self.captureOnCommitCallbacks(execute=True):
                        response = self.client.post('/submit/correction/', self.data())
            self.assertEqual(response.status_code, 302)
            self.assertNotIn('editor@example.com', '\n'.join(logs.output))
            self.assertNotIn('secret-token', '\n'.join(logs.output))
        self.assertEqual(Submission.objects.count(), 2)

    def test_tampered_token_rejected(self):
        response = self.client.post('/submit/correction/', self.data(form_token=str(uuid.uuid4())))
        self.assertIn('form_token', response.context['form'].errors)
        self.assertFalse(Submission.objects.exists())

    def test_honeypot_discards_spam(self):
        response = self.client.post('/submit/correction/', self.data(website='https://spam.example'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Submission.objects.exists())

    def test_rate_limit_is_shared_by_submission_types(self):
        for _ in range(10):
            self.assertEqual(self.client.post('/submit/correction/', self.data()).status_code, 302)
        response = self.client.post('/submit/request/', self.data(title='Another article'))
        self.assertEqual(response.status_code, 429)
        self.assertEqual(Submission.objects.count(), 10)
        self.assertEqual(response['Retry-After'], '3600')
        self.assertEqual(self.client.post('/submit/improvement/', self.data()).status_code, 429)
        self.assertTrue(all('127.0.0.1' not in key for key in RateLimit.objects.values_list('key', flat=True)))

    def test_csrf_is_enforced_and_valid_form_works(self):
        client = Client(enforce_csrf_checks=True)
        self.assertEqual(client.post('/submit/correction/', self.data()).status_code, 403)
        self.assertEqual(client.post('/submit/improvement/', self.data()).status_code, 403)
        response = client.get('/submit/correction/')
        token = response.context['form']['form_token'].value()
        response = client.post('/submit/correction/', self.data(form_token=token, csrfmiddlewaretoken=client.cookies['csrftoken'].value))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Submission.objects.count(), 1)

    def test_admin_can_still_review_legacy_questions(self):
        record = Submission.objects.create(kind='question', article='bitcoin', details='Question')
        url = f'/admin/submissions/submission/{record.pk}/change/'
        self.assertEqual(self.client.get(url).status_code, 302)
        user = get_user_model().objects.create_superuser('editor', password='test-long-password')
        self.client.force_login(user)
        self.assertContains(self.client.get('/admin/submissions/submission/'), str(record.pk)[:8])
        response = self.client.post(url, {'status': 'resolved', 'public_summary': 'Corrected the date.', 'internal_notes': 'Clarified in the article.', 'resulting_url': 'https://chainlore.xyz/p/bitcoin/'})
        self.assertEqual(response.status_code, 302)
        record.refresh_from_db()
        self.assertEqual(record.status, 'resolved')
        self.assertEqual(record.details, 'Question')

    def test_admin_duplicate_link_and_no_self_duplicate(self):
        original = Submission.objects.create(kind='request', title='Topic', details='Details')
        duplicate = Submission.objects.create(kind='request', title='Topic', details='More details')
        self.client.force_login(get_user_model().objects.create_superuser('editor', password='test-long-password'))
        url = f'/admin/submissions/submission/{duplicate.pk}/change/'
        response = self.client.post(url, {'status': 'declined', 'duplicate_of': original.pk})
        self.assertEqual(response.status_code, 302)
        duplicate.refresh_from_db()
        self.assertEqual(duplicate.duplicate_of, original)
        response = self.client.post(url, {'status': 'declined', 'duplicate_of': duplicate.pk})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'cannot be a duplicate of itself')

    def test_admin_decision_emails_submitter_once(self):
        record = Submission.objects.create(kind='correction', article='bitcoin', claim='Claim', email='reader@example.com')
        self.client.force_login(get_user_model().objects.create_superuser('editor', password='test-long-password'))
        url = f'/admin/submissions/submission/{record.pk}/change/'
        self.client.post(url, {'status': 'reviewing'})
        self.assertEqual(len(mail.outbox), 0)
        self.client.post(url, {'status': 'resolved', 'public_summary': 'Corrected the date.', 'resulting_url': 'https://chainlore.xyz/p/bitcoin/'})
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.to, ['reader@example.com'])
        self.assertEqual(message.subject, 'Update on your Chainlore error report')
        self.assertIn('the Bitcoin article', message.body)
        self.assertIn('https://chainlore.xyz/p/bitcoin/', message.body)
        self.assertIn(str(record.reference), message.body)
        self.client.post(url, {'status': 'resolved', 'public_summary': 'Corrected the date.', 'internal_notes': 'Edited again.'})
        self.assertEqual(len(mail.outbox), 1)
        record.refresh_from_db()
        self.assertEqual(record.notified_status, 'resolved')
        self.assertIsNotNone(record.notified_at)

    def test_admin_decision_without_email_or_configuration_sends_nothing(self):
        silent = Submission.objects.create(kind='request', title='Topic')
        self.client.force_login(get_user_model().objects.create_superuser('editor', password='test-long-password'))
        self.client.post(f'/admin/submissions/submission/{silent.pk}/change/', {'status': 'declined', 'public_summary': 'The original article is accurate.'})
        record = Submission.objects.create(kind='request', title='Topic', email='reader@example.com')
        with override_settings(NOTIFICATIONS_ENABLED=False):
            response = self.client.post(f'/admin/submissions/submission/{record.pk}/change/', {'status': 'declined', 'public_summary': 'The original article is accurate.'}, follow=True)
        self.assertContains(response, 'Email is not configured')
        self.assertEqual(len(mail.outbox), 0)
        record.refresh_from_db()
        self.assertEqual(record.notified_status, '')

    def test_admin_login_throttled(self):
        for _ in range(10):
            self.client.post('/admin/login/', {'username': 'unknown', 'password': 'wrong'})
        self.assertEqual(self.client.post('/admin/login/', {}).status_code, 429)

    def test_user_text_is_escaped(self):
        response = self.client.post('/submit/request/', self.data(title='', details='<script>alert(1)</script>'))
        self.assertContains(response, '&lt;script&gt;')
        self.assertNotContains(response, '<script>alert(1)</script>')

    def test_unknown_prefill_does_not_inject_markup(self):
        response = self.client.get('/submit/correction/?article=%22%3E%3Cscript%3E')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '<script>')

    def test_admin_bootstrap_creates_working_private_credentials_once(self):
        output = StringIO()
        call_command('bootstrap_admin', stdout=output)
        credentials = self.root / 'admin-initial-credentials.txt'
        text = credentials.read_text()
        password = text.split('Password: ', 1)[1].strip()
        self.assertEqual(credentials.stat().st_mode & 0o777, 0o600)
        self.assertNotIn(password, output.getvalue())
        self.assertTrue(self.client.login(username='admin', password=password))
        call_command('bootstrap_admin', stdout=output)
        self.assertEqual(credentials.read_text(), text)
        self.assertEqual(get_user_model().objects.count(), 1)
