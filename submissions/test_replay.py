from io import StringIO
from unittest.mock import patch
from django.core.management import call_command, CommandError
from django.test import TestCase, override_settings
from .models import Submission


class ReplayTests(TestCase):
    @override_settings(PRODUCTION=True, EDITORIAL_SHADOW=True, AUTOMATION_ENABLED=False, ARTICLE_GIT_REMOTE='')
    @patch('submissions.management.commands.replay_editorial.step')
    def test_production_replay_is_refused_before_any_work(self, checker):
        with self.assertRaises(CommandError):
            call_command('replay_editorial', source='unused', stdout=StringIO())
        checker.assert_not_called()
        self.assertEqual(Submission.objects.count(),0)
