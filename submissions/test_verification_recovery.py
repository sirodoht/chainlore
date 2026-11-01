import copy
import json
from io import StringIO
from unittest.mock import patch
from django.test import TestCase, override_settings
from django.core.management import call_command, CommandError
from django.utils import timezone
from .models import Submission, AutomationRun, Verification, AutomationEvent, ProviderSpend
from .verification import digest, payload, step
from .budgets import reserve, complete, totals, BudgetExceeded, estimate
from .test_verification import SOURCE, evidence, report
from . import editorial


@override_settings(VERIFICATION_BATCH_SIZE=100)
class VerificationRecoveryTests(TestCase):
    def setUp(self):
        self.run=AutomationRun.objects.create(submission=Submission.objects.create(kind='correction',status='reviewing'),
            state='checking',draft={'edits':['saved']},research={'saved':'research'})
        self.check=Verification.objects.create(run=self.run,source=SOURCE,source_hash=digest(SOURCE))
        self.run.editorial={'stage':'check','check_id':self.check.pk,'candidate':SOURCE,'revisions':0}
        self.run.save()

    def truncated(self):
        response=evidence()[0]
        response.update(stop_reason='max_tokens',model='checker high')
        response['content'].append({'type':'text','text':'{"units": ['})
        return response

    def finished(self):
        return {'stop_reason':'end_turn','model':'checker-v1','content':[{'type':'text','text':json.dumps(report())}]}

    @patch('submissions.ai_providers.call')
    def test_truncation_preserves_draft_and_reuses_independent_evidence(self,call):
        call.side_effect=[self.truncated(),self.finished()]
        editorial.process(self.run)
        self.run.refresh_from_db();self.check.refresh_from_db()
        self.assertEqual(self.run.state,'checking')
        self.assertEqual(self.run.editorial['revisions'],0)
        self.assertEqual(self.run.draft,{'edits':['saved']})
        self.assertEqual(self.run.research,{'saved':'research'})
        self.assertEqual(self.check.state,'pending')
        step(self.check)
        self.assertEqual(self.check.state,'passed')
        request=call.call_args.args[3]
        self.assertEqual(call.call_args.args[2],'fact_check_report')
        self.assertNotIn('tools',request)
        self.assertEqual(request['max_tokens'],32000)
        data=json.loads(request['messages'][0]['content'])
        self.assertIn('https://example.com/history',data['fetched_sources'])
        self.assertNotIn('writer_research',data)
        self.assertEqual(data['article'],SOURCE)

    @patch('submissions.ai_providers.call')
    def test_repeated_incomplete_reports_block_without_rewriting(self,call):
        call.return_value=self.truncated()
        for _ in range(3):
            self.run.refresh_from_db();editorial.process(self.run)
        self.run.refresh_from_db();self.check.refresh_from_db()
        self.assertEqual(call.call_count,3)
        self.assertEqual(self.check.state,'incomplete')
        self.assertEqual(self.run.state,'blocked')
        self.assertEqual(self.run.editorial['revisions'],0)
        self.assertEqual(self.run.draft,{'edits':['saved']})
        self.assertIsNone(self.run.next_attempt_at)
        step(self.check)
        self.assertEqual(call.call_count,3)

    @patch('submissions.ai_providers.call')
    def test_saved_response_is_assessed_after_crash_without_another_paid_call(self,call):
        self.check.session={'payload':payload(self.check),'responses':evidence(),'mode':'report','batches':[{'ids':[u['id'] for u in report()['units']],'responses':[self.finished()]}]}
        self.check.save()
        step(self.check)
        call.assert_not_called()
        self.assertEqual(self.check.state,'passed')

    @patch('submissions.ai_providers.call')
    def test_saved_evidence_can_finish_on_a_later_day_with_a_new_report(self,call):
        original=payload(self.check);data=json.loads(original['messages'][0]['content']);data['today']='2000-01-01'
        original['messages'][0]['content']=json.dumps(data)
        self.check.session={'payload':original,'responses':evidence(),'mode':'report'};self.check.save()
        call.return_value=self.finished()
        step(self.check)
        self.assertEqual(self.check.state,'passed')
        self.assertEqual(json.loads(call.call_args.args[3]['messages'][0]['content'])['today'],timezone.localdate().isoformat())

    @patch('submissions.management.commands.resume_verification.publication_lock')
    def test_recovery_retains_failed_audit_and_restores_same_candidate(self,lock):
        self.run.state='blocked';self.run.last_error='run_token_budget'
        self.run.editorial.update(stage='research',revisions=1);self.run.save()
        self.check.state='failed';self.check.completed_at=timezone.now()
        self.check.report={'errors':['invalid_check_report']}
        self.check.session={'payload':payload(self.check),'responses':[self.truncated()]};self.check.save()
        call_command('resume_verification',submission=str(self.run.submission_id),stdout=StringIO())
        self.run.refresh_from_db();self.check.refresh_from_db()
        self.assertEqual(self.check.state,'failed')
        self.assertEqual(self.run.state,'checking')
        self.assertEqual(self.run.editorial['revisions'],0)
        resumed=Verification.objects.get(pk=self.run.editorial['check_id'])
        self.assertEqual(resumed.source,self.check.source)
        self.assertEqual(resumed.session['responses'],self.check.session['responses'])
        self.assertEqual(resumed.state,'pending')
        self.assertEqual(resumed.approved_hash,'')
        with self.assertRaises(CommandError):
            call_command('resume_verification',submission=str(self.run.submission_id),stdout=StringIO())

    @patch('submissions.management.commands.resume_verification.publication_lock')
    def test_recovery_cannot_bypass_factual_findings(self,lock):
        self.run.state='blocked';self.run.save()
        self.check.state='failed';self.check.report={'errors':['unsupported_unit_4']};self.check.save()
        with self.assertRaises(CommandError):
            call_command('resume_verification',submission=str(self.run.submission_id),stdout=StringIO())
        self.assertEqual(self.run.verifications.count(),1)

    @patch('submissions.ai_providers.call')
    def test_contradictory_pass_retries_report_with_feedback_without_rewriting(self,call):
        self.check.session={'payload':payload(self.check),'responses':evidence(),'mode':'report'}
        self.check.save()
        invalid=report();invalid['source_rules_met']=False
        invalid['units'][0]['claims'][0]['quote']='A quote absent from the source'
        call.return_value={'stop_reason':'end_turn','model':'checker-v1','content':[{'type':'text','text':json.dumps(invalid)}]}
        editorial.process(self.run)
        self.run.refresh_from_db();self.check.refresh_from_db()
        self.assertEqual(self.run.state,'checking')
        self.assertEqual(self.run.editorial['revisions'],0)
        self.assertEqual(self.check.approved_hash,'')
        call.return_value=self.finished()
        step(self.check)
        self.assertEqual(self.check.state,'passed')
        data=json.loads(call.call_args.args[3]['messages'][0]['content'])
        self.assertIn('source_rules_check_missing',data['previous_report_validation_errors'])
        self.assertEqual(data['previous_report'],invalid)

    @patch('submissions.management.commands.resume_verification.publication_lock')
    def test_contradictory_recovery_preserves_attempts_and_rejects_later_paid_work(self,lock):
        self.run.state='revising';self.run.editorial.update(stage='research',revisions=1);self.run.save()
        invalid=report();invalid['freshness_checked']=False
        self.check.state='failed';self.check.completed_at=timezone.now()
        self.check.report={'assessment':invalid,'errors':['source_or_freshness_check_missing']}
        batch={'ids':[u['id'] for u in invalid['units']], 'responses':[self.finished()], 'processed_responses':1}
        self.check.session={'payload':payload(self.check),'responses':evidence(),'mode':'report','batches':[batch]};self.check.save()
        spend=reserve(self.run,'anthropic','research',{'max_tokens':10})
        with self.assertRaisesMessage(CommandError,'Later paid work exists'):
            call_command('resume_verification',submission=str(self.run.submission_id),stdout=StringIO())
        spend.delete()
        call_command('resume_verification',submission=str(self.run.submission_id),stdout=StringIO())
        self.run.refresh_from_db()
        resumed=Verification.objects.get(pk=self.run.editorial['check_id'])
        self.assertEqual(len(resumed.session['batches'][0]['responses']),1)
        self.assertEqual(resumed.session['batches'][0]['processed_responses'],1)
        self.assertEqual(resumed.approved_hash,'')
        self.assertEqual(self.run.editorial['revisions'],0)


