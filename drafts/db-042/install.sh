#!/usr/bin/env bash
# Install the pitches-server systemd unit. One-time run (needs sudo password).
# After install, the nohup instance gets replaced by a proper service that
# survives reboots and is in the sudo NOPASSWD restart list.

set -euo pipefail

UNIT_SRC="/home/assistant/projects/drafts/db-042/pitches.service"
UNIT_DST="/etc/systemd/system/pitches.service"

if [[ ! -f "$UNIT_SRC" ]]; then
  echo "missing unit file: $UNIT_SRC" >&2
  exit 1
fi

echo "stopping nohup instance on :3778 (if any)..."
pkill -f "node /home/assistant/projects/assistant/pitches-server.js" 2>/dev/null || true
sleep 1

echo "installing $UNIT_DST (sudo required)..."
sudo cp "$UNIT_SRC" "$UNIT_DST"
sudo chmod 644 "$UNIT_DST"
sudo systemctl daemon-reload
sudo systemctl enable --now pitches
sleep 2

echo "verifying..."
sudo systemctl status pitches --no-pager | head -8
ss -ltn | grep 3778 || { echo "NOT LISTENING after install"; exit 1; }
curl -sk -o /dev/null -w "pitch/1993: %{http_code}\n" https://pitch.runatyr.games/1993

echo
echo "done. add to NOPASSWD sudoers if you want agent-triggered restarts:"
echo "  assistant ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart pitches, /usr/bin/systemctl status pitches"
