import logging
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.utils import timezone
from .catalog import articles
from .models import Submission

FINAL = {Submission.Status.RESOLVED, Submission.Status.DECLINED}
logger = logging.getLogger(__name__)


def notify_admin(submission):
    if not settings.NOTIFICATIONS_ENABLED or not settings.ADMIN_NOTIFICATION_EMAIL:
        return
    kind = submission.get_kind_display().lower()
    review_url = 'https://chainlore.xyz' + reverse('admin:submissions_submission_change', args=[submission.pk])
    body = '\n'.join([
        f'A new {kind} is ready for review.', '',
        f'Subject: {submission.title or submission.article}',
        f'Reference: {submission.reference}', '',
        f'Review the submission: {review_url}',
    ])
    try:
        send_mail(f'New Chainlore {kind}', body, None, [settings.ADMIN_NOTIFICATION_EMAIL])
    except (smtplib.SMTPException, OSError):
        # Keep the saved submission and avoid logging addresses or SMTP credentials.
        logger.error('Admin notification failed for submission %s', submission.reference)


def notify_provider_problem(control):
    """The caller records acceptance/failure and owns the retry policy."""
    url = 'https://chainlore.xyz' + reverse('admin:submissions_automationcontrol_changelist')
    body = '\n'.join([
        'Chainlore article automation has paused because a provider needs attention.', '',
        f'Error code: {control.reason}',
        'No further requests will be processed until the queue is resumed.',
        'The affected request keeps its completed work and attempt allowance.', '',
        'Fix the provider credentials, billing, permissions or API configuration,',
        'then select the queue and use Resume queue in the admin:', url,
    ])
    send_mail('Chainlore article queue paused', body, None, [settings.ADMIN_NOTIFICATION_EMAIL])


def pending(submission):
    """Whether the submitter left an email and has not yet heard about this decision."""
    return bool(submission.email) and submission.status in FINAL and submission.notified_status != submission.status


def notify(submission):
    kind = submission.get_kind_display().lower()
    if submission.title:
        subject = f'"{submission.title}"'
    else:
        title = articles().get(submission.article, {}).get('title', submission.article)
        subject = f'the {title} article'
    lines = [f'Thank you for your {kind} about {subject}.', '']
    if submission.status == Submission.Status.RESOLVED:
        lines.append('We have acted on it.')
        if submission.resulting_url:
            lines += ['', f'You can see the result here: {submission.resulting_url}']
    else:
        lines.append('We have decided not to act on it.')
    lines += ['', f'Reference: {submission.reference}', '',
              'You are receiving this because you left your email address with your submission. '
              'We will not email you about it again.', '', 'Chainlore', 'https://chainlore.xyz/']
    send_mail(f'Update on your Chainlore {kind}', '\n'.join(lines), None, [submission.email])
    submission.notified_status = submission.status
    submission.notified_at = timezone.now()
    Submission.objects.filter(pk=submission.pk).update(notified_status=submission.notified_status, notified_at=submission.notified_at)
