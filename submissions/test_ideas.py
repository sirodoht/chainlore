import json
import tempfile
from datetime import timedelta
from pathlib import Path
from unittest.mock import patch
from django.test import TestCase, override_settings
from django.utils import timezone
from . import ideas, editorial
from .models import AutomationRun, Submission

CATALOG = {
    'bitcoin': {'title': 'Bitcoin', 'status': 'ai-fact-checked', 'sections': {'history': 'History', 'timeline': 'Timeline'}},
    'aave': {'title': 'Aave', 'status': 'draft', 'sections': {'history': 'History'}},
}


def reply(value):
    return {'stop_reason': 'end_turn', 'content': [{'type': 'text', 'text': json.dumps(value)}]}


class IdeaTests(TestCase):
    def setUp(self):
        self.site = tempfile.TemporaryDirectory()
        root = Path(self.site.name)
        (root / 'p').mkdir()
        (root / 'p' / 'bitcoin.md').write_text('x' * 4000)
        (root / 'p' / 'aave.md').write_text('x' * 1000)
        self.settings = override_settings(SITE_ROOT=root, IDEAS_ENABLED=True, IDEAS_DAILY_LIMIT=1,
                                          IDEAS_NEW_ARTICLE_SHARE=0.75)
        self.settings.enable()
        patcher = patch('submissions.ideas.articles', return_value=CATALOG)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.settings.disable)
        self.addCleanup(self.site.cleanup)

    def run_for(self, submission):
        return AutomationRun.objects.create(submission=submission, inputs={key: getattr(submission, key)
            for key in ('title', 'details', 'sources', 'kind', 'article', 'section', 'claim', 'correction')})

    @patch('submissions.ideas.random.random', return_value=0.5)
    def test_new_article_chosen_three_quarters_of_the_time_and_once_a_day(self, _):
        job = ideas.enqueue()
        self.assertEqual(job.kind, 'request')
        self.assertTrue(ideas.is_idea(job))
        self.assertEqual(job.title, '')
        self.assertIsNone(ideas.enqueue())

    @patch('submissions.ideas.random.random', return_value=0.8)
    def test_improvement_chosen_otherwise(self, _):
        job = ideas.enqueue()
        self.assertEqual(job.kind, 'improvement')
        self.assertIn(job.article, CATALOG)
        self.assertEqual(job.public_title, f'Editor’s improvement: {job.title}')

    @override_settings(IDEAS_ENABLED=False)
    def test_disabled(self):
        self.assertIsNone(ideas.enqueue())

    @patch('submissions.ideas.random.choices', side_effect=lambda choices, weights: [choices[0]])
    def test_improvement_target_prefers_short_drafts_and_skips_busy_or_recent(self, choices):
        ideas.improvement_target(CATALOG)
        slugs, weights = choices.call_args.args
        weight = dict(zip(slugs, weights))
        self.assertGreater(weight['aave'], weight['bitcoin'])
        Submission.objects.create(kind='correction', article='aave', status='new')
        self.assertEqual(ideas.improvement_target(CATALOG), 'bitcoin')
        Submission.objects.create(kind='improvement', article='bitcoin', status='resolved', maintenance_key='idea:old:1')
        self.assertIsNone(ideas.improvement_target(CATALOG))
        Submission.objects.filter(maintenance_key='idea:old:1').update(created_at=timezone.now()-timedelta(days=40))
        self.assertEqual(ideas.improvement_target(CATALOG), 'bitcoin')

    @patch('submissions.ai_providers.call', return_value=reply({'title': 'Ethereum', 'details': 'The programmable blockchain and its history.'}))
    def test_new_article_proposal_fills_request(self, call):
        submission = Submission.objects.create(kind='request', maintenance_key='idea:2026-01-01:1', public_title=ideas.NEW_ARTICLE_LABEL)
        run = self.run_for(submission)
        self.assertTrue(ideas.pending(run))
        editorial.process(run)
        submission.refresh_from_db(); run.refresh_from_db()
        self.assertEqual(submission.title, 'Ethereum')
        self.assertEqual(submission.public_title, 'Editor’s pick: Ethereum')
        self.assertEqual(run.inputs['title'], 'Ethereum')
        self.assertEqual(run.editorial, {})
        self.assertFalse(ideas.pending(run))
        request = json.loads(call.call_args.args[3]['messages'][0]['content'])
        self.assertIn('Bitcoin', request['existing_articles'])

    @patch('submissions.ai_providers.call', return_value=reply({'title': 'bitcoin', 'details': 'Duplicate subject of an existing page.'}))
    def test_duplicate_proposals_retry_then_block(self, call):
        Submission.objects.create(kind='request', title='Queued subject')
        submission = Submission.objects.create(kind='request', maintenance_key='idea:2026-01-01:1')
        run = self.run_for(submission)
        editorial.process(run)
        run.refresh_from_db()
        self.assertEqual(run.editorial['idea_attempts'], 1)
        self.assertEqual(run.editorial['idea_rejected'], ['bitcoin'])
        request = json.loads(call.call_args.args[3]['messages'][0]['content'])
        self.assertEqual(request['already_requested'], ['Queued subject'])
        for _ in range(2):
            editorial.process(run)
        run.refresh_from_db()
        self.assertEqual(run.state, 'blocked')
        self.assertEqual(run.last_error, 'idea_not_found')
        self.assertEqual(Submission.objects.get(pk=submission.pk).title, '')

    @patch('submissions.ai_providers.call', return_value=reply({'section': 'Timeline', 'details': 'Add the 2024 halving and ETF approvals.'}))
    def test_improvement_proposal_reads_article_and_keeps_valid_section(self, call):
        submission = Submission.objects.create(kind='improvement', article='bitcoin', title='Bitcoin', maintenance_key='idea:2026-01-01:1')
        run = self.run_for(submission)
        editorial.process(run)
        submission.refresh_from_db()
        self.assertEqual(submission.section, 'Timeline')
        self.assertEqual(submission.details, 'Add the 2024 halving and ETF approvals.')
        request = json.loads(call.call_args.args[3]['messages'][0]['content'])
        self.assertEqual(request['article'], 'x' * 4000)

    @override_settings(AUTOMATION_DAILY_LIMIT=10, MAINTENANCE_ENABLED=True)
    @patch('submissions.maintenance.enqueue')
    @patch('submissions.ideas.random.random', return_value=0.1)
    def test_readers_first_then_idea_before_maintenance(self, _, maintenance):
        from .autonomous_worker import schedule
        reader = Submission.objects.create(kind='request', title='Reader priority')
        self.assertEqual(schedule().submission_id, reader.pk)
        AutomationRun.objects.filter(submission=reader).update(state='published')
        idea = schedule()
        self.assertTrue(ideas.is_idea(idea.submission))
        maintenance.assert_not_called()
        # A later reader submission is started ahead of the active idea.
        late = Submission.objects.create(kind='request', title='Late reader')
        self.assertEqual(schedule().submission_id, late.pk)
