from datetime import datetime, timezone
import ipaddress
from django.conf import settings
from django.db import transaction
from django.utils.crypto import salted_hmac
from django.utils.timezone import now
from .models import RateLimit


def client_network(value):
    """One bucket per IPv4 address or IPv6 /64, so rotating within a prefix gains nothing."""
    try:
        address = ipaddress.ip_address(value.strip())
    except ValueError:
        # Unparseable values share one bucket rather than each minting a fresh allowance.
        return 'unknown'
    if address.version == 6 and address.ipv4_mapped:
        address = address.ipv4_mapped
    if address.version == 6:
        return str(ipaddress.ip_network((address, 64), strict=False))
    return str(address)


def allow(request, scope, limit, seconds):
    # Caddy overwrites this header; the service only listens on loopback.
    address = client_network(request.META.get('HTTP_X_CHAINLORE_IP', '') if settings.PRODUCTION else request.META.get('REMOTE_ADDR', ''))
    current = now()
    bucket = int(current.timestamp()) // seconds
    key = salted_hmac('chainlore.rate-limit', f'{scope}:{address}:{bucket}', algorithm='sha256').hexdigest()
    expires = datetime.fromtimestamp((bucket + 1) * seconds, tz=timezone.utc)
    with transaction.atomic():
        RateLimit.objects.filter(expires_at__lte=current).delete()
        record, _ = RateLimit.objects.get_or_create(key=key, defaults={'expires_at': expires})
        if record.count >= limit:
            return False
        record.count += 1
        record.save(update_fields=['count'])
    return True
