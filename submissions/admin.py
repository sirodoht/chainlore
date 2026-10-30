import smtplib
from django.conf import settings
from django.contrib import admin, messages
from django.utils.html import format_html
from . import notify
from .models import Submission

admin.site.site_header = 'Chainlore submissions'
admin.site.site_title = 'Chainlore admin'
admin.site.index_title = 'Review queue'


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['reference_short', 'kind', 'subject', 'status', 'created_at', 'duplicate_of']
    list_filter = ['status', 'kind', 'article', 'created_at']
    search_fields = ['reference', 'title', 'article', 'details', 'claim', 'email']
    date_hierarchy = 'created_at'
    readonly_fields = ['notified_status', 'notified_at', 'reference', 'kind', 'article_link', 'article', 'section', 'article_revision', 'title', 'details', 'claim', 'correction', 'sources', 'email', 'created_at', 'updated_at']
    autocomplete_fields = ['duplicate_of']
    fieldsets = [
        ('Review', {'fields': ['status', 'internal_notes', 'duplicate_of', 'resulting_url', 'notified_status', 'notified_at']}),
        ('Submission', {'fields': ['reference', 'kind', 'article_link', 'article', 'section', 'article_revision', 'title', 'details', 'claim', 'correction', 'sources', 'email', 'created_at', 'updated_at']}),
    ]

    @admin.display(description='Reference')
    def reference_short(self, obj):
        return str(obj.reference)[:8]

    @admin.display(description='Subject')
    def subject(self, obj):
        return obj.title or obj.article

    @admin.display(description='Article page')
    def article_link(self, obj):
        if obj.article:
            return format_html('<a href="/p/{}/">View article</a>', obj.article)
        return '—'

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not notify.pending(obj):
            return
        if not settings.NOTIFICATIONS_ENABLED:
            messages.warning(request, 'Email is not configured, so the submitter was not told about this decision.')
            return
        try:
            notify.notify(obj)
        except (smtplib.SMTPException, OSError):
            messages.error(request, 'The submitter could not be emailed. Save again to retry.')
        else:
            messages.info(request, 'Emailed the submitter about this decision.')
