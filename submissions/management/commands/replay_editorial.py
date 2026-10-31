"""Run the real independent checker in an isolated, non-publishing environment."""
import json
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum
from submissions.models import AutomationRun, Submission, Verification
from submissions.verification import digest, step, inventory
from submissions.ai_providers import ProviderError
from submissions.article_validation import InvalidArticle
from submissions.budgets import BudgetExceeded


class Command(BaseCommand):
    help = 'Check a source file without publishing, in an isolated shadow database.'

    def add_arguments(self, parser):
        parser.add_argument('--source', required=True)
        parser.add_argument('--expect', choices=['passed', 'failed'])

    def handle(self, *args, **options):
        if settings.PRODUCTION or not settings.EDITORIAL_SHADOW or settings.AUTOMATION_ENABLED or settings.ARTICLE_GIT_REMOTE:
            raise CommandError('Replay requires non-production shadow mode, a disabled worker, and no publication remote.')
        # Never use the live database even if environment flags were changed.
        if settings.DATA_DIR.resolve() == Path('/var/www/chainlore/private'):
            raise CommandError('Use a separate DATA_DIR and migrate its database first.')
        source = Path(options['source']).read_text()
        if len(source.encode()) > 200000:
            raise CommandError('Replay source is too large.')
        submission = Submission.objects.create(kind='question', title='Private verification replay')
        run = AutomationRun.objects.create(submission=submission, state='checking', inputs={'replay': True})
        check = Verification.objects.create(run=run, source=source, source_hash=digest(source))
        try:
            for _ in range(3 + ((len(inventory(source)[0])+settings.VERIFICATION_BATCH_SIZE-1)//settings.VERIFICATION_BATCH_SIZE)*settings.VERIFICATION_REPORT_ATTEMPTS):
                check = step(check)
                if check.state != 'pending':
                    break
        except (ProviderError, InvalidArticle, BudgetExceeded) as exc:
            run.state = 'blocked'; run.last_error = str(exc); run.save()
            raise CommandError(str(exc)) from None
        run.state = 'blocked' if check.state == 'passed' else 'insufficient'
        run.last_error = 'shadow_verified_not_published' if check.state == 'passed' else ''
        run.save()
        usage = run.spend.aggregate(reserved=Sum('reserved_tokens'), input=Sum('input_tokens'), output=Sum('output_tokens'))
        self.stdout.write(json.dumps({'check_id': check.pk, 'state': check.state, 'checker': check.checker,
            'source_hash': check.source_hash, 'errors': check.report.get('errors', []),
            'opened_sources': len(check.evidence), 'published': False, 'tokens': usage}))
        if options['expect'] and check.state != options['expect']:
            raise CommandError('Checker outcome did not match the expected replay result.')
