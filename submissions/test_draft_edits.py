"""Regression coverage for publishing useful partial edits without false certification."""
import copy
import json
from datetime import timedelta
from io import StringIO
from unittest.mock import patch
from django.test import TestCase, override_settings
from django.core.management import call_command
from django.utils import timezone
from . import editorial, verification
from .autonomous_worker import unblock_due, schedule
from .improvements import apply_patch, validate_patch, split_article
from .models import AutomationRun, ArticleRevision, Submission, Verification, ProviderSpend
from .test_verification import SOURCE, URL, evidence, report


class DraftEditTests(TestCase):
    def setUp(self):
        self.original = SOURCE.replace('status: draft', 'status: ai-fact-checked\nchecked: 2026-10-01\nchecked_by: historical-model high')
        self.submission = Submission.objects.create(kind='improvement', article='example', status='reviewing')
        self.run = AutomationRun.objects.create(submission=self.submission, state='checking', inputs={'article':'example'}, research={'content':evidence()[0]['content']})
        self.record = ArticleRevision.objects.create(run=self.run, slug='example', title='Example',
            original_markdown=self.original, base_content_hash=verification.digest(self.original), base_revision='a'*40)
        self.proposal = {'edits':[{'anchor':'## References','position':'before','markdown':'## History\n\nExample launched in 2009.[^1]'}],
                         'references':f'[^1]: [History]({URL})'}

    def candidate(self):
        validate_patch(self.record, self.proposal, self.run.research)
        return apply_patch(self.record, self.proposal, self.original)

    def start(self, source=None):
        self.run.draft = self.proposal
        editorial.begin_check(self.run, source or self.candidate())
        return Verification.objects.get(pk=self.run.editorial['check_id'])

    def scoped_report(self, check):
        result = report(check.source)
        ids = {u['id'] for u in verification.check_inventory(check)[0]}
        result['units'] = [u for u in result['units'] if u['id'] in ids]
        return result

    def test_unrelated_old_references_and_claims_do_not_block_edit(self):
        self.original = self.original.replace('## References', 'An old unrelated claim.[^old]\n\n## References') + '\n[^old]: [Old](https://unavailable.example.org/page)\n'
        self.record.original_markdown = self.original
        self.record.base_content_hash = verification.digest(self.original)
        self.record.save()
        check = self.start()
        units, urls = verification.check_inventory(check)
        self.assertEqual(urls, [URL])
        self.assertFalse(any('unrelated' in u['text'] for u in units))
        self.assertEqual(verification.validate_report(check, self.scoped_report(check), evidence())[0], [])

    def test_changed_reference_rechecks_existing_claim_even_when_text_is_identical(self):
        source = self.original.replace(URL, 'https://new.example.org/history')
        check = self.start(source)
        units, urls = verification.check_inventory(check)
        self.assertTrue(any('Example launched in 2009' in u['text'] for u in units))
        self.assertEqual(urls, ['https://new.example.org/history'])
        self.assertIn('unopened_references', verification.validate_report(check, self.scoped_report(check), evidence())[0])

    @patch('submissions.ai_providers.call')
    def test_scoped_pass_publishes_draft_and_preserves_check_history(self, call):
        check = self.start()
        call.return_value = evidence()[0]
        verification.step(check)  # Source collection only.
        self.assertEqual(check.state, 'pending')
        call.return_value = {'model':'independent-checker','stop_reason':'end_turn',
            'content':[{'type':'text','text':json.dumps(self.scoped_report(check))}]}
        verification.step(check)
        self.assertEqual(check.state, 'passed', check.report)
        metadata, _ = split_article(check.approved_source)
        self.assertEqual(metadata['status'], 'draft')
        self.assertEqual(metadata['checked'], '2026-10-01')
        self.assertEqual(metadata['checked_by'], 'historical-model high')
        self.assertEqual(metadata['written_by'], 'test-writer high')
        self.record.markdown = check.approved_source
        verification.require_verified(self.record)
        self.record.markdown += '\nChanged after approval.'
        with self.assertRaisesMessage(ValueError, 'publication_requires_exact_verified_source'):
            verification.require_verified(self.record)

    def test_reference_count_over_forty_is_valid_and_collection_stays_batched(self):
        extra = ''.join(f'\n[^r{i}]: [Source](https://example.com/ref-{i})\n' for i in range(60))
        check = Verification.objects.create(run=self.run, source=SOURCE+extra,
            source_hash=verification.digest(SOURCE+extra), session={'scope':'full'})
        self.assertEqual(len(verification.check_inventory(check)[1]), 61)
        with patch('submissions.ai_providers.call', return_value=evidence()[0]) as call:
            verification.step(check)
        request = call.call_args.args[3]
        self.assertEqual(len(json.loads(request['messages'][0]['content'])['missing_reference_urls']), 4)
        self.assertEqual(request['tools'][0]['max_uses'], 4)

    @patch('submissions.ai_providers.call')
    def test_small_heading_edit_needs_no_new_sources(self, call):
        self.original = self.original.replace('Example launched in 2009.[^1]', '## Origins\n\nExample launched in 2009.[^1]')
        self.record.original_markdown = self.original
        self.record.base_content_hash = verification.digest(self.original)
        self.record.save()
        self.proposal = {'edits':[{'anchor':'## Origins','position':'replace','markdown':'## History'}], 'references':''}
        check = self.start()
        self.assertEqual(verification.check_inventory(check)[1], [])
        call.return_value = {'model':'checker','stop_reason':'end_turn','content':[{'type':'text','text':json.dumps(self.scoped_report(check))}]}
        verification.step(check)
        self.assertEqual(check.state, 'passed', check.report)
        self.assertNotIn('tools', call.call_args.args[3])

    def test_existing_sources_can_be_reused_without_new_research(self):
        validate_patch(self.record, self.proposal, {'content':[]})

    def test_empty_or_noop_edit_cannot_be_approved(self):
        check = self.start(self.original)
        with self.assertRaisesMessage(ValueError, 'no_useful_edit'):
            verification.step(check)

    def test_insufficient_writer_response_tries_smaller_edit_not_full_article_check(self):
        self.run.editorial = {'stage':'write','revisions':0}
        self.run.save()
        response = {'stop_reason':'end_turn','content':[{'type':'text','text':'{"insufficient_evidence":true}'}]}
        with patch('submissions.ai_providers.write_improvement', return_value=response):
            editorial.process(self.run)
        self.run.refresh_from_db()
        self.assertEqual(self.run.state, 'revising')
        self.assertFalse(self.run.verifications.exists())
        self.assertIn('smaller', str(self.run.editorial['feedback']))

    def test_reopened_technical_failure_retains_audit_and_spend_and_is_idempotent(self):
        self.run.state = 'insufficient'
        self.run.editorial = {'stage':'check','feedback':'verification_reference_limit'}
        self.run.save()
        self.submission.status = 'insufficient'; self.submission.save()
        editorial.event(self.run, 'decision', state='insufficient')
        ProviderSpend.objects.create(run=self.run, provider='anthropic', stage='writing', reserved_tokens=100, input_tokens=50, output_tokens=10, state='completed')
        old = Verification.objects.create(run=self.run, source=SOURCE, source_hash=verification.digest(SOURCE), state='pending')
        with patch('submissions.management.commands.reopen_suggestions.publication_lock'):
            for _ in range(2):
                call_command('reopen_suggestions', all_stalled=True, stdout=StringIO())
        self.run.refresh_from_db(); self.submission.refresh_from_db(); old.refresh_from_db()
        self.assertEqual(self.run.state, 'queued')
        self.assertEqual(self.submission.status, 'reviewing')
        self.assertEqual(old.state, 'pending')
        self.assertEqual(self.run.events.filter(kind='workflow_recovered').count(), 1)
        self.assertEqual(self.run.spend.get().input_tokens, 50)
        self.assertFalse(self.run.verifications.filter(state='passed').exists())

    def test_incomplete_report_retry_keeps_evidence_and_completed_groups(self):
        check = self.start()
        check.state = 'incomplete'
        check.session.update(payload=verification.payload(check), responses=evidence(), mode='report',
            batches=[{'ids':['5'], 'report':{'verdict':'pass'}, 'responses':[]}, {'ids':['6'], 'responses':[{'stop_reason':'max_tokens'}]}])
        check.save()
        editorial.block(self.run, 'verification_report_incomplete')
        self.run.next_attempt_at = timezone.now()-timedelta(seconds=1); self.run.save()
        unblock_due(); self.run.refresh_from_db()
        resumed = self.run.verifications.get(pk=self.run.editorial['check_id'])
        self.assertNotEqual(resumed.pk, check.pk)
        self.assertEqual(resumed.session['responses'], evidence())
        self.assertIn('report', resumed.session['batches'][0])
        self.assertEqual(resumed.session['batches'][1]['responses'], [])
        self.assertEqual(Verification.objects.get(pk=check.pk).state, 'incomplete')

    def test_budget_raise_wakes_saved_step_without_resetting_usage(self):
        self.run.state='blocked';self.run.last_error='run_token_budget'
        self.run.editorial={'stage':'research', 'budget_block':{'required':1500,'limit':1000}}
        self.run.save()
        with override_settings(EDITORIAL_RUN_TOKEN_LIMIT=1200):unblock_due()
        self.run.refresh_from_db();self.assertEqual(self.run.state,'blocked')
        with override_settings(EDITORIAL_RUN_TOKEN_LIMIT=2000):unblock_due()
        self.run.refresh_from_db();self.assertEqual(self.run.state,'queued')

    @override_settings(MAINTENANCE_ENABLED=True)
    def test_reader_preempts_active_maintenance(self):
        self.submission.kind='maintenance';self.submission.save()
        reader=Submission.objects.create(kind='improvement',article='example')
        self.assertEqual(schedule().submission_id, reader.pk)

    def test_background_checks_are_deduplicated_and_queued_even_if_fresh(self):
        from .maintenance import queue_full_check
        self.record.content_hash='a'*64
        queue_full_check(self.record);queue_full_check(self.record)
        self.assertEqual(Submission.objects.filter(kind='maintenance', article='example').count(),1)

    def test_public_tracker_shows_partial_result_and_maintenance_separately(self):
        from . import tracking
        self.submission.status='resolved';self.submission.public_summary='Updated a section.';self.submission.save()
        self.run.state='published';self.run.editorial={'fulfillment':'partial'};self.run.save()
        row = tracking.present(tracking.queryset().get(pk=self.submission.pk), {'example':{'title':'Example'}})
        self.assertEqual(row['status_label'],'Partly updated')
        self.assertEqual(row['title'],'Example')
        Submission.objects.create(kind='maintenance',article='example')
        with patch('submissions.views.articles', return_value={}):
            self.assertEqual(self.client.get('/submit/all/').context['page'].paginator.count, 1)
            self.assertEqual(self.client.get('/submit/all/?type=maintenance').context['page'].paginator.count, 1)

    def test_partial_screening_is_accepted_but_no_progress_is_not(self):
        from .ai_providers import approved_improvement
        from .test_automation import decision
        self.assertTrue(approved_improvement(decision(suitable='yes', coverage='partial')))
        self.assertFalse(approved_improvement(decision(suitable='yes', coverage='none')))

    @override_settings(MAINTENANCE_ENABLED=False)
    def test_disabled_maintenance_does_not_start_queued_background_check(self):
        self.run.state='published';self.run.save()
        self.submission.status='resolved';self.submission.save()
        Submission.objects.create(kind='maintenance',article='example')
        self.assertIsNone(schedule())

    def test_private_gift_link_token_cannot_be_published_in_a_citation(self):
        private_url=URL+'?accessToken=private-gift-token'
        self.proposal['references']=f'[^1]: [History]({private_url})'
        research={'content':evidence(url=private_url)[0]['content']}
        with self.assertRaisesMessage(ValueError, 'private_source_url'):
            validate_patch(self.record,self.proposal,research)
