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
    def test_explicit_missing_evidence_ends_with_a_clear_outcome_not_another_round(self, writer):
        self.run.submission.kind='request';self.run.submission.save()
        writer.return_value=written_patch({'insufficient_evidence':True})
        editorial.process(self.run)
        self.run.refresh_from_db();self.run.submission.refresh_from_db()
        self.assertEqual(self.run.state,'insufficient')
        self.assertEqual(self.run.submission.status,'insufficient')
        self.assertEqual(self.run.research,RESEARCH)
        self.assertEqual(writer.call_count,1)

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
