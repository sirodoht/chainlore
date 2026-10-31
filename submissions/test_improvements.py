import copy
import json
from unittest.mock import patch
from django.utils import timezone
from datetime import timedelta
from . import ai_providers as ai
from .article_validation import InvalidArticle
from .automation import run_worker
from .automation_control import retry_runs
from .git_publication import commit_and_push, git
from .improvements import snapshot_article, validate_patch
from .models import ArticleRevision, AutomationRun, GeneratedArticle, Submission
from .test_automation import AutomationFixture, RESEARCH, decision

REAL_WRITE_IMPROVEMENT = ai.write_improvement

ADDITION = 'The additional research describes a fictional milestone in the history of the protocol. Its technical design provides more context for readers interested in the topic, according to the cited documentation.[^1]'
PATCH = {'edits': [{'anchor': '## References', 'position': 'before',
                    'markdown': '## Additional context\n\n' + ADDITION}],
         'references': '[^1]: [Technical design](https://docs.example.com/design)'}


def written_patch(value=None):
    return {'stop_reason': 'end_turn', '_written_by': 'revision-writer-v1 (high effort)',
            'content': [{'type': 'text', 'text': json.dumps(PATCH if value is None else value)}]}


class ImprovementTests(AutomationFixture):
    def setUp(self):
        super().setUp()
        self.submission.kind = 'improvement'
        self.submission.title = ''
        self.submission.article = 'bitcoin'
        self.submission.details = 'Add a section with more context.'
        self.submission.save()
        self.original = git(self.remote, 'show', 'main:pages/bitcoin.md') + '\n'
        for name, value in [('write_improvement', written_patch()), ('review_improvement', decision(suitable='yes'))]:
            mock = patch.object(ai, name, return_value=value)
            setattr(self, name, mock.start())
            self.addCleanup(mock.stop)

    def test_publish_preserves_original_author_and_references_and_returns_to_draft(self):
        run_worker()
        record = ArticleRevision.objects.get()
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'published')
        self.assertEqual(record.original_markdown, self.original)
        source = git(self.remote, 'show', 'main:pages/bitcoin.md')
        self.assertIn('written_by: Opus 5.5 High', source)
        self.assertIn('status: draft', source)
        self.assertNotIn('checked_by:', source)
        self.assertNotIn('\nchecked:', source)
        self.assertNotIn('reviewed_by:', source)
        self.assertIn('## Additional context', source)
        self.assertIn(f'[^imp-{run.pk}-1]', source)
        self.assertIn('[^core30]:', source)  # Existing named references survive unchanged.
        self.assertEqual(set(git(self.remote, 'diff-tree', '--no-commit-id', '--name-only', '-r', 'main').splitlines()), {'pages/bitcoin.md'})
        commit = git(self.remote, 'log', '-1', '--format=%B')
        self.assertTrue(commit.startswith('feat(content):'))
        self.assertIn('revision-writer-v1 (high effort)', commit)
        self.assertNotIn(self.submission.email, git(self.remote, 'show', 'main'))
        self.assertNotIn(self.submission.details, commit)
        self.assertEqual(record.git_revision, git(self.remote, 'rev-parse', 'main'))
        self.assertFalse(GeneratedArticle.objects.exists())
        self.submission.refresh_from_db()
        self.assertEqual(self.submission.resulting_url, 'https://chainlore.xyz/p/bitcoin/')
        self.write_article.assert_not_called()
        self.assertNotIn('email', run.inputs)
        html = (self.root / 'published/current/p/bitcoin/index.html').read_text()
        self.assertIn('/submit/improvement/?article=bitcoin', html)
        self.assertIn('Suggest an improvement', html)
        self.assertNotIn('Fact-checked by', html)

    def test_concurrent_unrelated_edit_is_preserved(self):
        def screen(*args):
            self.edit_remote(lambda checkout: (checkout / 'pages/bitcoin.md').write_text(
                (checkout / 'pages/bitcoin.md').read_text().replace('## History', '## Origins and history')))
            return decision(suitable='yes')
        self.review_improvement.side_effect = screen
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        source = git(self.remote, 'show', 'main:pages/bitcoin.md')
        self.assertIn('## Origins and history', source)
        self.assertIn('## Additional context', source)

    def test_concurrent_edit_to_same_anchor_is_held_for_review(self):
        proposal = copy.deepcopy(PATCH)
        proposal['edits'][0]['anchor'] = '## History'
        proposal['edits'][0]['position'] = 'after'
        self.write_improvement.return_value = written_patch(proposal)
        def screen(*args):
            self.edit_remote(lambda checkout: (checkout / 'pages/bitcoin.md').write_text(
                (checkout / 'pages/bitcoin.md').read_text().replace('## History', '## Edited history')))
            return decision(suitable='yes')
        self.review_improvement.side_effect = screen
        run_worker()
        run = AutomationRun.objects.get()
        self.assertEqual(run.state, 'review')
        self.assertEqual(run.last_error, 'improvement_passage_changed')
        self.assertNotIn('## Additional context', git(self.remote, 'show', 'main:pages/bitcoin.md'))
        self.assertIsNone(ArticleRevision.objects.get().published_at)
        self.assertEqual(retry_runs([run.pk], actor_id=7, restart=True), 1)
        self.assertFalse(ArticleRevision.objects.exists())
        self.assertTrue(run.events.filter(kind='improvement_restart').exists())

    def test_invalid_output_never_replaces_article_with_placeholder(self):
        self.write_improvement.return_value = written_patch({'insufficient_evidence': True})
        before = git(self.remote, 'rev-parse', 'main')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.assertEqual(self.write_improvement.call_count, 2)
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), before)
        self.assertEqual(ArticleRevision.objects.get().markdown, '')
        self.assertFalse(GeneratedArticle.objects.exists())

    def test_missing_research_and_rejected_edits_leave_article_unchanged(self):
        self.research.return_value = {'content': []}
        before = git(self.remote, 'rev-parse', 'main')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.write_improvement.assert_not_called()
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), before)

    def test_output_screening_holds_unsuitable_improvement(self):
        self.review_improvement.return_value = decision(suitable='no')
        before = git(self.remote, 'rev-parse', 'main')
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'review')
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), before)

    def test_retry_after_push_does_not_duplicate_changes(self):
        with patch('submissions.publication.shutil.copytree', side_effect=OSError('publication unavailable')):
            run_worker()
        revision = git(self.remote, 'rev-parse', 'main')
        self.assertIsNone(ArticleRevision.objects.get().published_at)
        AutomationRun.objects.update(next_attempt_at=timezone.now() - timedelta(seconds=1))
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), revision)
        self.assertEqual(git(self.remote, 'show', 'main:pages/bitcoin.md').count('## Additional context'), 1)
        self.write_improvement.assert_called_once()

    def test_push_race_retries_using_latest_repository_content(self):
        def race(source, paths, credits):
            self.edit_remote(lambda checkout: (checkout / 'pages/bitcoin.md').write_text(
                (checkout / 'pages/bitcoin.md').read_text().replace('## History', '## Concurrent history')))
            return commit_and_push(source, paths, credits)
        with patch('submissions.publication.commit_and_push', side_effect=race):
            run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'retry')
        AutomationRun.objects.update(next_attempt_at=timezone.now() - timedelta(seconds=1))
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        source = git(self.remote, 'show', 'main:pages/bitcoin.md')
        self.assertIn('## Concurrent history', source)
        self.assertIn('## Additional context', source)
        self.write_improvement.assert_called_once()

    def test_multiple_suggestions_keep_separate_history(self):
        run_worker()
        Submission.objects.create(kind='improvement', article='bitcoin', details='Add more context.')
        second = copy.deepcopy(PATCH)
        second['edits'][0]['markdown'] = second['edits'][0]['markdown'].replace('Additional context', 'Further context')
        self.write_improvement.return_value = written_patch(second)
        run_worker()
        self.assertEqual(ArticleRevision.objects.filter(published_at__isnull=False).count(), 2)
        source = git(self.remote, 'show', 'main:pages/bitcoin.md')
        self.assertIn('## Additional context', source)
        self.assertIn('## Further context', source)
        self.assertIn('[^imp-1-1]', source)
        self.assertIn('[^imp-2-1]', source)

    def test_untrusted_sources_unsafe_markup_and_wholesale_rewrites_are_rejected(self):
        run = AutomationRun.objects.create(submission=self.submission, inputs={'article': 'bitcoin'})
        record = snapshot_article(run)
        for change in ('source', 'markup', 'whole_article', 'duplicate_anchor'):
            proposal = copy.deepcopy(PATCH)
            if change == 'source':
                proposal['references'] = '[^1]: [Fake](https://not-researched.example.com/)'
            elif change == 'markup':
                proposal['edits'][0]['markdown'] += '<script>alert(1)</script>'
            elif change == 'whole_article':
                proposal['edits'][0].update(anchor=self.original, position='replace')
            else:
                proposal['edits'].append(proposal['edits'][0].copy())
            with self.subTest(change=change), self.assertRaises(InvalidArticle):
                validate_patch(record, proposal, RESEARCH)

    def test_replacing_paragraph_removes_only_its_newly_unused_reference(self):
        old = 'This is a fictional paragraph included to test an exact replacement and its source reference.[^old-only]'
        def add_paragraph(checkout):
            path = checkout / 'pages/bitcoin.md'
            path.write_text(path.read_text().replace('## References', old + '\n\n## References') +
                            '\n[^old-only]: [Old source](https://docs.example.com/history)\n')
        self.edit_remote(add_paragraph)
        proposal = copy.deepcopy(PATCH)
        proposal['edits'] = [{'anchor': old, 'position': 'replace', 'markdown': ADDITION}]
        self.write_improvement.return_value = written_patch(proposal)
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        source = git(self.remote, 'show', 'main:pages/bitcoin.md')
        self.assertNotIn('[^old-only]', source)
        self.assertIn('[^core30]:', source)
        self.assertIn('The additional research describes', source)

    def test_crash_after_remote_push_before_database_checkpoint_is_idempotent(self):
        def crash(source, paths, credits):
            commit_and_push(source, paths, credits)
            raise OSError('checkpoint interrupted')
        with patch('submissions.publication.commit_and_push', side_effect=crash):
            run_worker()
        self.assertEqual(ArticleRevision.objects.get().git_revision, '')
        revision = git(self.remote, 'rev-parse', 'main')
        AutomationRun.objects.update(next_attempt_at=timezone.now() - timedelta(seconds=1))
        run_worker()
        self.assertEqual(AutomationRun.objects.get().state, 'published')
        self.assertEqual(git(self.remote, 'rev-parse', 'main'), revision)
        self.assertEqual(git(self.remote, 'show', 'main:pages/bitcoin.md').count('## Additional context'), 1)

    def test_provider_payload_uses_article_and_actual_writer_credit(self):
        run = AutomationRun.objects.create(submission=self.submission,
            inputs={'article': 'bitcoin', 'kind': 'improvement'}, research=RESEARCH)
        record = snapshot_article(run)
        payload = ai.research_payload(run)
        request = json.loads(payload['messages'][0]['content'])
        self.assertEqual(request['existing_article'], self.original)
        self.assertNotIn(self.submission.email, json.dumps(request))
        with patch.object(ai, 'call', return_value={'model': 'actual-revision-model'}) as call:
            result = REAL_WRITE_IMPROVEMENT(run, record)
        self.assertEqual(result['_written_by'], 'actual-revision-model (high effort)')
        sent = json.loads(call.call_args.args[3]['messages'][0]['content'])
        self.assertEqual(sent['existing_article'], self.original)
        self.assertNotIn(self.submission.email, json.dumps(sent))
