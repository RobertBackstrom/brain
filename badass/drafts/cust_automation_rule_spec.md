# CUST template engine — native Jira Automation rule spec

For Nancy to build in the Jira UI. This is the no-touch version of the template engine:
create a Location Epic, the rule clones the right template's Stories into it automatically.

Until this rule exists, the same job is done by the script `cust_spawn_location.py` (PM runs
it on request). The script and the rule are interchangeable - the script is the fallback and
the rule is the goal.

---

## What it does

When anyone creates an Epic in CUST and sets the `Template Source` field, the rule looks up
that template's canonical Stories and clones them into the new Epic - with Components,
Location, and Fix Version copied down from the Epic.

PM intake becomes: create Epic, set 4 fields (Component=Client, Component=Type, Location,
Fix Version, Template Source), save. The ~4-20 Stories appear automatically.

---

## Build steps

**Project Settings → Automation → Create rule.**

### 1. Trigger
- **Work item created**

### 2. Condition — "Issue fields condition"
- Field: **Issue Type**, condition: **equals**, value: **Epic**

### 3. Condition — "Issue fields condition"
- Field: **Template Source**, condition: **is not empty**

### 4. Condition — "Issue fields condition" (safety net)
- Field: **Summary**, condition: **does not start with**, value: **TEMPLATE:**
- (Stops the rule firing if someone ever edits/recreates a template Epic.)

### 5. Action — "Lookup work items"
- JQL:
  ```
  project = CUST AND component = TEMPLATES AND issuetype = Story AND "Template Source" = "{{triggerIssue.Template Source}}"
  ```
- This returns the template Stories for the matching type into `{{lookupIssues}}`.

### 6. Branch — "For each: Results of the lookup work items action"
Inside the branch, add one action:

- **Action — "Create work item"**
  - Project: **CUST**
  - Issue type: **Story**
  - Summary: `{{lookupIssue.summary}}`
  - Parent: `{{triggerIssue.key}}`
  - Components: `{{triggerIssue.components}}`
  - Fix versions: `{{triggerIssue.fixVersions}}`
  - Location: `{{triggerIssue.Location}}`
  - T-shirt Size: `{{lookupIssue.T-shirt Size}}`  *(copies the template's size if one is set)*

### 7. Name + turn on
- Name: **CUST: Spawn template Stories on new Location Epic**
- Scope: **Single project — CUST**
- Turn the rule **ON**.

---

## Test it (do this once, like the PM pilot)

1. Create an Epic in CUST: summary "RULE TEST - delete me", Component = E1 Series + Course
   Explainers, Location = TBC, Fix Version = E1 2026 S3, **Template Source = Course Explainers**.
2. Save. Within ~30 seconds, 4 Stories should appear under it (the Course Explainers checklist).
3. Check one Story carries Location = TBC and both Components.
4. Delete the test Epic + its 4 Stories once confirmed.

---

## Notes

- **Plan limits:** BADASS is on the Jira Standard trial (1,700 automation executions/month, or
  unlimited for single-project rules). One spawn = 1 execution + the branch iterations. Comfortable
  headroom; revisit only if the plan drops back to Free (100/month).
- **Rule actor:** leave as the default automation actor, or set to a service/admin account so
  created Stories aren't all attributed to a person.
- **If the lookup returns nothing:** check the template Stories carry the `Template Source` field
  (they were bulk-set 2026-05-20). New template Stories added later must also carry it, or the
  rule won't see them. The script `cust_seed_templates.py` and any future template edits should
  keep that field populated on Stories, not just Epics.
- **Why Stories carry Template Source:** lets the lookup be a single flat JQL. Without it the rule
  needs two chained lookups (find template Epic, then its children) - workable but more brittle.
