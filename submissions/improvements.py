"""Targeted article edits with source validation and conservative conflict handling."""
from datetime import date
import hashlib
from pathlib import Path
import re
import tempfile
from django.conf import settings
from django.db import transaction
from . import ai_providers as ai
from .article_validation import InvalidArticle, PLACEHOLDER, citable_urls, extract_draft, require, validate_draft
from .git_publication import GitPublicationError, clone_source, git
from .models import ArticleRevision


class ImprovementConflict(GitPublicationError):
    pass


def split_article(source):
    if not source.startswith('---\n') or source.count('---\n') < 2:
        raise ImprovementConflict('article_metadata_missing')
    _, front, body = source.split('---\n', 2)
    metadata = dict(line.split(':', 1) for line in front.splitlines() if ':' in line)
    return {key: value.strip() for key, value in metadata.items()}, body


def snapshot_article(run):
    slug = run.inputs['article']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ImprovementConflict('invalid_article_slug')
    with tempfile.TemporaryDirectory(prefix='improvement-', dir=settings.DATA_DIR) as directory:
        source = Path(directory) / 'source'
        clone_source(source)
        path = source / 'pages' / (slug + '.md')
        if not path.is_file() or path.is_symlink() or path.parent.is_symlink():
            raise ImprovementConflict('article_missing_from_git')
        if path.stat().st_size > 200000:
            raise ImprovementConflict('article_too_large_for_improvement')
        markdown = path.read_text()
        metadata, _ = split_article(markdown)
        record = ArticleRevision.objects.create(
            run=run, slug=slug, title=metadata['title'], original_markdown=markdown,
            base_content_hash=hashlib.sha256(markdown.encode()).hexdigest(),
            base_revision=git(source, 'rev-parse', 'HEAD'))
    run.inputs['title'] = record.title
    run.save(update_fields=['inputs', 'updated_at'])
    return record


