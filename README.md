# Chainlore

An AI native encyclopedia of crypto.

Live at https://chainlore.xyz. A static, Wikipedia-inspired site with
muted sage and blue accents. Original encyclopedia drafts are credited to
Opus 5.5 High. Each article records its editorial status and, when
applicable, the fact-checker and check date.

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

Each article links to its Markdown at `/p/<slug>.md`, alongside its HTML page
at `/p/<slug>/`.

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
editorial queue for sending status notifications. New submissions notify the configured
admin; resolving or declining a submission emails the submitter if they supplied an address.
Submissions are private;
receipt pages show a reference number without exposing submitted text or email.
Source URLs are validated but never fetched by the submission endpoint.

Configure the admin recipient with `CHAINLORE_ADMIN_EMAIL` or a private
`admin-email` file in `CHAINLORE_DATA_DIR`. On Brick, the file belongs to `deploy`
with mode `600`, outside the repository and public site. Email delivery uses the
existing private `postmark-token` file. Duplicate form posts and discarded spam
do not trigger admin emails. Delivery failures are logged with the submission
reference, and the submission remains saved for review; there is no automatic retry.

Article and section links prefill the forms. Each form has CSRF protection,
a hidden spam field, and a signed token to prevent repeated posts from creating
duplicate records. Limits are 10 submissions per connection per hour and
10 admin login attempts per connection per 15 minutes. Rate-limit keys use
hashed addresses and expire at the end of their window; raw addresses are not
stored in the submission database.

### Automatic article requests

The production `chainlore-worker.timer` runs every minute. It processes new article
requests (including an existing backlog), one at a time, with a default limit of
10 new runs per UTC day. Error reports remain in the manual queue.

1. Save an immutable snapshot of title, scope, and source hints. The email field
   and server secrets are never sent to either model.
2. Resolve exact existing titles locally. Ask Jev (`jev-latest`) about broad
   crypto relevance and injected instructions. People, organisations, events,
   laws, technology, history, culture, and concepts are in scope. Uncertain
   classifications proceed to research. Reject only clear off-topic/spam or
   injection findings (confidence at least 0.8 and probability at least 0.9).
   Duplicate detection uses actual title/slug matches, including the writer's
   canonical title, rather than model uncertainty about related subjects.
3. Have `claude-haiku-5-5`, with adaptive thinking at high effort, research with
   up to eight web searches and six source retrievals (4,000 content tokens each),
   then write a bounded JSON/Markdown draft in a separate call without tools. No model gets
   shell access, filesystem tools, email tools, or publishing credentials.
4. Check the slug, metadata, inert Markdown, citations, and source provenance.
   Citations must be pages research opened or results the search tool returned.
   Every accepted subject gets a page: a rejected draft is rewritten once with the
   reason, then replaced by a fixed placeholder that lists any sources found and
   contains no model text. Jev holds a draft only when it is confident the draft
   is spam, off-topic, injected, or exposes contact details. This does not confer
   an AI fact-checked status: generated articles are explicitly published as drafts.
5. Rebuild the full site, run the static checker, and atomically switch its public
   symlink. Email the requester about the resulting article or declined request.

Missing or malformed screening results go to review. Transient provider errors retry from
saved checkpoints, at most three attempts with backoff, so an outage can still
leave a run Failed until it is retried from the admin. The worker never silently
substitutes a model or treats a failed screening call as an approval.
Provider errors, requests, responses, usage, decisions, validation results, hashes,
publication IDs, and notification outcomes are available in the private admin
under Automation runs, Automation events, and Generated articles. Hidden model
thinking stays out of audit events and saved research; only the private research
checkpoint keeps the opaque signed blocks needed to resume a paused turn.
Notifications retry up to three times, one hour apart;
SMTP acceptance does not prove inbox delivery. Existing admin-new-submission
notifications keep their original behavior.

Research handles `pause_turn` by sending the exact paused assistant content back
in a capped loop (three responses total). It saves each completed response before
continuing, so a later error or worker restart resumes from that checkpoint.
The final research record merges all content blocks and usage; writing and source
validation can use evidence from every part. Search/fetch allowances are reduced
across continuations, not reset. Research cut short by the continuation cap still
goes on to writing from the pages it fetched. Continuations keep both tools, as the API expects, so a spent
tool keeps one use for any pending call; each continuation can exceed the budget by
at most one use per tool. Each research HTTP request has a 300-second timeout;
the worker's 35-minute deadline covers three such requests, the other model calls,
build checks and notifications. An interrupted in-flight HTTP request can still
lose work that the provider has not returned; completed responses are preserved.

