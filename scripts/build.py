#!/usr/bin/env python3
"""Build Chainlore from Markdown. No server or JavaScript framework required."""
import copy
import hashlib
import html
import json
import os
import random
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from string import Template
from urllib.parse import urlencode, urlsplit, urlunsplit

import markdown

ROOT = Path(os.environ.get('CHAINLORE_BUILD_ROOT', Path(__file__).resolve().parent.parent)).resolve()
OUT = ROOT / 'dist'
SUPPORTING = ('INDEX.md', 'VISION.md', 'ABOUT.md', 'POLICY.md')
ROUTES = {'INDEX.md': '/all-articles/', 'VISION.md': '/vision/',
          'ABOUT.md': '/about/', 'POLICY.md': '/policy/', 'README.md': '/'}
# Status values, display labels, and the POLICY.md section that defines each.
STATUSES = {'draft': ('Draft', 'statuses'),
            'ai-fact-checked': ('AI fact-checked', 'ai-fact-checked'),
            'human-reviewed': ('Human reviewed', 'human-reviewed')}
ARTICLE_FIELDS = ('title', 'ticker', 'category', 'status', 'updated', 'written_by')
STATUS_FIELDS = {'ai-fact-checked': ('checked', 'checked_by'),
                 'human-reviewed': ('checked', 'checked_by', 'reviewed', 'reviewed_by')}
TEMPLATE = Template((ROOT / 'site/template.html').read_text())
# Timeline rows state a date only as precisely as it is known: 2018, 2018-09,
# 2018-09-26, or a range within one month, 2023-03-10–13.
TIMELINE_DATE = re.compile(r'(\d{4})(?:-(\d{2})(?:-(\d{2})(?:–(\d{2}))?)?)?')
# Rows match a view by their text. Rules favour precision: a missed row stays in the full timeline.
TIMELINE_VIEWS = {
    'hacks': {'label': 'Hacks', 'title': 'Timeline of crypto hacks', 'summary': 'Exploits, thefts, and their aftermath.',
              'pattern': re.compile(r'\b(?:hack(?:s|ed)?|exploit\w*|theft|stolen|drain|hijacked|attackers?)\b', re.I)},
    'laws': {'label': 'Laws', 'title': 'Timeline of crypto law', 'summary': 'Legislation, rules, and regulatory decisions.',
             'pattern': re.compile(r'\bAct\b|\bBill\b|Ordinance|Royal Assent|legal tender|acceptance voluntary|executive order|mining crackdown|final rule|\bMiCA\b|stablecoin guidance|FSB final|finalises its framework|digital commodity|staff statement|approves spot')},
    'collapses': {'label': 'Collapses', 'title': 'Timeline of crypto collapses', 'summary': 'Failures, bankruptcies, market crashes, and depegs.',
                  'pattern': re.compile(r'collaps|chapter 11|bankrupt|insolven|depeg|civil rehabilitation|website closed|black thursday|\brun on\b|\bfinance run\b|loses peg|\bfell to\b|\bfalls to\b|chain halted|\bfail\b|shuts down|shutdown|crises|market crash|liquidation cascade|UST withdrawals|Alameda balance sheet|sale of its FTT|non-binding letter|Binance withdraws', re.I)},
}
# Regulation articles also record how companies responded to a law, which is not itself law.
TIMELINE_MARKET = re.compile(r'\b(?:announces?|delists|(?:JPYC|SBI) launches|begins (?:phased )?roll\w+)\b')
TIMELINE_STOPWORDS = {'a', 'an', 'and', 'at', 'for', 'in', 'into', 'its', 'of', 'on', 'the', 'to', 'with'}


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


def validate(meta, path):
    """Return the problems with an article's front matter, per POLICY.md."""
    errors = [f'{path.name}: missing {field}' for field in ARTICLE_FIELDS if not meta.get(field)]
    status = meta.get('status')
    if status and status not in STATUSES:
        errors.append(f'{path.name}: unknown status {status!r}, expected one of {", ".join(STATUSES)}')
    errors += [f'{path.name}: status {status} requires {field}' for field in STATUS_FIELDS.get(status, ()) if not meta.get(field)]
    for field in ('updated', 'checked', 'reviewed'):
        try:
            if meta.get(field):
                date.fromisoformat(meta[field])
        except ValueError:
            errors.append(f'{path.name}: {field} is not a YYYY-MM-DD date: {meta[field]}')
    return errors


