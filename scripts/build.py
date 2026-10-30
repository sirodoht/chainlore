#!/usr/bin/env python3
"""Build Chainlore from Markdown. No server or JavaScript framework required."""
import copy
import hashlib
import html
import json
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from string import Template
from urllib.parse import urlsplit, urlunsplit

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist'
ROUTES = {'INDEX.md': '/all-articles/', 'VISION.md': '/vision/',
          'INSPIRATION.md': '/inspiration/', 'ABOUT.md': '/about/', 'README.md': '/'}
TEMPLATE = Template((ROOT / 'site/template.html').read_text())


def serialize(node):
    return ET.tostring(node, encoding='unicode', method='html')


def plain(node):
    return ' '.join(''.join(node.itertext()).split())


def load(path):
    text = path.read_text()
    meta = {}
    if text.startswith('---\n'):
        _, front, text = text.split('---\n', 2)
        for line in front.strip().splitlines():
            key, value = line.split(':', 1)
            meta[key.strip()] = value.strip()
    return meta, text


def render(path):
    meta, text = load(path)
    md = markdown.Markdown(extensions=['tables', 'footnotes', 'toc', 'fenced_code'],
                           extension_configs={'toc': {'permalink': False}}, output_format='xhtml')
    tree = ET.fromstring('<div>' + md.convert(text) + '</div>')
    for link in tree.iter('a'):
        url = urlsplit(link.get('href', ''))
        if not url.scheme and not url.netloc and url.path.endswith('.md'):
            target = (path.parent / url.path).resolve()
            key = target.relative_to(ROOT).as_posix()
            if key not in ROUTES:
                raise ValueError(f'Unknown Markdown link in {path.name}: {key}')
            link.set('href', urlunsplit(('', '', ROUTES[key], url.query, url.fragment)))
    heading = tree.find('h1')
    title = meta.get('title', plain(heading) if heading is not None else path.stem)
    if heading is not None:
        tree.remove(heading)
    first_p = tree.find('p')
    lead = copy.deepcopy(first_p) if first_p is not None else ET.Element('p')
    # Excerpts link to the article's citation IDs, never nonexistent homepage anchors.
    for link in lead.iter('a'):
        if link.get('href', '').startswith('#'):
            link.set('href', ROUTES[path.relative_to(ROOT).as_posix()] + link.get('href'))
        link.attrib.pop('id', None)
    clean_lead = copy.deepcopy(lead)
    for parent in clean_lead.iter():
        for child in list(parent):
            if child.tag == 'sup':
                parent.remove(child)
    description = plain(clean_lead)
    toc_items = [(node.get('id'), plain(node)) for node in tree.findall('h2')]
    if meta:
        table = tree.find('table')
        if table is not None:
            tree.remove(table)
            box = ET.Element('aside', {'class': 'infobox', 'aria-label': f'{title} facts'})
            ET.SubElement(box, 'div', {'class': 'infobox-title'}).text = title
            box.append(table)
            tree.insert(1, box)
    for table in list(tree.findall('table')):
        index = list(tree).index(table)
        tree.remove(table)
        wrapper = ET.Element('div', {'class': 'table-scroll', 'tabindex': '0', 'role': 'region', 'aria-label': f'{title} table'})
        wrapper.append(table)
        tree.insert(index, wrapper)
    return {'meta': meta, 'title': title, 'tree': tree, 'toc': toc_items,
            'lead': serialize(lead), 'description': description, 'text': plain(tree), 'source': path}


def write_page(route, title, content, source='INDEX.md', description='', toc='', active='Article'):
    tabs = f'<a class="active" href="{route}" aria-current="page">{html.escape(active)}</a>'
    if route != '/all-articles/':
        tabs += '<a href="/all-articles/">All articles</a>'
    output = TEMPLATE.substitute(title=html.escape(title + ' — Chainlore') if route != '/' else 'Chainlore — The AI native crypto encyclopedia',
        description=html.escape(description[:300], quote=True), path=route, content=content,
        source='/sources/' + source, toc=toc, tabs=tabs,
        css_version=hashlib.sha256((ROOT / 'site/assets/site.css').read_bytes()).hexdigest()[:12])
    destination = OUT / route.strip('/') / 'index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output)


def article(page):
    meta = page['meta']
    route = ROUTES[page['source'].relative_to(ROOT).as_posix()]
    title = page['title']
    details = 'From Chainlore, the AI native crypto encyclopedia'
    if meta:
        updated = date.fromisoformat(meta['updated']).strftime('%-d %B %Y')
        status = 'AI fact-checked' if meta['status'] == 'ai-fact-checked' else meta['status'].capitalize()
        details = f'<span>{html.escape(meta["category"])} · {html.escape(meta["ticker"])}</span><span>Updated {updated}</span><span class="status">{html.escape(status)}</span>'
    content = f'<header class="article-header"><h1>{html.escape(title)}</h1><div class="article-meta">{details}</div></header>'
    if meta.get('status') == 'draft':
        content += '<p class="notice">This article is marked as a draft. Its source metadata does not yet record a completed fact-check.</p>'
    content += '<article class="article-body">' + ''.join(serialize(node) for node in page['tree']) + '</article>'
    toc = '<details class="contents" open><summary>Contents</summary><ul>' + ''.join(f'<li><a href="#{html.escape(anchor)}">{html.escape(label)}</a></li>' for anchor, label in page['toc']) + '</ul></details>' if page['toc'] else ''
    write_page(route, title, content, page['source'].relative_to(ROOT).as_posix(), page['description'], toc)


