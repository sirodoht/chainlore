#!/usr/bin/env bash
# Runs on Brick as root, after the public files and application have been uploaded.
set -euo pipefail
umask 077
release="$1"
[[ "$release" =~ ^[0-9]{8}T[0-9]{6}Z-[a-f0-9]{12}$ ]]
root=/var/www/chainlore
app="$root/app-releases/$release"
backup="$root/backups/$release"
uv=/home/deploy/.local/bin/uv

test -x "$uv"
test -s "$root/releases/$release/index.html"
test -s "$app/manage.py"
# Main Caddy imports belong to the Brick repository and are applied by its CI.
grep -Fxq 'import /etc/caddy/chainlore.caddy' /etc/caddy/Caddyfile
if ss -lnt '( sport = :5011 )' | tail -n +2 | grep -q .; then
    systemctl is-active --quiet chainlore
fi
mkdir -m 700 "$backup"
install -d -o deploy -g deploy -m 700 "$root/private"
cp -p /etc/caddy/Caddyfile "$backup/Caddyfile"
cp -p /etc/caddy/chainlore.caddy "$backup/chainlore.caddy"
if [[ -f /etc/systemd/system/chainlore.service ]]; then
    cp -p /etc/systemd/system/chainlore.service "$backup/chainlore.service"
fi
previous="$(readlink "$root/current" || true)"
previous_app="$(readlink "$root/app-current" || true)"
printf '%s\n' "$previous" > "$backup/previous-release"
printf '%s\n' "$previous_app" > "$backup/previous-app-release"

# sqlite3.backup() takes a consistent snapshot even while the service is running.
if [[ -f "$root/private/submissions.sqlite3" ]]; then
    /usr/bin/python3 - "$root/private/submissions.sqlite3" "$backup/submissions.sqlite3" <<'PY'
import sqlite3
import sys
with sqlite3.connect('file:' + sys.argv[1] + '?mode=ro', uri=True) as source:
    with sqlite3.connect(sys.argv[2]) as target:
        source.backup(target)
        assert target.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
PY
    test -s "$backup/submissions.sqlite3"
    echo 'Database backup created and integrity checked.'
fi
chown -R deploy:deploy "$app" "$root/releases/$release"
cd "$app"
as_deploy() {
    runuser -u deploy -- env CHAINLORE_PRODUCTION=1 CHAINLORE_DATA_DIR="$root/private" \
        CHAINLORE_SITE_ROOT="$root/releases/$release" "$@"
}
as_deploy "$uv" sync --locked --no-dev --python /usr/bin/python3
as_deploy .venv/bin/python manage.py check --deploy --fail-level WARNING
as_deploy .venv/bin/python manage.py migrate --noinput
as_deploy .venv/bin/python manage.py collectstatic --noinput --verbosity 0
chmod -R a+rX "$app/staticfiles"
as_deploy .venv/bin/python manage.py bootstrap_admin

rollback() {
    trap - ERR
    echo 'Activation failed; restoring the previous code and routing. Database is not reversed.' >&2
    cp -p "$backup/chainlore.caddy" /etc/caddy/chainlore.caddy
    if [[ -n "$previous" ]]; then
        ln -s "$previous" "$root/rollback-$release"
        mv -Tf "$root/rollback-$release" "$root/current"
    fi
    if [[ -n "$previous_app" && -f "$backup/chainlore.service" ]]; then
        ln -s "$previous_app" "$root/app-rollback-$release"
        mv -Tf "$root/app-rollback-$release" "$root/app-current"
        cp -p "$backup/chainlore.service" /etc/systemd/system/chainlore.service
        systemctl daemon-reload
        systemctl restart chainlore
    else
        systemctl disable --now chainlore || true
        rm -f /etc/systemd/system/chainlore.service "$root/app-current"
        systemctl daemon-reload
    fi
    caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
    systemctl reload caddy
    exit 1
}
trap rollback ERR

ln -s "$root/releases/$release" "$root/next-$release"
mv -Tf "$root/next-$release" "$root/current"
ln -s "$app" "$root/app-next-$release"
mv -Tf "$root/app-next-$release" "$root/app-current"
install -m 644 "$app/deploy/chainlore.service" /etc/systemd/system/chainlore.service
install -m 644 "$app/deploy/chainlore.caddy" /etc/caddy/chainlore.caddy
caddy fmt --overwrite /etc/caddy/chainlore.caddy
caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile
systemctl daemon-reload
systemctl enable chainlore
systemctl restart chainlore
curl --fail --silent --show-error --retry 8 --retry-delay 1 --retry-connrefused \
    -H 'Host: chainlore.xyz' -H 'X-Forwarded-Proto: https' http://127.0.0.1:5011/_service/health/
systemctl reload caddy
systemctl is-active --quiet chainlore caddy
printf '\nDeployed: %s\nPrevious public release: %s\nPrevious app: %s\nBackup: %s\n' \
    "$release" "$previous" "${previous_app:-none}" "$backup"
