"""Admit calls against estimates; settle completed calls against reported usage."""
import json
from django.conf import settings
from django.db import transaction
from django.db.models import Case, F, IntegerField, Sum, When
from django.utils import timezone
from .models import ProviderSpend


class BudgetExceeded(Exception):
    pass


def accounted_tokens():
    # Failed/interrupted calls retain their reservations: their cost is unknown.
    return Case(When(state='completed', then=F('input_tokens')+F('output_tokens')),
                default=F('reserved_tokens'), output_field=IntegerField())


def totals(queryset):
    return queryset.aggregate(accounted=Sum(accounted_tokens()), reserved=Sum('reserved_tokens'),
                              input=Sum('input_tokens'), output=Sum('output_tokens'))


def estimate(payload):
    amount = len(json.dumps(payload).encode()) + payload.get('max_tokens', 4000)
    amount += sum(t.get('max_uses', 0) * (t.get('max_content_tokens', 4000) + 2000) for t in payload.get('tools', []))
    # Server tools repeat model sampling over growing context. A tool allowance
    # alone missed that cost. This is headroom, not an upper bound or an invoice.
    return amount * (3 if payload.get('tools') else 1)


def reserve(run, provider, stage, payload):
    amount = estimate(payload)
    with transaction.atomic():
        today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        daily = totals(ProviderSpend.objects.filter(created_at__gte=today))['accounted'] or 0
        total = totals(ProviderSpend.objects.filter(run=run))['accounted'] or 0
        if total + amount > settings.EDITORIAL_RUN_TOKEN_LIMIT:
            raise BudgetExceeded('run_token_budget')
        if daily + amount > settings.EDITORIAL_DAILY_TOKEN_LIMIT:
            raise BudgetExceeded('daily_token_budget')
        return ProviderSpend.objects.create(run=run, provider=provider, stage=stage, reserved_tokens=amount)


def complete(reservation, result):
    usage = result.get('usage')
    if not isinstance(usage, dict):
        return
    values = [usage.get('input_tokens'), usage.get('output_tokens'),
              usage.get('cache_creation_input_tokens', 0), usage.get('cache_read_input_tokens', 0)]
    if any(type(value) is not int or value < 0 for value in values):
        return  # Missing/invalid accounting never releases the reservation.
    reservation.input_tokens = values[0] + values[2] + values[3]
    reservation.output_tokens = values[1]
    reservation.state = 'completed'
    reservation.save(update_fields=['input_tokens', 'output_tokens', 'state'])