def long_date(value):
    return date.fromisoformat(value).strftime('%-d %B %Y')


def citation_letter(index):
    """Label repeat citations a, b, ... z, aa, ab, as Wikipedia does."""
    label = ''
    index += 1
    while index:
        index, remainder = divmod(index - 1, 26)
        label = chr(97 + remainder) + label
    return label


def wikipedia_backlinks(tree):
    """Lead each reference with ^ for one citation, or ^ a b c linking to each of several."""
    for paragraph in tree.iterfind('.//li/p'):
        links = [link for link in paragraph if link.get('class') == 'footnote-backref']
        if not links:
            continue
        for link in links:
            paragraph.remove(link)
        backlinks = ET.Element('span', {'class': 'backlinks'})
        if len(links) == 1:
            links[0].text = '^'
            links[0].tail = None
            backlinks.append(links[0])
        else:
            backlinks.text = '^ '
            for index, link in enumerate(links):
                link.text = None
                link.tail = ' '
                ET.SubElement(link, 'sup').text = citation_letter(index)
                backlinks.append(link)
        backlinks.tail = ' ' + (paragraph.text or '')
        paragraph.text = None
        paragraph.insert(0, backlinks)


def render(path):
    meta, text = load(path)
    md = markdown.Markdown(extensions=['tables', 'footnotes', 'toc', 'fenced_code'],
                           extension_configs={'toc': {'permalink': False}}, output_format='xhtml')
    tree = ET.fromstring('<div>' + md.convert(text) + '</div>')
    wikipedia_backlinks(tree)
    for link in tree.iter('a'):
        url = urlsplit(link.get('href', ''))
        if url.netloc and url.scheme in ('', 'http', 'https') and url.hostname != 'chainlore.xyz':
            link.set('rel', ' '.join(dict.fromkeys([*link.get('rel', '').split(), 'external'])))
            link.set('aria-label', f'{plain(link)} (external link)')
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
            tree.insert(0, box)
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
    report_error_link = ''
    improvement_link = ''
    if source.startswith('pages/'):
        report_error_link = '<a href="/submit/correction/?' + urlencode({'article': Path(source).stem}) + '">Report an error</a>'
        improvement_link = '<a href="/submit/improvement/?' + urlencode({'article': Path(source).stem}) + '">Suggest an improvement</a>'
    source_url = '/p/' + Path(source).name if source.startswith('pages/') else '/sources/' + source
    source_link = f'<a href="{html.escape(source_url, quote=True)}">View Markdown source</a>' if route != '/' and source else ''
    output = TEMPLATE.substitute(title=html.escape(title + ' - Chainlore') if route != '/' else 'Chainlore - The AI native crypto encyclopedia',
        description=html.escape(description[:300], quote=True), path=route, content=content,
        source_link=source_link,
        toc=toc, tabs=tabs, report_error_link=report_error_link, improvement_link=improvement_link,
        sidebar_class='sidebar sidebar-home' if route == '/' else 'sidebar',
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
        errors = validate(meta, page['source'])
        if errors:
            raise ValueError('\n'.join(errors))
        details = f'<span>Updated {long_date(meta["updated"])}</span>'
        details += f'<span>Written by {html.escape(meta["written_by"])}</span>'
        label, anchor = STATUSES[meta['status']]
        details += f'<span><a href="/policy/#{anchor}">{label}</a></span>'
        if meta['status'] in ('ai-fact-checked', 'human-reviewed'):
            details += f'<span>Fact-checked by {html.escape(meta["checked_by"])} on {long_date(meta["checked"])}</span>'
        if meta['status'] == 'human-reviewed':
            details += f'<span>Reviewed by {html.escape(meta["reviewed_by"])} on {long_date(meta["reviewed"])}</span>'
    content = f'<header class="article-header"><h1>{html.escape(title)}</h1><div class="article-meta">{details}</div></header>'
    if meta.get('status') == 'draft':
        content += '<p class="notice">This article is a draft. It has not yet passed a fact-check under the <a href="/policy/">editorial policy</a> and may contain errors.</p>'
    if meta:
        slug = page['source'].stem
        for heading in page['tree'].findall('h2'):
            heading_title = plain(heading)
            for kind, label in (('correction', 'Report an error'), ('improvement', 'Suggest an improvement')):
                link = ET.SubElement(heading, 'a', {
                    'class': 'section-report',
                    'href': '/submit/' + kind + '/?' + urlencode({'article': slug, 'section': heading.get('id', '')}),
                    'aria-label': f'{label}: {heading_title}',
                })
                link.text = label
    content += '<article class="article-body">' + ''.join(serialize(node) for node in page['tree']) + '</article>'
    if meta:
        content += f'<nav class="article-actions" aria-label="Article suggestions and corrections"><a href="/submit/correction/?article={slug}">Report an error</a><a href="/submit/improvement/?article={slug}">Suggest an improvement</a><a href="/submit/request/">Request an article</a></nav>'
    elif route == '/all-articles/':
        content += '<p><a href="/submit/request/">Request an article</a></p>'
    toc = '<nav class="contents" aria-label="Contents"><div class="contents-heading">Contents</div><ul>' + ''.join(f'<li><a href="#{html.escape(anchor)}">{html.escape(label)}</a></li>' for anchor, label in page['toc']) + '</ul></nav>' if page['toc'] else ''
    write_page(route, title, content, page['source'].relative_to(ROOT).as_posix(), page['description'], toc)


def timeline_date(value):
    """Parse a table date, or return None so one odd row cannot fail a publication."""
    match = TIMELINE_DATE.fullmatch(value)
    if not match:
        return None
    year, month, day, end = (int(part) if part else None for part in match.groups())
    try:
        start = date(year, month or 1, day or 1)
        last = date(year, month, end) if end else start
    except ValueError:
        return None
    if last < start:
        return None
    if end:
        label = f'{day}–{last.strftime("%-d %B %Y")}'
    else:
        label = start.strftime('%-d %B %Y' if day else '%B %Y' if month else '%Y')
    days = [start.replace(day=number) for number in range(day, last.day + 1)] if day else []
    return {'value': value, 'start': start, 'order': (year, month or 0, day or 0), 'label': label, 'days': days}


def inline_html(cell, route):
    """Return a table cell's contents without its citations, keeping the text around them."""
    cell = copy.deepcopy(cell)
    for parent in cell.iter():
        for index, child in reversed(list(enumerate(parent))):
            if child.tag == 'sup':
                if index:
                    parent[index - 1].tail = (parent[index - 1].tail or '') + (child.tail or '')
                else:
                    parent.text = (parent.text or '') + (child.tail or '')
                parent.remove(child)
    for link in cell.iter('a'):
        if link.get('href', '').startswith('#'):
            link.set('href', route + link.get('href'))
    return html.escape(cell.text or '', quote=False) + ''.join(serialize(node) for node in cell)


def event_views(words, category):
    views = {key for key, view in TIMELINE_VIEWS.items() if view['pattern'].search(words)}
    if category == 'Regulation' and 'hacks' not in views and not TIMELINE_MARKET.search(words):
        views.add('laws')
    return views


def article_events(slug, page):
    """Yield an event for each row of tables headed Date, or None for a row with an unusable date."""
    route = f'/p/{slug}/'
    section = ''
    for number, node in enumerate(page['tree']):
        if node.tag in ('h2', 'h3'):
            section = node.get('id', '')
        for table in node.iter('table'):
            if [plain(cell).lower() for cell in table.iterfind('thead/tr/th')][:1] != ['date']:
                continue
            for row in table.iterfind('tbody/tr'):
                cells = row.findall('td')
                when = timeline_date(plain(cells[0]))
                text = ': '.join(filter(None, (inline_html(cell, route).strip() for cell in cells[1:])))
                if not when or not text:
                    yield None
                    continue
                words = ' '.join(re.sub(r'<[^>]+>', '', text).split())
                yield {'date': when, 'html': text, 'words': words, 'table': number,
                       'views': event_views(words, page['meta'].get('category')),
                       'sources': {slug: (page['title'], f'{route}#{section}' if section else route, page['meta'].get('status') == 'draft')}}


def word_overlap(first, second):
    first, second = (set(re.sub(r'(?:es|ed|e|s)$', '', word) for word in re.findall(r'[a-z0-9$]+', text.lower())) - TIMELINE_STOPWORDS - {''} for text in (first, second))
    return len(first & second) / (min(len(first), len(second)) or 1)


def same_event(first, second):
    """Articles word one event differently: compare the date, then the shared words."""
    if first['date']['value'] != second['date']['value']:
        return False
    # A row often omits its article's own subject, so titles count, at a lower bar.
    titled = [' '.join([event['words'], *(source[0] for source in event['sources'].values())]) for event in (first, second)]
    similar = word_overlap(first['words'], second['words']) >= 0.7 or word_overlap(*titled) >= 0.6
    if first['sources'].keys() & second['sources'].keys():
        # Rows of one table are distinct. Across tables, one exact day is one event.
        return first['table'] != second['table'] and (similar or bool(first['date']['days']))
    return similar


def merge_events(events):
    merged = []
    for event in events:
        for existing in merged:
            if same_event(existing, event):
                # Keep the fullest wording, preferring text outside draft articles.
                keep = min(existing, event, key=lambda item: (all(source[2] for source in item['sources'].values()), -len(item['words'])))
                existing.update(html=keep['html'], words=keep['words'], table=keep['table'],
                                sources=existing['sources'] | event['sources'], views=existing['views'] | event['views'])
                break
        else:
            merged.append(event)
    return sorted(merged, key=lambda event: event['date']['order'])


def timeline_item(event):
    sources = event['sources'].values()
    subjects = ' · '.join(f'<a href="{html.escape(url, quote=True)}">{html.escape(title)}</a>' for title, url, _ in sources)
    draft = ' <a class="timeline-draft" href="/policy/#statuses">Draft</a>' if all(source[2] for source in sources) else ''
    when = event['date']
    return f'<li><time datetime="{when["value"].split("–")[0]}">{when["label"]}</time><span class="timeline-subject">{subjects}</span><span class="timeline-event">{event["html"]}{draft}</span></li>'


def timeline_nav(current):
    links = [('/timeline/', 'All events')] + [(f'/timeline/{key}/', view['label']) for key, view in TIMELINE_VIEWS.items()] + [('/on-this-day/', 'On this day')]
    return '<nav class="timeline-views" aria-label="Timeline views">' + ''.join(
        f'<a href="{route}"{" aria-current=page" if route == current else ""}>{label}</a>' for route, label in links) + '</nav>'


def timeline_page(route, title, summary, events, today):
    """Write one chronological view, ending with scheduled events."""
    past = [event for event in events if event['date']['start'] <= today]
    groups = {}
    for event in past:
        groups.setdefault(str(event['date']['start'].year), []).append(event)
    sections = [(f'y{year}', year, rows) for year, rows in groups.items()]
    if len(past) < len(events):
        sections.append(('scheduled', f'Scheduled as of {today.strftime("%-d %B %Y")}', events[len(past):]))
    articles = len({slug for event in events for slug in event['sources']})
    content = f'<header class="article-header"><h1>{html.escape(title)}</h1></header><p>{summary} {len(events)} dated events from {articles} articles. Each links to the article that records it, where the sources are. Dates are as precise as those articles state them, and events from draft articles are marked.</p>'
    content += timeline_nav(route)
    content += '<form class="timeline-filter" role="search" hidden><label for="timeline-filter">Filter events</label><input id="timeline-filter" type="search" placeholder="Name, project, or year" autocomplete="off"><span id="timeline-count" role="status"></span></form>'
    content += '<nav class="timeline-years" aria-label="Years">' + ''.join(f'<a href="#{anchor}">{label}</a>' for anchor, label, _ in sections if anchor != 'scheduled') + '</nav>'
    for anchor, label, rows in sections:
        content += f'<section class="timeline-section"><h2 id="{anchor}">{label}</h2><ol class="timeline">' + ''.join(timeline_item(event) for event in rows) + '</ol></section>'
    toc = '<nav class="contents" aria-label="Contents"><div class="contents-heading">Years</div><ul>' + ''.join(f'<li><a href="#{anchor}">{"Scheduled" if anchor == "scheduled" else label}</a></li>' for anchor, label, _ in sections) + '</ul></nav>'
    write_page(route, title, content, source='', description=f'{summary} {len(events)} dated events from the Chainlore crypto encyclopedia.', toc=toc, active='Timeline')


def day_route(day):
    return f'/on-this-day/{day.strftime("%B-%-d").lower()}/'


def on_this_day(events, today):
    """Write a page per calendar day. Only exact dates qualify, and scheduled events have not happened."""
    days = {}
    for event in events:
        if event['date']['start'] <= today:
            for day in event['date']['days']:
                days.setdefault(day.strftime('%m-%d'), []).append(event)
    # 2024 was a leap year, so these are all 366 possible days.
    calendar = [date(2024, 1, 1) + timedelta(days=offset) for offset in range(366)]
    recorded = [day for day in calendar if day.strftime('%m-%d') in days]
    for index, day in enumerate(recorded):
        label = day.strftime('%-d %B')
        rows = days[day.strftime('%m-%d')]
        pager = ''.join(f'<a href="{day_route(other)}">{text}</a>' for other, text in (
            (recorded[index - 1], '← ' + recorded[index - 1].strftime('%-d %B')),
            (recorded[(index + 1) % len(recorded)], recorded[(index + 1) % len(recorded)].strftime('%-d %B') + ' →')))
        content = f'<header class="article-header"><h1>On this day: {label}</h1></header>{timeline_nav("")}<ol class="timeline">{"".join(timeline_item(event) for event in rows)}</ol><nav class="timeline-pager" aria-label="Other days">{pager}</nav>'
        summary = '; '.join(f'{event["date"]["start"].year}: {event["words"]}' for event in rows)
        write_page(day_route(day), f'On this day: {label}', content, source='', description=f'{label} in crypto history. {summary}', active='On this day')
    months = {}
    for day in calendar:
        cell = f'<a href="{day_route(day)}" data-day="{day.month}-{day.day}">{day.day}</a>' if day in recorded else str(day.day)
        months.setdefault(day.strftime('%B'), []).append(f'<li>{cell}</li>')
    content = f'<header class="article-header"><h1>On this day</h1></header><p>What happened in crypto on each day of the year, from {sum(map(len, days.values()))} entries with an exact date. Events known only to the month or year are in the <a href="/timeline/">full timeline</a>.</p>{timeline_nav("/on-this-day/")}'
    content += '<section id="on-this-day-today" hidden><h2 id="today"></h2></section><section class="timeline-section"><h2 id="browse">Browse by date</h2><div class="calendar">'
    content += ''.join(f'<div><h3>{month}</h3><ol>{"".join(cells)}</ol></div>' for month, cells in months.items()) + '</div></section>'
    write_page('/on-this-day/', 'On this day', content, source='', description='What happened in crypto on each day of the year.', active='On this day')
    return ['/on-this-day/'] + [day_route(day) for day in recorded]


def timeline(pages):
    """Merge every article's dated rows, write the timeline pages, and return (routes, events, skipped rows)."""
    rows = [row for slug, page in pages.items() for row in article_events(slug, page)]
    events = merge_events(row for row in rows if row)
    today = date.today()
    timeline_page('/timeline/', 'Timeline of crypto', 'One history of crypto, merged from every article.', events, today)
    routes = ['/timeline/']
    for key, view in TIMELINE_VIEWS.items():
        routes.append(f'/timeline/{key}/')
        timeline_page(routes[-1], view['title'], view['summary'], [event for event in events if key in event['views']], today)
    return routes + on_this_day(events, today), events, sum(row is None for row in rows)


def homepage(pages, event_count):
    feature = pages['hyperliquid']
    # INDEX.md is the single source of article summaries and subject groups.
    index = render(ROOT / 'INDEX.md')
    summaries, index_html = {}, ''
    for node in index['tree']:
        if node.tag == 'h2':
            index_html += f'<h3>{html.escape(plain(node))}</h3>'
        elif node.tag == 'ul':
            links = [item.find('a') for item in node.findall('li')]
            for link in links:
                summary = ' '.join((link.tail or '').split()).lstrip(': ')
                summaries[link.get('href').strip('/').split('/')[-1]] = summary[:1].upper() + summary[1:]
            index_html += '<p>' + ' · '.join(f'<a href="{html.escape(link.get("href"))}">{html.escape(plain(link))}</a>' for link in links) + '</p>'
    # A fresh random pick of other articles on each build.
    picks = random.sample([slug for slug in pages if slug != 'hyperliquid'], 5)
    rows = ''.join(f'<div class="article-row"><h3><a href="/p/{slug}/">{pages[slug]["title"]}</a></h3><p>{html.escape(summaries.get(slug) or pages[slug]["description"][:150])}</p></div>' for slug in picks)
    counts = Counter(p['meta']['status'] for p in pages.values())
    statuses = ', '.join(f'{label} ({counts[key]})' for key, (label, _) in STATUSES.items() if counts[key])
    references = sum(len(re.findall(r'^\[\^[^\]]+\]:', p['source'].read_text(), re.M)) for p in pages.values())
    content = f'''<section class="welcome"><h1><span>Chainlore</span></h1><p>An AI native encyclopedia of crypto.</p><p class="subline"><a href="/all-articles/">{len(pages)} articles</a> · {references} references · <a href="/timeline/">{event_count} timeline events</a></p></section>
<div class="home-grid">
<section class="panel"><h2>Featured article</h2><h3 class="feature-title"><a href="/p/hyperliquid/">Hyperliquid</a></h3><div class="feature-lead">{feature['lead']}</div><div class="feature-bottom"><span>History · Technology · Governance</span><a href="/p/hyperliquid/">Full article →</a></div></section>
<section class="panel blue"><h2>More articles</h2>{rows}<p class="more-link"><a href="/all-articles/">All {len(pages)} articles →</a></p></section>
</div>
<div class="home-bottom"><section><h2>Subjects</h2>{index_html}<p><a href="/all-articles/">Article index →</a></p></section><section><h2>About Chainlore</h2><p>Articles cover the history, technology, supply, governance, and incidents of blockchains and protocols.</p><p>Fact-check credits appear on each article. Article statuses: {statuses}.</p><p><a href="/about/">Authorship and review</a> · <a href="/policy/">Editorial policy</a> · <a href="/vision/">Editorial scope</a> · <a href="https://github.com/sirodoht/chainlore" rel="external" aria-label="Source code (external link)">Source code</a></p></section></div>'''
    write_page('/', 'Chainlore', content, description='An AI native encyclopedia of crypto, with articles on blockchains, stablecoins, protocols, and incidents.', active='Main page')


def main():
    sources = sorted((ROOT / 'pages').glob('*.md'))
    for path in sources:
        ROUTES[path.relative_to(ROOT).as_posix()] = f'/p/{path.stem}/'
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'site/assets', OUT / 'assets')
    # Alphabetical browsing is stable as new articles are added.
    pages = {path.stem: render(path) for path in sources}
    for page in pages.values():
        article(page)
    for name in SUPPORTING:
        article(render(ROOT / name))
    timeline_routes, events, skipped = timeline(pages)
    homepage(pages, len(events))
    (OUT / 'article-catalog.json').write_text(json.dumps({slug: {'title': p['title'], 'sections': dict(p['toc'])} for slug, p in pages.items()}, ensure_ascii=False))
    write_page('/search/', 'Search', '<header class="article-header"><h1>Search Chainlore</h1></header><p id="search-status" role="status">Loading search…</p><noscript><p>Search requires JavaScript. You can browse every article in the index.</p></noscript><ul id="search-results" class="search-results"></ul><p><a href="/all-articles/">Browse all articles →</a></p>', description='Search the Chainlore encyclopedia.', active='Search')
    write_page('/404/', 'Page not found', '<h1>Page not found</h1><p>This page is not in the encyclopedia yet.</p><p><a href="/">Return to the main page</a> or <a href="/all-articles/">browse all articles</a>.</p>', active='Page not found')
    (OUT / 'search-index.json').write_text(json.dumps([{'title': p['title'], 'ticker': p['meta']['ticker'], 'url': f'/p/{slug}/', 'description': p['description'], 'text': p['text']} for slug, p in pages.items()], ensure_ascii=False))
    all_sources = sources + [ROOT / name for name in ('README.md',) + SUPPORTING]
    for path in all_sources:
        destination = OUT / 'p' / path.name if path.parent == ROOT / 'pages' else OUT / 'sources' / path.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, destination)
    urls = ['/'] + sorted(route for key, route in ROUTES.items() if key != 'README.md') + timeline_routes
    (OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>https://chainlore.xyz{route}</loc></url>' for route in urls) + '</urlset>\n')
    (OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://chainlore.xyz/sitemap.xml\n')
    print(f'Built {len(pages)} articles and {len(SUPPORTING) + 3} supporting pages in {OUT}')
    print(f'Built {len(timeline_routes)} timeline pages from {len(events)} events; {skipped} rows skipped for unusable dates')


if __name__ == '__main__':
    main()
