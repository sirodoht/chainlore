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
from .verification import digest, step as check_step, opened_sources, evidence_responses

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
    run.editorial = {'stage': 'triage', 'revisions': 0}
    run.save()
    event(run, 'attempt_started', policy_version=3)
    if run.submission.kind == 'maintenance':
        from .maintenance import enrich
        begin_check(run, enrich(record.original_markdown, record.slug))


def begin_check(run, source):
    check = Verification.objects.create(run=run, source=source, source_hash=digest(source))
    run.state = 'checking'
    save(run, 'check', check_id=check.pk, candidate=source)
    event(run, 'checking_started', source_hash=check.source_hash)


def insufficient(run, reason):
    conclude(run, 'insufficient', reason)


def revise(run, reason):
    count = run.editorial.get('revisions', 0)
    check = run.verifications.filter(pk=run.editorial.get('check_id'), state='failed').first() if isinstance(reason, dict) else None
    assessment = reason.get('assessment', {}) if isinstance(reason, dict) else {}
    supported_ids = {u['id'] for u in assessment.get('units', []) if u.get('verdict') in ('supported', 'nonfactual')}
    if check:
        for batch in check.session.get('batches', []):
            supported_ids.update(u['id'] for u in batch.get('report', {}).get('units', [])
                                 if u.get('verdict') in ('supported', 'nonfactual'))
    supported = len(supported_ids)
    score = {'supported':supported, 'issues':len(assessment.get('issues', [])),
             'candidate':digest(run.editorial.get('candidate', ''))}
    previous = run.editorial.get('revision_progress')
    advancing = previous is None or (bool(assessment) and score['candidate'] != previous['candidate'] and
        (score['supported'] > previous['supported'] or
         (score['supported'] >= previous['supported'] and score['issues'] < previous['issues'])))
    stalled = 0 if advancing else run.editorial.get('stalled_revisions', 0)+1
    run.editorial.update(revision_progress=score, stalled_revisions=stalled)
    if stalled >= settings.EDITORIAL_MAX_STALLED_REVISIONS:
        insufficient(run, 'Repeated correction passes did not improve the verified coverage or resolve the remaining findings. The existing article has been preserved.')
        return
    run.inputs['verification_feedback'] = reason
    # Checker findings already identify concrete edits and fetched evidence.
    # Reuse those documents instead of discarding work and researching again.
    targeted = False
    if check:
        sources = opened_sources(evidence_responses(check))
        research = {'content':[{'type':'web_fetch_tool_result', 'content':{'type':'web_fetch_result','url':url,
            'content':{'source':{'type':'text','data':text}}}} for url,text in sources.items()]}
        if sources:
            try:
                ai.research_context(research)
            except ai.ProviderError:
                targeted = bool(run.research)
            else:
                run.research = research
                targeted = True
    if not targeted:
        run.research = {}
        run.research_session = {}
    run.output_review = {}
    run.state = 'revising'
    run.editorial.pop('writer_response', None)
    run.editorial.pop('writer_problem', None)
    run.editorial.update(stage='write' if targeted else 'research', revisions=count+1, feedback=reason, writer_retries=0)
    run.save()
    event(run, 'revision_requested', attempt=count+1, targeted=targeted, stalled_revisions=stalled)


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


def write_candidate(run):
    kind = run.submission.kind
    problem = run.editorial.get('feedback')
    if run.editorial.get('writer_problem'):
        problem = {'checker_feedback':problem, 'output_problem':run.editorial['writer_problem']}
    if kind == 'request':
        response = writer_response(run, kind, problem)
        draft = extract_draft(response)
        source, _ = validate_draft(draft, run.research)
        source, _ = attribute_source(source, response.get('_written_by', 'Unknown'))
        run.draft = draft
        run.editorial['writer_credit'] = response.get('_written_by', 'Unknown')
    else:
        record = run.article_revision
        response = writer_response(run, kind, problem)
        draft = extract_draft(response)
        if draft.get('insufficient_evidence'):
            # A checker can validate the existing article independently; a no-edit
            # writer response never by itself dismisses a correction report.
            run.editorial['no_change'] = True
            source = record.original_markdown
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
        insufficient(run, 'Independent checking supported the existing article, but the suggested improvement could not be substantiated.')
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
    save(run, 'publish', approved_hash=check.approved_hash)
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
        if not citable_urls(run.research):
            revise(run, 'Research did not return usable evidence; try different primary sources.')
        else:
            save(run, 'write')
        return
    if stage == 'write':
        try:
            write_candidate(run)
        except InvalidArticle as exc:
            if str(exc) == 'insufficient_evidence':
                revise(run, 'The writer could not support the requested article from the saved evidence; investigate missing sources.')
            else:
                retry_writing(run, str(exc))
        return
    if stage == 'screen':
        result = ai.review_output(run) if run.submission.kind == 'request' else ai.review_improvement(run, run.article_revision)
        run.output_review = result
        run.save(update_fields=['output_review', 'updated_at'])
        if ai.approved_improvement(result):
            begin_check(run, run.editorial['candidate'])
        else:
            revise(run, 'Output screening did not establish that the draft answers the request without unsuitable content.')
        return
    if stage == 'check':
        check = Verification.objects.get(pk=run.editorial['check_id'], run=run)
        check = check_step(check)
        if check.state == 'incomplete':
            run.state = 'blocked'
            run.last_error = check.report['errors'][0]
            run.next_attempt_at = None
            run.save()
            event(run, 'operational_block', code=run.last_error)
        elif check.state == 'failed':
            revise(run, check.report)
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
    return (f'Updated {sections} with independently checked source material. ' if sections else
            'A sourced change was independently fact-checked and published. ') + 'The activity history links to the exact changes.'
