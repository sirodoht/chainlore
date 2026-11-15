"""Checkpointed autonomous editorial state machine. One bounded stage per tick."""
from datetime import timedelta
import hashlib
import json
from django.conf import settings
from django.utils import timezone
from . import ai_providers as ai
from .article_validation import InvalidArticle, citable_urls, extract_draft, validate_draft
from .attribution import attribute_source
from .improvements import snapshot_article, validate_patch, apply_patch
from .models import AutomationEvent, ArticleRevision, GeneratedArticle, Submission, Verification
from .budgets import BudgetExceeded
from .verification import close_unchecked, digest, step as check_step

ACTIVE = ['queued', 'running', 'retry', 'researching', 'checking', 'revising', 'publishing']


def event(run, kind, **data):
    AutomationEvent.objects.create(run=run, kind=kind, data=data)


def save(run, stage=None, **values):
    run.editorial.update(values)
    if stage:
        run.editorial['stage'] = stage
    run.save(update_fields=['editorial', 'state', 'updated_at'])


def conclude(run, state, summary, url='', duplicate=None):
    run.state = state
    run.last_error = ''
    run.next_attempt_at = None
    run.save()
    status = {'published': 'resolved', 'duplicate': 'resolved', 'declined': 'declined',
              'insufficient': 'insufficient'}.get(state, 'reviewing')
    submission = Submission.objects.get(pk=run.submission_id)
    if submission.status in ('new', 'reviewing'):
        submission.status = status
        submission.public_summary = summary
        submission.resulting_url = url
        if duplicate:
            submission.duplicate_of = duplicate
        submission.save()
    event(run, 'decision', state=state, reason=summary, resulting_url=url)


def prepare(run):
    from .catalog import articles
    from .automation import existing_match
    record = None
    if run.submission.kind in ('correction', 'improvement', 'maintenance'):
        record = ArticleRevision.objects.filter(run=run).first() or snapshot_article(run)
    else:
        match = existing_match(run.inputs['title'], articles())
        if match:
            url = f'https://chainlore.xyz/p/{match}/'
            original = Submission.objects.filter(status='resolved', resulting_url=url).exclude(pk=run.submission_id).exclude(automation__state='duplicate').order_by('created_at').first()
            conclude(run, 'duplicate', 'This subject is already covered by an existing article.', url, original)
            return
    # Legacy unpublished output never skips the new verification gate.
    run.state = 'researching'
    Submission.objects.filter(pk=run.submission_id, status='new').update(status='reviewing', updated_at=timezone.now())
    run.editorial = {'stage': 'triage', 'revisions': 0, 'workflow_version': 4}
    run.save()
    event(run, 'attempt_started', policy_version=4)
    if run.submission.kind == 'maintenance':
        from .maintenance import enrich
        begin_check(run, enrich(record.original_markdown, record.slug))


def begin_check(run, source):
    scope = 'full' if run.submission.kind == 'maintenance' else 'draft' if run.submission.kind == 'request' else 'edit'
    session = {'scope': scope}
    if scope == 'edit':
        session.update(original_source=run.article_revision.original_markdown,
                       base_hash=run.article_revision.base_content_hash)
    check = Verification.objects.create(run=run, source=source, source_hash=digest(source), session=session)
    run.state = 'checking'
    save(run, 'check', check_id=check.pk, candidate=source)
    event(run, 'checking_started', source_hash=check.source_hash)


def insufficient(run, reason):
    conclude(run, 'insufficient', reason)


def block(run, code, retry=True):
    run.last_error = code
    run.state = 'blocked'
    attempts = run.editorial.get('operational_retries', 0)
    run.next_attempt_at = None
    if retry and attempts < settings.EDITORIAL_MAX_RECOVERIES:
        run.editorial['operational_retries'] = attempts + 1
        run.next_attempt_at = timezone.now() + timedelta(hours=2 ** attempts)
    run.save()
    event(run, 'operational_block', code=code)


def nothing_published(run, summary):
    """A clear outcome instead of another attempt: the article is left as it was."""
    conclude(run, 'insufficient', summary)


