from unittest.mock import patch
from django.test import override_settings
from django.utils import timezone
from . import editorial
from .automation import run_worker
from .git_publication import git
from .improvements import split_article
from .models import AutomationRun, ArticleRevision, Verification
from .verification import digest
from . import test_automation as fixtures
from . import test_improvements as improvements


def approve(check):
    # Provider responses are mocked here; separate verification tests exercise
    # real coverage, opened evidence, quotes, dates and hash requirements.
    metadata,body=split_article(check.source)
    if check.session.get('scope') in ('edit','draft'):
        metadata['status']='draft'
    else:
        metadata.update(status='ai-fact-checked',checked=timezone.localdate().isoformat(),checked_by='independent-test-checker high')
    check.checker='independent-test-checker high'
    check.approved_source='---\n'+'\n'.join(f'{k}: {v}' for k,v in metadata.items())+'\n---\n'+body
    check.approved_hash=digest(check.approved_source)
    check.state='passed';check.completed_at=timezone.now();check.save()
    return check


class EditorialIntegrationTests(fixtures.AutomationFixture):
    def setUp(self):
        super().setUp()
        override=override_settings(AUTONOMOUS_EDITORIAL_ENABLED=True,MAINTENANCE_ENABLED=False)
        override.enable();self.addCleanup(override.disable)
        self.checker=patch('submissions.editorial.check_step',side_effect=approve).start()
        self.addCleanup(patch.stopall)
        patch('submissions.ai_providers.review_improvement', return_value=fixtures.decision(suitable='yes')).start()

    def drive(self,limit=9):
        for _ in range(limit):
            run_worker()
            run=AutomationRun.objects.get(submission=self.submission)
            if run.state in ('published','declined','insufficient','blocked','duplicate'):
                return run
        return run

    def test_request_publishes_only_verified_content(self):
        run=self.drive()
        self.assertEqual(run.state,'published',run.last_error)
        source=git(self.remote,'show','main:pages/test-protocol.md')
        self.assertIn('status: draft',source)
        self.assertNotIn('checked_by: independent-test-checker high',source)
        self.assertNotIn('private@example.net',source)
        self.submission.refresh_from_db()
        self.assertIn('draft article',self.submission.public_summary)
        self.assertEqual(self.submission.automation.editorial['publication_scope'],'draft')
        from .models import Submission
        self.assertTrue(Submission.objects.filter(kind='maintenance',article='test-protocol').exists())
        self.assertEqual(Verification.objects.filter(run=run,state='passed').count(),1)

    def test_error_report_uses_same_checked_publication_pipeline(self):
        self.submission.kind='correction';self.submission.article='bitcoin';self.submission.claim='A disputed claim';self.submission.save()
        with patch('submissions.ai_providers.write_improvement',return_value=improvements.written_patch()):
            run=self.drive()
        self.assertEqual(run.state,'published',run.last_error)
        self.assertEqual(run.inputs['claim'],'A disputed claim')
        source=git(self.remote,'show','main:pages/bitcoin.md')
        self.assertIn('## Additional context',source)
        self.assertIn('status: draft',source)
        self.assertIn('written_by: Opus 5.5 High',source)

    def test_concurrent_edit_invalidates_verified_patch(self):
        self.submission.kind='improvement';self.submission.article='bitcoin';self.submission.save()
        with patch('submissions.ai_providers.write_improvement',return_value=improvements.written_patch()):
            for _ in range(5):run_worker()
            self.edit_remote(lambda checkout:(checkout/'pages/bitcoin.md').write_text((checkout/'pages/bitcoin.md').read_text().replace('## References','## Concurrent addition\n\nAn editor added this passage.\n\n## References')))
            run_worker()
        run=AutomationRun.objects.get(submission=self.submission)
        self.assertEqual(run.state,'retry')
        self.assertFalse(ArticleRevision.objects.filter(run=run).exists())
        source=git(self.remote,'show','main:pages/bitcoin.md')
        self.assertIn('Concurrent addition',source)
        self.assertNotIn('## Additional context',source)

    def test_failed_verifier_never_publishes(self):
        def fail(check):
            check.state='failed';check.report={'errors':['unopened_references']};check.save();return check
        self.checker.side_effect=fail
        run=self.drive(40)
        self.assertEqual(run.state,'blocked')
        self.assertEqual(run.last_error,'useful_edit_not_completed')
        self.assertNotIn('pages/test-protocol.md',git(self.remote,'ls-tree','-r','--name-only','main'))
