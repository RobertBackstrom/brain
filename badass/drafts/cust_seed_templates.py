#!/usr/bin/env python3
"""CUST step (c) — seed the 8 template Epics + canonical Stories under TEMPLATES.

Idempotent-ish: checks for an existing "TEMPLATE: <name>" Epic before creating.
Children are only added when the Epic is freshly created (avoids dupes on re-run).
"""
import json, base64, urllib.request, urllib.error, sys

SITE = "https://badass-studios.atlassian.net"
with open("/home/assistant/.claude/.atlassian-credentials-badass.json") as f:
    cr = json.load(f)
AUTH = base64.b64encode(f"{cr['email']}:{cr['apiToken']}".encode()).decode()

COMP = {  # component name -> id
    "TEMPLATES": "10158", "AR Live Broadcast": "10150", "VR Live Broadcast": "10151",
    "AR App": "10152", "Environment Production": "10153", "Course Explainers": "10154",
    "UEFN": "10155", "Steam-Console": "10156", "Format Explainer": "10157",
}
EPIC, STORY = "10000", "10004"
TEMPLATE_SOURCE_FIELD = "customfield_10233"

def api(method, path, body=None):
    url = f"{SITE}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Basic {AUTH}")
    req.add_header("Accept", "application/json")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            txt = r.read().decode()
            return json.loads(txt) if txt else {}
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read().decode()}

def adf(text):
    return {"type": "doc", "version": 1, "content": [
        {"type": "paragraph", "content": [{"type": "text", "text": text}]}]}

def find_epic(summary):
    jql = f'project = CUST AND issuetype = Epic AND summary ~ "{summary}"'
    r = api("GET", f"/rest/api/3/search/jql?jql={urllib.parse.quote(jql)}&fields=summary")
    for i in r.get("issues", []):
        if i["fields"]["summary"] == summary:
            return i["key"]
    return None

# template name -> (component, content owner, seed source, [child story summaries])
TEMPLATES = {
    "AR Live Broadcast": ("Alex", "E12026-542", [
        "Import Artist Sub-Levels", "Configure StreamDeck for AR Broadcast",
        "Test AR Broadcast Actors with Simulated Data", "TrackMapper Camera Pre-Positioning",
        "Visual Quality Assessment (Fake Video-In)", "Blackmagic Card & SDI Output Test",
        "Camera Rig & B20 Assembly", "SDI & Video Format Verification (On-Site)",
        "Mo-Sys Lens Tweaking", "Local Fibre Test", "LiveLink & Camera Tracking Setup",
        "Al Kamel Data Feed & WebSocket Relay", "SunTracker - Broadcast Room Config",
        "SunTracker - Hoist Raised Setup (repeat daily)", "Camera GPS Positioning",
        "AR Calibration - UE Component Setup", "AR Calibration - Solve & Save",
        "Import Sponsors Level & Final Spline Tweak", "Pre-Live Sign-Offs",
        "Live Broadcast Operations",
    ]),
    "VR Live Broadcast": ("John", "E12026-657", [
        "VR Broadcast Default Camera Placements", "VR Broadcast Default Camera Rail Placements",
        "VR Broadcast Default Event Specific Camera and Rail Placement",
        "VR Broadcast Water Object Buoyancy Setup", "VR Broadcast Stream Deck Control Setup",
        "VR Broadcast Nameplate Data Verification", "VR Broadcast DT_Teams Update",
        "VR Broadcast Buoy and Track Placement via KMZ",
        "VR Broadcast Finalized Camera Placements", "VR Broadcast Finalized Camera Tracks",
        "VR Broadcast Finalized Event Specific Camera and Tracks",
        "VR Broadcast Finalized Data Panel", "Hitbox based data setter",
        "Update Long/Short Lap to utilize hitbox zones",
        "Starting Lap", "Normal Lap", "Long/Short Lap",
    ]),
    "AR App": ("Ben", "E12026-279 / E12026-312", [
        "Enhanced Boat Viewer", "Environment implementation", "UI update",
        "Align with E1 vision for the AR app", "Manipulation UI rework",
        "Vision Pro app build (V0.1.0)",
    ]),
    "Environment Production": ("Marco", "E12026-677", [
        "Environment Preproduction", "Environment Production",
        "AR Environment Production", "Environment Optimization",
    ]),
    "Course Explainers": ("Jake", "E12026-396", [
        "Confirm and set up Boat Pathing/Rails",
        "Broadcast Cinematic Environment Enhancement",
        "Cinematic Lighting and Atmosphere Setup",
        "Course Explainer Render Setup and Output",
    ]),
    "UEFN": ("TBD", "E12026-213", [
        "Publish island at least 5 days before event",
        "Check the 7 edits / 7 days edit rule and implement on time",
    ]),
    "Steam-Console": ("Sezar", "E12026-682", [
        "Import Environment to Game",
    ]),
    "Format Explainer": ("TBD (Jake / Marketing)", "E12026-185 / -186 / -421", []),
}

for name, (owner, src, children) in TEMPLATES.items():
    summary = f"TEMPLATE: {name}"
    existing = find_epic(summary)
    if existing:
        print(f"  skip Epic (exists): {summary} = {existing}")
        continue
    desc = (f"TEMPLATE EPIC - do not work directly. Canonical {name} checklist, "
            f"cloned into each new Location Epic via Jira Automation once the rule is wired. "
            f"Content owner: {owner} (reviews + resizes after each race week). "
            f"Seed source: {src}. T-shirt sizes intentionally blank - owner sets them in the "
            f"first sizing pass.")
    body = {"fields": {
        "project": {"key": "CUST"},
        "issuetype": {"id": EPIC},
        "summary": summary,
        "description": adf(desc),
        "components": [{"id": COMP["TEMPLATES"]}, {"id": COMP[name]}],
        TEMPLATE_SOURCE_FIELD: {"value": name},
    }}
    r = api("POST", "/rest/api/3/issue", body)
    if "_error" in r:
        print(f"  FAIL Epic {summary}: {r['_error']} {r['_body'][:300]}")
        continue
    epic_key = r["key"]
    print(f"  created Epic: {summary} = {epic_key} ({len(children)} children)")
    for child in children:
        cbody = {"fields": {
            "project": {"key": "CUST"},
            "issuetype": {"id": STORY},
            "summary": child,
            "parent": {"key": epic_key},
            "components": [{"id": COMP["TEMPLATES"]}, {"id": COMP[name]}],
        }}
        cr_ = api("POST", "/rest/api/3/issue", cbody)
        if "_error" in cr_:
            print(f"      FAIL child '{child}': {cr_['_error']} {cr_['_body'][:200]}")
        else:
            print(f"      + {cr_['key']}  {child}")

print("\n=== Template seed complete ===")
