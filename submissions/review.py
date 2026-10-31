"""Staff review of the current publication, with private error-report counts."""
import calendar
from collections import Counter
from datetime import date
from urllib.parse import urlencode

from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET

from .catalog import articles
from .models import Submission


STATUSES = {
    'draft': 'Draft',
    'ai-fact-checked': 'AI fact-checked',
    'human-reviewed': 'Human reviewed',
}
FILTERS = {
    'all': 'All articles',
    'attention': 'Needs attention',
    'draft': 'Drafts',
    'overdue': 'Due for recheck',
    'reports': 'With open error reports',
    'human': 'Awaiting human review',
    'reviewed': 'Human reviewed',
}
SORTS = {'priority': 'Review priority', 'oldest': 'Oldest full check', 'title': 'Article A–Z'}


def parse_date(value):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def six_months_after(value):
    month = value.month + 6
    year = value.year + (month - 1) // 12
    month = (month - 1) % 12 + 1
    return date(year, month, min(value.day, calendar.monthrange(year, month)[1]))


def reports_url(slug=None):
    query = {'kind__exact': 'correction', 'status__in': 'new,reviewing', 'duplicate_of__isnull': 'True'}
    if slug is not None:
        query['article__exact'] = slug
    return reverse('admin:submissions_submission_changelist') + '?' + urlencode(query)


def review_rows(catalog, reports, today):
    rows = []
    for slug, page in catalog.items():
        status = page.get('status', '')
        checked = parse_date(page.get('checked')) if status in ('ai-fact-checked', 'human-reviewed') else None
        issues = []
        if status not in STATUSES:
            issues.append('Review metadata unavailable')
        elif status != 'draft' and (not checked or not page.get('checked_by')):
            issues.append('Full-check date or checker missing')
        if checked and checked > today:
            issues.append('Full-check date is in the future')
        if status == 'human-reviewed' and (
            not parse_date(page.get('reviewed')) or not page.get('reviewed_by')
        ):
            issues.append('Human review credit missing')
        due = six_months_after(checked) if checked and checked <= today else None
        overdue = bool(due and today > due)
        report_count = reports.get(slug, 0)
        reasons = []
        if report_count:
            reasons.append(f'{report_count} open error report' + ('s' if report_count != 1 else ''))
        if status == 'draft':
            reasons.append('Needs a fact-check')
        if overdue:
            reasons.append('Full check is over six months old')
        reasons.extend(issues)
        rows.append({
            'slug': slug, 'title': page['title'], 'category': page.get('category', ''),
            'status': status, 'status_label': STATUSES.get(status, 'Status unavailable'),
            'checked': checked, 'checked_by': page.get('checked_by', '') if checked else '',
            'reviewed': parse_date(page.get('reviewed')) if status == 'human-reviewed' else None,
            'reviewed_by': page.get('reviewed_by', '') if status == 'human-reviewed' else '',
            'updated': parse_date(page.get('updated')), 'due': due, 'overdue': overdue,
            'reports': report_count, 'reports_url': reports_url(slug), 'reasons': reasons,
            'attention': bool(reasons),
            'priority': 0 if report_count else 1 if status == 'draft' or issues else 2 if overdue else 3,
        })
    return rows


@require_GET
def dashboard(request):
    if not (request.user.has_perm('submissions.view_submission') or
            request.user.has_perm('submissions.change_submission')):
        raise PermissionDenied
    today = timezone.localdate()
    context = {**admin.site.each_context(request), 'title': 'Article review', 'today': today,
               'reports_url': reports_url(), 'filters': FILTERS, 'sorts': SORTS}
    try:
        catalog = articles()
        if not isinstance(catalog, dict) or any(
            not isinstance(page, dict) or not isinstance(page.get('title'), str)
            for page in catalog.values()
        ):
            raise ValueError('Invalid article catalogue')
    except (OSError, ValueError):
        context['catalog_unavailable'] = True
        return TemplateResponse(request, 'admin/review_dashboard.html', context, status=503)

    # Duplicate reports point to their canonical report and should not inflate urgency.
    reports = dict(Submission.objects.filter(
        kind=Submission.Kind.CORRECTION,
        status__in=[Submission.Status.NEW, Submission.Status.REVIEWING],
        duplicate_of__isnull=True,
    ).values('article').annotate(total=Count('reference')).values_list('article', 'total'))
    rows = review_rows(catalog, reports, today)
    statuses = Counter(row['status'] for row in rows)
    counts = {'all': len(rows), 'attention': sum(row['attention'] for row in rows),
              'draft': statuses['draft'], 'overdue': sum(row['overdue'] for row in rows),
              'reports': sum(bool(row['reports']) for row in rows),
              'human': statuses['ai-fact-checked'], 'reviewed': statuses['human-reviewed']}
    selected = request.GET.get('filter', 'all')
    if selected not in FILTERS:
        selected = 'all'
    sort = request.GET.get('sort', 'priority')
    if sort not in SORTS:
        sort = 'priority'
    query = request.GET.get('q', '').strip()[:200]
    predicates = {
        'all': lambda row: True,
        'attention': lambda row: row['attention'],
        'draft': lambda row: row['status'] == 'draft',
        'overdue': lambda row: row['overdue'],
        'reports': lambda row: row['reports'],
        'human': lambda row: row['status'] == 'ai-fact-checked',
        'reviewed': lambda row: row['status'] == 'human-reviewed',
    }
    rows = [row for row in rows if predicates[selected](row) and
            query.casefold() in f"{row['title']} {row['slug']} {row['category']}".casefold()]
    order = {
        'priority': lambda row: (row['priority'], row['checked'] or date.min, row['title'].casefold()),
        'oldest': lambda row: (row['checked'] or date.min, row['title'].casefold()),
        'title': lambda row: (row['title'].casefold(), row['slug']),
    }
    rows.sort(key=order[sort])
    context.update(rows=rows, counts=counts, selected=selected, sort=sort, query=query,
                   open_reports=sum(reports.values()),
                   unmatched_reports=sum(count for slug, count in reports.items() if slug not in catalog))
    return TemplateResponse(request, 'admin/review_dashboard.html', context)
