import hashlib
from django.conf import settings
from django.db import connection, transaction
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET, require_http_methods
from .catalog import articles, revision
from .forms import SubmissionForm
from .limits import allow
from .models import Submission
from .notify import notify_admin

TITLES = {'request': 'Request an article', 'correction': 'Report an error', 'improvement': 'Suggest an improvement'}


def context(**kwargs):
    css = settings.SITE_ROOT / 'assets/site.css'
    return {'css_version': hashlib.sha256(css.read_bytes()).hexdigest()[:12], **kwargs}


@require_GET
@never_cache
def index(request):
    return render(request, 'submissions/index.html', context(title='Article suggestions and corrections'))


@require_http_methods(['GET', 'POST'])
@never_cache
def submit(request, kind):
    if kind not in TITLES:
        raise Http404
    if request.method == 'POST' and not allow(request, 'submission', 10, 3600):
        response = render(request, 'submissions/limited.html', context(title='Submission limit reached'), status=429)
        response['Retry-After'] = '3600'
        return response
    initial = {}
    slug = request.GET.get('article', '')
    catalog = articles()
    if slug in catalog:
        initial['article'] = slug
        section = request.GET.get('section', '')
        initial['section'] = catalog[slug]['sections'].get(section, '')
    form = SubmissionForm(request.POST if request.method == 'POST' else None, kind=kind, initial=initial)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        reference = data.pop('form_token')
        honeypot = data.pop('website')
        if not honeypot:
            submission, created = Submission.objects.get_or_create(reference=reference, defaults={
                **data, 'kind': kind, 'article_revision': revision() if kind != 'request' else '',
            })
            if created:
                transaction.on_commit(lambda: notify_admin(submission))
        return redirect('submission-received', reference=reference)
    return render(request, 'submissions/form.html', context(title=TITLES[kind], form=form, kind=kind))


@require_GET
@never_cache
def received(request, reference):
    # Receipts never disclose submission text, email, or moderation status.
    return render(request, 'submissions/received.html', context(title='Submission received', reference=reference))


@require_GET
def health(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
        cursor.fetchone()
    return HttpResponse('ok', content_type='text/plain')


def development_site(request, path):
    from django.views.static import serve
    if not path or path.endswith('/'):
        path += 'index.html'
    return serve(request, path, document_root=settings.SITE_ROOT)