def publish_confirmed(run, check):
    """The check did not pass whole. Publish what it confirmed and queue the rest."""
    from . import salvage
    if check.session.get('scope') not in ('edit', 'draft'):
        # A full check certifies an existing article. Nothing is deleted from a
        # published article automatically: findings become one targeted edit.
        _, rejected, unchecked = salvage.confirmed_units(check)
        record = ArticleRevision.objects.filter(run=run).first()
        if rejected and record:
            salvage.queue_repair(record, check, [unit['text'] for unit in rejected], salvage.checker_issues(check))
            summary = (f'The full check could not confirm {len(rejected)} passage{"s" if len(rejected) != 1 else ""} against '
                       'the cited sources. The article is unchanged and keeps its current status; a targeted repair '
                       'of those passages has been queued.')
        else:
            summary = ('The full check could not be completed for every passage, so the article was not certified. '
                       'It is unchanged and keeps its current status.')
        event(run, 'full_check_not_certified', rejected=len(rejected), unchecked=len(unchecked))
        nothing_published(run, summary)
        return
    try:
        approved, left_out = salvage.confirmed_subset(run, check)
    except InvalidArticle as exc:
        event(run, 'nothing_confirmed', check_id=check.pk, reason=str(exc))
        nothing_published(run, 'The checker could not confirm any of the proposed text against its sources, so nothing '
                               'was published. ' + ('No article was created.' if run.submission.kind == 'request'
                                                    else 'The existing article is unchanged.'))
        return
    run.editorial.update(check_id=approved.pk, candidate=approved.source, fulfillment='partial', left_out=len(left_out))
    run.editorial['follow_up'] = salvage.remainder_details(
        'An earlier edit was published without the passages below because the checker could not confirm them. '
        'Research sources that state them and add only what those sources support.',
        left_out, salvage.checker_issues(check)) if left_out else ''
    run.save(update_fields=['draft', 'editorial', 'updated_at'])
    event(run, 'confirmed_subset_approved', check_id=approved.pk, previous_check_id=check.pk, left_out=len(left_out))
    publish_checked(run, approved)


def writer_response(run, kind, problem):
    saved = run.editorial.get('writer_response')
    if saved and not saved.get('processed'):
        return saved['response']
    response = ai.write_article(run, problem) if kind == 'request' else ai.write_improvement(run, run.article_revision, problem)
    run.editorial['writer_response'] = {'response':response, 'processed':False}
    run.save(update_fields=['editorial','updated_at'])
    return response


def retry_writing(run, reason):
    attempts = run.editorial.get('writer_retries', 0)+1
    if run.editorial.get('writer_response'):
        run.editorial['writer_response']['processed'] = True
    run.editorial.update(writer_retries=attempts, writer_problem=reason)
    run.last_error = 'writing_output_incomplete'
    run.state = 'blocked' if attempts >= settings.EDITORIAL_WRITING_ATTEMPTS else 'revising'
    run.next_attempt_at = None
    run.save()
    event(run, 'writing_incomplete' if run.state == 'blocked' else 'writing_retry', attempt=attempts, reason=reason)
    if run.state == 'blocked':
        block(run, 'writing_output_incomplete')


def write_candidate(run):
    kind = run.submission.kind
    problem = run.editorial.get('feedback')
    if run.editorial.get('writer_problem'):
        problem = {'checker_feedback':problem, 'output_problem':run.editorial['writer_problem']}
    if kind == 'request':
        response = writer_response(run, kind, problem)
        draft = extract_draft(response)
        source, _ = validate_draft(draft, run.research, minimum_length=50)
        source, _ = attribute_source(source, response.get('_written_by', 'Unknown'))
        run.draft = draft
        run.editorial['writer_credit'] = response.get('_written_by', 'Unknown')
    else:
        record = run.article_revision
        response = writer_response(run, kind, problem)
        draft = extract_draft(response)
        if draft.get('insufficient_evidence'):
            nothing_published(run, 'The writer found no edit it could support from the available sources. The existing article is unchanged.')
            return
        else:
            validate_patch(record, draft, run.research)
            source = apply_patch(record, draft, record.original_markdown)
            run.editorial['no_change'] = False
        run.draft = draft
        run.editorial['writer_credit'] = response.get('_written_by', 'Unknown')
    run.editorial['writer_response']['processed'] = True
    run.editorial.pop('writer_problem', None)
    run.editorial['writer_retries'] = 0
    run.last_error = ''
    run.save(update_fields=['draft', 'editorial', 'last_error', 'updated_at'])
    if run.editorial.get('no_change'):
        begin_check(run, source)
    else:
        save(run, 'screen', candidate=source)


def publish_checked(run, check):
    from .catalog import articles
    from .publication import publication_lock, publish_site
    if settings.EDITORIAL_SHADOW:
        run.state = 'blocked'
        run.last_error = 'shadow_verified_not_published'
        run.next_attempt_at = None
        run.save()
        event(run, 'shadow_verified', approved_hash=check.approved_hash)
        return
    kind = run.submission.kind
    if run.editorial.get('no_change') and kind == 'improvement':
        block(run, 'no_useful_edit', retry=False)
        return
    if kind == 'request':
        from .automation import existing_match
        match = existing_match(run.draft['title'], articles())
        if match:
            conclude(run, 'duplicate', 'This subject is already covered by an existing article.', f'https://chainlore.xyz/p/{match}/')
            return
        old = GeneratedArticle.objects.filter(run=run, published_at__isnull=True).first()
        if old and old.slug != run.draft['slug']:
            event(run, 'unpublished_candidate_replaced', previous_slug=old.slug)
            old.delete()
        GeneratedArticle.objects.update_or_create(run=run, defaults={'slug': run.draft['slug'],
            'title': run.draft['title'], 'markdown': check.approved_source, 'content_hash': check.approved_hash})
    else:
        record = run.article_revision
        record.markdown = check.approved_source
        record.content_hash = check.approved_hash
        record.writer_credit = run.editorial.get('writer_credit', '')
        record.save()
    run.state = 'publishing'
    save(run, 'publish', approved_hash=check.approved_hash, publication_scope=check.session.get('scope', 'full'))
    # Worker owns the lock. Publisher also verifies the exact source against the
    # latest Git base before committing, so a concurrent edit invalidates approval.
    publish_site()


