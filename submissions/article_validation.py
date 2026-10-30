"""Accept only bounded, inert Markdown with source URLs present in research results."""
import hashlib
import ipaddress
import json
import re
import xml.etree.ElementTree as ET
from datetime import date
from urllib.parse import urlsplit
import markdown
from django.utils.text import slugify


class InvalidArticle(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise InvalidArticle(reason)


def public_url(value):
    try:
        url = urlsplit(value)
        host = url.hostname or ''
        if url.scheme != 'https' or url.username or url.password or url.port not in (None, 443):
            return False
        if '.' not in host or host.endswith(('.local', '.localhost', '.internal')) or host == 'localhost':
            return False
        try:
            return ipaddress.ip_address(host).is_global
        except ValueError:
            return bool(re.fullmatch(r'[a-zA-Z0-9.-]+', host))
    except ValueError:
        return False


def evidence_urls(response):
    urls = set()
    for block in response.get('content', []):
        if block.get('type') == 'web_fetch_tool_result' and isinstance(block.get('content'), dict):
            result = block['content']
            source = result.get('content', {}).get('source', {})
            if (result.get('type') == 'web_fetch_result' and public_url(result.get('url', ''))
                    and source.get('type') == 'text' and source.get('data', '').strip()):
                urls.add(result['url'])
    return urls


def extract_draft(response):
    require(response.get('stop_reason') == 'end_turn', 'writing_incomplete')
    text = ''.join(block['text'] for block in response.get('content', []) if block.get('type') == 'text')
    try:
        result = json.loads(text)
    except (ValueError, TypeError):
        raise InvalidArticle('writing_invalid_json') from None
    require(isinstance(result, dict), 'writing_invalid_object')
    return result


def validate_draft(draft, research):
    require(not draft.get('insufficient_evidence'), 'insufficient_evidence')
    for field in ('title', 'slug', 'ticker', 'category', 'markdown'):
        require(isinstance(draft.get(field), str), 'missing_' + field)
    title, slug, body = draft['title'], draft['slug'], draft['markdown']
    require(bool(re.fullmatch(r'[\w ()’\x27.,+-]{1,100}', title)), 'invalid_title')
    require(bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug)) and slug == slugify(title) and len(slug) <= 100, 'invalid_slug')
    require(bool(re.fullmatch(r'[A-Za-z0-9 .-]{1,30}', draft['ticker'])), 'invalid_ticker')
    require(draft['category'] in ('Layer 1', 'Layer 2', 'DeFi', 'Stablecoin', 'Exchange', 'Infrastructure', 'Other'), 'invalid_category')
    require(800 <= len(body) <= 45000, 'invalid_article_length')
    require(not any(c in body for c in ('<', '>', '\x00')) and '```' not in body and '![' not in body, 'unsafe_markdown')
    require(not re.search(r'^# |^---\s*$', body, re.M), 'unexpected_front_matter_or_h1')
    require(not re.search(r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}', body), 'contact_information')
    definitions = re.findall(r'^\[\^(\d+)\]:\s+\[([^\]\n]+)\]\((https://[^\s)]+)\)\s*$', body, re.M)
    markers = re.findall(r'\[\^(\d+)\](?!:)', body)
    ids = [item[0] for item in definitions]
    require(len(ids) >= 3 and len(ids) == len(set(ids)) and set(ids) == set(markers), 'invalid_footnotes')
    urls = {item[2] for item in definitions}
    require(len(urls) >= 3 and len({urlsplit(url).hostname for url in urls}) >= 2, 'insufficient_sources')
    require(urls <= evidence_urls(research), 'source_not_in_research')
    require('## References' in body, 'missing_references')
    # Paragraphs with prose must cite evidence; tables and headings are exempt.
    prose = body.split('## References')[0]
    for paragraph in re.split(r'\n\s*\n', prose):
        lines = paragraph.strip().splitlines()
        if lines and not lines[0].startswith(('#', '|')):
            require(bool(re.search(r'\[\^\d+\]', paragraph)), 'uncited_paragraph')
    rendered = markdown.markdown(body, extensions=['tables', 'footnotes', 'toc'])
    try:
        tree = ET.fromstring('<div>' + rendered + '</div>')
    except ET.ParseError:
        raise InvalidArticle('invalid_rendered_html') from None
    allowed = {'div', 'p', 'h2', 'h3', 'h4', 'ul', 'ol', 'li', 'strong', 'em', 'a', 'sup', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'hr', 'br'}
    for node in tree.iter():
        require(node.tag in allowed, 'unsafe_element')
        require(all(key in {'href', 'id', 'class', 'title', 'style'} for key in node.attrib), 'unsafe_attribute')
        if node.tag == 'a':
            href = node.get('href', '')
            require(href in urls or href.startswith(('#fn:', '#fnref:')), 'unapproved_link')
    front = '\n'.join(f'{key}: {draft[key]}' for key in ('title', 'ticker', 'category'))
    source = f'---\n{front}\nstatus: draft\nupdated: {date.today().isoformat()}\n---\n\n{body.strip()}\n'
    return source, hashlib.sha256(source.encode()).hexdigest()
