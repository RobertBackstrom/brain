#!/usr/bin/env bash
# install-root.sh — same as install.sh, but uses `su` (root password) instead
# of `sudo` (assistant user password). Use this if you only have the root pw.

set -euo pipefail

UNIT_SRC="/home/assistant/projects/drafts/db-042/pitches.service"
UNIT_DST="/etc/systemd/system/pitches.service"

if [[ ! -f "$UNIT_SRC" ]]; then
  echo "missing unit file: $UNIT_SRC" >&2
  exit 1
fi

echo "stopping nohup instance on :3778 (if any)..."
pkill -f "node pitches-server.js" 2>/dev/null || true
sleep 1

echo "installing systemd unit — root password required..."
su -c "cp '$UNIT_SRC' '$UNIT_DST' && \
       chmod 644 '$UNIT_DST' && \
       systemctl daemon-reload && \
       systemctl enable --now pitches && \
       sleep 2 && \
       systemctl status pitches --no-pager | head -8"

echo
echo "verifying..."
ss -ltn | grep 3778 || { echo "NOT LISTENING after install"; exit 1; }
curl -sk -o /dev/null -w "pitch/1993/: %{http_code}\n" https://pitch.runatyr.games/1993/

echo
echo "done. pitches-server is now managed by systemd and survives reboots."
