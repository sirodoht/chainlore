import uuid
from django.core.management.base import BaseCommand, CommandError
from submissions.automation_control import resume_approved_improvements
from submissions.models import AutomationRun


class Command(BaseCommand):
    help = 'Queue one held improvement with a saved valid yes, retaining all model results.'

    def add_arguments(self, parser):
        parser.add_argument('reference', type=uuid.UUID)

    def handle(self, *args, **options):
        ids = list(AutomationRun.objects.filter(submission_id=options['reference']).values_list('pk', flat=True))
        try:
            count = resume_approved_improvements(ids)
        except (ValueError, BlockingIOError) as exc:
            raise CommandError('Queue paused or worker busy; retry when available.') from exc
        if count != 1:
            raise CommandError('No eligible held improvement with a saved valid yes was found.')
        self.stdout.write('Queued the saved approved improvement; no research, writing or screening was repeated.')