def homepage(pages):
    feature = pages['hyperliquid']
    summaries = {
        'bitcoin': 'A proof-of-work blockchain and peer-to-peer electronic cash system.',
        'ethereum': 'A programmable blockchain for smart contracts, secured by proof of stake.',
        'hyperliquid': 'A layer 1 blockchain with an onchain order book for perpetual futures and spot trading.',
        'arbitrum': 'Optimistic rollups that scale Ethereum, with governance through the Arbitrum DAO.',
    }
    rows = ''.join(f'<div class="article-row"><span class="article-number">{i:02}</span><div><h3><a href="/{slug}/">{p["title"]}</a><span>{p["meta"]["ticker"]} · {p["meta"]["category"]}</span></h3><p>{summaries.get(slug, html.escape(p["description"][:150]))}</p></div></div>' for i, (slug, p) in enumerate(pages.items(), 1))
    index = render(ROOT / 'INDEX.md')
    index_html = ''.join(serialize(node) for node in index['tree'] if node.tag != 'p')
    index_html = index_html.replace('<h2', '<h3').replace('</h2>', '</h3>')
    references = sum(len(re.findall(r'^\[\^[^\]]+\]:', p['source'].read_text(), re.M)) for p in pages.values())
    content = f'''<section class="welcome"><h1><span>Chainlore</span></h1><p>An AI native encyclopedia of crypto.</p><p class="subline"><a href="/all-articles/">{len(pages)} articles</a> · {references} references</p></section>
<div class="home-grid">
<section class="panel"><h2>Featured article</h2><div class="eyebrow">{feature['meta']['category']} blockchain</div><h3 class="feature-title"><a href="/hyperliquid/">Hyperliquid</a><small>HYPE</small></h3><div class="feature-lead">{feature['lead']}</div><div class="feature-bottom"><span>History · Technology · Governance</span><a href="/hyperliquid/">Full article →</a></div></section>
<section class="panel blue"><h2>Articles</h2>{rows}</section>
</div>
<div class="home-bottom"><section><h2>Subjects</h2>{index_html}<p><a href="/all-articles/">Article index →</a></p></section><section><h2>About Chainlore</h2><p>Articles cover the history, technology, supply, governance, and incidents of blockchains and protocols.</p><p>Encyclopedia articles were written and fact-checked by Opus 5.5 High. The current articles retain draft status in their source metadata.</p><p><a href="/about/">Authorship and review</a> · <a href="/vision/">Editorial scope</a> · <a href="/inspiration/">Reference sites</a></p></section></div>'''
    write_page('/', 'Chainlore', content, description='An AI native encyclopedia of crypto, with articles on Bitcoin, Ethereum, Hyperliquid, and Arbitrum.', active='Main page')


def main():
    sources = sorted((ROOT / 'pages').glob('*.md'))
    for path in sources:
        ROUTES[path.relative_to(ROOT).as_posix()] = f'/{path.stem}/'
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'site/assets', OUT / 'assets')
    pages = {}
    # Alphabetical browsing is stable as new articles are added.
    for path in sources:
        page = render(path)
        pages[path.stem] = page
        article(page)
    for name in ('INDEX.md', 'VISION.md', 'INSPIRATION.md', 'ABOUT.md'):
        article(render(ROOT / name))
    homepage(pages)
    write_page('/search/', 'Search', '<header class="article-header"><h1>Search Chainlore</h1></header><p id="search-status" role="status">Loading search…</p><noscript><p>Search requires JavaScript. You can browse every article in the index.</p></noscript><ul id="search-results" class="search-results"></ul><p><a href="/all-articles/">Browse all articles →</a></p>', description='Search the Chainlore encyclopedia.', active='Search')
    write_page('/404/', 'Page not found', '<h1>Page not found</h1><p>This page is not in the encyclopedia yet.</p><p><a href="/">Return to the main page</a> or <a href="/all-articles/">browse all articles</a>.</p>', active='Page not found')
    (OUT / 'search-index.json').write_text(json.dumps([{'title': p['title'], 'ticker': p['meta']['ticker'], 'url': f'/{slug}/', 'description': p['description'], 'text': p['text']} for slug, p in pages.items()], ensure_ascii=False))
    all_sources = sources + [ROOT / name for name in ('README.md', 'INDEX.md', 'VISION.md', 'INSPIRATION.md', 'ABOUT.md')]
    for path in all_sources:
        destination = OUT / 'sources' / path.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, destination)
    urls = ['/'] + sorted(route for key, route in ROUTES.items() if key != 'README.md')
    (OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>https://chainlore.xyz{route}</loc></url>' for route in urls) + '</urlset>\n')
    (OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://chainlore.xyz/sitemap.xml\n')
    print(f'Built {len(pages)} articles and 7 supporting pages in {OUT}')


if __name__ == '__main__':
    main()
