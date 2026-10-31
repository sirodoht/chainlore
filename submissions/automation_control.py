"""Persistent queue circuit breaker and explicit, audited operator recovery."""
from datetime import timedelta
import logging
import smtplib
from django.conf import settings
from django.db import transaction
from django.utils import timezone
from .article_validation import PLACEHOLDER
from .ai_providers import approved_improvement
from .models import AutomationControl, AutomationEvent, AutomationRun, Submission
from .notify import notify_provider_problem
from .publication import publication_lock

logger = logging.getLogger(__name__)


def pause_for_provider(run, error):
    with transaction.atomic():
        # An infrastructure failure is not a failed attempt by the requester.
        run.attempts = max(0, run.attempts - 1)
        run.state = 'blocked'
        run.last_error = str(error)
        run.next_attempt_at = None
        run.save()
        control, _ = AutomationControl.objects.update_or_create(pk=1, defaults={
            'paused': True, 'reason': str(error), 'blocked_run': run,
            'paused_at': timezone.now(), 'alert_attempts': 0,
            'alert_sent_at': None, 'alert_retry_at': None,
        })
        AutomationEvent.objects.create(run=run, kind='queue_paused', data={
            'reason': str(error), 'attempt_charged': False, 'attempts': run.attempts})
    logger.error('Article queue paused: %s (run %s)', str(error), run.pk)
    return control


def deliver_provider_alert(control):
    now = timezone.now()
    if (not control.paused or control.alert_sent_at or control.alert_attempts >= 3
            or (control.alert_retry_at and control.alert_retry_at > now)):
        return
    control.alert_attempts += 1
    control.alert_retry_at = now + timedelta(hours=1)
    control.save(update_fields=['alert_attempts', 'alert_retry_at', 'updated_at'])
    try:
        if not settings.NOTIFICATIONS_ENABLED or not settings.ADMIN_NOTIFICATION_EMAIL:
            raise OSError('admin_email_not_configured')
        notify_provider_problem(control)
    except (smtplib.SMTPException, OSError):
        outcome = 'failed'
        logger.error('Article queue alert failed (attempt %s); see Automation queue in admin.', control.alert_attempts)
    else:
        outcome = 'smtp_accepted'
        control.alert_sent_at = now
        control.save(update_fields=['alert_sent_at', 'updated_at'])
    if control.blocked_run_id:
        AutomationEvent.objects.create(run_id=control.blocked_run_id, kind='queue_alert', data={
            'outcome': outcome, 'attempt': control.alert_attempts})


def resume_queue(actor_id):
    with publication_lock(blocking=False), transaction.atomic():
        control, _ = AutomationControl.objects.get_or_create(pk=1)
        if not control.paused:
            return 0
        count = 0
        for run in AutomationRun.objects.filter(state='blocked'):
            run.state = 'queued'
            run.last_error = ''
            run.next_attempt_at = None
            run.save(update_fields=['state', 'last_error', 'next_attempt_at', 'updated_at'])
            AutomationEvent.objects.create(run=run, kind='queue_resumed', data={
                'actor_id': actor_id, 'previous_reason': control.reason, 'attempts': run.attempts})
            count += 1
        control.paused = False
        control.alert_retry_at = None
        control.auto_resume_at = None
        control.probe_attempts = 0
        control.save(update_fields=['paused', 'alert_retry_at', 'auto_resume_at', 'probe_attempts', 'updated_at'])
        return count


