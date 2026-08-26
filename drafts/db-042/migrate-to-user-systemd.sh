#!/usr/bin/env bash
# migrate-to-user-systemd.sh — move pitches-server to systemd --user.
# One-time root for `loginctl enable-linger assistant`. Everything else is
# user-level and never needs root again.

set -euo pipefail

# code-server shells (and some other non-PAM spawns) don't set XDG_RUNTIME_DIR,
# which systemctl --user needs to find the dbus. Set it defensively.
export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"

USER_UNIT="$HOME/.config/systemd/user/pitches.service"

if [[ ! -f "$USER_UNIT" ]]; then
  echo "missing user unit: $USER_UNIT" >&2
  exit 1
fi

# 1. Enable linger — allows user systemd services to survive logout + start
#    at boot. Root password required, ONE TIME only.
if loginctl show-user assistant --property=Linger 2>/dev/null | grep -q "Linger=yes"; then
  echo "linger already enabled for assistant, skipping"
else
  echo "enabling linger (root password required, ONE TIME only)..."
  su -c 'loginctl enable-linger assistant'
fi

# 2. If an /etc/systemd/system/pitches.service from a previous install.sh run
#    is active, stop + disable it first so ports don't conflict.
if [[ -f /etc/systemd/system/pitches.service ]]; then
  echo "system-level pitches.service exists — stopping + disabling it..."
  su -c 'systemctl disable --now pitches 2>/dev/null; rm -f /etc/systemd/system/pitches.service; systemctl daemon-reload'
fi

# 3. Stop the nohup instance (if any) so the user service can bind :3778.
echo "stopping nohup instance on :3778 (if any)..."
pkill -f "node pitches-server.js" 2>/dev/null || true
sleep 1

# 4. Enable + start the user service. No sudo needed beyond this point.
echo "enabling + starting user service..."
systemctl --user daemon-reload
systemctl --user enable --now pitches
sleep 2

# 5. Verify.
echo
echo "=== status ==="
systemctl --user status pitches --no-pager | head -10
echo
echo "=== port 3778 ==="
ss -ltn | grep 3778 || { echo "NOT LISTENING"; exit 1; }
echo
echo "=== external ==="
curl -sk -o /dev/null -w "pitch/1993/: %{http_code}\n" https://pitch.runatyr.games/1993/

echo
echo "done. manage with:"
echo "  systemctl --user restart pitches"
echo "  systemctl --user status pitches"
echo "  systemctl --user stop pitches"
echo "no sudo needed. ever."
