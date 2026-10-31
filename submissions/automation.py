"""Bounded, resumable article-request pipeline. Invoked by a single systemd worker."""
from datetime import timedelta
import json
import logging
import smtplib
from django.conf import settings
from django.db import transaction
from django.db.models import F, Q
from django.utils import timezone
from django.utils.text import slugify
from . import ai_providers as ai
from . import notify
from .attribution import attribute_source, historical_writer_credit
from .article_validation import InvalidArticle, citable_urls, extract_draft, stub_draft, validate_draft
from .catalog import articles
from .git_publication import GitPublicationError
from .improvements import ImprovementConflict, process_improvement
from .models import AutomationControl, AutomationEvent, AutomationRun, GeneratedArticle, Submission
from .automation_control import deliver_provider_alert, pause_for_provider
from .publication import publication_lock, publish_site

logger = logging.getLogger(__name__)
ACTIVE = ['queued', 'running', 'retry']


def event(run, kind, **data):
    AutomationEvent.objects.create(run=run, kind=kind, data=data)


def finish(run, state, reason, url=''):
    run.state = state
    run.last_error = reason if state in ('failed', 'review') else ''
    run.save()
    status = {'published': 'resolved', 'duplicate': 'resolved', 'declined': 'declined'}.get(state, 'reviewing')
    Submission.objects.filter(pk=run.submission_id, status__in=['new', 'reviewing']).update(
        status=status, resulting_url=url, public_summary=(
            'This request was declined because it is outside the editorial scope or contains instructions that cannot be processed safely.'
            if state == 'declined' and reason == 'out_of_scope_or_injection' else ''), updated_at=timezone.now())
    event(run, 'decision', state=state, reason=reason, resulting_url=url)


def existing_match(title, catalog):
    normalized = slugify(title)
    return next((slug for slug, item in catalog.items() if normalized in (slug, slugify(item['title']))), None)


def draft_article(run):
    # An accepted subject always gets a page: retry the writer once, then use a placeholder.
    problem = None
    if citable_urls(run.research):
        for _ in range(2):
            try:
                response = ai.write_article(run, problem)
                draft = extract_draft(response)
                draft['_written_by'] = response.get('_written_by', 'Unknown')
                validate_draft(draft, run.research)
                return draft
            except InvalidArticle as exc:
                problem = str(exc)
                event(run, 'validation', passed=False, reason=problem)
            except ai.ProviderError as exc:
                if exc.retryable or exc.account_problem:
                    raise
                problem = str(exc)
                event(run, 'provider_error', code=problem, retryable=False, account_problem=False)
                break
    event(run, 'placeholder_used', reason=problem or 'no_citable_sources')
    return stub_draft(run.inputs['title'], run.research)


def process(run):
    run.attempts += 1
    run.state = 'running'
    run.save()
    event(run, 'attempt_started', attempt=run.attempts, policy_version=2)
    submission = Submission.objects.get(pk=run.submission_id)
    if submission.status not in ('new', 'reviewing'):
        finish(run, 'review', 'submission_already_decided')
        return
    Submission.objects.filter(pk=submission.pk, status='new').update(status='reviewing', updated_at=timezone.now())
    if submission.kind == 'improvement':
        process_improvement(run)
        return
    catalog = articles()
    # An unpublished record is the checked replacement awaiting publication.
    # A published record may be the old placeholder retained during regeneration.
    prepared = GeneratedArticle.objects.filter(run=run).first()
    if prepared and prepared.published_at is None and run.draft:
        publish_site()
        return
    # The retained placeholder must not count as a duplicate of its replacement.
    if prepared:
        catalog = {slug: item for slug, item in catalog.items() if slug != prepared.slug}
    match = existing_match(run.inputs['title'], catalog)
    if match:
        finish(run, 'duplicate', 'existing_title_or_slug', f'https://chainlore.xyz/p/{match}/')
        return
    if not run.triage:
        run.triage = ai.triage(run, {slug: data['title'] for slug, data in catalog.items()})
        run.save(update_fields=['triage', 'updated_at'])
    if not ai.valid_triage(run.triage):
        finish(run, 'review', 'triage_invalid_response')
        return
    if ai.confident(run.triage, 'scope', 'out_of_scope') or ai.confident(run.triage, 'injection', 'injection'):
        finish(run, 'declined', 'out_of_scope_or_injection')
        return
    # Research plausible requests, including uncertain classifications. Duplicate
    # detection uses actual title/slug matches before and after canonicalisation.
    event(run, 'triage_passed', policy_version=2, decision='research_unless_clearly_rejected')
    if not run.research:
        run.research = ai.research(run)
        run.save(update_fields=['research', 'updated_at'])
    if not run.draft:
        run.draft = draft_article(run)
        run.save(update_fields=['draft', 'updated_at'])
    source, digest = validate_draft(run.draft, run.research)
    credit = run.draft.get('_written_by') or historical_writer_credit(run.events.order_by('pk'), run.draft['markdown'])
    source, digest = attribute_source(source, credit)
    event(run, 'validation', passed=True, content_hash=digest)
    match = existing_match(run.draft['title'], catalog)
    if match:
        finish(run, 'duplicate', 'canonical_subject_already_exists', f'https://chainlore.xyz/p/{match}/')
        return
    if not run.output_review:
        run.output_review = ai.review_output(run)
        run.save(update_fields=['output_review', 'updated_at'])
    if not ai.valid_output_review(run.output_review):
        finish(run, 'review', 'output_review_invalid_response')
        return
    if ai.confident(run.output_review, 'suitable', 'no'):
        finish(run, 'review', 'output_rejected_as_spam_off_topic_or_injection')
        return
    # Respect a manual decision made while provider calls were in progress.
    submission.refresh_from_db()
    if submission.status != 'reviewing':
        finish(run, 'review', 'submission_changed_during_generation')
        return
    with transaction.atomic():
        base_hash = prepared.content_hash if prepared else ''
        if prepared:
            prepared.delete()
        GeneratedArticle.objects.create(slug=run.draft['slug'], run=run, title=run.draft['title'],
                                        markdown=source, content_hash=digest, base_content_hash=base_hash)
    publish_site()


