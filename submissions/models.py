import uuid
from django.core.exceptions import ValidationError
from django.db import models, transaction


class Submission(models.Model):
    class Kind(models.TextChoices):
        # Retained only for reviewing historical records; no public question form.
        QUESTION = 'question', 'Article question'
        REQUEST = 'request', 'Article request'
        IMPROVEMENT = 'improvement', 'Article improvement'
        CORRECTION = 'correction', 'Error report'
        MAINTENANCE = 'maintenance', 'Scheduled maintenance'

    class Status(models.TextChoices):
        NEW = 'new', 'New'
        REVIEWING = 'reviewing', 'Reviewing'
        RESOLVED = 'resolved', 'Resolved'
        DECLINED = 'declined', 'Declined'
        INSUFFICIENT = 'insufficient', 'Insufficient evidence'

    maintenance_key = models.CharField(max_length=180, blank=True, null=True, unique=True)
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
    public_title = models.CharField(max_length=200, blank=True, help_text='Optional short title approved for public display. Never include contact details.')
    public_summary = models.TextField(max_length=2000, blank=True, help_text='Public progress note, explanation of changes, or reason for declining. Do not copy private submission text.')
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
        seen = {self.reference}
        target = self.duplicate_of
        while target:
            if target.pk in seen:
                raise ValidationError({'duplicate_of': 'Duplicate links cannot form a cycle.'})
            if self.kind != 'question' and target.kind == 'question':
                raise ValidationError({'duplicate_of': 'Choose an article request, error report, or improvement.'})
            seen.add(target.pk)
            target = target.duplicate_of

    def save(self, *args, **kwargs):
        with transaction.atomic():
            fields = ['status', 'duplicate_of_id', 'public_title', 'public_summary', 'resulting_url']
            previous = type(self).objects.filter(pk=self.pk).values(*fields).first()
            super().save(*args, **kwargs)
            current = type(self).objects.filter(pk=self.pk).values(*fields).get()
            if previous and previous != current:
                label = ('Marked as duplicate' if current['duplicate_of_id'] else
                         {'new': 'Queued', 'reviewing': 'Review started', 'resolved': 'Resolved',
                          'declined': 'Declined', 'insufficient': 'Insufficient evidence'}[current['status']])
                if previous['status'] == current['status'] and previous['duplicate_of_id'] == current['duplicate_of_id']:
                    label = 'Public update'
                SubmissionUpdate.objects.create(submission=self, label=label, note=current['public_summary'])


class SubmissionUpdate(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='public_updates')
    label = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at', 'pk']


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
        RESEARCHING = 'researching', 'Researching'
        CHECKING = 'checking', 'Checking'
        REVISING = 'revising', 'Revising'
        PUBLISHING = 'publishing', 'Publishing'
        INSUFFICIENT = 'insufficient', 'Insufficient evidence'

    submission = models.OneToOneField(Submission, on_delete=models.PROTECT, related_name='automation')
    state = models.CharField(max_length=16, choices=State.choices, default=State.QUEUED, db_index=True)
    editorial = models.JSONField(default=dict)
    recovery_attempts = models.PositiveIntegerField(default=0)
    reserved_tokens = models.PositiveIntegerField(default=0)
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
        return f'{self.pk}: {self.submission.title or self.submission.article} ({self.state})'


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
    base_content_hash = models.CharField(max_length=64, blank=True)
    git_revision = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class AutomationControl(models.Model):
    """Singleton circuit breaker, shared by every worker invocation."""
    id = models.PositiveSmallIntegerField(primary_key=True, default=1, editable=False)
    paused = models.BooleanField(default=False)
    auto_resume_at = models.DateTimeField(null=True, blank=True)
    probe_attempts = models.PositiveIntegerField(default=0)
    reason = models.CharField(max_length=200, blank=True)
    blocked_run = models.ForeignKey(AutomationRun, null=True, blank=True, on_delete=models.PROTECT)
    paused_at = models.DateTimeField(null=True, blank=True)
    alert_attempts = models.PositiveIntegerField(default=0)
    alert_retry_at = models.DateTimeField(null=True, blank=True)
    alert_sent_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Article request queue'


class ArticleRevision(models.Model):
    """An improvement checkpoint; published content remains authoritative in Git."""
    run = models.OneToOneField(AutomationRun, primary_key=True, on_delete=models.PROTECT, related_name='article_revision')
    slug = models.SlugField(max_length=100, db_index=True)
    title = models.CharField(max_length=200)
    original_markdown = models.TextField()
    base_content_hash = models.CharField(max_length=64)
    base_revision = models.CharField(max_length=40)
    markdown = models.TextField(blank=True)
    content_hash = models.CharField(max_length=64, blank=True)
    writer_credit = models.CharField(max_length=250, blank=True)
    git_revision = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Verification(models.Model):
    run = models.ForeignKey(AutomationRun, on_delete=models.PROTECT, related_name='verifications')
    source = models.TextField()
    source_hash = models.CharField(max_length=64, db_index=True)
    state = models.CharField(max_length=12, default='pending')
    checker = models.CharField(max_length=250, blank=True)
    session = models.JSONField(default=dict)
    report = models.JSONField(default=dict)
    evidence = models.JSONField(default=dict)
    approved_source = models.TextField(blank=True)
    approved_hash = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)


class ProviderSpend(models.Model):
    """Conservative token reservations survive crashes and bound API expenditure."""
    run = models.ForeignKey(AutomationRun, on_delete=models.PROTECT, related_name='spend')
    provider = models.CharField(max_length=20)
    stage = models.CharField(max_length=50)
    reserved_tokens = models.PositiveIntegerField()
    input_tokens = models.PositiveIntegerField(default=0)
    output_tokens = models.PositiveIntegerField(default=0)
    state = models.CharField(max_length=12, default='reserved')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
