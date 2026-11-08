"""Budgeted maintenance uses the same verifier/publication path as reader work."""
from datetime import date, timedelta
import re
from django.conf import settings
from django.utils import timezone
from .catalog import articles
from .models import Submission
from .improvements import split_article


def enrich(source, slug):
    metadata, body = split_article(source)
    aliases = {'Exchanges': 'Exchange', 'Decentralised finance': 'DeFi'}
    metadata['category'] = aliases.get(metadata.get('category'), metadata.get('category', 'Other'))
    catalog = articles()
    # Conservative related links: only subjects actually named in the existing
    # public prose. Never auto-merge distinct articles or remove content.
    if '## See also' not in body and '## References' in body:
        related = [other for other, item in catalog.items() if other != slug and
                   len(item['title']) > 3 and re.search(r'\b'+re.escape(item['title'])+r'\b', body.split('## References')[0], re.I)]
        if related:
            links = '\n'.join(f'- [{catalog[other]["title"]}]({other}.md)' for other in sorted(related)[:5])
            body = body.replace('## References', '## See also\n\n'+links+'\n\n## References', 1)
    return '---\n'+'\n'.join(f'{k}: {v}' for k,v in metadata.items())+'\n---\n'+body


def enqueue():
    if not settings.MAINTENANCE_ENABLED:
        return None
    today = timezone.localdate()
    if Submission.objects.filter(kind='maintenance', created_at__date=today).count() >= settings.MAINTENANCE_DAILY_LIMIT:
        return None
    catalog = articles()
    choices = []
    for slug, page in catalog.items():
        try:
            checked = date.fromisoformat(page.get('checked', ''))
        except ValueError:
            checked = date.min
        if page.get('status') != 'draft' and checked != date.min and (today-checked).days < settings.MAINTENANCE_INTERVAL_DAYS:
            continue
        if Submission.objects.filter(article=slug, status__in=['new', 'reviewing']).exists():
            continue
        recent = Submission.objects.filter(kind='maintenance', article=slug,
            created_at__gte=timezone.now()-timedelta(days=7)).exists()
        if not recent:
            choices.append((checked, slug, page['title']))
    if not choices:
        return None
    _, slug, title = min(choices)
    key = f'{slug}:{today.isoformat()}'
    submission, _ = Submission.objects.get_or_create(maintenance_key=key, defaults={
        'kind': 'maintenance', 'article': slug, 'title': title, 'public_title': f'Scheduled check: {title}',
        'details': 'Check every source and claim, investigate significant developments since the last check, repair broken references using equivalent primary evidence, and maintain category and related-article consistency.'})
    return submission


def queue_full_check(record):
    """One pending background check per article, even after several useful edits."""
    if Submission.objects.filter(kind='maintenance', article=record.slug, status__in=['new', 'reviewing']).exists():
        return
    Submission.objects.get_or_create(maintenance_key=f'published:{record.slug}:{record.content_hash}', defaults={
        'kind': 'maintenance', 'article': record.slug, 'title': record.title,
        'public_title': f'Background check: {record.title}',
        'details': 'Independently check the entire current article and its sources. Repair inaccessible references using equivalent evidence. Reader edits were published as Draft; only a completed full check may certify the article.'})
