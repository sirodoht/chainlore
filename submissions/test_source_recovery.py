import json
from io import StringIO
from unittest.mock import patch

from django.core.management import call_command, CommandError
from django.test import TestCase, override_settings
from django.utils import timezone

from . import editorial
from .models import AutomationRun, Submission, Verification, AutomationEvent
from .verification import digest, payload, source_gaps, step, report_payload, inventory
from .test_verification import SOURCE, evidence, report


@override_settings(VERIFICATION_BATCH_SIZE=100)
class SourceRecoveryTests(TestCase):
    def setUp(self):
        self.run = AutomationRun.objects.create(submission=Submission.objects.create(kind='correction', status='reviewing'),
            state='checking', draft={'saved': True}, research={'saved': True})
        self.check = Verification.objects.create(run=self.run, source=SOURCE, source_hash=digest(SOURCE))
        self.run.editorial = {'stage':'check', 'check_id':self.check.pk, 'candidate':SOURCE, 'revisions':0}
        self.run.save()

    def response(self, blocks, stop='end_turn'):
        return {'stop_reason':stop, 'model':'test-checker', 'content':blocks}

    def ready_report(self):
        return self.response([{'type':'text','text':json.dumps(report())}])

    def missing_search(self):
        self.check.session = {'payload':payload(self.check), 'responses':[
            self.response([evidence()[0]['content'][1]], 'max_tokens')], 'mode':'report'}
        self.check.save()

    def test_reports_keep_readable_search_evidence_and_preserve_opaque_audit(self):
        responses=evidence()
        search=responses[0]['content'][0]['content'][0]
        search.update(encrypted_content='opaque-provider-blob',title='History update',page_age='2026-10-31',snippet='Readable evidence')
        self.check.session={'payload':payload(self.check),'responses':responses,'mode':'report'}
        request=report_payload(self.check,inventory(SOURCE)[0])
        data=json.loads(request['messages'][0]['content'])
        clean=data['freshness_search_results'][0]['content'][0]
        self.assertNotIn('encrypted_content',clean)
        self.assertEqual(clean['snippet'],'Readable evidence')
        self.assertEqual(clean['title'],'History update')
        self.assertEqual(clean['url'],search['url'])
        self.assertEqual(search['encrypted_content'],'opaque-provider-blob')

    @patch('submissions.ai_providers.call')
    def test_truncated_source_pass_finishes_search_before_any_report(self, call):
        opened = self.response([evidence()[0]['content'][1]], 'max_tokens')
        search = self.response([evidence()[0]['content'][0]])
        call.side_effect = [opened, search, self.ready_report()]
        editorial.process(self.run)
        self.check.refresh_from_db()
        self.assertEqual(self.check.session['mode'], 'sources')
        self.run.refresh_from_db(); editorial.process(self.run)
        self.check.refresh_from_db(); self.run.refresh_from_db()
        self.assertEqual(call.call_args.args[2], 'fact_check_sources')
        self.assertEqual([t['name'] for t in call.call_args.args[3]['tools']], ['web_search'])
        self.assertEqual(self.run.editorial['revisions'], 0)
        self.assertEqual(self.run.draft, {'saved':True})
        self.assertEqual(self.check.state, 'pending')
        self.assertEqual(self.check.approved_hash, '')
        step(self.check)
        self.assertEqual(self.check.state, 'passed')
        self.assertEqual(call.call_args.args[2], 'fact_check_report')
        self.assertNotIn('tools', call.call_args.args[3])

    @patch('submissions.ai_providers.call')
    def test_missing_reference_uses_fetch_only_and_never_accepts_a_textual_completion(self, call):
        self.check.session={'payload':payload(self.check), 'responses':[self.response([evidence()[0]['content'][0]])], 'mode':'report'}
        self.check.save()
        call.side_effect=[self.response([{'type':'text','text':'All references opened.'}]),
                          self.response([evidence()[0]['content'][1]])]
        step(self.check)
        self.assertEqual([t['name'] for t in call.call_args.args[3]['tools']], ['web_fetch'])
        self.assertEqual(source_gaps(self.check)['missing_urls'], ['https://example.com/history'])
        self.assertEqual(self.check.approved_hash, '')
        step(self.check)
        self.assertEqual(source_gaps(self.check), {'missing_urls':[], 'search_missing':False})
        self.assertEqual(self.check.state, 'pending')

    @patch('submissions.ai_providers.call')
    def test_repeated_tool_failures_block_without_rejecting_or_rewriting(self, call):
        self.missing_search()
        call.return_value=self.response([{'type':'web_search_tool_result','content':{'type':'web_search_tool_result_error','error_code':'unavailable'}}])
        for _ in range(3):
            self.run.refresh_from_db(); editorial.process(self.run)
        self.run.refresh_from_db(); self.check.refresh_from_db(); self.run.submission.refresh_from_db()
        self.assertEqual(self.check.state,'incomplete')
        self.assertEqual(self.check.report['errors'],['verification_sources_incomplete'])
        self.assertEqual(self.run.state,'blocked')
        self.assertEqual(self.run.submission.status,'reviewing')
        self.assertEqual(self.run.editorial['revisions'],0)
        step(self.check)
        self.assertEqual(call.call_count,3)

    @patch('submissions.ai_providers.call')
    def test_saved_search_is_assessed_after_restart_without_a_paid_call(self, call):
        self.missing_search()
        self.check.session['source_recovery']={'responses':[self.response([evidence()[0]['content'][0]])],
            'processed_responses':0, 'before':{'missing_urls':[], 'search_missing':True}}
        self.check.save()
        step(self.check)
        call.assert_not_called()
        self.assertEqual(self.check.session['mode'],'report')
        self.assertEqual(self.check.approved_hash,'')

    @patch('submissions.ai_providers.call')
    def test_complete_sources_do_not_hide_genuine_checker_findings(self, call):
        self.check.session={'payload':payload(self.check), 'responses':evidence(), 'mode':'report'}
        self.check.save()
        finding=report(); finding.update(verdict='revise', issues=['Correct the launch date.'])
        call.return_value=self.response([{'type':'text','text':json.dumps(finding)}])
        editorial.process(self.run)
        self.run.refresh_from_db(); self.check.refresh_from_db()
        self.assertEqual(self.check.state,'failed')
        self.assertEqual(self.run.state,'revising')
        self.assertEqual(self.run.editorial['revisions'],1)

    @patch('submissions.management.commands.resume_verification.publication_lock')
    def test_reopen_only_source_failure_preserves_old_outcome_and_revision_count(self, lock):
        self.missing_search()
        assessment=report(); assessment.update(verdict='insufficient',freshness_checked=False,issues=['Missing live search.'])
        self.check.state='failed'; self.check.completed_at=timezone.now()
        self.check.report={'assessment':assessment,'errors':['no_live_freshness_search','source_or_freshness_check_missing','checker_did_not_pass','unresolved_checker_issues']}
        self.check.save()
        self.run.editorial['revisions']=2;self.run.save()
        editorial.insufficient(self.run,'Processing ended before source collection completed.')
        with self.assertRaises(CommandError):
            call_command('resume_verification',submission=str(self.run.submission_id),stdout=StringIO())
        self.check.report['errors'].append('unsupported_unit_5');self.check.save()
        with self.assertRaises(CommandError):
            call_command('resume_verification',submission=str(self.run.submission_id),reopen_incomplete_sources=True,stdout=StringIO())
        self.check.report['errors'].remove('unsupported_unit_5');self.check.save()
        call_command('resume_verification',submission=str(self.run.submission_id),reopen_incomplete_sources=True,stdout=StringIO())
        self.run.refresh_from_db();self.check.refresh_from_db();self.run.submission.refresh_from_db()
        self.assertEqual(self.check.state,'failed')
        self.assertEqual(self.run.state,'checking')
        self.assertEqual(self.run.submission.status,'reviewing')
        self.assertEqual(self.run.editorial['revisions'],2)
        recovered=self.run.verifications.order_by('-pk').first()
        self.assertEqual(recovered.source_hash,self.check.source_hash)
        self.assertEqual(recovered.session['mode'],'sources')
        self.assertEqual(recovered.approved_hash,'')
        self.assertTrue(self.run.events.filter(kind='decision',data__state='insufficient').exists())

    @patch('submissions.management.commands.resume_verification.publication_lock')
    def test_higher_report_allowance_preserves_completed_groups_and_previous_attempts(self, lock):
        completed={'ids':['1'],'responses':[],'report':{'units':[report()['units'][0]]},'checker':'test-checker'}
        stopped=self.response([], 'max_tokens');stopped['usage']={'input_tokens':10,'output_tokens':16000}
        unfinished={'ids':[u['id'] for u in report()['units'][1:]],'responses':[stopped,stopped],'processed_responses':2}
        self.check.session={'payload':payload(self.check),'responses':evidence(),'mode':'report','batches':[completed,unfinished]}
        self.check.state='incomplete';self.check.completed_at=timezone.now()
        self.check.report={'assessment':{},'errors':['verification_output_incomplete']};self.check.save()
        self.run.state='blocked';self.run.save()
        with override_settings(VERIFICATION_REPORT_TOKENS=16000), self.assertRaises(CommandError):
            call_command('resume_verification',submission=str(self.run.submission_id),increase_report_allowance=True,stdout=StringIO())
        call_command('resume_verification',submission=str(self.run.submission_id),increase_report_allowance=True,stdout=StringIO())
        recovered=self.run.verifications.order_by('-pk').first()
        self.assertEqual(recovered.session['batches'][0],completed)
        pending=recovered.session['batches'][1]
        self.assertEqual(pending['responses'],[])
        self.assertEqual(len(pending['previous_attempts'][0]['responses']),2)
        self.assertEqual(pending['output_allowance'],32000)
        self.assertEqual(recovered.approved_hash,'')
