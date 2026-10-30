#!/usr/bin/env python3
"""Verify article front matter, and every local link, asset, and fragment in the generated site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

from build import load, validate

SOURCE = Path(__file__).resolve().parent.parent
ROOT = SOURCE / 'dist'
DYNAMIC_ROUTES = {'/submit/', '/submit/request/', '/submit/correction/'}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.errors = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append('Duplicate ID: ' + attrs['id'])
            self.ids.add(attrs['id'])
        for key in ('href', 'src', 'action'):
            if key in attrs:
                self.links.append(attrs[key])


def main():
    pages = {path: Page(path) for path in ROOT.rglob('*.html')}
    errors = [error for path in sorted((SOURCE / 'pages').glob('*.md')) for error in validate(load(path)[0], path)]
    if not pages:
        raise SystemExit('No built pages. Run scripts/build.py first.')
    for path, page in pages.items():
        errors.extend(f'{path.relative_to(ROOT)}: {error}' for error in page.errors)
        base = '/' + path.relative_to(ROOT).as_posix().removesuffix('index.html')
        for link in page.links:
            url = urlsplit(urljoin(base, link))
            if url.scheme or url.netloc:
                continue
            if url.path in DYNAMIC_ROUTES:
                continue
            target = ROOT / unquote(url.path).lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{base}: missing target {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{base}: missing fragment {link}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} HTML pages: article statuses, local links, assets, IDs, and citation anchors valid.')


if __name__ == '__main__':
    main()
