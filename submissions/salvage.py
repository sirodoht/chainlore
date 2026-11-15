"""Keep what the checker confirmed, leave out the rest, and queue the remainder.

A check that confirms only part of a candidate still ends in a publication:
software removes the unconfirmed passages (it never rewrites them), re-matches
every remaining unit against the saved verdicts, and publishes that subset as
Draft. Nothing here calls a model.
"""
import re
from .article_validation import InvalidArticle, validate_draft
from .improvements import apply_patch, split_article, validate_patch
from .models import Submission
from .verification import approve_confirmed, confirmed_units, inventory, structural_unit

SEPARATOR = re.compile(r'[| :\-]+')
FOLLOW_UP_PREFIX = 'followup:'
MAX_FOLLOW_UPS = 2


def blocks_of(text):
    return [block.strip() for block in re.split(r'\n\s*\n', text) if block.strip()]


def empty_headings(blocks):
    """Single-line headings with nothing under them before the next heading of their level."""
    empty = []
    for index, block in enumerate(blocks):
        level = re.match(r'(#+) ', block)
        if not level or '\n' in block:
            continue
        following = re.match(r'(#+) ', blocks[index + 1]) if index + 1 < len(blocks) else None
        if index + 1 == len(blocks) or (following and len(following[1]) <= len(level[1])):
            empty.append(index)
    return empty


def prune(text, keep):
    """Remove unconfirmed paragraphs, list items and table rows.

    Units are split exactly as verification.inventory splits them. Returns the
    remaining text and whether any factual unit remains.
    """
    original = blocks_of(text)
    already_empty = {original[index] for index in empty_headings(original)}
    kept, factual = [], False
    for block in original:
        if block.startswith('|') or block.startswith(('- ', '* ')):
            lines = block.splitlines()
            remaining, rows = [], 0
            for index, line in enumerate(lines):
                if not line.strip():
                    continue
                if SEPARATOR.fullmatch(line):
                    remaining.append(line)
                    continue
                header = index + 1 < len(lines) and bool(SEPARATOR.fullmatch(lines[index + 1]))
                unit = {'text': line.strip(), 'table_header': header}
                if structural_unit(unit):
                    remaining.append(line)
                    rows += not header
                elif keep(unit['text']):
                    remaining.append(line)
                    rows += 1
                    factual = True
            if rows:
                kept.append('\n'.join(remaining))
        elif structural_unit({'text': block}):
            kept.append(block)
        elif keep(block):
            kept.append(block)
            factual = True
    # A heading whose content was all removed goes too; one that was already bare stays.
    while True:
        index = next((index for index in empty_headings(kept) if kept[index] not in already_empty), None)
        if index is None:
            break
        del kept[index]
    return '\n\n'.join(kept), factual


def used_definitions(references, text):
    """Footnote definitions still cited by the remaining text."""
    return '\n'.join(line for line in references.strip().splitlines()
                     if (label := re.match(r'\[\^([^\]]+)\]:', line)) and f'[^{label[1]}]' in text)


def pruned_patch(run, record, confirmed):
    """The saved patch without the edits, paragraphs and rows that were not confirmed."""
    prefix = f'imp-{run.pk}-'
    namespaced = lambda value: re.sub(r'\[\^(\d+)\]', lambda match: f'[^{prefix}{match[1]}]', value)
    # Text already in the article was not part of this check and needs no verdict.
    unchanged = {unit['text'] for unit in inventory(record.original_markdown, allow_empty=True)[0]}
    keep = lambda text: namespaced(text) in confirmed or text in unchanged
    edits = []
    for edit in run.draft.get('edits', []):
        text, factual = prune(edit['markdown'], keep)
        if edit['position'] == 'replace':
            # A replacement stands in for existing text, so it is kept whole or not at all.
            if text == '\n\n'.join(blocks_of(edit['markdown'])):
                edits.append(edit)
        elif text and (factual or not prune(edit['markdown'], lambda _: True)[1]):
            edits.append({**edit, 'markdown': text})
    if not edits:
        raise InvalidArticle('nothing_confirmed')
    patch = {**run.draft, 'edits': edits,
             'references': used_definitions(run.draft.get('references', ''), '\n'.join(edit['markdown'] for edit in edits))}
    patch.pop('markdown', None)
    validate_patch(record, patch, run.research)
    return patch, apply_patch(record, patch, record.original_markdown)


