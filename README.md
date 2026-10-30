# Chainlore

An AI native encyclopedia of crypto.

Live at https://chainlore.xyz. A static, Wikipedia-inspired site with
muted sage and blue accents. Encyclopedia articles are credited to
Opus 5.5 High for writing and fact-checking; article draft status is
preserved separately in the editorial record.

## Build and preview

Requires Python 3.9 or newer. The only direct dependency is Python-Markdown.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/check.py
.venv/bin/python -m http.server 8000 --directory dist
```

Open http://localhost:8000. The build reads `pages/*.md`, `INDEX.md`,
`VISION.md`, `INSPIRATION.md`, and `ABOUT.md`, then writes `dist/`.
Article links become HTML routes; tables, footnotes, and contents are
rendered from Markdown. The check script verifies all internal links,
assets, unique IDs, and citation anchors. Search uses a generated JSON
index in the browser. Articles and navigation work without JavaScript.

Add an article in `pages/` with the front matter below and link it from
`INDEX.md`. It will be included in the build, search, and sitemap.

## Deploy to Brick

With SSH access to `root@01z.io`, and `rsync`, `scp`, and `curl` installed:

```sh
git add <changed-files>
git commit -m "Describe the update"
./deploy.sh
```

The script requires a clean, committed checkout, builds and checks locally,
and uploads only `dist/` via rsync to `/var/www/chainlore/releases/`.
It atomically switches `/var/www/chainlore/current`, installs the checked-in
Caddy snippet, validates the entire Caddy configuration, and reloads Caddy.
No application service, database, GitHub remote, or CI is needed.

The first deployment adds `import /etc/caddy/chainlore.caddy` to the live
Caddyfile, preserving existing routes. The same import must be retained
in Brick's `Caddyfile.j2` before any future infrastructure deployment.
DNS is managed separately in Hetzner: `chainlore.xyz` points to Brick.

Each release records its commit in `/build-info.json`. Previous releases
are retained. Caddy configuration and the previous release path are saved
in `/var/www/chainlore/backups/<release>/`. Configuration failures restore
the previous route and release automatically. A public HTTPS check runs
after deployment; if it fails, inspect DNS and certificate issuance before
deciding whether to roll back.

For a manual content rollback, choose a known release on Brick, then run:

```sh
ssh root@01z.io
ln -s /var/www/chainlore/releases/<previous-release> /var/www/chainlore/rollback
mv -Tf /var/www/chainlore/rollback /var/www/chainlore/current
```

No Caddy reload is needed for a content-only rollback. Config backups are
available if routing also needs restoring; validate before reloading.

## Why

Chainlore documents the history, technology, governance, and incidents of
blockchains and protocols. See [editorial scope](VISION.md).

## Contents

| File | Purpose |
|---|---|
| [VISION.md](VISION.md) | What Chainlore is and what it is not |
| [INDEX.md](INDEX.md) | Every page in the encyclopedia |
| [INSPIRATION.md](INSPIRATION.md) | Existing sites we learn from |
| [ABOUT.md](ABOUT.md) | Public authorship credit and editorial process |
| [POLICY.md](POLICY.md) | Page statuses, fact-checking, and source rules |
| [pages/](pages/) | The articles, one Markdown file per subject |

## Page conventions

Every page in `pages/` follows the same shape:

1. **Front matter**: title, ticker, category, status, last updated date.
2. **Lead**: one paragraph that says what the subject is.
3. **Infobox**: a two-column table of hard facts.
4. **Body sections**: History, Technology, Token, Governance, Incidents
   and controversies, as applicable.
5. **Timeline**: dated events, oldest first.
6. **See also**: links to other Chainlore pages.
7. **References**: numbered footnotes, preferring primary sources such as
   whitepapers, specifications, official docs, governance proposals, and
   onchain data.

Rules:

- Every factual claim should be traceable to a reference.
- Dates are written as `D Month YYYY` in prose and `YYYY-MM-DD` in tables.
- Figures that change constantly (price, TVL, market cap) are not
  hardcoded into prose. Link to a live source instead.
- Every page has a status: `draft`, `ai-fact-checked`, or
  `human-reviewed`. [POLICY.md](POLICY.md) sets out what each requires
  and the source rules every page must meet.
- File names are lowercase and hyphenated: `pages/arbitrum.md`.