Missing credentials, HTTP 400/401/402/403/404 configuration/account errors and
recognized spend-cap errors pause the entire queue in the persistent Automation
control record. The affected run becomes Waiting for provider recovery without
consuming an attempt; subsequent worker ticks make no model calls and leave new
requests queued. The worker alerts the configured admin, logs the pause, and
records alert acceptance/failure. Failed alerts retry hourly, up to three attempts.
The admin control remains visible even if email is suppressed or unavailable.
A run that hits such an error again after a resume is marked Failed instead of
pausing the queue a second time, so one bad request cannot block those behind it.
If the problem was account-wide, the next run pauses the queue as usual.

After fixing the provider settings or billing, select the control in
`/admin/submissions/automationcontrol/` and choose **Resume queue after fixing
provider settings**. Under Automation runs, **Retry failed runs from their saved
stage** recovers failed requests without SQL edits. **Restart screening and
research for held review runs** deliberately starts fresh screening/research while
preserving the old audit events. **Regenerate placeholder pages with fresh research**
re-runs research and writing for a published placeholder, which stays live until a
replacement passes every check. These operations require the respective change
permission, respect the worker lock, and record the operator in the audit log;
ordinary audit fields remain read-only. Resolved/published runs cannot be retried
through these actions.

Provider keys are read by the worker from `TYPESAFE_API_KEY` and `ANTHROPIC_API_KEY`,
or private files `jev-api-key` and `anthropic-api-key` in `CHAINLORE_DATA_DIR`
(owner `deploy`, mode `600` on Brick). Never put credentials in source, prompts,
unit files, or public build artifacts. `CHAINLORE_AUTOMATION_ENABLED=1` enables
processing; `CHAINLORE_AUTOMATION_DAILY_LIMIT` changes the daily run cap. Local
development defaults to disabled. Stop `chainlore-worker.timer` and the worker
service together to pause production processing immediately.

Generated Markdown is authoritative in SQLite, not automatically committed to
Git. Every deployment combines the shipped Git sources with these database
articles, updating the index, search, sitemap, and Markdown URLs. A page added
deliberately to `pages/` with the same slug supersedes the generated version.
Generated articles join the index and homepage subject lists using their category
metadata (for example, Exchange maps to Exchanges). Existing curated entries and
summaries stay in place. Infrastructure and Other topics sections appear only when
needed; request provenance is not a public category.
Back up the database to retain generated articles and their audit history.
Public releases are under `published/releases/`, with an atomic `published/current`
symlink; the existing `current` path points to that symlink. The worker can write
only the private data and publication directories under systemd's sandbox.

For local processing after setting private credentials:

```sh
CHAINLORE_AUTOMATION_ENABLED=1 uv run --locked python manage.py process_requests
```

`manage.py publish_site --base-release dist` rebuilds the publication from Git
sources and database articles without calling a model. It uses the same lock as
the worker. A failed build leaves the previous public site intact.

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
| `current` | Symlink to `published/current` |
| `published/releases/<publication>/` | Complete checked site, including database articles |
| `published/current` | Atomically switched active publication |
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

Before a manual rollback, stop `chainlore-worker.timer` and `chainlore-worker.service`.
For a content-only rollback, atomically switch `published/current` to a retained
public release. Keep `current` pointing to `published/current`. The exact previous
publication is recorded in `backups/<release>/previous-publication`. For a service
rollback, also switch `app-current` to the matching app release, restore its worker
units, and restart `chainlore.service`, after checking database compatibility.
Restart the worker timer only when ready to process and publish requests again.
Configuration and database snapshots are in `backups/<release>/`.
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

1. **Front matter**: title, ticker, category, status, last updated date, and `written_by` (writer model and effort).
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

Writer attribution is required by the build. `checked_by` records the actual
checker model and effort; `checked` records the check date. Application names
alone are insufficient. See POLICY.md and AGENTS.md for attribution on later
edits and checks. These credits appear in article headers and Markdown exports.

The automated writer copies its model identifier from the provider response
(falling back to the request identifier) and effort from the request into
`written_by`; generated text cannot set its own credit. The credit is saved
with the draft for retries and publication. Migration 0006 recovers credits for
existing database articles from matching writing responses and their requests,
updates content hashes, and uses `Unknown` when evidence is absent. Placeholder
pages credit the fixed Chainlore template. Jev screening remains separately
audited and does not populate `checked_by`.
