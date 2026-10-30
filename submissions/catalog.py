import json
from django.conf import settings


def articles():
    return json.loads(settings.ARTICLE_CATALOG.read_text())


def revision():
    path = settings.SITE_ROOT / 'build-info.json'
    return json.loads(path.read_text()).get('revision', '') if path.exists() else ''
