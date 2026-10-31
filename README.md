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

The build merges every article table whose first column is headed `Date` into
`/timeline/`, with `/timeline/hacks/`, `/timeline/laws/` and
`/timeline/collapses/` views and `/on-this-day/<month>-<day>/` pages. Dates are
`2018`, `2018-09`, `2018-09-26` or a same-month range, `2023-03-10–13`, and are
shown only as precisely as stated. Only exact dates reach the day pages. Rows
with any other date are left out rather than failing the build, and the build
prints how many. Rows dated after the build appear under Scheduled. The same
event in several articles is merged by date and wording, and the views are
keyword rules (`TIMELINE_VIEWS` in `scripts/build.py`).

```sh
uv run --locked python manage.py test submissions
uv run --locked python manage.py makemigrations --check --dry-run
```

The static checker validates article metadata, internal links, and citation
anchors. Django tests cover form validation, CSRF, duplicate submissions,
spam controls, private receipts, and admin access and review operations.

## Submissions

- `/submit/all/`: public tracker for article requests, errors, and improvements, with type/status filters and pagination.
- `/submit/track/<reference>/`: progress, public outcome, article/original-submission links, and dated activity history. Receipts link directly here.
- `/submit/request/`: required article title, with optional scope, sources, and email.
- `/submit/correction/`: quoted claim and explanation, with optional source links and replacement text.
- `/submit/improvement/`: article and suggested improvement, with optional section, sources, and email.
- `/admin/`: authenticated operations queue with filters, search, internal notes,
  duplicate links, and a URL for the resulting article change.
- `/admin/review/`: editorial operations dashboard for staff with submission view or
  change permission. It reads status, attribution, and dates from the current
  published catalogue and joins unresolved, non-duplicate error-report counts.
  Search and filter drafts, overdue checks, open reports, or articles awaiting
  completed verification. Checks become due after 30 days; this does not
  automatically change article statuses. A new check date requires verification of the entire resulting article. The admin header links to the dashboard.

Email is optional and never published. It is available only in the authenticated
editorial queue for sending status notifications. New submissions notify the configured
admin; resolving or declining a submission emails the submitter if they supplied an address.
Submission text, email, sources, internal notes, and provider audit payloads stay
private. The public tracker shows type, dates, status, and approved public titles
and summaries. Historical private titles are not automatically republished:
neutral titles use the related published article or a short reference until a
published title is available. Automated decisions provide public outcomes. Resolved automated requests link to the published
article; improvements also link to the publication commit in their activity history.
Duplicate submissions link to the original where one exists, or the existing article.

Owner overrides can set **Public title** and **Public summary** in the submission admin. Routine processing does not require these overrides.
A new manual resolved/declined decision requires an outcome note (duplicates are
exempt); resolved article requests also require the resulting article URL.
These public changes are recorded as dated updates. Legacy decisions without a
public explanation say so rather than inventing a reason or transition date.
Automation history uses a fixed allowlist of milestone labels, never provider
responses or exception text. Held work is re-investigated automatically; retrying runs show Queued and
operational failures show Blocked with a retry time where available. The existing staff automation actions provide retry/recovery.
Source URLs are validated but never fetched by the submission endpoint.

Configure the admin recipient with `CHAINLORE_ADMIN_EMAIL` or a private
`admin-email` file in `CHAINLORE_DATA_DIR`. On Brick, the file belongs to `deploy`
with mode `600`, outside the repository and public site. Email delivery uses the
existing private `postmark-token` file. Duplicate form posts and discarded spam
do not trigger admin emails. Delivery failures are logged with the submission
reference, and the submission remains queued for automated processing; the new-submission alert has no automatic retry.

Article and section links prefill both error-report and improvement forms. Each form has CSRF protection,
a hidden spam field, and a signed token to prevent repeated posts from creating
duplicate records. Limits are 10 submissions across all three types per connection per hour and
10 admin login attempts per connection per 15 minutes. Rate-limit keys use
hashed addresses and expire at the end of their window; raw addresses are not
stored in the submission database.

### Autonomous editorial pipeline

