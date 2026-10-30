from django.core.management.base import BaseCommand
from submissions.automation import run_worker


class Command(BaseCommand):
    help = 'Process one queued article request and pending decision notifications.'

    def handle(self, *args, **options):
        self.stdout.write(f'Processed {run_worker()} request(s).')
