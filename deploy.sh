#!/usr/bin/env bash
# Build locally, upload an immutable release with rsync, then switch Caddy's root.
set -euo pipefail
cd "$(dirname "$0")"

host="${DEPLOY_HOST:-root@01z.io}"
python="${PYTHON:-.venv/bin/python}"
remote_root=/var/www/chainlore

if [[ ! -x "$python" ]]; then
    echo 'Create .venv and install requirements.txt first; see README.md.' >&2
    exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
    echo 'Commit the intended changes before deploying (working tree must be clean).' >&2
    exit 1
fi

"$python" scripts/build.py
"$python" scripts/check.py
bash -n deploy.sh
revision="$(git rev-parse HEAD)"
release="$(date -u +%Y%m%dT%H%M%SZ)-${revision:0:12}"
printf '{"revision":"%s","release":"%s"}\n' "$revision" "$release" > dist/build-info.json

# Only generated public files are uploaded. No Git checkout, secrets, or source tools.
ssh "$host" bash -s -- "$release" <<'REMOTE'
set -euo pipefail
release="$1"
systemctl is-active --quiet caddy
test -f /etc/caddy/Caddyfile
if [[ -e /var/www/chainlore/current && ! -L /var/www/chainlore/current ]]; then
    echo 'Refusing to replace a non-symlink document root.' >&2
    exit 1
fi
install -d -m 755 /var/www/chainlore/releases /var/www/chainlore/backups
mkdir -m 755 "/var/www/chainlore/releases/$release"
REMOTE

rsync -az --chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r dist/ "$host:$remote_root/releases/$release/"
scp deploy/chainlore.caddy "$host:$remote_root/releases/$release.caddy"

ssh "$host" bash -s -- "$release" <<'REMOTE'
set -euo pipefail
release="$1"
root=/var/www/chainlore
backup="$root/backups/$release"
mkdir -m 700 "$backup"
cp -p /etc/caddy/Caddyfile "$backup/Caddyfile"
if [[ -f /etc/caddy/chainlore.caddy ]]; then
    cp -p /etc/caddy/chainlore.caddy "$backup/chainlore.caddy"
fi
previous="$(readlink "$root/current" || true)"
printf '%s\n' "$previous" > "$backup/previous-release"
test -s "$backup/Caddyfile"
test -s "$root/releases/$release/index.html"

rollback() {
    trap - ERR
    echo 'Deployment failed; restoring the previous route and release.' >&2
    cp -p "$backup/Caddyfile" /etc/caddy/Caddyfile
    if [[ -f "$backup/chainlore.caddy" ]]; then
        cp -p "$backup/chainlore.caddy" /etc/caddy/chainlore.caddy
    else
        rm -f /etc/caddy/chainlore.caddy
    fi
    if [[ -n "$previous" ]]; then
        ln -s "$previous" "$root/rollback-$release"
        mv -Tf "$root/rollback-$release" "$root/current"
    else
        rm -f "$root/current"
    fi
    caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
    systemctl reload caddy
    exit 1
}
trap rollback ERR

chown -R deploy:deploy "$root/releases/$release"
ln -s "$root/releases/$release" "$root/next-$release"
mv -Tf "$root/next-$release" "$root/current"
install -m 644 "$root/releases/$release.caddy" /etc/caddy/chainlore.caddy

# This project deliberately deploys over SSH without GitHub or CI.
# Preserve every unrelated site and add only this application's import.
if ! grep -Fxq 'import /etc/caddy/chainlore.caddy' /etc/caddy/Caddyfile; then
    printf '\nimport /etc/caddy/chainlore.caddy\n' >> /etc/caddy/Caddyfile
fi
caddy fmt --overwrite /etc/caddy/chainlore.caddy
caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
systemctl reload caddy
systemctl is-active --quiet caddy
printf 'Deployed release: %s\nPrevious release: %s\nConfiguration backup: %s\n' "$release" "${previous:-none (first deployment)}" "$backup"
REMOTE

# Certificate issuance can take a few seconds on the first deployment.
curl --fail --silent --show-error --retry 8 --retry-delay 3 --retry-all-errors \
    https://chainlore.xyz/build-info.json
printf '\nLive: https://chainlore.xyz\n'
