"""Resume a saved corrective pass without restarting research or approving content."""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from submissions import editorial
from submissions.models import AutomationRun, AutomationEvent
from submissions.publication import publication_lock
from submissions.verification import digest


class Command(BaseCommand):
    help = 'Resume an automatically closed correction using its saved checker findings and source evidence.'

    def add_arguments(self, parser):
        parser.add_argument('--submission', required=True)

    def handle(self, *args, **options):
        with publication_lock(blocking=False), transaction.atomic():
            try:
                run = AutomationRun.objects.select_related('submission').get(submission_id=options['submission'])
            except (AutomationRun.DoesNotExist, ValueError):
                raise CommandError('Submission has no recoverable run.') from None
            check = run.verifications.order_by('-pk').first()
            if (run.state != 'insufficient' or run.submission.status != 'insufficient' or not check
                    or check.state != 'failed' or check.report.get('assessment', {}).get('verdict') != 'revise'
                    or not check.completed_at or run.submission.resulting_url or run.submission.duplicate_of_id
                    or not run.events.filter(kind='decision',data__state='insufficient',created_at__gte=check.completed_at).exists()):
                raise CommandError('Only an automated exhausted-correction outcome with actionable checker findings can be resumed.')
            if not run.draft or digest(check.source) != check.source_hash or run.editorial.get('candidate') != check.source:
                raise CommandError('The saved candidate or cumulative patch is unavailable or changed.')
            if run.spend.filter(created_at__gt=check.completed_at).exists():
                raise CommandError('Later paid work exists; do not replace it with an older check.')
            editorial.revise(run, check.report)
            if run.state != 'revising' or run.editorial['stage'] != 'write':
                raise CommandError('Saved evidence does not support a progressing targeted correction.')
            run.last_error='';run.next_attempt_at=None;run.save()
            submission=run.submission
            submission.status='reviewing'
            submission.public_summary='Correcting the reported claims and citations using saved source evidence. The previous outcome remains in the activity history.'
            submission.save()
            AutomationEvent.objects.create(run=run,kind='correction_resumed',data={'check_id':check.pk,'source_hash':check.source_hash})
            self.stdout.write(f'Resumed targeted correction from check {check.pk}. No publication approval granted.')
