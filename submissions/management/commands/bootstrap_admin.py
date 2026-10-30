import os
import secrets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction


class Command(BaseCommand):
    help = 'Create the first admin and save credentials privately; never reset an existing account.'

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write('An administrator already exists; no account changes made.')
            return
        if User.objects.filter(username='admin').exists():
            raise CommandError('The admin username is already taken. Create a superuser manually.')
        credentials = settings.DATA_DIR / 'admin-initial-credentials.txt'
        password = secrets.token_urlsafe(24)
        with transaction.atomic():
            User.objects.create_superuser('admin', password=password)
            with open(credentials, 'x', opener=lambda path, flags: os.open(path, flags, 0o600)) as file:
                file.write(f'URL: https://chainlore.xyz/admin/\nUsername: admin\nPassword: {password}\n')
        self.stdout.write('Administrator created. Credentials saved in the private data directory.')
