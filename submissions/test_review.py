import json
import tempfile
from datetime import date
from pathlib import Path
from unittest.mock import patch

from django.contrib.auth.models import Permission, User
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Submission


@override_settings(PASSWORD_HASHERS=['django.contrib.auth.hashers.MD5PasswordHasher'])
class ReviewDashboardTests(TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.catalog = Path(directory.name) / 'article-catalog.json'
        self.pages = {
            'draft': {'title': 'Draft article', 'category': 'History', 'status': 'draft',
                      'checked': '2026-01-01', 'checked_by': 'Historical checker'},
            'old': {'title': 'Old check', 'status': 'ai-fact-checked',
                    'checked': '2026-04-30', 'checked_by': 'Old checker'},
            'current': {'title': 'Current article', 'status': 'ai-fact-checked',
                        'checked': '2026-10-30', 'checked_by': 'Current checker'},
            'human': {'title': 'Human article', 'status': 'human-reviewed',
                      'checked': '2026-05-01', 'checked_by': 'AI checker',
                      'reviewed': '2026-10-29', 'reviewed_by': 'Human reviewer'},
        }
        self.write_catalog()
        override = override_settings(ARTICLE_CATALOG=self.catalog, SECURE_SSL_REDIRECT=False)
        override.enable()
        self.addCleanup(override.disable)
        clock = patch('submissions.review.timezone.localdate', return_value=date(2026, 10, 31))
        clock.start()
        self.addCleanup(clock.stop)
        self.editor = User.objects.create_superuser('editor', password='test-password')
        self.url = reverse('review-dashboard')

    def write_catalog(self):
        self.catalog.write_text(json.dumps(self.pages))

    def login(self):
        self.client.force_login(self.editor)

    def report(self, article='current', **kwargs):
        return Submission.objects.create(article=article, kind='correction', **kwargs)

    def test_authentication_and_submission_permissions_are_required(self):
        self.assertRedirects(self.client.get(self.url), '/admin/login/?next=/admin/review/', fetch_redirect_response=False)
        reader = User.objects.create_user('reader', password='test-password')
        self.client.force_login(reader)
        self.assertEqual(self.client.get(self.url).status_code, 302)
        reader.is_staff = True
        reader.save()
        self.assertEqual(self.client.get(self.url).status_code, 403)
        reader.user_permissions.add(Permission.objects.get(codename='view_submission'))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('no-store', response['Cache-Control'])
        self.assertIn('private', response['Cache-Control'])

    def test_dashboard_counts_dates_and_historical_draft_credits(self):
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.context['counts'], {
            'all': 4, 'attention': 3, 'draft': 1, 'overdue': 2, 'reports': 0, 'human': 2, 'reviewed': 1,
        })
        rows = {row['slug']: row for row in response.context['rows']}
        self.assertIsNone(rows['draft']['checked'])
        self.assertNotContains(response, 'Historical checker')
        self.assertContains(response, 'Human reviewer')
        self.assertEqual(rows['old']['due'], date(2026, 5, 30))
        self.assertTrue(rows['human']['overdue'])
        self.assertEqual(rows['human']['status'], 'human-reviewed')
        self.assertEqual(rows['old']['status'], 'ai-fact-checked')

    def test_thirty_day_boundary(self):
        self.login()
        with patch('submissions.review.timezone.localdate', return_value=date(2026, 5, 30)):
            response = self.client.get(self.url, {'filter': 'overdue'})
        self.assertEqual(response.context['rows'], [])

    def test_open_reports_exclude_closed_duplicates_and_other_submission_kinds(self):
        canonical = self.report(details='Private claim', email='private@example.test', internal_notes='Private notes')
        self.report(status='reviewing')
        self.report(status='resolved')
        self.report(status='declined')
        self.report(duplicate_of=canonical)
        self.report(article='removed')
        Submission.objects.create(kind='improvement', article='current', details='An improvement')
        self.login()
        response = self.client.get(self.url)
        self.assertEqual(response.context['open_reports'], 3)
        self.assertEqual(response.context['unmatched_reports'], 1)
        first = response.context['rows'][0]
        self.assertEqual((first['slug'], first['reports']), ('current', 2))
        for private in ('private@example.test', 'Private claim', 'Private notes'):
            self.assertNotContains(response, private)
        queue = self.client.get(first['reports_url'])
        self.assertEqual(queue.status_code, 200)
        self.assertEqual(queue.context['cl'].result_count, 2)

    def test_filters_search_and_sort(self):
        self.report()
        self.login()
        for name, expected in [('draft', ['draft']), ('overdue', ['human', 'old']), ('reports', ['current']),
                               ('human', ['current', 'old']), ('reviewed', ['human'])]:
            response = self.client.get(self.url, {'filter': name, 'sort': 'title'})
            self.assertEqual([row['slug'] for row in response.context['rows']], expected)
        response = self.client.get(self.url, {'q': 'HISTORY'})
        self.assertEqual([row['slug'] for row in response.context['rows']], ['draft'])
        response = self.client.get(self.url, {'sort': 'oldest'})
        self.assertEqual([row['slug'] for row in response.context['rows']], ['draft', 'old', 'human', 'current'])
        response = self.client.get(self.url, {'q': 'no matches'})
        self.assertContains(response, 'No articles match these filters.')
        response = self.client.get(self.url, {'filter': 'invalid', 'sort': 'invalid'})
        self.assertEqual((response.context['selected'], response.context['sort']), ('all', 'priority'))

    def test_catalogue_is_read_from_current_publication_on_each_request(self):
        self.login()
        self.assertEqual(self.client.get(self.url).context['counts']['all'], 4)
        self.pages['new'] = {'title': 'Newly published', 'status': 'draft'}
        self.write_catalog()
        self.assertEqual(self.client.get(self.url).context['counts']['draft'], 2)
        self.pages.pop('old')
        self.write_catalog()
        self.assertEqual(self.client.get(self.url).context['counts']['overdue'], 1)

    def test_missing_or_future_check_metadata_is_flagged(self):
        self.pages['legacy'] = {'title': 'Old catalogue format', 'sections': {}}
        self.pages['current']['checked'] = '2027-01-01'
        self.pages['old']['checked'] = 'invalid'
        self.write_catalog()
        self.login()
        response = self.client.get(self.url, {'filter': 'attention'})
        self.assertEqual({row['slug'] for row in response.context['rows']}, {'legacy', 'current', 'old', 'draft', 'human'})
        self.assertContains(response, 'Review metadata unavailable')
        self.assertContains(response, 'Full-check date is in the future')
        self.assertContains(response, 'Full-check date or checker missing')

    def test_missing_or_broken_catalogue_is_not_presented_as_zero_articles(self):
        self.login()
        self.catalog.unlink()
        self.assertContains(self.client.get(self.url), 'counts could not be loaded', status_code=503)
        for content in ('broken json', '[]', '{"a": {}}'):
            self.catalog.write_text(content)
            self.assertContains(self.client.get(self.url), 'counts could not be loaded', status_code=503)

    def test_titles_and_search_are_escaped_and_post_is_read_only(self):
        self.pages['current']['title'] = '<script>alert(1)</script>'
        self.write_catalog()
        self.login()
        response = self.client.get(self.url)
        self.assertContains(response, '&lt;script&gt;alert(1)&lt;/script&gt;')
        self.assertNotContains(response, '<script>alert(1)</script>')
        response = self.client.get(self.url, {'q': '"><script>alert(1)</script>'})
        self.assertNotContains(response, '<script>alert(1)</script>')
        self.assertEqual(self.client.post(self.url, {'status': 'human-reviewed'}).status_code, 405)
        self.assertEqual(json.loads(self.catalog.read_text()), self.pages)
        self.assertEqual(Submission.objects.count(), 0)

    def test_admin_header_has_dashboard_link(self):
        self.login()
        self.assertContains(self.client.get('/admin/'), 'href="/admin/review/"')
