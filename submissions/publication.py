"""Commit accepted drafts, then publish a validated snapshot of the Git branch."""
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import xml.etree.ElementTree as ET
import markdown
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.utils import timezone as django_timezone
from .categories import CATEGORY_SECTIONS
from .git_publication import clone_source, commit_and_push, stage_articles
from .models import AutomationEvent, AutomationRun, GeneratedArticle, Submission, ArticleRevision


def article_summary(record):
    """Use an excerpt of the validated lead, without another model call or new claims."""
    body = record.markdown.split('---\n', 2)[-1].strip()
    if 'This is a placeholder:' in body:
        return 'Draft awaiting fuller coverage.'
    lead = re.split(r'\n\s*\n', body, maxsplit=1)[0]
    lead = re.sub(r'\[\^[^\]]+\]', '', lead)
    tree = ET.fromstring('<div>' + markdown.markdown(lead) + '</div>')
    paragraph = tree.find('p')
    text = ' '.join(''.join(paragraph.itertext()).split()) if paragraph is not None else ''
    text = re.sub(r'^' + re.escape(record.title) + r'\s+(?:is|was|are|were)\s+', '', text, flags=re.I)
    if not text:
        return 'Draft awaiting fuller coverage.'
    if len(text) > 180:
        text = text[:177].rsplit(' ', 1)[0].rstrip('.,;:') + '…'
    text = text[:1].upper() + text[1:]
    # Rendered plain text must remain text when inserted back into Markdown.
    return re.sub(r'([\\`*{}\[\]<>_])', r'\\\1', text)


def index_generated_articles(index, records):
    """Merge published articles into subject lists, retaining curated index text."""
    additions = {}
    for record in records:
        # Keep an editor's existing placement and avoid duplicate index entries.
        if f'](pages/{record.slug}.md)' in index:
            continue
        front = record.markdown.split('---\n', 2)[1] if record.markdown.startswith('---\n') else ''
        category = re.search(r'^category:\s*([^\n]+)', front, re.M)
        heading = CATEGORY_SECTIONS.get(category.group(1).strip() if category else '', 'Other topics')
        additions.setdefault(heading, []).append(f'- [{record.title}](pages/{record.slug}.md): {article_summary(record)}')
    for heading, links in additions.items():
        section = re.search(r'^## ' + re.escape(heading) + r'\s*$', index, re.M)
        if section:
            following = re.search(r'^## ', index[section.end():], re.M)
            end = section.end() + following.start() if following else len(index)
            index = index[:end].rstrip() + '\n' + '\n'.join(links) + '\n\n' + index[end:]
        else:
            index = index.rstrip() + f'\n\n## {heading}\n\n' + '\n'.join(links) + '\n'
    return index


