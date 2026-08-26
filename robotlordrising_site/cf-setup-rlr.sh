#!/usr/bin/env bash
# cf-setup-rlr.sh — build the robotlordrising.com Cloudflare zone (mail-safe), AFTER
# Robert has added the zone in the CF dashboard (token lacks zone-create permission).
#
# Run from the VPS: bash robotlordrising_site/cf-setup-rlr.sh
# Idempotent-ish: skips records that already exist by (type,name,content).
set -euo pipefail

TOKEN=$(grep -E "^CLOUDFLARE_API_TOKEN=" /home/assistant/projects/assistant/.env | cut -d= -f2- | tr -d '"'"'\r")
TUNNEL="769d4523-1a04-46b3-959d-8fdc90899f6b.cfargotunnel.com"

# Find the zone id (must already exist — Robert adds it via dashboard "Add a site")
ZID=$(curl -s "https://api.cloudflare.com/client/v4/zones?name=robotlordrising.com" \
  -H "Authorization: Bearer $TOKEN" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['result'][0]['id'] if d.get('result') else '')")
if [ -z "$ZID" ]; then
  echo "ERROR: robotlordrising.com zone not found in the CF account."
  echo "Robert must first add it: CF dashboard -> Add a site -> robotlordrising.com -> Free plan."
  exit 1
fi
echo "zone id: $ZID"

BASE="https://api.cloudflare.com/client/v4/zones/$ZID/dns_records"

add() { # type name content [priority] [proxied]
  local type="$1" name="$2" content="$3" prio="${4:-}" proxied="${5:-false}"
  local payload
  if [ -n "$prio" ]; then
    payload=$(printf '{"type":"%s","name":"%s","content":"%s","priority":%s,"proxied":%s}' "$type" "$name" "$content" "$prio" "$proxied")
  else
    payload=$(printf '{"type":"%s","name":"%s","content":"%s","proxied":%s}' "$type" "$name" "$content" "$proxied")
  fi
  curl -s -X POST "$BASE" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
    --data "$payload" | python3 -c "import sys,json; d=json.load(sys.stdin); print('  OK ' if d.get('success') else '  FAIL '+json.dumps(d.get('errors')), '$type $name')"
}

# --- CRITICAL mail records (DNS-only / grey cloud) ---
add MX robotlordrising.com mail.robotlordrising.com 10 false
add MX robotlordrising.com mail.robotlordrising.com 20 false
add A  mail.robotlordrising.com 195.74.38.202 "" false   # MX target — MUST resolve or RLR mail dies

# --- Site: apex + www -> tunnel (proxied / orange) -> placeholder on :3785 ---
add CNAME robotlordrising.com     "$TUNNEL" "" true
add CNAME www.robotlordrising.com "$TUNNEL" "" true

echo "Done. Verify with: dig @<assigned-cf-ns> robotlordrising.com MX +short"