def validate_patch(record, patch, research):
    edits, references = patch.get('edits'), patch.get('references')
    require(isinstance(edits, list) and 1 <= len(edits) <= 30, 'invalid_improvement_edits')
    require(isinstance(references, str) and references.strip(), 'missing_improvement_references')
    # References must contain only definitions; no unvalidated prose after References.
    require(all(re.fullmatch(r'\[\^\d+\]:\s+\[[^\]\n]+\]\(https?://[^\s)]+\)', line)
                for line in references.strip().splitlines()), 'invalid_improvement_references')
    _, body = split_article(record.original_markdown)
    require(body.count('## References') == 1, 'unsupported_reference_section')
    prose = body.split('## References')[0]
    blocks = {block.strip() for block in re.split(r'\n\s*\n', prose) if block.strip()}
    anchors, snippets, replaced = set(), [], 0
    for edit in edits:
        require(isinstance(edit, dict), 'invalid_improvement_edit')
        anchor, text, position = edit.get('anchor'), edit.get('markdown'), edit.get('position')
        require(isinstance(anchor, str) and 1 <= len(anchor) <= 5000, 'invalid_improvement_anchor')
        require(isinstance(text, str) and text.strip(), 'empty_improvement_edit')
        require(PLACEHOLDER not in text, 'improvement_placeholder')
        require(position in ('before', 'after', 'replace'), 'invalid_improvement_position')
        require(anchor not in anchors, 'duplicate_improvement_anchor')
        anchors.add(anchor)
        require((anchor in blocks and prose.count(anchor) == 1) or
                (anchor == '## References' and position == 'before'), 'improvement_anchor_not_unique')
        require(not re.search(r'^\[\^|^## References\s*$', text, re.M), 'references_inside_improvement')
        if position == 'replace':
            require(not anchor.startswith(('#', '|', '- ', '* ')), 'unsupported_improvement_replacement')
            replaced += len(anchor)
        snippets.append(text.strip())
    # This is a substantive editing pass, not a complete rewrite of the original author.
    require(replaced <= len(prose) // 3, 'improvement_rewrites_too_much')
    # Validate only new text here. Curated article titles need not slugify to their
    # historic filenames (for example, Non-fungible token lives at nft.md).
    draft = {'title': 'Article improvement', 'slug': 'article-improvement', 'ticker': 'None',
             'category': 'Other', 'markdown': '\n\n'.join(snippets) + '\n\n## References\n\n' + references.strip()}
    validate_draft(draft, research, minimum_length=50)


def apply_patch(record, patch, current):
    """Apply only exact, unchanged paragraph anchors; preserve other editors' work."""
    metadata, body = split_article(current)
    if metadata.get('title') != record.title:
        raise ImprovementConflict('article_identity_changed')
    prefix = f'imp-{record.run_id}-'
    if f'[^{prefix}' in body:
        # A previous push succeeded before its DB checkpoint. Never apply it twice,
        # including if an editor has subsequently changed or checked the article.
        return current
    if body.count('## References') != 1:
        raise ImprovementConflict('article_references_changed')
    prose = body.split('## References')[0]
    blocks = {block.strip() for block in re.split(r'\n\s*\n', prose) if block.strip()}
    operations = []
    replaced_references = set()
    for edit in patch['edits']:
        anchor, position = edit['anchor'], edit['position']
        if not ((anchor in blocks and prose.count(anchor) == 1) or
                (anchor == '## References' and position == 'before')):
            raise ImprovementConflict('improvement_passage_changed')
        start = body.index(anchor)
        text = re.sub(r'\[\^(\d+)\]', lambda match: f'[^{prefix}{match[1]}]', edit['markdown'].strip())
        if position == 'before':
            operations.append((start, start, text + '\n\n'))
        elif position == 'after':
            end = start + len(anchor)
            operations.append((end, end, '\n\n' + text))
        else:
            replaced_references.update(re.findall(r'\[\^([^\]]+)\]', anchor))
            operations.append((start, start + len(anchor), text))
    for start, end, text in sorted(operations, reverse=True):
        body = body[:start] + text + body[end:]
    # A replaced paragraph may have been the only use of an old reference.
    # Remove only those newly orphaned definitions; retain every still-used source.
    for label in replaced_references:
        marker = re.escape('[^' + label + ']')
        if not re.search(marker + r'(?!:)', body):
            body = re.sub(r'^' + marker + r':[^\n]*(?:\n[ \t]+[^\n]*)*\n?', '', body, flags=re.M)
    references = re.sub(r'\[\^(\d+)\]', lambda match: f'[^{prefix}{match[1]}]', patch['references'].strip())
    body = body.rstrip() + '\n\n' + references + '\n'
    require(len(body) <= 200000, 'improved_article_too_large')
    metadata.update(status='draft', updated=date.today().isoformat())
    metadata.setdefault('written_by', 'Unknown')
    for field in ('checked', 'checked_by', 'reviewed', 'reviewed_by'):
        metadata.pop(field, None)
    front = '\n'.join(f'{key}: {value}' for key, value in metadata.items())
    return '---\n' + front + '\n---\n' + body


def reconcile_revision(record, current):
    if current is None:
        raise ImprovementConflict('article_removed_from_git')
    if record.git_revision:
        # Already pushed; subsequent editorial changes belong to the repository.
        return current
    validate_patch(record, record.run.draft, record.run.research)
    return apply_patch(record, record.run.draft, current)


def process_improvement(run):
    from .automation import event, finish
    from .publication import publish_site
    record = ArticleRevision.objects.filter(run=run).first() or snapshot_article(run)
    if record.markdown:
        publish_site()
        return
    if not run.triage:
        run.triage = ai.triage(run, {record.slug: {'title': record.title}})
        run.save(update_fields=['triage', 'updated_at'])
    if not ai.valid_triage(run.triage):
        finish(run, 'review', 'triage_invalid_response')
        return
    if ai.confident(run.triage, 'scope', 'out_of_scope') or ai.confident(run.triage, 'injection', 'injection'):
        finish(run, 'declined', 'out_of_scope_or_injection')
        return
    event(run, 'triage_passed', decision='research_article_improvement')
    if not run.research:
        run.research = ai.research(run)
        run.save(update_fields=['research', 'updated_at'])
    if not citable_urls(run.research):
        finish(run, 'review', 'improvement_has_no_sources')
        return
    if not run.draft:
        problem = None
        for _ in range(2):
            try:
                response = ai.write_improvement(run, record, problem)
                patch = extract_draft(response)
                validate_patch(record, patch, run.research)
                patch['_written_by'] = response.get('_written_by', 'Unknown')
                patch['markdown'] = apply_patch(record, patch, record.original_markdown)
                run.draft = patch
                run.save(update_fields=['draft', 'updated_at'])
                break
            except InvalidArticle as exc:
                problem = str(exc)
                event(run, 'validation', passed=False, reason=problem)
        if not run.draft:
            finish(run, 'review', problem or 'invalid_improvement')
            return
    validate_patch(record, run.draft, run.research)
    if not run.output_review:
        run.output_review = ai.review_improvement(run, record)
        run.save(update_fields=['output_review', 'updated_at'])
    if not ai.approved_improvement(run.output_review):
        finish(run, 'review', 'improvement_needs_review')
        return
    with transaction.atomic():
        run.submission.refresh_from_db()
        if run.submission.status != 'reviewing':
            finish(run, 'review', 'submission_changed_during_generation')
            return
        record.markdown = apply_patch(record, run.draft, record.original_markdown)
        record.content_hash = hashlib.sha256(record.markdown.encode()).hexdigest()
        record.writer_credit = run.draft['_written_by']
        record.save(update_fields=['markdown', 'content_hash', 'writer_credit'])
    publish_site()
