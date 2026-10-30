# Chainlore

An AI native encyclopedia of crypto.

Live at https://chainlore.xyz. A static, Wikipedia-inspired site with
muted sage and blue accents. Encyclopedia articles are credited to
Opus 5.5 High for writing and fact-checking; article draft status is
preserved separately in the editorial record.

## Build and preview

Requires uv and Python 3.11 or newer. Dependencies are declared in
`pyproject.toml` and locked in `uv.lock`. The encyclopedia is generated
HTML; Django 5.2 LTS handles submissions and the private review queue.

```sh
uv sync --locked
uv run --locked python scripts/build.py
uv run --locked python scripts/check.py
uv run --locked python manage.py migrate
uv run --locked python manage.py createsuperuser
uv run --locked python manage.py runserver 8000
```

Open http://localhost:8000. In development, Django serves both the generated
site and the forms. Local data and the generated secret key live in `.data/`,
which is ignored by Git. Production serves the generated site directly from
Caddy.

The build reads `pages/*.md`, `INDEX.md`, `VISION.md`, `ABOUT.md`, and
`POLICY.md`. It writes `dist/`, including the search index and an article
catalog used to preselect articles and sections in forms. Add articles to
`pages/` and link them from `INDEX.md`.

```sh
uv run --locked python manage.py test submissions
uv run --locked python manage.py makemigrations --check --dry-run
```

The static checker validates article metadata, internal links, and citation
anchors. Django tests cover form validation, CSRF, duplicate submissions,
spam controls, private receipts, and admin access and review operations.

## Submissions

- `/submit/request/`: required article title, with optional scope, sources, and email.
- `/submit/correction/`: quoted claim, explanation, source links, and optional replacement text.
- `/admin/`: authenticated review queue with filters, search, internal notes,
  duplicate links, and a URL for the resulting article change.

Email is optional and never published. It is available only in the authenticated
editorial queue for replying to the submitter. No emails are sent automatically. Submissions are private;
receipt pages show a reference number without exposing submitted text or email.
Source URLs are validated but never fetched by the submission endpoint.

Article and section links prefill the forms. Each form has CSRF protection,
a hidden spam field, and a signed token to prevent repeated posts from creating
duplicate records. Limits are 10 submissions per connection per hour and
10 admin login attempts per connection per 15 minutes. Rate-limit keys use
hashed addresses and expire at the end of their window; raw addresses are not
stored in the submission database.

## Deploy to Brick

Requires SSH access to `root@01z.io`, plus local uv, rsync, and curl.
Brick needs `/home/deploy/.local/bin/uv` and Python 3.11 or newer.

```sh
git add <changed-files>
git commit -m "Describe the update"
./deploy.sh
```

The script requires a clean checkout, builds the static site, runs checks and
tests, and uploads versioned releases with rsync. Application code runs as
`deploy`. Caddy serves articles directly and proxies `/submit/` and `/admin/`
to Gunicorn on `127.0.0.1:5011`. Django admin assets are served by Caddy under
`/service-static/`. The health endpoint is loopback-only through Caddy routing.

Paths on Brick:

| Path under `/var/www/chainlore/` | Contents |
|---|---|
| `releases/<release>/` | Public HTML, assets, article catalog, and commit metadata |
| `current` | Symlink to the active public release |
| `app-releases/<release>/` | Django code, uv environment, and admin static assets |
| `app-current` | Symlink to the active service release |
| `private/` | SQLite database, secret key, and initial admin credentials; mode 700 |
| `backups/<release>/` | Previous release paths, configuration, service unit, and database snapshot |

The private directory is outside all Caddy document roots and rsync destinations.
Before migrations, the script backs up an existing database using SQLite's
backup API and checks the backup's integrity. Dependencies, migrations, and
static collection run before switching releases. Activation installs the
systemd unit and app-owned Caddy snippet, checks the complete Caddy config,
restarts the service, checks its health, and reloads Caddy.

The main Caddyfile is owned by the Brick repository. Its Chainlore import
must already be committed, pushed, and deployed through Brick CI; this script
does not edit the main Caddyfile. Chainlore itself deploys without GitHub.

### Admin access

The first deployment creates an `admin` account with a random password and
writes its credentials to `private/admin-initial-credentials.txt` with mode 600.
Later deployments leave existing accounts and passwords unchanged. Retrieve
that file privately over SSH; do not add it to Git. Passwords can be changed
through the admin's Change password page. After recording the password in a
password manager, the initial credentials file can be removed.

### Rollback

Activation failures restore the previous public and app symlinks, Caddy snippet,
and systemd unit. The database is never automatically reversed. Migrations
must be reviewed for compatibility with the previous app before deploying;
stop for migrations that need a different rollback procedure.

For a manual content-only rollback, switch `current` to a retained public
release. For a service rollback, also switch `app-current` to the matching
app release and restart `chainlore.service`, after checking database
compatibility. Configuration and database snapshots are in `backups/<release>/`.
Do not restore a database over newer submissions without a recovery plan.

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