@override_settings(EDITORIAL_DAILY_TOKEN_LIMIT=1000,EDITORIAL_RUN_TOKEN_LIMIT=1000)
class BudgetSettlementTests(TestCase):
    def setUp(self):
        self.run=AutomationRun.objects.create(submission=Submission.objects.create(kind='request'))

    def test_completed_usage_releases_unused_estimate(self):
        entry=reserve(self.run,'anthropic','check',{'max_tokens':800})
        complete(entry,{'usage':{'input_tokens':50,'output_tokens':50}})
        reserve(self.run,'anthropic','check',{'max_tokens':800})
        self.assertEqual(totals(ProviderSpend.objects.all())['accounted'],100+estimate({'max_tokens':800}))

    def test_actual_overrun_and_cache_tokens_are_charged(self):
        entry=reserve(self.run,'anthropic','check',{'max_tokens':100})
        complete(entry,{'usage':{'input_tokens':100,'output_tokens':300,'cache_read_input_tokens':400,'cache_creation_input_tokens':100}})
        self.assertEqual(totals(ProviderSpend.objects.all())['accounted'],900)
        with self.assertRaisesMessage(BudgetExceeded,'run_token_budget'):
            reserve(self.run,'anthropic','check',{'max_tokens':100})

    def test_missing_or_invalid_usage_keeps_reservation(self):
        entry=reserve(self.run,'anthropic','check',{'max_tokens':800})
        for result in ({},{'usage':{}},{'usage':{'input_tokens':-1,'output_tokens':2}}):
            complete(entry,result)
            entry.refresh_from_db();self.assertEqual(entry.state,'reserved')
            with self.assertRaises(BudgetExceeded):reserve(self.run,'anthropic','check',{'max_tokens':800})

    def test_daily_limit_includes_other_runs_actual_usage(self):
        entry=reserve(self.run,'anthropic','check',{'max_tokens':100})
        complete(entry,{'usage':{'input_tokens':600,'output_tokens':200}})
        other=AutomationRun.objects.create(submission=Submission.objects.create(kind='request'))
        with self.assertRaisesMessage(BudgetExceeded,'daily_token_budget'):
            reserve(other,'anthropic','check',{'max_tokens':300})

    def test_server_tools_receive_extra_reservation_headroom(self):
        plain={'max_tokens':100}
        tools={**plain,'tools':[{'max_uses':2,'max_content_tokens':4000}]}
        self.assertGreater(estimate(tools),3*estimate(plain))

    @override_settings(EDITORIAL_DAILY_TOKEN_LIMIT=1000000,EDITORIAL_RUN_TOKEN_LIMIT=1000000)
    @patch('submissions.ai_providers.credential',return_value='test')
    @patch('submissions.ai_providers.urllib.request.urlopen')
    def test_report_transport_has_its_own_output_allowance(self,transport,credential):
        from .ai_providers import call
        transport.return_value.__enter__.return_value.read.return_value=json.dumps({'usage':{'input_tokens':10,'output_tokens':10}}).encode()
        call(self.run,'anthropic','fact_check_report',{'max_tokens':64000,'model':'test'})
        self.assertEqual(json.loads(transport.call_args.args[0].data)['max_tokens'],32000)

