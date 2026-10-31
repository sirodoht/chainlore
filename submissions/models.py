import uuid
from django.core.exceptions import ValidationError
from django.db import models


class Submission(models.Model):
    class Kind(models.TextChoices):
        # Retained only for reviewing historical records; no public question form.
        QUESTION = 'question', 'Article question'
        REQUEST = 'request', 'Article request'
        CORRECTION = 'correction', 'Error report'

    class Status(models.TextChoices):
        NEW = 'new', 'New'
        REVIEWING = 'reviewing', 'Reviewing'
        RESOLVED = 'resolved', 'Resolved'
        DECLINED = 'declined', 'Declined'

    reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kind = models.CharField(max_length=12, choices=Kind.choices)
    article = models.SlugField(blank=True)
    section = models.CharField(max_length=200, blank=True)
    article_revision = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=200, blank=True)
    details = models.TextField(max_length=5000, blank=True)
    claim = models.TextField(max_length=3000, blank=True)
    correction = models.TextField(max_length=3000, blank=True)
    sources = models.TextField(max_length=10000, blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NEW, db_index=True)
    internal_notes = models.TextField(blank=True)
    resulting_url = models.URLField(blank=True, verbose_name='Resulting article or change URL')
    duplicate_of = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='duplicates')
    notified_status = models.CharField(max_length=12, choices=Status.choices, blank=True, verbose_name='Submitter emailed about')
    notified_at = models.DateTimeField(null=True, blank=True, verbose_name='Submitter emailed at')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{str(self.reference)[:8]} — {self.get_kind_display()}: {self.title or self.article}'

    def clean(self):
        if self.duplicate_of_id == self.reference:
            raise ValidationError({'duplicate_of': 'A submission cannot be a duplicate of itself.'})


class RateLimit(models.Model):
    key = models.CharField(max_length=64, primary_key=True)
    count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(db_index=True)


class AutomationRun(models.Model):
    class State(models.TextChoices):
        QUEUED = 'queued', 'Queued'
        RUNNING = 'running', 'Running'
        RETRY = 'retry', 'Retry scheduled'
        BLOCKED = 'blocked', 'Waiting for provider recovery'
        REVIEW = 'review', 'Needs review'
        DECLINED = 'declined', 'Declined'
        PUBLISHED = 'published', 'Published'
        DUPLICATE = 'duplicate', 'Already covered'
        FAILED = 'failed', 'Failed'

    submission = models.OneToOneField(Submission, on_delete=models.PROTECT, related_name='automation')
    state = models.CharField(max_length=16, choices=State.choices, default=State.QUEUED, db_index=True)
    inputs = models.JSONField(default=dict)
    triage = models.JSONField(default=dict)
    research = models.JSONField(default=dict)
    research_session = models.JSONField(default=dict)
    draft = models.JSONField(default=dict)
    output_review = models.JSONField(default=dict)
    attempts = models.PositiveIntegerField(default=0)
    next_attempt_at = models.DateTimeField(null=True, blank=True)
    last_error = models.CharField(max_length=200, blank=True)
    notification_attempts = models.PositiveIntegerField(default=0)
    notification_retry_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}: {self.submission.title} ({self.state})'


class AutomationEvent(models.Model):
    run = models.ForeignKey(AutomationRun, on_delete=models.PROTECT, related_name='events')
    kind = models.CharField(max_length=40)
    data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']


class GeneratedArticle(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    run = models.OneToOneField(AutomationRun, on_delete=models.PROTECT, related_name='generated_article')
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    content_hash = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class AutomationControl(models.Model):
    """Singleton circuit breaker, shared by every worker invocation."""
    id = models.PositiveSmallIntegerField(primary_key=True, default=1, editable=False)
    paused = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, blank=True)
    blocked_run = models.ForeignKey(AutomationRun, null=True, blank=True, on_delete=models.PROTECT)
    paused_at = models.DateTimeField(null=True, blank=True)
    alert_attempts = models.PositiveIntegerField(default=0)
    alert_retry_at = models.DateTimeField(null=True, blank=True)
    alert_sent_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Article request queue'
