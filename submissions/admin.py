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


# Audit records and source artifacts are visible only to authenticated staff.
# They are append-only in the application; no public endpoints expose them.
from .models import AutomationControl, AutomationEvent, AutomationRun, GeneratedArticle
from .automation_control import regenerate_placeholders, resume_queue, retry_runs


class AuditAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AutomationRun)
class AutomationRunAdmin(AuditAdmin):
    list_display = ['id', 'submission', 'state', 'attempts', 'last_error', 'created_at']
    list_filter = ['state', 'created_at']
    search_fields = ['submission__title', 'submission__reference']
    actions = ['retry_failed', 'restart_review', 'regenerate_placeholder']

    def has_operate_permission(self, request):
        return request.user.has_perm('submissions.change_automationrun')

    def recover(self, request, queryset, restart=False, operation=None):
        ids = list(queryset.values_list('pk', flat=True))
        try:
            count = operation(ids, request.user.pk) if operation else retry_runs(ids, request.user.pk, restart=restart)
        except BlockingIOError:
            self.message_user(request, 'The worker is busy. Try again after its current run finishes.', messages.WARNING)
        except ValueError as exc:
            self.message_user(request, str(exc), messages.WARNING)
        else:
            self.message_user(request, f'Queued {count} request(s). Previous decisions remain in the audit log.')

    @admin.action(description='Retry failed runs from their saved stage', permissions=['operate'])
    def retry_failed(self, request, queryset):
        self.recover(request, queryset)

    @admin.action(description='Restart screening and research for held review runs', permissions=['operate'])
    def restart_review(self, request, queryset):
        self.recover(request, queryset, restart=True)

    @admin.action(description='Regenerate placeholder pages with fresh research', permissions=['operate'])
    def regenerate_placeholder(self, request, queryset):
        self.recover(request, queryset, operation=regenerate_placeholders)


@admin.register(AutomationControl)
class AutomationControlAdmin(AuditAdmin):
    list_display = ['__str__', 'paused', 'reason', 'paused_at', 'alert_attempts', 'alert_sent_at']
    actions = ['resume']

    def has_operate_permission(self, request):
        return request.user.has_perm('submissions.change_automationcontrol')

    @admin.action(description='Resume queue after fixing provider settings', permissions=['operate'])
    def resume(self, request, queryset):
        if not queryset.filter(pk=1).exists():
            return
        try:
            count = resume_queue(request.user.pk)
        except BlockingIOError:
            self.message_user(request, 'The worker is busy. Try again after its current run finishes.', messages.WARNING)
        else:
            self.message_user(request, f'Queue resumed; {count} waiting request(s) requeued with their saved work.')


@admin.register(AutomationEvent)
class AutomationEventAdmin(AuditAdmin):
    list_display = ['id', 'run', 'kind', 'created_at']
    list_filter = ['kind', 'created_at']
    search_fields = ['run__submission__title', 'run__submission__reference']
    list_select_related = ['run__submission']


@admin.register(GeneratedArticle)
class GeneratedArticleAdmin(AuditAdmin):
    list_display = ['slug', 'title', 'run', 'published_at', 'content_hash']
    search_fields = ['slug', 'title']
