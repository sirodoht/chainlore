import hashlib
import importlib
import importlib.util
from types import SimpleNamespace
from unittest.mock import patch
from django.apps import apps
from django.conf import settings
from django.db import connection
from django.test import SimpleTestCase, TestCase, override_settings
from . import ai_providers as ai
from .attribution import historical_writer_credit
from .models import AutomationEvent, AutomationRun, GeneratedArticle, Submission
from .test_automation import DRAFT, RESEARCH, written
from .automation import draft_article


class WriterAttributionTests(SimpleTestCase):
    @override_settings(ANTHROPIC_MODEL='requested-alias')
    def test_provider_model_and_actual_effort_override_generated_credit(self):
        response = written({**DRAFT, '_written_by': 'Forged credit', 'written_by': 'Forged credit'})
        response['model'] = 'resolved-model-v2'
        response.pop('_written_by')
        run = SimpleNamespace(inputs={}, research=RESEARCH)
        with patch.object(ai, 'call', return_value=response) as call:
            draft = draft_article(run)
        self.assertEqual(draft['_written_by'], 'resolved-model-v2 (high effort)')
        self.assertEqual(call.call_args.args[3]['model'], 'requested-alias')

    def test_missing_response_model_uses_requested_model(self):
        with override_settings(ANTHROPIC_MODEL='requested-version'), patch.object(ai, 'call', return_value={}):
            response = ai.write_article(SimpleNamespace(inputs={}, research=RESEARCH))
        self.assertEqual(response['_written_by'], 'requested-version (high effort)')

    def test_recovery_matches_the_saved_text_instead_of_a_later_attempt(self):
        events = [
            SimpleNamespace(kind='writing_request', data={'model': 'original-model', 'output_config': {'effort': 'high'}}),
            SimpleNamespace(kind='writing_response', data=written()),
            SimpleNamespace(kind='writing_request', data={'model': 'later-model'}),
            SimpleNamespace(kind='writing_response', data=written({**DRAFT, 'markdown': 'A different draft'})),
        ]
        self.assertEqual(historical_writer_credit(events, DRAFT['markdown']), 'original-model (high effort)')
        self.assertEqual(historical_writer_credit(events, 'Unrecorded text'), 'Unknown')


class AttributionMigrationTests(TestCase):
    def test_backfill_uses_matching_history_and_updates_hash_without_rewriting_body(self):
        migration = importlib.import_module('submissions.migrations.0006_article_writer_credits')
        for slug, expected in [('recorded', 'historical-model (high effort)'), ('missing', 'Unknown'),
                               ('placeholder', 'Chainlore template (no model)')]:
            run = AutomationRun.objects.create(submission=Submission.objects.create(kind='request', title=slug))
            body = DRAFT['markdown'] if slug != 'placeholder' else (
                f'{slug} is the subject of a reader request that Chainlore accepted as a cryptocurrency topic. '
                'This is a placeholder: automated research could not produce a full article.')
            source = f'---\ntitle: {slug}\nstatus: draft\n---\n\n{body}'
            record = GeneratedArticle.objects.create(slug=slug, run=run, title=slug, markdown=source, content_hash='old')
            if slug == 'recorded':
                AutomationEvent.objects.create(run=run, kind='writing_request', data={'model': 'historical-model', 'output_config': {'effort': 'high'}})
                AutomationEvent.objects.create(run=run, kind='writing_response', data=written())
                AutomationEvent.objects.create(run=run, kind='writing_response', data=written({**DRAFT, 'markdown': None}))
                AutomationEvent.objects.create(run=run, kind='writing_request', data={'model': 'later-model'})
                AutomationEvent.objects.create(run=run, kind='writing_response', data=written({**DRAFT, 'markdown': 'Unpublished replacement'}))
            if slug == 'placeholder':
                AutomationEvent.objects.create(run=run, kind='placeholder_used', data={})
            migration.backfill(apps, SimpleNamespace(connection=connection))
            record.refresh_from_db()
            self.assertIn(f'written_by: {expected}\n', record.markdown)
            self.assertEqual(record.markdown.split('---\n', 2)[2], source.split('---\n', 2)[2])
            self.assertEqual(record.content_hash, hashlib.sha256(record.markdown.encode()).hexdigest())
            migration.backfill(apps, SimpleNamespace(connection=connection))
            record.refresh_from_db()
            self.assertEqual(record.markdown.count('written_by:'), 1)


class ArticleCreditDisplayTests(SimpleTestCase):
    def test_required_writer_and_current_check_credits(self):
        spec = importlib.util.spec_from_file_location('chainlore_build', settings.BASE_DIR / 'scripts/build.py')
        build = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build)
        path = settings.BASE_DIR / 'pages/bitcoin.md'
        # render() resolves all cross-article links, even when testing one page.
        for article in (settings.BASE_DIR / 'pages').glob('*.md'):
            build.ROUTES['pages/' + article.name] = '/p/' + article.stem + '/'
        page = build.render(path)
        with patch.object(build, 'write_page') as write:
            build.article(page)
        html = write.call_args.args[2]
        self.assertIn('Written by Opus 5.5 High', html)
        self.assertIn('Fact-checked by GPT-6-Astra high on 30 October 2026', html)
        page = build.render(path)
        page['meta']['status'] = 'draft'
        with patch.object(build, 'write_page') as write:
            build.article(page)
        self.assertNotIn('Fact-checked by', write.call_args.args[2])
        del page['meta']['written_by']
        self.assertIn('bitcoin.md: missing written_by', build.validate(page['meta'], path))
