import copy
from io import StringIO
from unittest.mock import patch
from django.core.management import call_command, CommandError
from django.test import TestCase
from django.utils import timezone
from . import editorial
from .models import AutomationRun, Submission, ArticleRevision, Verification
from .improvements import validate_patch, apply_patch
from .article_validation import InvalidArticle
from .test_verification import SOURCE, evidence
from .test_automation import RESEARCH
from .test_improvements import PATCH, written_patch
from .verification import digest


class EditorialProgressTests(TestCase):
    def setUp(self):
        self.feedback={'assessment':{'verdict':'revise','issues':['Add the missing citation.']},'errors':['unresolved_checker_issues']}
        self.run=AutomationRun.objects.create(submission=Submission.objects.create(kind='correction',status='reviewing'),
            state='revising',research=copy.deepcopy(RESEARCH),draft=copy.deepcopy(PATCH),
            editorial={'stage':'write','revisions':2,'candidate':SOURCE,'feedback':self.feedback})
        self.record=ArticleRevision.objects.create(run=self.run,slug='example',title='Example',original_markdown=SOURCE,
            base_content_hash=digest(SOURCE),base_revision='a'*40)

    @patch('submissions.ai_providers.write_improvement')
    def test_truncated_writing_retains_research_feedback_and_revision_count(self, writer):
        writer.side_effect=[{'stop_reason':'max_tokens','content':[]},written_patch()]
        editorial.process(self.run)
        self.run.refresh_from_db()
        self.assertEqual(self.run.editorial['feedback'],self.feedback)
        self.assertEqual(self.run.editorial['revisions'],2)
        self.assertEqual(self.run.research,RESEARCH)
        self.assertEqual(self.run.draft,PATCH)
        self.assertEqual(self.run.editorial['stage'],'write')
        editorial.process(self.run)
        self.run.refresh_from_db()
        self.assertEqual(writer.call_args.args[2]['checker_feedback'],self.feedback)
        self.assertEqual(self.run.editorial['stage'],'screen')
        self.assertEqual(self.run.editorial['revisions'],2)

    @patch('submissions.ai_providers.write_improvement')
    def test_saved_writer_response_is_validated_after_crash_without_another_call(self, writer):
        self.run.editorial['writer_response']={'response':written_patch(),'processed':False};self.run.save()
        editorial.process(self.run)
        writer.assert_not_called()
        self.run.refresh_from_db()
        self.assertEqual(self.run.editorial['stage'],'screen')

    @patch('submissions.ai_providers.write_article')
    def test_explicit_missing_evidence_returns_to_research_not_format_retry(self, writer):
        self.run.submission.kind='request';self.run.submission.save()
        writer.return_value=written_patch({'insufficient_evidence':True})
        editorial.process(self.run)
        self.run.refresh_from_db()
        self.assertEqual(self.run.editorial['stage'],'research')
        self.assertEqual(self.run.research,{})
        self.assertEqual(self.run.editorial['writer_retries'],0)
        self.assertEqual(self.run.state,'revising')

    @patch('submissions.ai_providers.write_improvement')
    def test_repeated_format_failures_remain_operational_not_factual_rejections(self, writer):
        writer.return_value={'stop_reason':'max_tokens','content':[]}
        for _ in range(3):
            self.run.refresh_from_db();editorial.process(self.run)
        self.run.refresh_from_db();self.run.submission.refresh_from_db()
        self.assertEqual(self.run.state,'blocked')
        self.assertEqual(self.run.submission.status,'reviewing')
        self.assertEqual(self.run.editorial['revisions'],2)
        self.assertEqual(self.run.editorial['feedback'],self.feedback)

    def test_corrections_continue_beyond_two_when_verified_coverage_advances(self):
        self.run.editorial['revisions']=0
        for index in range(4):
            candidate=SOURCE+'\n'*index
            reason={'assessment':{'verdict':'revise','issues':['Correct the remaining claim.'],
                'units':[{'id':str(i),'verdict':'supported'} for i in range(index+1)]},'errors':['unresolved_checker_issues']}
            check=Verification.objects.create(run=self.run,source=candidate,source_hash=digest(candidate),state='failed',
                session={'responses':evidence()},report=reason)
            self.run.editorial.update(candidate=candidate,check_id=check.pk)
            editorial.revise(self.run,reason)
            self.assertEqual(self.run.state,'revising')
            self.assertEqual(self.run.editorial['stage'],'write')
        self.assertEqual(self.run.editorial['revisions'],4)
        for _ in range(2):editorial.revise(self.run,reason)
        self.assertEqual(self.run.state,'revising')
        self.assertTrue(self.run.editorial['smallest_edit'])
        for _ in range(2):editorial.revise(self.run,reason)
        self.assertEqual(self.run.state,'blocked')
        self.assertEqual(self.run.last_error,'useful_edit_not_completed')

    def test_table_citation_repairs_preserve_facts_and_other_content(self):
        table='| Date | Event |\n|---|---|\n| 2009 | Example launched with its first public software release. |'
        self.record.original_markdown=SOURCE.replace('| Date | Event |\n|---|---|\n| 2009 | Example launched.[^1] |',table)
        proposal={'edits':[{'anchor':table,'position':'replace','markdown':table.replace('release.','release.[^1]')}],
                  'references':'[^1]: [Design](https://docs.example.com/design)'}
        validate_patch(self.record,proposal,RESEARCH)
        revised=apply_patch(self.record,proposal,self.record.original_markdown)
        self.assertIn(f'release.[^imp-{self.run.pk}-1]',revised)
        self.assertIn('Example launched in 2009.[^1]',revised)
        proposal['edits'][0]['markdown']=proposal['edits'][0]['markdown'].replace('2009','2010')
        with self.assertRaisesMessage(InvalidArticle,'unsupported_improvement_replacement'):
            validate_patch(self.record,proposal,RESEARCH)

    @patch('submissions.management.commands.resume_editorial_correction.publication_lock')
    def test_exhausted_correction_reopens_with_saved_findings_and_no_approval(self, lock):
        check=Verification.objects.create(run=self.run,source=SOURCE,source_hash=digest(SOURCE),state='failed',
            completed_at=timezone.now(),session={'responses':evidence()},report=self.feedback)
        self.run.editorial.update(stage='check',check_id=check.pk);self.run.save()
        editorial.insufficient(self.run,'Old revision limit reached.')
        call_command('resume_editorial_correction',submission=str(self.run.submission_id),stdout=StringIO())
        self.run.refresh_from_db();self.run.submission.refresh_from_db();check.refresh_from_db()
        self.assertEqual(self.run.state,'revising')
        self.assertEqual(self.run.editorial['stage'],'write')
        self.assertEqual(self.run.editorial['feedback'],self.feedback)
        self.assertEqual(self.run.submission.status,'reviewing')
        self.assertEqual(self.run.editorial['revisions'],3)
        self.assertEqual(check.state,'failed')
        self.assertFalse(self.run.verifications.filter(state='passed').exists())
        with self.assertRaises(CommandError):
            call_command('resume_editorial_correction',submission=str(self.run.submission_id),stdout=StringIO())
