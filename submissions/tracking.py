"""Public projections of the private queue. Never render raw inputs or audit data."""
import re
from urllib.parse import urlsplit
from django.db.models import Case, CharField, F, Q, Value, When
from django.db.models.functions import Coalesce, Greatest
from django.urls import reverse
from .models import Submission

KINDS = {key: label for key, label in Submission.Kind.choices if key != 'question'}
STATUSES = {'queued': 'Queued', 'in-progress': 'Processing', 'researching': 'Researching',
            'checking': 'Checking', 'revising': 'Revising', 'publishing': 'Publishing',
            'blocked': 'Blocked', 'insufficient': 'Insufficient evidence',
            'resolved': 'Resolved', 'declined': 'Declined', 'duplicate': 'Duplicate'}


def queryset():
    return Submission.objects.filter(kind__in=KINDS).select_related('automation', 'duplicate_of').annotate(
        tracking_status=Case(
            When(duplicate_of__isnull=False, then=Value('duplicate')),
            When(status='insufficient', then=Value('insufficient')),
            When(status='declined', then=Value('declined')),
            When(status='resolved', automation__state='duplicate', then=Value('duplicate')),
            When(status='resolved', then=Value('resolved')),
            When(automation__state='blocked', then=Value('blocked')),
            When(automation__state__in=['researching','checking','revising','publishing'], then=F('automation__state')),
            When(automation__state__in=['review', 'failed'], then=Value('queued')),
            When(automation__state__in=['queued', 'retry'], then=Value('queued')),
            When(Q(status='reviewing') | Q(automation__state='running'), then=Value('in-progress')),
            When(kind='correction', then=Value('queued')),
            default=Value('queued'), output_field=CharField()),
        tracking_updated=Greatest(F('updated_at'), Coalesce(F('automation__updated_at'), F('updated_at'))),
    )


def result_link(url, catalog):
    """Only link to actual public articles, never arbitrary submitted URLs."""
    parts = urlsplit(url)
    if parts.scheme != 'https' or parts.netloc != 'chainlore.xyz' or parts.query or parts.fragment:
        return ''
    match = re.fullmatch(r'/p/([a-z0-9-]+)/', parts.path)
    return parts.path if match and match[1] in catalog else ''


def present(submission, catalog):
    state = submission.tracking_status
    run = getattr(submission, 'automation', None)
    result = result_link(submission.resulting_url, catalog)
    result_slug = result.split('/')[2] if result else ''
    subject = catalog.get(submission.article or result_slug, {}).get('title', '')
    title = submission.public_title or (f'{KINDS[submission.kind]}: {subject}' if subject else
                                       f'{KINDS[submission.kind]} #{str(submission.pk)[:8]}')
    duplicate = submission.duplicate_of
    if duplicate is None and state == 'duplicate' and result:
        duplicate = Submission.objects.filter(kind__in=KINDS, status='resolved', resulting_url=submission.resulting_url).exclude(pk=submission.pk).exclude(automation__state='duplicate').order_by('created_at').first()
    original = reverse('submission-detail', args=[duplicate.pk]) if duplicate and duplicate.kind in KINDS else ''
    outcome = submission.public_summary
    if not outcome:
        if state == 'duplicate':
            outcome = 'This submission is already covered by an earlier submission or article.'
        elif state == 'insufficient':
            outcome = 'The available evidence did not establish a publishable change. The existing article is preserved.'
        elif state == 'resolved' and run and run.state == 'published' and result:
            outcome = ('The requested article was published.' if submission.kind == 'request'
                       else 'An updated version of the article was published.')
        elif state == 'resolved':
            outcome = 'Marked resolved. A detailed outcome has not yet been recorded.'
        elif state == 'declined':
            known_decline = run and run.events.filter(kind='decision', data__reason='out_of_scope_or_injection').exists()
            outcome = ('This request was declined because it is outside the editorial scope or contains instructions that cannot be processed safely.' if known_decline else
                       'Marked declined. A public reason has not yet been recorded.')
        else:
            outcome = {'queued': 'Waiting to be processed. Check back here for updates.',
                       'in-progress': 'This submission is being worked on.',
                       'researching': 'Sources are being researched.',
                       'checking': 'An independent pass is checking the proposed article against live sources.',
                       'revising': 'The proposed article is being revised to address verification findings.',
                       'publishing': 'The verified version is being published.',
                       'blocked': 'Processing is blocked by an operational issue. The current article is preserved.'}[state]
    if state == 'blocked' and run:
        reasons = {
            'daily_token_budget': 'The next processing step would exceed the shared daily budget. Saved work is retained.',
            'run_token_budget': 'The next processing step would exceed this submission’s budget. Saved work is retained; a budget adjustment is needed to continue.',
            'verification_output_incomplete': 'The checker could not finish its report within the allowed reporting attempts. The draft and retrieved evidence are retained.',
            'verification_report_incomplete': 'The checker did not return a complete report after the allowed attempts. The draft and retrieved evidence are retained.',
            'invalid_check_report': 'The checker did not return a usable report after the allowed attempts. The draft and retrieved evidence are retained.',
            'verification_evidence_stale': 'Saved verification evidence needs a fresh source check before processing can continue.',
            'verification_sources_incomplete': 'The checker could not finish collecting source evidence within the allowed attempts. The draft and retrieved sources are retained; this is not a factual rejection.',
            'shadow_verified_not_published': 'Verification passed in a non-publishing test run.'}
        outcome = reasons.get(run.last_error, 'Processing is blocked by a provider or publication failure; saved work is retained.')
        outcome += (' A retry is scheduled for ' + run.next_attempt_at.strftime('%-d %B %Y, %H:%M UTC') + '.' if run.next_attempt_at else ' No automatic retry is currently scheduled.')
    return {'reference': submission.pk, 'title': title, 'kind': KINDS[submission.kind],
            'status': state, 'status_label': STATUSES[state], 'created_at': submission.created_at,
            'updated_at': submission.tracking_updated, 'outcome': outcome, 'result_url': result,
            'original_url': original, 'url': reverse('submission-detail', args=[submission.pk])}


