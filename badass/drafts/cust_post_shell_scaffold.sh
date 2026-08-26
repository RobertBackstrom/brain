#!/usr/bin/env bash
# CUST post-shell scaffold — runs once Nancy confirms project exists.
# Creates: 14 Components, 2 Fix Versions, 3 boards.
# Idempotency: skips Components/Versions that already exist by name.

set -euo pipefail
CREDS=$(jq -r '.email + ":" + .apiToken' /home/assistant/.claude/.atlassian-credentials-badass.json)
SITE="https://badass-studios.atlassian.net"
PROJECT_KEY="CUST"
LEAD_ID="6061d442b30f0d007010a907"  # Robert

api() { curl -sS -u "$CREDS" -H "Accept: application/json" -H "Content-Type: application/json" "$@"; }

# --- 1. Fetch project ID ---
PROJECT_ID=$(api "$SITE/rest/api/3/project/$PROJECT_KEY" | jq -r '.id')
echo "Project $PROJECT_KEY id=$PROJECT_ID"

# --- 2. Components ---
COMPONENTS=(
  # Client components
  "E1 Series|Client engagement: UIM E1 Championship (electric powerboat racing). 8-venue 2026 season."
  "Show Jumping|Client engagement: Show Jumping / PJL. Migrated from SJ project."
  "F1 VR|Client engagement: F1 VR. Migrated from F1 project."
  "Blackbook|Client engagement: Blackbook Motor Sports AR app."
  "BMS|Client engagement: Blackbook Motor Sports (migrated from BMS project, may close from here)."
  # Project-type components (per #6 decision)
  "AR Live Broadcast|Project type: AR live broadcast overlays. Includes Graphics + Live GP (folded in)."
  "VR Live Broadcast|Project type: VR live broadcast experience."
  "AR App|Project type: AR mobile app, including Vision Pro variant."
  "Environment Production|Project type: 3D environment for digital twins."
  "Course Explainers|Project type: pre-race cinematic explainers."
  "UEFN|Project type: Fortnite Creative / UEFN island."
  "Steam-Console|Project type: Steam + console game build."
  "Format Explainer|Project type: race-wide format-explainer videos (was E12026-185/186/421)."
  # Templates bucket
  "TEMPLATES|Hidden bucket for template Epics. Not worked directly; cloned via Jira Automation."
)

# Fetch existing components
EXISTING=$(api "$SITE/rest/api/3/project/$PROJECT_KEY/components" | jq -r '.[].name')

for c in "${COMPONENTS[@]}"; do
  NAME="${c%%|*}"
  DESC="${c#*|}"
  if echo "$EXISTING" | grep -qFx "$NAME"; then
    echo "  skip Component (exists): $NAME"
    continue
  fi
  api -X POST "$SITE/rest/api/3/component" -d "{
    \"name\": $(jq -Rn --arg v "$NAME" '$v'),
    \"description\": $(jq -Rn --arg v "$DESC" '$v'),
    \"project\": \"$PROJECT_KEY\",
    \"leadAccountId\": \"$LEAD_ID\",
    \"assigneeType\": \"PROJECT_LEAD\"
  }" | jq -r '"  created Component: " + .name'
done

# --- 3. Fix Versions ---
VERSIONS=(
  "E1 2025 S2|Historical Season 2 (Jeddah). Backfill on legacy Epics."
  "E1 2026 S3|Current Season 3 (Como done, Dubrovnik in flight, Monaco/Lagos/Miami/Bahamas/TBC upcoming)."
)
EXISTING_V=$(api "$SITE/rest/api/3/project/$PROJECT_KEY/versions" | jq -r '.[].name')
for v in "${VERSIONS[@]}"; do
  NAME="${v%%|*}"
  DESC="${v#*|}"
  if echo "$EXISTING_V" | grep -qFx "$NAME"; then
    echo "  skip Version (exists): $NAME"
    continue
  fi
  api -X POST "$SITE/rest/api/3/version" -d "{
    \"name\": $(jq -Rn --arg v "$NAME" '$v'),
    \"description\": $(jq -Rn --arg v "$DESC" '$v'),
    \"project\": \"$PROJECT_KEY\",
    \"released\": false,
    \"archived\": false
  }" | jq -r '"  created Version: " + .name'
done

# --- 4. Filters + Boards ---
# We need a filter per board (Jira boards are filter-backed). Each filter shared with the project's group.
mkfilter() {
  local NAME="$1" JQL="$2" DESC="$3"
  api -X POST "$SITE/rest/api/3/filter" -d "{
    \"name\": $(jq -Rn --arg v "$NAME" '$v'),
    \"description\": $(jq -Rn --arg v "$DESC" '$v'),
    \"jql\": $(jq -Rn --arg v "$JQL" '$v')
  }" | jq -r '.id'
}

# Board "CUST - All" : all live work, excludes TEMPLATES component
F_ALL=$(mkfilter "CUST - All Work" \
  "project = CUST AND component != TEMPLATES ORDER BY Rank ASC" \
  "All active CUST work, excluding the TEMPLATES bucket.")
echo "  created Filter CUST-All id=$F_ALL"

# Board "CUST - Per-Client" - need to use a saved filter that groups by Client component
F_PERCLIENT=$(mkfilter "CUST - Per Client" \
  "project = CUST AND component in (\"E1 Series\", \"Show Jumping\", \"F1 VR\", \"Blackbook\", \"BMS\") ORDER BY component, Rank ASC" \
  "Active CUST work grouped by Client component.")
echo "  created Filter CUST-Per-Client id=$F_PERCLIENT"

# Board "CUST - Per-Location" - location filter via cf - placeholder, will populate once cf id known
F_PERLOC=$(mkfilter "CUST - Per Location (Dubrovnik pilot)" \
  "project = CUST AND \"Location\" = Dubrovnik ORDER BY Rank ASC" \
  "Pilot board: CUST work scoped to Dubrovnik. Per-location boards cloned from this once template engine is live.")
echo "  created Filter CUST-Per-Location id=$F_PERLOC"

# Create boards via agile API
mkboard() {
  local NAME="$1" FID="$2" TYPE="${3:-scrum}"
  api -X POST "$SITE/rest/agile/1.0/board" -d "{
    \"name\": $(jq -Rn --arg v "$NAME" '$v'),
    \"type\": \"$TYPE\",
    \"filterId\": $FID,
    \"location\": {\"type\": \"project\", \"projectKeyOrId\": \"$PROJECT_KEY\"}
  }" | jq -r '"  created Board: " + .name + " (id=" + (.id|tostring) + ")"'
}

mkboard "CUST - All" "$F_ALL" "scrum"
mkboard "CUST - Per Client" "$F_PERCLIENT" "kanban"
mkboard "CUST - Per Location (Dubrovnik pilot)" "$F_PERLOC" "kanban"

echo ""
echo "=== Scaffold complete ==="
echo "Visit: $SITE/jira/software/projects/$PROJECT_KEY"