@contextmanager
def publication_lock(blocking=True):
    with open(settings.DATA_DIR / 'automation.lock', 'a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB))
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def build_source(source):
    env = {**os.environ, 'CHAINLORE_BUILD_ROOT': str(source)}
    for script in ('build.py', 'check.py'):
        result = subprocess.run([sys.executable, str(settings.BASE_DIR / 'scripts' / script)], env=env,
                                capture_output=True, timeout=120)
        if result.returncode:
            # Output could contain untrusted article text. Never copy it into logs.
            raise ValueError('site_' + script.removesuffix('.py') + '_failed')


def publish_site(base_release=None, import_legacy=False):
    """Caller holds publication_lock. No model-controlled commands or filesystem paths."""
    output = settings.PUBLICATION_ROOT
    releases = output / 'releases'
    releases.mkdir(parents=True, exist_ok=True, mode=0o755)
    os.chmod(output, 0o755)
    os.chmod(releases, 0o755)
    source_info = Path(base_release or settings.SITE_ROOT) / 'build-info.json'
    info = json.loads(source_info.read_text()) if source_info.exists() else {'revision': 'development', 'release': 'development'}
    name = 'generated-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ-') + uuid.uuid4().hex[:12]
    target = releases / name
    ready_states = ['publishing'] if settings.AUTONOMOUS_EDITORIAL_ENABLED else ['queued', 'running', 'retry']
    eligible = Q(published_at__isnull=True, run__state__in=ready_states,
                 run__submission__status='reviewing')
    if import_legacy:
        eligible |= Q(published_at__isnull=False)
    records = list(GeneratedArticle.objects.filter(eligible).order_by('slug'))
    revisions = list(ArticleRevision.objects.filter(
        published_at__isnull=True, run__state__in=ready_states,
        run__submission__status='reviewing').exclude(markdown='').select_related('run').order_by('created_at'))
    # Serialize suggestions for the same article. A later one is picked up by its worker tick.
    seen = {record.slug for record in records}
    for record in revisions:
        if record.slug not in seen:
            records.append(record)
            seen.add(record.slug)
    with tempfile.TemporaryDirectory(prefix='publication-', dir=settings.DATA_DIR) as directory:
        source = Path(directory) / 'source'
        clone_source(source)
        paths = stage_articles(source, records, index_generated_articles)
        build_source(source)
        # Validate before committing; a rejected/non-fast-forward push never goes live.
        credits = [f'{record.slug}: {record.writer_credit}' for record in records
                   if isinstance(record, ArticleRevision) and f'pages/{record.slug}.md' in paths]
        edit_credits = []
        if settings.AUTONOMOUS_EDITORIAL_ENABLED and any(record.published_at is None for record in records):
            verification_credits = []
            for record in records:
                if record.published_at is not None:
                    continue
                check = record.run.verifications.filter(state='passed', approved_hash=record.content_hash).latest('pk')
                credit = f'{record.slug}: {check.checker}; checked {check.completed_at.date()}; source {check.approved_hash}; audit {check.pk}'
                if check.session.get('scope') in ('edit', 'draft'):
                    edit_credits.append(credit)
                else:
                    verification_credits.append(credit)
            revision = commit_and_push(source, paths, credits, verification_credits, edit_credits)
        else:
            revision = commit_and_push(source, paths, credits) if credits else commit_and_push(source, paths)
        published_hashes = {}
        for record in records:
            published_hashes[record.slug] = hashlib.sha256((source / 'pages' / (record.slug + '.md')).read_bytes()).hexdigest()
            type(record).objects.filter(pk=record.pk).update(
                git_revision=revision, markdown=record.markdown, content_hash=record.content_hash)
            AutomationEvent.objects.create(run_id=record.run_id, kind='git_publication', data={
                'revision': revision, 'slug': record.slug,
                'content_hash': published_hashes[record.slug]})
        info['app_revision'] = info.get('app_revision', info['revision'])
        info['revision'] = revision
        info['publication'] = name
        info.pop('generated_articles', None)
        (source / 'dist' / 'build-info.json').write_text(json.dumps(info) + '\n')
        shutil.copytree(source / 'dist', target)
    # Only rendered public files are copied; private sources, prompts and DB stay outside.
    for root, dirs, files in os.walk(target):
        os.chmod(root, 0o755)
        for file in files:
            os.chmod(Path(root) / file, 0o644)
    next_link = output / ('.next-' + uuid.uuid4().hex)
    next_link.symlink_to(target)
    os.replace(next_link, output / 'current')
    with transaction.atomic():
        for record in records:
            # Keeping an existing page live does not complete its regeneration.
            if record.published_at is not None:
                continue
            type(record).objects.filter(pk=record.pk).update(published_at=django_timezone.now())
            # A deploy can finish a publication interrupted after its source was saved.
            if AutomationRun.objects.filter(pk=record.run_id, state__in=ready_states).update(state='published', last_error='', updated_at=django_timezone.now()):
                submission = Submission.objects.get(automation__pk=record.run_id)
                if submission.status == 'reviewing':
                    submission.status = 'resolved'
                    submission.resulting_url = f'https://chainlore.xyz/p/{record.slug}/'
                    if settings.AUTONOMOUS_EDITORIAL_ENABLED:
                        run = AutomationRun.objects.get(pk=record.run_id)
                        submission.public_title = record.title
                        if submission.kind == 'maintenance':
                            submission.public_summary = 'The article was independently checked against live sources and refreshed where evidence supported changes.'
                        elif run.editorial.get('no_change'):
                            submission.public_summary = 'An independent source check supported the existing article. No factual correction was justified; its check record has been refreshed.'
                        elif submission.kind == 'request':
                            submission.public_summary = ('A sourced draft article was published. Full-article checking is queued separately.' if run.editorial.get('publication_scope') == 'draft' else 'The requested article was independently fact-checked and published.')
                        else:
                            from .editorial import change_summary
                            submission.public_summary = change_summary(run, record)
                            if run.editorial.get('publication_scope') == 'edit':
                                submission.public_summary += ' The changed passages were checked; the article is labelled Draft pending full-article checking.'
                        if run.editorial.get('fulfillment') == 'partial':
                            submission.public_summary += ' This addresses part of the suggestion; the full requested coverage is not complete.'
                    submission.save()
                    if settings.AUTONOMOUS_EDITORIAL_ENABLED and run.editorial.get('publication_scope') in ('edit', 'draft'):
                        from .maintenance import queue_full_check
                        queue_full_check(record)
                AutomationEvent.objects.create(run_id=record.run_id, kind='publication', data={
                    'release': name, 'content_hash': published_hashes[record.slug], 'slug': record.slug,
                    'revision': revision, 'decision': 'committed_article_published'})
    return name
