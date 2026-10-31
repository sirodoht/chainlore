"""Recover interrupted checks without deleting history or bypassing publication checks."""
import copy
import json
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from submissions.models import AutomationRun, Verification, AutomationEvent
from submissions.publication import publication_lock
from submissions.article_validation import extract_draft, InvalidArticle
from submissions.verification import digest, contradictory_pass


class Command(BaseCommand):
    help = 'Resume an interrupted verification from its saved candidate and independently fetched evidence.'

    def add_arguments(self, parser):
        parser.add_argument('--submission', required=True)

    def handle(self, *args, **options):
        with publication_lock(blocking=False), transaction.atomic():
            try:
                run = AutomationRun.objects.select_related('submission').get(submission_id=options['submission'])
            except (AutomationRun.DoesNotExist, ValueError):
                raise CommandError('Submission has no recoverable run.') from None
            check = run.verifications.order_by('-pk').first()
            contradictory = bool(check and contradictory_pass(check.report.get('assessment', {}), check.report.get('errors', [])))
            unused_revision = contradictory and run.state == 'revising' and run.editorial.get('stage') == 'research'
            if (run.state != 'blocked' and not unused_revision) or run.submission.status not in ('new', 'reviewing'):
                raise CommandError('Only blocked or unused contradictory-report revisions on undecided runs can be recovered.')
            if not check or check.state not in ('failed','incomplete') or (not contradictory and check.report.get('errors') not in (
                    ['invalid_check_report'], ['verification_output_incomplete'], ['verification_report_incomplete'])):
                raise CommandError('The last check was not an interrupted report. Factual findings cannot be bypassed.')
            if digest(check.source) != check.source_hash or run.editorial.get('candidate') != check.source:
                raise CommandError('Saved candidate changed; a fresh source check is required.')
            if json.loads(check.session['payload']['messages'][0]['content'])['today'] != timezone.localdate().isoformat():
                raise CommandError('Saved evidence is from a different day; run a fresh source check.')
            if run.spend.filter(created_at__gt=check.completed_at).exists():
                raise CommandError('Later paid work exists; do not replace it with an older check.')
            if not run.draft:
                kind = 'writing_response' if run.submission.kind == 'request' else 'improvement_writing_response'
                event = run.events.filter(kind=kind,created_at__lte=check.created_at).order_by('-pk').first()
                if not event:
                    raise CommandError('Saved writing response is unavailable.')
                try:
                    run.draft = extract_draft(event.data)
                except InvalidArticle:
                    raise CommandError('Saved writing response cannot be recovered.') from None
            session = copy.deepcopy(check.session)
            if contradictory:
                batch = next((b for b in session.get('batches', []) if 'report' not in b), None)
                if batch is None:
                    raise CommandError('Contradictory report has no recoverable group checkpoint.')
                batch.update(validation_errors=check.report['errors'], rejected_report=check.report['assessment'])
            else:
                session.pop('batches', None)
            session.update(mode='report', report_responses=[], processed_report_responses=0, recovered_from=check.pk)
            recovered = Verification.objects.create(run=run,source=check.source,source_hash=check.source_hash,session=session)
            # The legacy path requested a rewrite solely because the report was
            # truncated. Undo that unused attempt, preserving its audit events.
            if run.editorial.get('stage') == 'research':
                run.editorial['revisions'] = max(0, run.editorial.get('revisions',0)-1)
            run.editorial.update(stage='check',check_id=recovered.pk)
            run.inputs.pop('verification_feedback',None)
            run.editorial.pop('feedback',None)
            run.state='checking';run.last_error='';run.next_attempt_at=None
            run.save()
            AutomationEvent.objects.create(run=run,kind='verification_recovered',data={'previous_check':check.pk,'check_id':recovered.pk,'source_hash':check.source_hash})
            self.stdout.write(f'Resumed verification {recovered.pk} from saved check {check.pk}. No publication approval granted.')
