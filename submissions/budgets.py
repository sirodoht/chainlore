"""Reserve a conservative upper bound before each paid call, including failed calls."""
import json
from django.conf import settings
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone
from .models import ProviderSpend


class BudgetExceeded(Exception):
    pass


def reserve(run, provider, stage, payload):
    # UTF-8 bytes overestimate ordinary input tokens. Tool content is capped separately.
    amount = len(json.dumps(payload).encode()) + payload.get('max_tokens', 4000)
    amount += sum(t.get('max_uses', 0) * (t.get('max_content_tokens', 4000) + 2000) for t in payload.get('tools', []))
    with transaction.atomic():
        today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        daily = ProviderSpend.objects.filter(created_at__gte=today).aggregate(n=Sum('reserved_tokens'))['n'] or 0
        total = ProviderSpend.objects.filter(run=run).aggregate(n=Sum('reserved_tokens'))['n'] or 0
        if daily + amount > settings.EDITORIAL_DAILY_TOKEN_LIMIT:
            raise BudgetExceeded('daily_token_budget')
        if total + amount > settings.EDITORIAL_RUN_TOKEN_LIMIT:
            raise BudgetExceeded('run_token_budget')
        return ProviderSpend.objects.create(run=run, provider=provider, stage=stage, reserved_tokens=amount)


def complete(reservation, result):
    usage = result.get('usage', {})
    reservation.input_tokens = max(0, int(usage.get('input_tokens', 0)))
    reservation.output_tokens = max(0, int(usage.get('output_tokens', 0)))
    reservation.state = 'completed'
    reservation.save(update_fields=['input_tokens', 'output_tokens', 'state'])
