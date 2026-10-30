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
    details = models.TextField(max_length=5000)
    claim = models.TextField(max_length=3000, blank=True)
    correction = models.TextField(max_length=3000, blank=True)
    sources = models.TextField(max_length=10000, blank=True)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NEW, db_index=True)
    internal_notes = models.TextField(blank=True)
    resulting_url = models.URLField(blank=True, verbose_name='Resulting article or change URL')
    duplicate_of = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='duplicates')
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
