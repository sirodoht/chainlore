import json
from datetime import timedelta
from unittest.mock import patch
from django.conf import settings
from django.test import TestCase, override_settings
from django.utils import timezone
from .models import AutomationRun, Submission, Verification, AutomationControl, ProviderSpend
from . import editorial
from .autonomous_worker import recover, unblock_due
from .budgets import reserve, BudgetExceeded
from .test_verification import SOURCE, digest


class AutonomousTests(TestCase):
    def setUp(self):
        self.submission=Submission.objects.create(kind='correction',article='bitcoin',status='reviewing')
        self.run=AutomationRun.objects.create(submission=self.submission,editorial={'stage':'check','revisions':0})

    def test_revisions_terminate_without_an_editor(self):
        for _ in range(3):editorial.revise(self.run,'unsupported claim')
        self.run.refresh_from_db();self.submission.refresh_from_db()
        self.assertEqual(self.run.state,'insufficient')
        self.assertEqual(self.submission.status,'insufficient')
        self.assertIn('preserved',self.submission.public_summary)

    def test_operational_failure_has_bounded_recovery(self):
        for _ in range(4):recover(self.run,'provider_network_error')
        self.run.refresh_from_db()
        self.assertEqual(self.run.state,'blocked')
        self.assertIsNone(self.run.next_attempt_at)

    def test_token_limit_reserves_failed_attempts_and_honours_daily_budget(self):
        with override_settings(EDITORIAL_DAILY_TOKEN_LIMIT=1000,EDITORIAL_RUN_TOKEN_LIMIT=1000):
            reserve(self.run,'anthropic','check',{'max_tokens':800})
            with self.assertRaises(BudgetExceeded):reserve(self.run,'anthropic','check',{'max_tokens':800})
        self.assertEqual(ProviderSpend.objects.count(),1)

    def test_pause_is_not_silently_removed_before_probe_time(self):
        control=AutomationControl.objects.create(pk=1,paused=True,auto_resume_at=timezone.now()+timedelta(hours=1))
        self.assertFalse(unblock_due())
        control.auto_resume_at=timezone.now()-timedelta(seconds=1);control.save()
        self.assertTrue(unblock_due())

    @override_settings(EDITORIAL_SHADOW=True)
    @patch('submissions.publication.publish_site')
    def test_shadow_check_cannot_publish(self,publish):
        check=Verification.objects.create(run=self.run,source=SOURCE,source_hash=digest(SOURCE),state='passed',approved_hash='a'*64)
        editorial.publish_checked(self.run,check)
        publish.assert_not_called()
        self.run.refresh_from_db()
        self.assertEqual(self.run.last_error,'shadow_verified_not_published')