The production worker runs one durable stage per timer invocation under the
publication lock. Requests, corrections and improvements share the same workflow.
Legacy held jobs are re-investigated automatically; they are never bulk-approved.

1. Screen broad crypto relevance and injected instructions. Exact existing-title
   matches resolve as duplicates; fuzzy overlap alone is not a rejection.
2. Research primary sources and reputable reporting. Existing articles and reported
   corrections are context, not evidence. Emails are excluded from provider inputs.
3. Write a draft or targeted patch, preserving original writer attribution.
4. A separate checker context independently opens every reference and searches for
   significant developments. It returns an ID-complete inventory of paragraphs and
   table rows, individual claims, fetched evidence excerpts, and support decisions.
5. Validate coverage, fetched URLs, excerpts, date and source hash. Persist the actual
   checker model/effort, report and source fingerprints. Tool failures cannot pass.
6. Retry unsupported work through at most two research/revision passes. Exhaustion
   ends as Insufficient evidence and preserves the current article.
7. Publish only the exact approved source, against its expected Git base. A concurrent
   edit restarts research against a fresh snapshot. Commit/push precede atomic publication.
8. Record a public explanation and article/commit links, then deliver outcome notifications.

`Verification` records are private audit artifacts. Their approved source hash must
match the file being staged. Existing independently checked content is not automatically
relabelled; this gate applies to new automated work. Historical human credits remain
supported, but human approval is not a workflow stage.

### Recovery and budgets

Transient failures retry with increasing delays, up to three recovery attempts.
Account/provider failures pause the queue and schedule up to three exponentially
spaced probes of the pending stage. Exhausted credentials/billing recovery remains
an explicit operational Blocked state. Owners retain pause/resume and budget controls.
The dashboard displays blockers and retry times; it is not an editor approval queue.

Each paid call reserves estimated input/output and tool headroom before sending.
Server-tool estimates include extra allowance for repeated sampling. Completed calls
settle against provider-reported input, output and cache input tokens; failed calls
or responses without usable usage retain their estimates. An in-flight call can
exceed its estimate: subsequent admission uses the higher actual cost. These are
call-admission budgets, not provider-enforced spending caps or currency invoices.
The dashboard shows the same accounted total used by admission checks.

Defaults and environment controls:

- `CHAINLORE_AUTONOMOUS_EDITORIAL=1`: default autonomous pipeline. Setting 0 retains
  the legacy pipeline for compatibility/testing only; it is not the production rollout.
- `CHAINLORE_EDITORIAL_SHADOW=1`: run checks without publishing; passed jobs explicitly
  stop in a shadow Blocked state. Never claim a shadow result was published.
- `CHAINLORE_AUTOMATION_DAILY_LIMIT=10`: new jobs per UTC day, including maintenance.
- `CHAINLORE_DAILY_TOKEN_LIMIT=2000000`: shared daily call-admission budget.
- `CHAINLORE_RUN_TOKEN_LIMIT=1500000`: lifetime call-admission budget per job.
- `CHAINLORE_CHECKER_MODEL`: explicit checker model; defaults to the configured writer
  model in a separate context, not an implicit provider/model substitution.
- `CHAINLORE_MAINTENANCE_ENABLED=1` and `CHAINLORE_MAINTENANCE_DAILY_LIMIT=1`:
  maintenance runs only after reader work, targeting drafts and checks at least 30 days
  old. Failed maintenance has a seven-day cooldown rather than an endless paid loop.

Daily-budget blocks resume the next day. A per-job budget or exhausted recovery needs
an operational limit/configuration decision, never an editorial approval. Both remain
visible and preserve the existing article. API secrets and database files stay private.

Interrupted or malformed verification output does not trigger rewriting. The checker
keeps the candidate and its independently fetched sources, then checks groups of at most four units with at most two report-only attempts per
group, a 16,000-token output allowance and no tools. Each cited group receives its
complete cited documents; uncited facts retain the full source set. Group approvals
are combined only when every unit is covered, then the full report is validated again. Complete
reports with factual findings still request revision. Incomplete reports end in an
explicit operational block; they never confer publication approval. Saved reports
are assessed after a restart before another paid call. Evidence from a different
UTC day requires a fresh source check.

