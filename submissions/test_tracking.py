import uuid
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import AutomationEvent, AutomationRun, Submission, SubmissionUpdate
from . import tests as form_tests
from .forms import new_token


class TrackingTests(TestCase):
    setUp = form_tests.SubmissionsTests.setUp

    def detail(self, record):
        return self.client.get(f'/submit/track/{record.pk}/')

    def test_all_types_filters_and_no_private_fields(self):
        secrets = dict(title='PRIVATE TITLE', details='PRIVATE DETAILS', claim='PRIVATE CLAIM',
                       correction='PRIVATE CORRECTION', sources='https://private.example/SECRET',
                       email='private@example.com', internal_notes='PRIVATE NOTES', section='PRIVATE SECTION')
        for kind in ('request', 'correction', 'improvement'):
            item = Submission.objects.create(kind=kind, article='bitcoin', **secrets)
            response = self.detail(item)
            self.assertEqual(response.status_code, 200)
            for value in secrets.values():
                self.assertNotContains(response, value)
        Submission.objects.create(kind='question', title='HISTORICAL QUESTION')
        page = self.client.get('/submit/all/')
        self.assertEqual(len(page.context['rows']), 3)
        self.assertNotContains(page, 'HISTORICAL QUESTION')
        for value in secrets.values():
            self.assertNotContains(page, value)
        self.assertIn('no-store', page['Cache-Control'])
        for kind in ('request', 'correction', 'improvement'):
            response = self.client.get('/submit/all/', {'type': kind})
            self.assertEqual(len(response.context['rows']), 1)
        response = self.client.get('/submit/all/', {'status': 'queued'})
        self.assertEqual(len(response.context['rows']), 3)

    def test_statuses_follow_processing_and_manual_decisions(self):
        record = Submission.objects.create(kind='request')
        run = AutomationRun.objects.create(submission=record)
        states = {'queued': 'queued', 'running': 'in-progress', 'retry': 'queued',
                  'blocked': 'blocked', 'review': 'queued', 'failed': 'queued',
                  'researching': 'researching', 'checking': 'checking', 'revising': 'revising', 'publishing': 'publishing'}
        for state, expected in states.items():
            run.state = state
            run.save()
            self.assertEqual(self.detail(record).context['item']['status'], expected)
            self.assertEqual(len(self.client.get('/submit/all/', {'status': expected}).context['rows']), 1)
        record.status = 'declined'
        record.public_summary = 'Outside our editorial scope.'
        record.save()
        self.assertEqual(self.detail(record).context['item']['status'], 'declined')
        record.status = 'resolved'
        record.save()
        self.assertEqual(self.detail(record).context['item']['status'], 'resolved')

    def test_publication_outcome_and_safe_history(self):
        record = Submission.objects.create(kind='improvement', article='bitcoin', status='resolved',
                                           resulting_url='https://chainlore.xyz/p/bitcoin/')
        run = AutomationRun.objects.create(submission=record, state='published', inputs={'secret': 'SECRET INPUT'}, last_error='SECRET ERROR')
        for kind in ('queued', 'attempt_started', 'research_request', 'writing_request', 'publication'):
            AutomationEvent.objects.create(run=run, kind=kind, data={'private': 'SECRET EVENT', 'revision': 'a'*40})
        AutomationEvent.objects.create(run=run, kind='research_response', data={'text': 'SECRET RESPONSE'})
        response = self.detail(record)
        self.assertContains(response, 'An updated version of the article was published.')
        self.assertContains(response, '/p/bitcoin/')
        self.assertContains(response, 'Research started')
        self.assertContains(response, 'Writing started')
        self.assertContains(response, 'Article updated')
        self.assertContains(response, 'https://github.com/sirodoht/chainlore/commit/'+'a'*40)
        self.assertNotContains(response, 'SECRET')
        self.assertEqual(len(response.context['history']), 6)

    def test_public_notes_escape_html_and_manual_history_is_retained(self):
        record = Submission.objects.create(kind='correction', article='bitcoin')
        record.status = 'resolved'
        record.public_title = '<script>alert(1)</script>'
        record.public_summary = 'Changed the launch date to 3 January 2009. <b>Test</b>'
        record.save()
        self.assertEqual(SubmissionUpdate.objects.count(), 1)
        response = self.detail(record)
        self.assertContains(response, '&lt;script&gt;alert(1)&lt;/script&gt;')
        self.assertNotContains(response, '<script>alert(1)</script>')
        self.assertContains(response, 'Changed the launch date')
        record.internal_notes = 'PRIVATE ONLY'
        record.save()
        self.assertEqual(SubmissionUpdate.objects.count(), 1)
        self.assertNotContains(self.detail(record), 'PRIVATE ONLY')

    def test_duplicate_original_and_automated_existing_article(self):
        original = Submission.objects.create(kind='request', status='resolved', resulting_url='https://chainlore.xyz/p/bitcoin/')
        duplicate = Submission.objects.create(kind='request', duplicate_of=original)
        self.assertContains(self.detail(duplicate), f'/submit/track/{original.pk}/')
        self.assertEqual(self.detail(duplicate).context['item']['status'], 'duplicate')
        auto = Submission.objects.create(kind='request', status='resolved', resulting_url=original.resulting_url)
        AutomationRun.objects.create(submission=auto, state='duplicate')
        response = self.detail(auto)
        self.assertContains(response, f'/submit/track/{original.pk}/')
        self.assertContains(response, 'View existing article')
        original.duplicate_of = duplicate
        with self.assertRaises(ValidationError):
            original.clean()

    def test_unsafe_result_urls_and_unavailable_records(self):
        for url in ('https://evil.example/', 'javascript:alert(1)', 'https://chainlore.xyz/admin/',
                    'https://chainlore.xyz/p/bitcoin/?secret=1', 'https://chainlore.xyz/p/missing/'):
            record = Submission.objects.create(kind='request', resulting_url=url)
            self.assertEqual(self.detail(record).context['item']['result_url'], '')
        self.assertEqual(self.client.get(f'/submit/track/{uuid.uuid4()}/').status_code, 404)
        old = Submission.objects.create(kind='question')
        self.assertEqual(self.detail(old).status_code, 404)
        self.assertEqual(self.client.post('/submit/all/').status_code, 405)

    def test_pagination_filters_empty_and_invalid_values(self):
        Submission.objects.bulk_create([Submission(kind='request') for _ in range(27)])
        page = self.client.get('/submit/all/', {'type': 'request', 'status': 'queued'})
        self.assertEqual(len(page.context['rows']), 25)
        self.assertContains(page, 'type=request&amp;status=queued&amp;page=2')
        self.assertEqual(len(self.client.get('/submit/all/?page=2').context['rows']), 2)
        self.assertEqual(self.client.get('/submit/all/?page=invalid').status_code, 200)
        self.assertEqual(self.client.get('/submit/all/?type=invalid&status=invalid').context['page'].paginator.count, 27)
        self.assertContains(self.client.get('/submit/all/?type=correction'), 'No submissions match')

    def test_receipt_links_and_honeypot_has_no_public_record(self):
        response = self.client.post('/submit/request/', {'title': 'Private suggestion', 'form_token': new_token()})
        record = Submission.objects.get()
        receipt = self.client.get(response.url)
        self.assertContains(receipt, f'/submit/track/{record.pk}/')
        self.assertContains(receipt, 'View all submissions')
        self.assertNotContains(self.detail(record), 'Private suggestion')
        self.client.post('/submit/request/', {'title': 'SPAM', 'website': 'bot', 'form_token': new_token()})
        self.assertEqual(Submission.objects.count(), 1)

    def test_editor_requires_reason_and_can_publish_safe_summary(self):
        self.client.force_login(get_user_model().objects.create_superuser('editor', password='long-password-test'))
        record = Submission.objects.create(kind='correction', article='bitcoin')
        url = f'/admin/submissions/submission/{record.pk}/change/'
        response = self.client.post(url, {'status': 'declined'})
        self.assertContains(response, 'Explain the outcome')
        response = self.client.post(url, {'status': 'declined', 'public_summary': 'The source confirms the existing date.', 'public_title': 'Bitcoin launch date'})
        self.assertEqual(response.status_code, 302)
        self.client.logout()
        self.assertContains(self.detail(record), 'The source confirms the existing date.')
        self.assertContains(self.client.get('/submit/all/'), 'Bitcoin launch date')

    def test_automated_decline_is_explained_without_overwriting_manual_decision(self):
        from .automation import finish
        record = Submission.objects.create(kind='request', status='reviewing')
        run = AutomationRun.objects.create(submission=record, state='running')
        finish(run, 'declined', 'out_of_scope_or_injection')
        self.assertContains(self.detail(record), 'outside the editorial scope')
        record.refresh_from_db()
        record.status = 'resolved'
        record.public_summary = 'An editor published the requested material.'
        record.save()
        finish(run, 'review', 'submission_already_decided')
        response = self.detail(record)
        self.assertEqual(response.context['item']['status'], 'resolved')
        self.assertContains(response, 'An editor published the requested material.')

    def test_budget_block_does_not_claim_recovery_attempts_exhausted(self):
        record=Submission.objects.create(kind='correction',article='bitcoin',status='reviewing')
        AutomationRun.objects.create(submission=record,state='blocked',last_error='run_token_budget',recovery_attempts=0)
        response=self.detail(record)
        self.assertContains(response,'budget adjustment is needed')
        self.assertContains(response,'No automatic retry is currently scheduled')
        self.assertNotContains(response,'attempts are exhausted')