def deliver_notifications():
    # SMTP acceptance is recorded, not claimed to prove inbox delivery.
    now = timezone.now()
    runs = AutomationRun.objects.filter(
        state__in=['published', 'duplicate', 'declined', 'insufficient'], notification_attempts__lt=3,
        submission__status__in=notify.FINAL,
    ).exclude(submission__email='').exclude(
        submission__notified_status=F('submission__status'),
    ).filter(
        Q(notification_retry_at__isnull=True) | Q(notification_retry_at__lte=now),
    ).select_related('submission').order_by('created_at', 'pk')
    for run in runs[:10]:
        if not notify.pending(run.submission):
            continue
        run.notification_attempts += 1
        run.notification_retry_at = now + timedelta(hours=1)
        run.save(update_fields=['notification_attempts', 'notification_retry_at', 'updated_at'])
        try:
            if not settings.NOTIFICATIONS_ENABLED:
                raise OSError('email_not_configured')
            notify.notify(run.submission)
        except (smtplib.SMTPException, OSError):
            event(run, 'notification', outcome='failed', attempt=run.notification_attempts)
        else:
            event(run, 'notification', outcome='smtp_accepted', attempt=run.notification_attempts)


def run_worker():
    if settings.AUTONOMOUS_EDITORIAL_ENABLED:
        from .autonomous_worker import run_worker as autonomous
        return autonomous()
    if not settings.AUTOMATION_ENABLED:
        return 0
    try:
        with publication_lock(blocking=False):
            control, _ = AutomationControl.objects.get_or_create(pk=1)
            if control.paused:
                deliver_provider_alert(control)
                deliver_notifications()
                return 0
            now = timezone.now()
            run = AutomationRun.objects.filter(state__in=ACTIVE).filter(
                Q(next_attempt_at__isnull=True) | Q(next_attempt_at__lte=now)).order_by('created_at').first()
            if not run:
                today = now.replace(hour=0, minute=0, second=0, microsecond=0)
                if AutomationRun.objects.filter(created_at__gte=today).count() < settings.AUTOMATION_DAILY_LIMIT:
                    submission = Submission.objects.filter(kind__in=['request', 'improvement'], status='new', automation__isnull=True).order_by('created_at').first()
                    if submission:
                        run = AutomationRun.objects.create(submission=submission, inputs={
                            'title': submission.title, 'details': submission.details, 'sources': submission.sources,
                            'kind': submission.kind, 'article': submission.article, 'section': submission.section})
                        event(run, 'queued', model=settings.ANTHROPIC_MODEL)
            if run:
                try:
                    if run.attempts >= 3:
                        finish(run, 'failed', 'attempt_limit_reached')
                    else:
                        process(run)
                except ai.ProviderError as exc:
                    event(run, 'provider_error', code=str(exc), retryable=exc.retryable, account_problem=exc.account_problem)
                    # A run that repeats the error after a resume is the likely cause,
                    # so it fails alone rather than blocking the queue behind it.
                    if exc.account_problem and not run.events.filter(kind='queue_paused').exists():
                        control = pause_for_provider(run, exc)
                        deliver_provider_alert(control)
                    elif exc.retryable and run.attempts < 3:
                        run.state = 'retry'
                        run.last_error = str(exc)
                        run.next_attempt_at = now + timedelta(minutes=5 * run.attempts)
                        run.save()
                    else:
                        finish(run, 'failed', str(exc))
                except InvalidArticle as exc:
                    event(run, 'validation', passed=False, reason=str(exc))
                    finish(run, 'review', str(exc))
                except ImprovementConflict as exc:
                    event(run, 'improvement_conflict', code=str(exc))
                    finish(run, 'review', str(exc))
                except GitPublicationError as exc:
                    # These codes are fixed by our Git wrapper; never include command output.
                    event(run, 'git_error', code=str(exc))
                    run.last_error = str(exc)
                    run.state = 'retry' if run.attempts < 3 else 'failed'
                    run.next_attempt_at = now + timedelta(minutes=5 * run.attempts)
                    run.save()
                except Exception as exc:
                    # Never log provider/request text or secrets from exception messages.
                    event(run, 'worker_error', error_type=type(exc).__name__)
                    run.last_error = 'worker_' + type(exc).__name__
                    run.state = 'retry' if run.attempts < 3 else 'failed'
                    run.next_attempt_at = now + timedelta(minutes=5 * run.attempts)
                    run.save()
                    logger.error('Automation run %s: %s', run.pk, type(exc).__name__)
            deliver_notifications()
            return int(run is not None)
    except BlockingIOError:
        return 0