def pruned_article(run, candidate, confirmed):
    """A new article without its unconfirmed paragraphs and rows."""
    metadata, body = split_article(candidate)
    if f'title: {metadata.get("title", "")}' not in confirmed:
        raise InvalidArticle('nothing_confirmed')
    ticker = metadata.get('ticker', 'None')
    if ticker != 'None' and f'ticker: {ticker}' not in confirmed:
        ticker = 'None'
    prose, _, references = body.partition('## References')
    text, factual = prune(prose, lambda value: value in confirmed)
    if not factual:
        raise InvalidArticle('nothing_confirmed')
    definitions = used_definitions(references, text)
    markdown = text + ('\n\n## References\n\n' + definitions if definitions else '')
    draft = {**run.draft, 'ticker': ticker, 'markdown': markdown}
    # The same structural rules as a fresh draft: footnotes, links and inert Markdown.
    validate_draft(draft, run.research, minimum_length=50)
    front = '\n'.join(f'{key}: {ticker if key == "ticker" else value}' for key, value in metadata.items())
    return draft, f'---\n{front}\n---\n\n{markdown.strip()}\n'


def confirmed_subset(run, check):
    """Return (approved check, left-out unit texts), or raise InvalidArticle if nothing was confirmed."""
    kept, rejected, unchecked = confirmed_units(check)
    confirmed = {unit['text'] for unit in kept}
    if check.session.get('scope') == 'edit':
        run.draft, source = pruned_patch(run, run.article_revision, confirmed)
    else:
        run.draft, source = pruned_article(run, check.source, confirmed)
    approved = approve_confirmed(check, source)
    left_out = [unit['text'] for unit in rejected + unchecked if unit['text'] not in source]
    return approved, left_out


def checker_issues(check):
    issues = [issue for batch in check.session.get('batches', []) for issue in (batch.get('report') or {}).get('issues', [])
              if isinstance(issue, str)]
    return list(dict.fromkeys(issues))


def remainder_details(action, passages, issues):
    lines = [action, '', 'Passages left out:']
    lines += [f'- {" ".join(text.split())[:400]}' for text in passages[:12]]
    if issues:
        lines += ['', 'Checker findings:'] + [f'- {" ".join(issue.split())[:400]}' for issue in issues[:12]]
    return '\n'.join(lines)[:5000]


def follow_up_depth(submission):
    key = submission.maintenance_key or ''
    return int(key.split(':')[1]) if re.fullmatch(FOLLOW_UP_PREFIX + r'\d+:\d+', key) else 0


def queue_follow_up(run, record):
    """After a partial publication, queue the unconfirmed remainder as its own smaller job."""
    follow_up = run.editorial.get('follow_up')
    depth = follow_up_depth(run.submission) + 1
    if not follow_up or depth > MAX_FOLLOW_UPS:
        return None
    submission, _ = Submission.objects.get_or_create(maintenance_key=f'{FOLLOW_UP_PREFIX}{depth}:{run.pk}', defaults={
        'kind': 'improvement', 'article': record.slug, 'title': record.title,
        'public_title': f'Follow-up: {record.title}', 'details': follow_up})
    return submission


def queue_repair(record, check, passages, issues):
    """A full check found unconfirmed passages in a published article: queue one targeted edit."""
    submission, _ = Submission.objects.get_or_create(
        maintenance_key=f'repair:{record.slug}:{check.source_hash[:16]}', defaults={
            'kind': 'improvement', 'article': record.slug, 'title': record.title,
            'public_title': f'Repair: {record.title}',
            'details': remainder_details(
                'A full check could not confirm the passages below against their cited sources. For each one, cite a '
                'source passage that states it, narrow or attribute the claim, or remove it. Change nothing else.',
                passages, issues)})
    return submission
