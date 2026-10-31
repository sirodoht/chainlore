"""Bounded scheduling, recovery and provider circuit breaking without editor gates."""
from datetime import timedelta
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from . import ai_providers as ai, editorial
from .article_validation import InvalidArticle
from .budgets import BudgetExceeded
from .git_publication import GitPublicationError
from .models import AutomationControl, AutomationRun, Submission, ArticleRevision, GeneratedArticle
from .publication import publication_lock


def recover(run, code, conflict=False):
    run.recovery_attempts += 1
    run.last_error = code
    if run.recovery_attempts > settings.EDITORIAL_MAX_RECOVERIES:
        if conflict:
            editorial.insufficient(run, 'The article kept changing during verification. No competing version was overwritten; a new submission can request a fresh attempt.')
        else:
            run.state = 'blocked'
            run.next_attempt_at = None
            run.save()
            editorial.event(run, 'operational_block', code=code)
        return
    if conflict:
        record = ArticleRevision.objects.filter(run=run).first()
        if record and not record.published_at and not record.git_revision:
            editorial.event(run, 'conflict_restarted', base_revision=record.base_revision)
            record.delete()
            run.editorial = {}
            run.research = {}; run.research_session = {}; run.draft = {}; run.output_review = {}
    run.state = 'retry'
    run.next_attempt_at = timezone.now()+timedelta(minutes=5*run.recovery_attempts)
    run.save()
    editorial.event(run, 'retry_scheduled', code=code, retry_at=run.next_attempt_at.isoformat())


def unblock_due():
    control, _ = AutomationControl.objects.get_or_create(pk=1)
    now = timezone.now()
    if control.paused:
        if not control.auto_resume_at or control.auto_resume_at > now:
            return False
        # One bounded probe of the pending real stage. Failed probes back off;
        # after three, credentials/billing remain an explicit operational block.
        control.paused = False
        control.auto_resume_at = None
        control.save()
    for run in AutomationRun.objects.filter(state='blocked', next_attempt_at__lte=now):
        run.state = 'queued'; run.next_attempt_at = None
        run.save()
        editorial.event(run, 'queue_resumed', reason='scheduled_probe')
    return True


def schedule():
    now = timezone.now()
    # Old held runs become automated investigations, not silently approved output.
    old = AutomationRun.objects.filter(state__in=['review', 'failed'], submission__status__in=['new', 'reviewing']).order_by('created_at').first()
    if old:
        old.state = 'queued'; old.editorial = {}; old.next_attempt_at = None
        old.save()
    run = AutomationRun.objects.filter(state__in=editorial.ACTIVE).filter(
        Q(next_attempt_at__isnull=True)|Q(next_attempt_at__lte=now)).select_related('submission').order_by('updated_at', 'pk').first()
    if run:
        return run
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if AutomationRun.objects.filter(created_at__gte=today).count() >= settings.AUTOMATION_DAILY_LIMIT:
        return None
    submission = Submission.objects.filter(kind__in=['request','improvement','correction','maintenance'],
        status='new', automation__isnull=True, duplicate_of__isnull=True).order_by('created_at').first()
    if not submission:
        from .maintenance import enqueue
        submission = enqueue()
    if submission:
        run = AutomationRun.objects.create(submission=submission, inputs={key: getattr(submission,key)
            for key in ('title','details','sources','kind','article','section','claim','correction')})
        editorial.event(run, 'queued', policy_version=3)
        return run


def run_worker():
    if not settings.AUTOMATION_ENABLED:
        return 0
    from .automation import deliver_notifications
    try:
        with publication_lock(blocking=False):
            if not unblock_due():
                deliver_notifications()
                return 0
            run = schedule()
            if run:
                try:
                    editorial.process(run)
                except BudgetExceeded as exc:
                    run.state = 'blocked'; run.last_error = str(exc)
                    run.next_attempt_at = (timezone.now()+timedelta(days=1)).replace(hour=0,minute=5,second=0,microsecond=0) if str(exc)=='daily_token_budget' else None
                    run.save()
                    editorial.event(run, 'budget_block', code=str(exc))
                except ai.ProviderError as exc:
                    if exc.account_problem:
                        control, _ = AutomationControl.objects.get_or_create(pk=1)
                        control.probe_attempts += 1
                        control.paused = True; control.reason = str(exc); control.blocked_run = run
                        control.paused_at = timezone.now()
                        control.auto_resume_at = timezone.now()+timedelta(hours=2**control.probe_attempts) if control.probe_attempts <= 3 else None
                        control.save()
                        run.state = 'blocked'; run.last_error = str(exc); run.next_attempt_at = control.auto_resume_at
                        run.save()
                        editorial.event(run, 'operational_block', code=str(exc))
                    else:
                        recover(run, str(exc))
                except InvalidArticle as exc:
                    editorial.revise(run, str(exc))
                except GitPublicationError as exc:
                    recover(run, str(exc), conflict=str(exc) in ('verified_base_changed','improvement_passage_changed','article_changed_in_git'))
                except Exception as exc:
                    # Exception bodies can contain provider text or credentials.
                    recover(run, 'worker_'+type(exc).__name__)
                else:
                    control, _ = AutomationControl.objects.get_or_create(pk=1)
                    if control.probe_attempts:
                        control.probe_attempts = 0; control.save(update_fields=['probe_attempts','updated_at'])
            deliver_notifications()
            return int(run is not None)
    except BlockingIOError:
        return 0
