"""Writer credits come from provider metadata, never from generated article text."""
import hashlib
import json


def writer_credit(request, response):
    model = response.get('model') or request.get('model') or 'Unknown'
    effort = request.get('output_config', {}).get('effort')
    # Credits are single-line front matter, not Markdown or provider output dumps.
    model = ' '.join(str(model).split())[:200]
    return f'{model} ({effort} effort)' if effort in ('low', 'medium', 'high', 'max') else model


def historical_writer_credit(events, body):
    request, credit = {}, 'Unknown'
    for event in events:
        if event.kind == 'writing_request':
            request = event.data
        elif event.kind == 'writing_response':
            text = ''.join(block.get('text', '') for block in event.data.get('content', []) if block.get('type') == 'text')
            try:
                draft = json.loads(text)
            except (ValueError, TypeError):
                continue
            if isinstance(draft, dict) and isinstance(draft.get('markdown'), str) and draft['markdown'].strip() == body.strip():
                credit = writer_credit(request, event.data)
        elif event.kind == 'placeholder_used' and 'is the subject of a reader request that Chainlore accepted as a cryptocurrency topic. This is a placeholder:' in body:
            credit = 'Chainlore template (no model)'
    return credit


def attribute_source(source, credit):
    """Add a missing credit without changing the article body or editorial status."""
    _, front, body = source.split('---\n', 2)
    if not any(line.startswith('written_by:') for line in front.splitlines()):
        front += f'written_by: {credit}\n'
    source = f'---\n{front}---\n{body}'
    return source, hashlib.sha256(source.encode()).hexdigest()
