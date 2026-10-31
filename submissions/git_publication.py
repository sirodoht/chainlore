"""Repository writes for article publication. Credentials never enter the checkout."""
import hashlib
import os
import re
import shlex
import subprocess
from django.conf import settings


class GitPublicationError(ValueError):
    pass


def git_env():
    env = {**os.environ, 'GIT_TERMINAL_PROMPT': '0',
           'GIT_CONFIG_GLOBAL': '/dev/null', 'GIT_CONFIG_NOSYSTEM': '1',
           'GIT_AUTHOR_NAME': 'Chainlore Bot', 'GIT_COMMITTER_NAME': 'Chainlore Bot',
           'GIT_AUTHOR_EMAIL': 'bot@chainlore.xyz', 'GIT_COMMITTER_EMAIL': 'bot@chainlore.xyz'}
    if settings.ARTICLE_GIT_KEY:
        env['GIT_SSH_COMMAND'] = (
            'ssh -F /dev/null -o BatchMode=yes -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes '
            '-o UserKnownHostsFile=' + shlex.quote(str(settings.ARTICLE_GIT_KNOWN_HOSTS)) +
            ' -i ' + shlex.quote(str(settings.ARTICLE_GIT_KEY)))
    return env


def git(directory, *args):
    result = subprocess.run(
        ['git', '-c', 'core.hooksPath=/dev/null', '-c', 'core.excludesFile=/dev/null',
         '-c', 'core.attributesFile=/dev/null', '-c', 'commit.gpgsign=false',
         '-C', str(directory), *args], env=git_env(), capture_output=True, timeout=120)
    if result.returncode:
        # Git/SSH output may contain local paths, credentials or untrusted remote text.
        raise GitPublicationError('git_' + args[0] + '_failed')
    return result.stdout.decode().strip()


def clone_source(directory):
    if not settings.ARTICLE_GIT_REMOTE:
        raise GitPublicationError('article_git_remote_not_configured')
    git(directory.parent, 'clone', '--depth=1', '--single-branch', '--branch',
        settings.ARTICLE_GIT_BRANCH, '--', settings.ARTICLE_GIT_REMOTE, str(directory))


def stage_articles(source, records, index_articles):
    """Never overwrite an editor's file; replacements require the exact old hash."""
    additions = []
    paths = []
    if (source / 'pages').is_symlink() or (source / 'INDEX.md').is_symlink():
        raise GitPublicationError('unsafe_article_path')
    for record in records:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', record.slug):
            raise GitPublicationError('invalid_stored_slug')
        relative = f'pages/{record.slug}.md'
        destination = source / relative
        if destination.is_symlink():
            raise GitPublicationError('unsafe_article_path')
        existing = destination.read_text() if destination.exists() else None
        if existing == record.markdown:
            additions.append(record)
            continue
        # Legacy import preserves deliberately curated repository articles.
        if record.published_at is not None and existing is not None:
            continue
        if record.published_at is None:
            if record.base_content_hash:
                digest = hashlib.sha256(existing.encode()).hexdigest() if existing is not None else ''
                if digest != record.base_content_hash:
                    raise GitPublicationError('article_changed_in_git')
            elif existing is not None:
                # A new page appeared while research was running. Publish the repo version.
                continue
            elif record.git_revision:
                raise GitPublicationError('article_removed_from_git')
        destination.write_text(record.markdown)
        paths.append(relative)
        additions.append(record)
    if additions:
        index = source / 'INDEX.md'
        before = index.read_text()
        after = index_articles(before, additions)
        if after != before:
            index.write_text(after)
            paths.append('INDEX.md')
    if paths:
        git(source, 'add', '--', *paths)
    return paths


def commit_and_push(source, paths):
    if paths:
        # All message text is fixed; no request text, email or research is committed.
        git(source, 'commit', '-m', 'Publish requested articles as Markdown')
        git(source, 'push', 'origin', 'HEAD:refs/heads/' + settings.ARTICLE_GIT_BRANCH)
    return git(source, 'rev-parse', 'HEAD')
