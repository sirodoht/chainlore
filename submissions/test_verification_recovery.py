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
        self.check.session={'payload':payload(self.check),'responses':evidence(),'mode':'report','report_responses':[self.finished()]}
        self.check.save()
        step(self.check)
        call.assert_not_called()
        self.assertEqual(self.check.state,'passed')

    @patch('submissions.ai_providers.call')
    def test_saved_evidence_cannot_receive_a_new_check_date(self,call):
        original=payload(self.check);data=json.loads(original['messages'][0]['content']);data['today']='2000-01-01'
        original['messages'][0]['content']=json.dumps(data)
        self.check.session={'payload':original,'responses':evidence(),'mode':'report'};self.check.save()
        step(self.check)
        call.assert_not_called()
        self.assertEqual(self.check.state,'incomplete')
        self.assertEqual(self.check.report['errors'],['verification_evidence_stale'])

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
