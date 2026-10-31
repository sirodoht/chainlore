"""Recover existing credits from the actual writing calls, not today's settings."""
import hashlib
import json
from django.db import migrations


def backfill(apps, schema_editor):
    Article = apps.get_model('submissions', 'GeneratedArticle')
    Event = apps.get_model('submissions', 'AutomationEvent')
    Run = apps.get_model('submissions', 'AutomationRun')
    alias = schema_editor.connection.alias
    for article in Article.objects.using(alias).iterator():
        _, front, body = article.markdown.split('---\n', 2)
        if any(line.startswith('written_by:') for line in front.splitlines()):
            continue
        request, credit = {}, 'Unknown'
        for event in Event.objects.using(alias).filter(run_id=article.run_id).order_by('pk'):
            if event.kind == 'writing_request':
                request = event.data
            elif event.kind == 'writing_response':
                text = ''.join(block.get('text', '') for block in event.data.get('content', []) if block.get('type') == 'text')
                try:
                    draft = json.loads(text)
                except (ValueError, TypeError):
                    continue
                if not isinstance(draft, dict) or not isinstance(draft.get('markdown'), str) or draft['markdown'].strip() != body.strip():
                    continue
                model = event.data.get('model') or request.get('model') or 'Unknown'
                credit = ' '.join(str(model).split())[:200]
                effort = request.get('output_config', {}).get('effort')
                if effort in ('low', 'medium', 'high', 'max'):
                    credit += f' ({effort} effort)'
            elif event.kind == 'placeholder_used' and body.strip().startswith(
                f'{article.title} is the subject of a reader request that Chainlore accepted as a cryptocurrency topic. This is a placeholder:'
            ):
                credit = 'Chainlore template (no model)'
        article.markdown = f'---\n{front}written_by: {credit}\n---\n{body}'
        article.content_hash = hashlib.sha256(article.markdown.encode()).hexdigest()
        article.save(using=alias, update_fields=['markdown', 'content_hash'])
        # Preserve the credit if publication resumes from a prepared draft.
        run = Run.objects.using(alias).get(pk=article.run_id)
        if run.draft and run.draft.get('markdown', '').strip() == body.strip():
            run.draft['_written_by'] = credit
            run.save(using=alias, update_fields=['draft'])


class Migration(migrations.Migration):
    dependencies = [('submissions', '0005_automationrun_research_session_and_more')]
    operations = [migrations.RunPython(backfill, migrations.RunPython.noop)]
