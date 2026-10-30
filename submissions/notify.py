from django.core.mail import send_mail
from django.utils import timezone
from .catalog import articles
from .models import Submission

FINAL = {Submission.Status.RESOLVED, Submission.Status.DECLINED}


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
