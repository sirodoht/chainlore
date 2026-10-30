from django.core.management.base import BaseCommand
from submissions.publication import publication_lock, publish_site


class Command(BaseCommand):
    help = 'Build Git sources plus database articles and atomically publish them.'

    def add_arguments(self, parser):
        parser.add_argument('--base-release')

    def handle(self, *args, **options):
        with publication_lock():
            self.stdout.write(publish_site(options['base_release']))