To recover a historical run held by this bug, use
`manage.py resume_verification --submission UUID` under the normal worker environment.
It requires a blocked, undecided run, an unchanged candidate, an interrupted report,
same-day evidence and no later paid work. It creates a new pending check using saved
evidence, restores a lost draft from the writing audit if necessary, and preserves
the earlier failed check. It neither raises budgets nor bypasses source verification.

### Scheduled upkeep and audit

Maintenance independently checks source availability, significant developments,
existing claims, categories and related links. Missing related links are selected
conservatively from article titles already mentioned in the public prose. Known category
aliases are normalized. No automated topic merges or deletions occur. Changes go through
the same exact-source verification gate as reader work.

The operations dashboard at `/admin/review/` combines active/blocked jobs, retry times,
provider token usage, article freshness and open error reports. `/submit/all/` exposes
safe public progress; raw requests, email and provider payloads are never rendered.

Testing includes malformed/incomplete checker reports, fabricated or unopened sources,
wrong dates, changed-after-check content, concurrent edits, exhausted revision limits,
budget blocks and shadow-mode publication prevention. Use `replay_editorial --source FILE --expect passed` to run
non-publishing checks on saved source snapshots before enabling new provider settings.

Provider credentials are read from `TYPESAFE_API_KEY` and `ANTHROPIC_API_KEY`,
or private `jev-api-key` and `anthropic-api-key` files in `CHAINLORE_DATA_DIR`.
On Brick these files belong to `deploy` with mode `600`. Local processing is
disabled unless `CHAINLORE_AUTOMATION_ENABLED=1`. No model receives credentials
or shell, email or filesystem tools. Provider account errors and budget blocks
are visible in the operations dashboard; owner controls can pause, resume or
retry saved stages without bypassing verification.

Every public article is authoritative in Git. Publication uses a fresh checkout,
stages only article paths and `INDEX.md`, validates the full build and pushes
without force as `Chainlore Bot`. Only a successful push can become the live site.
`build-info.json` records article `revision` and deployed `app_revision` separately.
Git retains article history; SQLite retains requests, evidence and workflow audit.

The worker and publisher need Git and repository write access. Brick uses
`/var/www/chainlore/private/article-git-key` and pinned host keys at
`/var/www/chainlore/private/github-known-hosts`, owned by `deploy`, mode `600`.
The service and activation script set `CHAINLORE_ARTICLE_GIT_REMOTE`,
`CHAINLORE_ARTICLE_GIT_KEY` and `CHAINLORE_ARTICLE_GIT_KNOWN_HOSTS`;
`CHAINLORE_ARTICLE_GIT_BRANCH` defaults to `main`. Local runs have no implicit
publication remote. Use disposable repositories for local end-to-end tests.
`manage.py publish_site --base-release dist` builds the current branch and any
pending, exactly verified publication under the worker's lock, without model calls.

## Deploy to Brick

Requires SSH access to `root@01z.io`, plus local uv, rsync, and curl.
Brick needs `/home/deploy/.local/bin/uv`, Python 3.11 or newer, Git, and the
article deploy key described above. Push the intended application commit to `main`
before deploying; publication reads article sources from the remote branch.

```sh
git add <changed-files>
git commit -m "feat: describe the update"
git push
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


For a real-provider verification replay, use a fresh private `CHAINLORE_DATA_DIR`,
set `CHAINLORE_EDITORIAL_SHADOW=1`, leave `CHAINLORE_PRODUCTION` and
`CHAINLORE_AUTOMATION_ENABLED` unset, and leave `CHAINLORE_ARTICLE_GIT_REMOTE`
empty. Migrate the isolated database, provide the usual provider credential, then
run `python manage.py replay_editorial --source submissions/fixtures/verification-supported.md --expect passed`.
Repeat with `verification-false-date.md --expect failed`. The command refuses a
production configuration, has no publication path, and prints only result codes,
source hashes and usage. Evidence and provider responses remain in the private
replay database. A historical article source can be checked the same way; do not
copy submission contact details into replay fixtures.
