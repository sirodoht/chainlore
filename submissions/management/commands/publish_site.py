from django.core.management.base import BaseCommand
from submissions.publication import publication_lock, publish_site


class Command(BaseCommand):
    help = 'Commit verified candidates and atomically publish the repository articles.'

    def add_arguments(self, parser):
        parser.add_argument('--base-release')
        parser.add_argument('--import-legacy', action='store_true',
                            help='One-time import of published database articles missing from Git.')

    def handle(self, *args, **options):
        with publication_lock():
            self.stdout.write(publish_site(options['base_release'], import_legacy=options['import_legacy']))
