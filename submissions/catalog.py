import hashlib
import json
from django.conf import settings

_cache = {}


def cached(path, parse):
    """Read a published file once per publication, not once per request.

    Publication switches a symlink to a new release, which changes the resolved
    file's identity, so the stat signature invalidates the entry. Callers must
    treat the returned value as read-only.
    """
    stat = path.stat()
    signature = (stat.st_ino, stat.st_mtime_ns, stat.st_size)
    entry = _cache.get((path, parse))
    if entry is None or entry[0] != signature:
        if len(_cache) > 32:
            _cache.clear()
        entry = _cache[(path, parse)] = (signature, parse(path.read_bytes()))
    return entry[1]


def _digest(data):
    return hashlib.sha256(data).hexdigest()[:12]


def articles():
    return cached(settings.ARTICLE_CATALOG, json.loads)


def revision():
    try:
        return cached(settings.SITE_ROOT / 'build-info.json', json.loads).get('revision', '')
    except FileNotFoundError:
        return ''


def css_version():
    return cached(settings.SITE_ROOT / 'assets/site.css', _digest)
