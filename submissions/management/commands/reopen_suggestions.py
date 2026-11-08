"""Recover historical automation failures without approving or erasing paid work."""
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from submissions.models import AutomationRun, AutomationControl
from submissions.publication import publication_lock
from submissions import editorial
from submissions.verification import source_gaps


class Command(BaseCommand):
    help = 'Reopen stalled suggestions once under the draft-edit workflow; preserve audits and budgets.'

    def add_arguments(self, parser):
        parser.add_argument('--submission', action='append', help='Submission UUID (repeatable).')
        parser.add_argument('--all-stalled', action='store_true')

    def handle(self, *args, **options):
        if bool(options['submission']) == bool(options['all_stalled']):
            raise CommandError('Choose --submission or --all-stalled.')
        with publication_lock(), transaction.atomic():
            if AutomationControl.objects.filter(paused=True).exists():
                raise CommandError('Queue is paused; recovery will not override the owner or provider pause.')
            runs = AutomationRun.objects.filter(state__in=['blocked', 'insufficient'],
                submission__status__in=['reviewing', 'insufficient'], submission__duplicate_of__isnull=True)
            if options['submission']:
                runs = runs.filter(submission_id__in=options['submission'])
            count = 0
            for run in runs.select_related('submission'):
                if run.editorial.get('workflow_version') == 4 or run.events.filter(kind='workflow_recovered', data__workflow_version=4).exists():
                    continue
                if run.submission.status == 'insufficient' and not run.events.filter(kind='decision', data__state='insufficient').exists():
                    continue  # A manual decision is not an automation failure.
                record = getattr(run, 'article_revision', None)
                generated = getattr(run, 'generated_article', None)
                if any(item and (item.published_at or item.git_revision) for item in (record, generated)):
                    continue
                editorial.event(run, 'workflow_recovered', previous_state=run.state,
                    previous_error=run.last_error, previous_editorial=run.editorial,
                    previous_summary=run.submission.public_summary, workflow_version=4)
                check = run.verifications.filter(pk=run.editorial.get('check_id')).first()
                feedback = {'action': 'Act on the suggestion with the smallest useful supported change. Partial progress is sufficient. Reuse existing references, clarify or reorganize coverage if new evidence is limited. Previous technical failures do not reject the suggestion.'}
                if check and check.state == 'incomplete':
                    feedback['missing_sources'] = source_gaps(check)['missing_urls']
                    feedback['source_action'] = 'Replace inaccessible citations with accessible equivalent evidence; do not repeat the failed fetches.'
                candidate = run.editorial.get('candidate', '')
                run.editorial = {'workflow_version': 4, 'stage': 'write' if run.research and record else 'research',
                    'revisions': 0, 'writer_retries': 0, 'feedback': feedback,
                    'candidate': candidate, 'smallest_edit': True}
                if not record and run.submission.kind != 'request':
                    run.editorial = {}  # A fresh Git snapshot is required before writing.
                if feedback.get('missing_sources'):
                    run.editorial['stage'] = 'research'
                    run.research = {}
                    run.research_session = {}
                run.inputs['verification_feedback'] = feedback
                run.output_review = {}
                run.state = 'queued'
                run.last_error = ''
                run.next_attempt_at = None
                run.recovery_attempts = 0
                run.save()
                run.submission.status = 'reviewing'
                run.submission.public_summary = 'Reopened after an automation failure. The worker will make a useful full or partial edit; earlier outcomes remain in the activity history.'
                run.submission.save()
                count += 1
        self.stdout.write(f'Reopened {count} stalled submissions; audit history and charged usage retained.')
