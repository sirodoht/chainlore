"""Recover interrupted checks without deleting history or bypassing publication checks."""
import copy
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction
from submissions.models import AutomationRun, Verification, AutomationEvent
from submissions.publication import publication_lock
from submissions.article_validation import extract_draft, InvalidArticle
from submissions.verification import digest, contradictory_pass, source_gaps


class Command(BaseCommand):
    help = 'Resume an interrupted verification from its saved candidate and independently fetched evidence.'

    def add_arguments(self, parser):
        parser.add_argument('--submission', required=True)
        parser.add_argument('--reopen-incomplete-sources', action='store_true',
                            help='Reopen an automated insufficient-evidence outcome caused solely by missing tool evidence.')
        parser.add_argument('--increase-report-allowance', action='store_true',
                            help='Retry a truncated group after raising its output allowance, retaining completed groups.')

    def handle(self, *args, **options):
        with publication_lock(blocking=False), transaction.atomic():
            try:
                run = AutomationRun.objects.select_related('submission').get(submission_id=options['submission'])
            except (AutomationRun.DoesNotExist, ValueError):
                raise CommandError('Submission has no recoverable run.') from None
            check = run.verifications.order_by('-pk').first()
            source_failure = False
            if options['reopen_incomplete_sources'] and check:
                gaps = source_gaps(check)
                errors = set(check.report.get('errors', []))
                source_failure = (check.state == 'failed' and check.report.get('assessment', {}).get('verdict') == 'insufficient'
                    and bool(gaps['missing_urls'] or gaps['search_missing'])
                    and bool(errors & {'no_live_freshness_search', 'unopened_references'})
                    and errors <= {'no_live_freshness_search', 'unopened_references', 'source_or_freshness_check_missing',
                                   'checker_did_not_pass', 'unresolved_checker_issues'}
                    and all(u.get('verdict') in ('supported', 'nonfactual') for u in check.report.get('assessment', {}).get('units', [])))
                if (not source_failure or run.state != 'insufficient' or run.submission.status != 'insufficient'
                        or run.submission.resulting_url or run.submission.duplicate_of_id
                        or not run.events.filter(kind='decision', data__state='insufficient', created_at__gte=check.completed_at).exists()):
                    raise CommandError('Only an automated outcome caused by missing source evidence can be reopened.')
            contradictory = bool(check and contradictory_pass(check.report.get('assessment', {}), check.report.get('errors', [])))
            unused_revision = contradictory and run.state == 'revising' and run.editorial.get('stage') == 'research'
            if not source_failure and ((run.state != 'blocked' and not unused_revision) or run.submission.status not in ('new', 'reviewing')):
                raise CommandError('Only blocked or unused contradictory-report revisions on undecided runs can be recovered.')
            if not check or check.state not in ('failed','incomplete') or (not source_failure and not contradictory and check.report.get('errors') not in (
                    ['invalid_check_report'], ['verification_output_incomplete'], ['verification_report_incomplete'])):
                raise CommandError('The last check was not an interrupted report. Factual findings cannot be bypassed.')
            if digest(check.source) != check.source_hash or run.editorial.get('candidate') != check.source:
                raise CommandError('Saved candidate changed; a fresh source check is required.')
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
            if options['increase_report_allowance']:
                batch = next((b for b in session.get('batches', []) if 'report' not in b), None)
                old_limit = batch.get('output_allowance', max((r.get('usage', {}).get('output_tokens', 0) for r in batch.get('responses', [])), default=0)) if batch else 0
                if (source_failure or contradictory or check.state != 'incomplete' or
                        check.report.get('errors') != ['verification_output_incomplete'] or not batch or not old_limit
                        or settings.VERIFICATION_REPORT_TOKENS <= old_limit
                        or not batch.get('responses') or any(r.get('stop_reason') != 'max_tokens' for r in batch['responses'])):
                    raise CommandError('A higher output allowance and a truncated group are required.')
                batch.setdefault('previous_attempts', []).append({'output_allowance':old_limit,'responses':batch['responses']})
                batch.update(responses=[], processed_responses=0, output_allowance=settings.VERIFICATION_REPORT_TOKENS)
            elif contradictory:
                batch = next((b for b in session.get('batches', []) if 'report' not in b), None)
                if batch is None:
                    raise CommandError('Contradictory report has no recoverable group checkpoint.')
                batch.update(validation_errors=check.report['errors'], rejected_report=check.report['assessment'])
            else:
                session.pop('batches', None)
            session.update(mode='report', report_responses=[], processed_report_responses=0, recovered_from=check.pk)
            if source_failure:
                session['mode'] = 'sources'
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
            if source_failure:
                submission = run.submission
                submission.status = 'reviewing'
                submission.public_summary = 'Verification resumed after incomplete source gathering. The previous outcome remains in the activity history.'
                submission.save()
            AutomationEvent.objects.create(run=run,kind='verification_recovered',data={'previous_check':check.pk,'check_id':recovered.pk,'source_hash':check.source_hash})
            self.stdout.write(f'Resumed verification {recovered.pk} from saved check {check.pk}. No publication approval granted.')