EVENT_LABELS = {
    'queued': 'Queued', 'attempt_started': 'Processing started',
    'research_request': 'Research started', 'improvement_research_request': 'Research started',
    'writing_request': 'Writing started', 'improvement_writing_request': 'Writing started',
    'queue_paused': 'Processing paused; operational recovery pending',
    'queue_resumed': 'Processing resumed', 'operator_retry': 'Queued for another attempt',
    'operator_regenerate': 'Queued for an expanded article',
    'operator_resume_approved': 'Approved improvement queued for publication',
    'improvement_conflict': 'Article changed during processing; preparing a fresh attempt',
    'provider_error': 'Processing interrupted', 'worker_error': 'Processing interrupted',
    'git_error': 'Publication delayed',
    'checking_started': 'Independent verification started', 'revision_requested': 'Revision requested by verification',
    'retry_scheduled': 'Retry scheduled', 'conflict_restarted': 'Restarted against the latest article',
    'operational_block': 'Operational blocker', 'budget_block': 'Processing budget reached',
    'shadow_verified': 'Verification passed in test mode',
    'verification_retry': 'Continuing verification from saved evidence',
    'verification_group_checked': 'A group of claims passed verification',
    'verification_incomplete': 'Verification report could not be completed',
    'verification_sources_retry': 'Completing missing verification sources',
    'verification_sources_complete': 'Verification sources collected',
    'verification_sources_incomplete': 'Verification source collection interrupted',
    'verification_recovered': 'Verification resumed from saved evidence',
}


def history(submission, catalog):
    entries = [{'date': submission.created_at, 'label': 'Received', 'note': '', 'link': ''}]
    for update in submission.public_updates.all():
        entries.append({'date': update.created_at, 'label': update.label, 'note': update.note, 'link': ''})
    run = getattr(submission, 'automation', None)
    if run:
        # Deliberately allowlist kinds and fields; provider payloads stay private.
        for event in run.events.filter(kind__in=[*EVENT_LABELS, 'decision', 'publication']).order_by('created_at', 'pk').values('kind', 'created_at', 'data__state', 'data__revision'):
            label = EVENT_LABELS.get(event['kind'])
            link = ''
            if event['kind'] == 'decision':
                label = {'published': 'Article published', 'duplicate': 'Already covered',
                         'declined': 'Declined', 'review': 'Further investigation required', 'failed': 'Processing interrupted', 'insufficient': 'Insufficient evidence'}.get(event['data__state'])
            elif event['kind'] == 'publication':
                label = 'Article published' if submission.kind == 'request' else 'Article updated'
                commit = event['data__revision']
                if re.fullmatch(r'[a-f0-9]{40}', str(commit)):
                    link = f'https://github.com/sirodoht/chainlore/commit/{commit}'
            if label:
                entries.append({'date': event['created_at'], 'label': label, 'note': '', 'link': link})
    entries.sort(key=lambda entry: entry['date'])
    # Older manual decisions may predate tracking. Do not invent transition dates.
    return entries
