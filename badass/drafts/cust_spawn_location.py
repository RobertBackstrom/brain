#!/usr/bin/env python3
"""CUST template engine — spawn a Location Epic from a template.

Clones a TEMPLATE: <type> Epic + its Stories into a new Location Epic,
with Client component, Location field, and Fix Version pre-set.

Usage:
  cust_spawn_location.py --template "AR Live Broadcast" --location Monaco
  cust_spawn_location.py --template "AR Live Broadcast" --location Monaco \\
      --client "E1 Series" --fixversion "E1 2026 S3" --epic-name "AR Live Broadcast - Monaco"
  cust_spawn_location.py ... --dry-run

This is the script-based engine. The native Jira Automation equivalent is
specced in cust_automation_rule_spec.md for Nancy to build in the UI.
"""
import json, base64, urllib.request, urllib.parse, urllib.error, argparse, sys

SITE = "https://badass-studios.atlassian.net"
with open("/home/assistant/.claude/.atlassian-credentials-badass.json") as f:
    cr = json.load(f)
AUTH = base64.b64encode(f"{cr['email']}:{cr['apiToken']}".encode()).decode()

COMP = {
    "TEMPLATES": "10158", "AR Live Broadcast": "10150", "VR Live Broadcast": "10151",
    "AR App": "10152", "Environment Production": "10153", "Course Explainers": "10154",
    "UEFN": "10155", "Steam-Console": "10156", "Format Explainer": "10157",
    "XR Headset": "10191",
    "E1 Series": "10145", "Show Jumping": "10146", "F1 VR": "10147",
    "Blackbook": "10148", "BMS": "10149",
}
EPIC, STORY = "10000", "10004"
F_LOCATION, F_TSHIRT, F_TEMPLATE_SOURCE = "customfield_10231", "customfield_10232", "customfield_10233"

def api(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{SITE}{path}", data=data, method=method)
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
    return {"type": "doc", "version": 1,
            "content": [{"type": "paragraph", "content": [{"type": "text", "text": text}]}]}

def search(jql, fields="summary"):
    q = urllib.parse.quote(jql)
    out, token = [], None
    while True:
        path = f"/rest/api/3/search/jql?jql={q}&fields={fields}&maxResults=100"
        if token:
            path += f"&nextPageToken={token}"
        r = api("GET", path)
        out += r.get("issues", [])
        token = r.get("nextPageToken")
        if not token:
            break
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True, help="Template type name, e.g. 'AR Live Broadcast'")
    ap.add_argument("--location", required=True, help="Location field value, e.g. Monaco")
    ap.add_argument("--client", default="E1 Series", help="Client component (default E1 Series)")
    ap.add_argument("--fixversion", default="E1 2026 S3", help="Fix Version name")
    ap.add_argument("--epic-name", default=None, help="Override new Epic summary")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.template not in COMP:
        sys.exit(f"Unknown template '{a.template}'. Known: {sorted(COMP)}")
    if a.client not in COMP:
        sys.exit(f"Unknown client component '{a.client}'.")

    # 1. Find the template Epic
    tmpl = [i for i in search(f'project = CUST AND issuetype = Epic AND summary ~ "TEMPLATE: {a.template}"')
            if i["fields"]["summary"] == f"TEMPLATE: {a.template}"]
    if not tmpl:
        sys.exit(f"Template Epic 'TEMPLATE: {a.template}' not found.")
    tmpl_key = tmpl[0]["key"]

    # 2. Fetch template child Stories (preserve Rank order)
    kids = search(f'parent = {tmpl_key} ORDER BY Rank ASC', fields=f"summary,{F_TSHIRT}")
    epic_name = a.epic_name or f"{a.template} - {a.location}"
    print(f"Template {tmpl_key} '{a.template}' -> new Epic '{epic_name}' "
          f"[{a.client} / {a.location} / {a.fixversion}], {len(kids)} stories")
    if a.dry_run:
        for k in kids:
            print(f"  would clone: {k['fields']['summary']}")
        return

    # 3. Resolve fix version id
    versions = api("GET", "/rest/api/3/project/CUST/versions")
    vid = next((v["id"] for v in versions if v["name"] == a.fixversion), None)
    if vid is None:
        sys.exit(f"Fix Version '{a.fixversion}' not found on CUST.")

    # 4. Create the Location Epic
    comps = [{"id": COMP[a.client]}, {"id": COMP[a.template]}]
    epic_body = {"fields": {
        "project": {"key": "CUST"},
        "issuetype": {"id": EPIC},
        "summary": epic_name,
        "description": adf(f"Location Epic spawned from {tmpl_key} (TEMPLATE: {a.template}). "
                           f"Client {a.client}, Location {a.location}, {a.fixversion}."),
        "components": comps,
        "fixVersions": [{"id": vid}],
        "labels": [a.location.replace(" ", "")],  # convention: location name as a label (sortable / quick-filter)
        F_LOCATION: {"value": a.location},
        F_TEMPLATE_SOURCE: {"value": a.template},
    }}
    r = api("POST", "/rest/api/3/issue", epic_body)
    if "_error" in r:
        sys.exit(f"Epic create failed: {r['_error']} {r['_body'][:400]}")
    epic_key = r["key"]
    print(f"  created Epic {epic_key}")

    # 5. Clone each Story
    made = 0
    for k in kids:
        f = k["fields"]
        sbody = {"fields": {
            "project": {"key": "CUST"},
            "issuetype": {"id": STORY},
            "summary": f["summary"],
            "parent": {"key": epic_key},
            "components": comps,
            "fixVersions": [{"id": vid}],
            "labels": [a.location.replace(" ", "")],  # convention: location name as a label
            F_LOCATION: {"value": a.location},
        }}
        if f.get(F_TSHIRT):  # carry T-shirt size if the template has one
            sbody["fields"][F_TSHIRT] = {"value": f[F_TSHIRT]["value"]}
        cr_ = api("POST", "/rest/api/3/issue", sbody)
        if "_error" in cr_:
            print(f"    FAIL '{f['summary']}': {cr_['_error']} {cr_['_body'][:200]}")
        else:
            made += 1
            print(f"    + {cr_['key']}  {f['summary']}")
    print(f"\nDone: {epic_key} + {made}/{len(kids)} stories. "
          f"{SITE}/browse/{epic_key}")

if __name__ == "__main__":
    main()