def process(run):
    run.submission.refresh_from_db()
    if run.submission.status not in ('new', 'reviewing'):
        run.state = 'published' if run.submission.status == 'resolved' else run.submission.status
        run.save(update_fields=['state', 'updated_at'])
        return
    if not run.editorial.get('stage'):
        from . import ideas
        if ideas.pending(run):
            ideas.propose(run)
        else:
            prepare(run)
        return
    stage = run.editorial['stage']
    if stage == 'triage':
        from .catalog import articles
        result = ai.triage(run, {slug: data['title'] for slug,data in articles().items()})
        run.triage = result
        run.save(update_fields=['triage', 'updated_at'])
        if not ai.valid_triage(result):
            raise InvalidArticle('screening_response_invalid')
        if ai.confident(result, 'scope', 'out_of_scope'):
            conclude(run, 'declined', 'The request is outside the encyclopedia’s cryptocurrency scope.')
        elif ai.confident(result, 'injection', 'injection'):
            conclude(run, 'declined', 'The submission contains instructions to control the system rather than an article request or factual correction.')
        else:
            save(run, 'research')
        return
    if stage == 'research':
        run.state = 'researching'
        if not run.research:
            run.research = ai.research(run)
            run.save(update_fields=['research', 'updated_at'])
        if not citable_urls(run.research) and run.submission.kind == 'request':
            nothing_published(run, 'Research found no usable sources for this subject, so no article was written.')
        else:
            save(run, 'write')
        return
    if stage == 'write':
        try:
            write_candidate(run)
        except InvalidArticle as exc:
            if str(exc) == 'insufficient_evidence':
                nothing_published(run, 'The sources found do not cover this subject well enough to write an article.')
            else:
                retry_writing(run, str(exc))
        return
    if stage == 'screen':
        result = ai.review_output(run) if run.submission.kind == 'request' else ai.review_improvement(run, run.article_revision)
        run.output_review = result
        run.save(update_fields=['output_review', 'updated_at'])
        if not ai.valid_output_review(result):
            raise InvalidArticle('screening_response_invalid')
        if ai.approved_improvement(result):
            coverage = result.get('answers', {}).get('coverage', {}).get('choice')
            run.editorial['fulfillment'] = 'complete' if coverage == 'complete' else 'partial'
            begin_check(run, run.editorial['candidate'])
        else:
            nothing_published(run, 'The drafted text did not make suitable progress on this suggestion, so nothing was published.'
                               + ('' if run.submission.kind == 'request' else ' The existing article is unchanged.'))
        return
    if stage == 'check':
        check = Verification.objects.get(pk=run.editorial['check_id'], run=run)
        try:
            check = check_step(check)
        except BudgetExceeded as exc:
            # The job's allowance ran out mid-check. Groups not yet checked stay
            # unconfirmed; what the finished groups confirmed is still published.
            if str(exc) != 'run_token_budget' or not close_unchecked(check, 'run_token_budget'):
                raise
        if check.state in ('failed', 'incomplete'):
            # No rewrite-and-recheck loop: every finished check ends in a
            # publication of what it confirmed, or a clear outcome.
            publish_confirmed(run, check)
        elif check.state == 'passed':
            publish_checked(run, check)
        return
    if stage == 'publish':
        check = Verification.objects.filter(run=run, state='passed', approved_hash=run.editorial['approved_hash']).latest('pk')
        publish_checked(run, check)
        return
    raise InvalidArticle('editorial_stage_invalid')


def change_summary(run, record):
    """Describe actual edited sections, using only verified public source text."""
    import re
    names = []
    original = getattr(record, 'original_markdown', '')
    for edit in run.draft.get('edits', []):
        anchor = edit.get('anchor', '')
        before = original.split(anchor, 1)[0] if anchor else ''
        headings = re.findall(r'^#{2,3} (.+)$', before, re.M)
        inserted = re.findall(r'^#{2,3} (.+)$', edit.get('markdown', ''), re.M)
        for heading in inserted or (headings[-1:] if headings else ['Introduction']):
            if heading in record.markdown and heading not in names:
                names.append(heading)
    sections = ', '.join(names[:5])[:200]
    return (f'Updated {sections}. ' if sections else
            'A useful edit was published. ') + 'The activity history links to the exact changes.'
