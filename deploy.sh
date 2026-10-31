#!/usr/bin/env bash
# Build and test locally; upload versioned static and Django releases to Brick.
set -euo pipefail
cd "$(dirname "$0")"

host="${DEPLOY_HOST:-root@01z.io}"
remote_root=/var/www/chainlore
if ! command -v uv >/dev/null 2>&1; then
    echo 'Install uv before deploying; see README.md.' >&2
    exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
    echo 'Commit the intended changes before deploying (working tree must be clean).' >&2
    exit 1
fi
git fetch --quiet origin main
if ! git merge-base --is-ancestor HEAD refs/remotes/origin/main; then
    echo 'Push this application commit to main before deploying; article publication reads main.' >&2
    exit 1
fi
uv run --locked python scripts/build.py
uv run --locked python scripts/check.py
uv run --locked python manage.py test submissions
uv run --locked python manage.py makemigrations --check --dry-run
bash -n deploy.sh
bash -n deploy/activate.sh
revision="$(git rev-parse HEAD)"
release="$(date -u +%Y%m%dT%H%M%SZ)-${revision:0:12}"
printf '{"revision":"%s","release":"%s"}\n' "$revision" "$release" > dist/build-info.json

ssh "$host" bash -s -- "$release" <<'REMOTE'
set -euo pipefail
release="$1"
[[ "$release" =~ ^[0-9]{8}T[0-9]{6}Z-[a-f0-9]{12}$ ]]
systemctl is-active --quiet caddy
test -x /home/deploy/.local/bin/uv
grep -Fxq 'import /etc/caddy/chainlore.caddy' /etc/caddy/Caddyfile
for link in current app-current; do
    if [[ -e "/var/www/chainlore/$link" && ! -L "/var/www/chainlore/$link" ]]; then
        echo "Refusing to replace non-symlink $link" >&2
        exit 1
    fi
done
install -d -m 755 /var/www/chainlore/releases /var/www/chainlore/app-releases /var/www/chainlore/backups
mkdir -m 755 "/var/www/chainlore/releases/$release" "/var/www/chainlore/app-releases/$release"
REMOTE

# Public files and application source have separate roots. Persistent data is never synced.
rsync -az --chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r dist/ "$host:$remote_root/releases/$release/"
rsync -az --chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r --exclude '__pycache__/' \
    pyproject.toml uv.lock manage.py service submissions deploy scripts site pages \
    README.md INDEX.md ABOUT.md VISION.md POLICY.md \
    "$host:$remote_root/app-releases/$release/"
ssh "$host" bash -s -- "$release" < deploy/activate.sh
curl --fail --silent --show-error --retry 3 --retry-delay 2 --retry-all-errors \
    https://chainlore.xyz/build-info.json
curl --fail --silent --show-error -o /dev/null https://chainlore.xyz/submit/request/
printf '\nLive: https://chainlore.xyz\nAdmin: https://chainlore.xyz/admin/\n'
