"""Rebuild Git sources plus durable database articles, then atomically switch the site."""
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.utils import timezone as django_timezone
from .categories import CATEGORY_SECTIONS
from .models import AutomationEvent, AutomationRun, GeneratedArticle, Submission


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
        additions.setdefault(heading, []).append(f'- [{record.title}](pages/{record.slug}.md)')
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


def publish_site(base_release=None):
    """Caller holds publication_lock. No model-controlled commands or filesystem paths."""
    base = settings.BASE_DIR
    output = settings.PUBLICATION_ROOT
    releases = output / 'releases'
    releases.mkdir(parents=True, exist_ok=True, mode=0o755)
    os.chmod(output, 0o755)
    os.chmod(releases, 0o755)
    source_info = Path(base_release or settings.SITE_ROOT) / 'build-info.json'
    info = json.loads(source_info.read_text()) if source_info.exists() else {'revision': 'development', 'release': 'development'}
    name = 'generated-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ-') + uuid.uuid4().hex[:12]
    target = releases / name
    records = list(GeneratedArticle.objects.filter(
        Q(published_at__isnull=False) |
        Q(run__state__in=['queued', 'running', 'retry'], run__submission__status='reviewing')
    ).order_by('slug'))
    with tempfile.TemporaryDirectory(prefix='publication-', dir=settings.DATA_DIR) as directory:
        source = Path(directory)
        for folder in ('pages', 'site'):
            shutil.copytree(base / folder, source / folder)
        for file in ('README.md', 'INDEX.md', 'ABOUT.md', 'VISION.md', 'POLICY.md'):
            shutil.copyfile(base / file, source / file)
        additions = []
        for record in records:
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', record.slug):
                raise ValueError('invalid_stored_slug')
            destination = source / 'pages' / (record.slug + '.md')
            # An article deliberately added to Git takes precedence over its generated original.
            if not destination.exists():
                destination.write_text(record.markdown)
                additions.append(record)
        if additions:
            index = source / 'INDEX.md'
            index.write_text(index_generated_articles(index.read_text(), additions))
        env = {**os.environ, 'CHAINLORE_BUILD_ROOT': str(source)}
        for script in ('build.py', 'check.py'):
            result = subprocess.run([sys.executable, str(base / 'scripts' / script)], env=env,
                                    capture_output=True, timeout=120)
            if result.returncode:
                # Output could contain untrusted article text. Never copy it into logs.
                raise ValueError('site_' + script.removesuffix('.py') + '_failed')
        info['publication'] = name
        info['generated_articles'] = {record.slug: record.content_hash for record in records}
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
            GeneratedArticle.objects.filter(pk=record.pk).update(published_at=django_timezone.now())
            # A deploy can finish a publication interrupted after its source was saved.
            if AutomationRun.objects.filter(pk=record.run_id, state__in=['queued', 'running', 'retry']).update(state='published', last_error=''):
                Submission.objects.filter(automation__pk=record.run_id, status='reviewing').update(
                    status='resolved', resulting_url=f'https://chainlore.xyz/p/{record.slug}/', updated_at=django_timezone.now())
                AutomationEvent.objects.create(run_id=record.run_id, kind='publication', data={
                    'release': name, 'content_hash': record.content_hash, 'slug': record.slug,
                    'decision': 'validated_draft_published'})
    return name