def regenerate_placeholders(ids, actor_id):
    # The placeholder stays published until a replacement passes every check.
    with publication_lock(blocking=False), transaction.atomic():
        if AutomationControl.objects.filter(pk=1, paused=True).exists():
            raise ValueError('Fix the provider settings and resume the queue first.')
        runs = AutomationRun.objects.filter(pk__in=ids, state__in=['published', 'review', 'failed'],
                                            generated_article__isnull=False,
                                            submission__status__in=['resolved', 'reviewing'])
        count = 0
        for run in runs:
            if PLACEHOLDER not in run.generated_article.markdown:
                continue
            previous = {'state': run.state, 'reason': run.last_error, 'attempts': run.attempts}
            run.research_session = {}
            run.research = {}
            run.draft = {}
            run.output_review = {}
            run.editorial = {}
            run.recovery_attempts = 0
            run.state = 'queued'
            run.attempts = 0
            run.last_error = ''
            run.next_attempt_at = None
            run.save()
            Submission.objects.filter(pk=run.submission_id).update(status='reviewing', updated_at=timezone.now())
            AutomationEvent.objects.create(run=run, kind='operator_regenerate', data={
                'actor_id': actor_id, 'previous': previous})
            count += 1
        return count


def retry_runs(ids, actor_id, restart=False):
    with publication_lock(blocking=False), transaction.atomic():
        if AutomationControl.objects.filter(pk=1, paused=True).exists():
            raise ValueError('Fix the provider settings and resume the queue first.')
        runs = AutomationRun.objects.filter(pk__in=ids, state__in=['review'] if restart else ['failed', 'blocked'],
                                            submission__status__in=['new', 'reviewing'])
        count = 0
        for run in runs:
            previous = {'state': run.state, 'reason': run.last_error, 'attempts': run.attempts}
            if restart:
                if hasattr(run, 'generated_article'):
                    continue
                # Keep earlier improvement snapshots and patches in the audit before restarting.
                if hasattr(run, 'article_revision'):
                    revision = run.article_revision
                    if revision.published_at or revision.git_revision:
                        continue
                    AutomationEvent.objects.create(run=run, kind='improvement_restart', data={
                        'base_revision': revision.base_revision, 'original_markdown': revision.original_markdown,
                        'draft': run.draft})
                    revision.delete()
                run.triage = {}
                run.research_session = {}
                run.research = {}
                run.draft = {}
                run.output_review = {}
            if restart:
                run.editorial = {}
            run.recovery_attempts = 0
            run.state = 'queued'
            run.attempts = 0
            run.last_error = ''
            run.next_attempt_at = None
            run.save()
            AutomationEvent.objects.create(run=run, kind='operator_retry', data={
                'actor_id': actor_id, 'restart_research': restart, 'previous': previous})
            count += 1
        return count


def resume_approved_improvements(ids, actor_id=None):
    """Recover only positive screening decisions, retaining all paid checkpoints."""
    with publication_lock(blocking=False), transaction.atomic():
        if AutomationControl.objects.filter(pk=1, paused=True).exists():
            raise ValueError('Fix the provider settings and resume the queue first.')
        runs = AutomationRun.objects.filter(
            pk__in=ids, state='review', last_error='improvement_needs_review',
            submission__kind='improvement', submission__status='reviewing',
            article_revision__published_at__isnull=True, article_revision__git_revision='')
        count = 0
        for run in runs:
            if not run.draft or not run.research or not approved_improvement(run.output_review):
                continue
            previous = {'state': run.state, 'reason': run.last_error, 'attempts': run.attempts}
            run.state = 'queued'
            run.last_error = ''
            run.attempts = 0
            run.next_attempt_at = None
            run.save(update_fields=['state', 'last_error', 'attempts', 'next_attempt_at', 'updated_at'])
            AutomationEvent.objects.create(run=run, kind='operator_resume_approved', data={
                'actor_id': actor_id, 'previous': previous, 'decision': 'accept_saved_yes_without_score_threshold'})
            count += 1
        return count


def pause_queue(actor_id):
    with publication_lock(blocking=False), transaction.atomic():
        control, _ = AutomationControl.objects.get_or_create(pk=1)
        control.paused = True
        control.reason = 'owner_paused'
        control.paused_at = timezone.now()
        control.auto_resume_at = None
        control.save()
        for run in AutomationRun.objects.filter(state__in=['queued','running','retry','researching','checking','revising','publishing']):
            AutomationEvent.objects.create(run=run, kind='queue_paused', data={'actor_id': actor_id, 'reason': 'owner_paused'})