@override_settings(VERIFICATION_BATCH_SIZE=2)
class GroupCoverageTests(TestCase):
    def setUp(self):
        self.run=AutomationRun.objects.create(submission=Submission.objects.create(kind='request'))
        self.check=Verification.objects.create(run=self.run,source=SOURCE,source_hash=digest(SOURCE))
        self.check.session={'payload':payload(self.check),'responses':evidence(),'mode':'report'}
        self.check.save()

    @patch('submissions.ai_providers.call')
    def test_only_complete_group_coverage_can_approve(self,call):
        def answer(run,provider,stage,request,**kwargs):
            data=json.loads(request['messages'][0]['content'])
            result=report();ids={u['id'] for u in data['units']}
            self.assertLessEqual(len(ids),2)
            result['units']=[u for u in result['units'] if u['id'] in ids]
            return {'stop_reason':'end_turn','model':'checker-test','content':[{'type':'text','text':json.dumps(result)}]}
        call.side_effect=answer
        step(self.check)
        self.assertEqual(self.check.state,'pending')
        self.assertEqual(self.check.approved_hash,'')
        self.check.refresh_from_db()
        while self.check.state=='pending':step(self.check)
        self.assertEqual(self.check.state,'passed')
        self.assertEqual({u['id'] for u in self.check.report['assessment']['units']},{u['id'] for u in report()['units']})
        self.assertEqual(len(self.check.report['assessment']['units']),len(report()['units']))

    @patch('submissions.ai_providers.call')
    def test_whole_report_cannot_skip_current_group_contract(self,call):
        call.return_value={'stop_reason':'end_turn','model':'checker-test','content':[{'type':'text','text':json.dumps(report())}]}
        step(self.check)
        self.assertEqual(self.check.state,'pending')
        self.assertEqual(self.check.report['errors'],['verification_report_incomplete'])
        self.assertEqual(self.check.approved_hash,'')

    def group_answer(self, request, findings=None):
        data=json.loads(request['messages'][0]['content'])
        result=report();ids={u['id'] for u in data['units']}
        result['units']=[u for u in result['units'] if u['id'] in ids]
        for unit in result['units']:
            if findings and unit['id'] in findings:
                unit.update(verdict='unsupported', claims=[])
                result['verdict']='revise'
                result['issues'].append(findings[unit['id']])
        return {'stop_reason':'end_turn','model':'checker-test','content':[{'type':'text','text':json.dumps(result)}]}

    @patch('submissions.ai_providers.call')
    def test_all_groups_feed_one_revision_and_survive_restart(self, call):
        self.run.submission.status='reviewing';self.run.submission.save()
        self.run.state='checking'
        self.run.editorial={'stage':'check','check_id':self.check.pk,'candidate':SOURCE,'revisions':0}
        self.run.save()
        units=report()['units']
        findings={units[0]['id']:'Correct the title.', units[-1]['id']:'Correct the final row.'}
        seen=[]
        def answer(run, provider, stage, request, **kwargs):
            seen.extend(u['id'] for u in json.loads(request['messages'][0]['content'])['units'])
            return self.group_answer(request, findings)
        call.side_effect=answer
        for _ in range((len(units)+1)//2):
            self.run.refresh_from_db()
            editorial.process(self.run)
            self.run.refresh_from_db();self.check.refresh_from_db()
            if len(seen)<len(units):
                self.assertEqual(self.run.state,'checking')
                self.assertEqual(self.run.editorial['revisions'],0)
                self.assertIsNone(self.check.completed_at)
            self.assertEqual(self.check.approved_hash,'')
        self.assertEqual(seen,[u['id'] for u in units])
        self.assertEqual(self.check.state,'failed')
        self.assertEqual(self.run.editorial['revisions'],1)
        self.assertEqual(self.run.editorial['stage'],'write')
        self.assertEqual(self.run.editorial['feedback']['assessment']['issues'],list(findings.values()))
        self.assertEqual(self.run.editorial['revision_progress']['supported'],len(units)-2)
        self.assertEqual(self.run.events.filter(kind='revision_requested').count(),1)
        self.assertEqual(self.run.events.filter(kind='verification_group_findings').count(),2)

    @patch('submissions.ai_providers.call')
    def test_later_pass_cannot_erase_earlier_failure_or_source_rules(self, call):
        first_id=report()['units'][0]['id']
        def answer(run,provider,stage,request,**kwargs):
            response=self.group_answer(request,{first_id:'Narrow the title.'})
            result=json.loads(response['content'][0]['text'])
            if result['issues']:
                result['source_rules_met']=False
            response['content'][0]['text']=json.dumps(result)
            return response
        call.side_effect=answer
        for _ in range((len(report()['units'])+1)//2):
            step(self.check);self.check.refresh_from_db()
        self.assertEqual(self.check.state,'failed')
        self.assertEqual(self.check.report['assessment']['issues'],['Narrow the title.'])
        self.assertFalse(self.check.report['assessment']['source_rules_met'])
        self.assertIn('source_rules_check_missing',self.check.report['errors'])
        self.assertEqual(self.check.approved_hash,'')

    @patch('submissions.ai_providers.call')
    def test_interrupted_later_group_preserves_earlier_findings(self, call):
        first_id=report()['units'][0]['id']
        call.side_effect=lambda run,provider,stage,request,**kwargs:self.group_answer(request,{first_id:'Fix the title.'})
        step(self.check);self.check.refresh_from_db()
        saved=copy.deepcopy(self.check.session['batches'][0])
        call.side_effect=None
        call.return_value={'stop_reason':'max_tokens','model':'checker-test','content':[]}
        for _ in range(2):
            step(self.check);self.check.refresh_from_db()
        self.assertEqual(self.check.state,'incomplete')
        self.assertEqual(self.check.session['batches'][0],saved)
        self.assertEqual(saved['report']['issues'],['Fix the title.'])
        self.assertEqual(self.check.approved_hash,'')
