---
name: Jira "assignable" ≠ "user missing"
description: When a Jira project rejects an assignee, default to "permission scheme excludes them", not "create a new user". Test before recommending admin actions.
type: feedback
originSessionId: 10c6d9ff-1c85-4f0d-9f5f-14bbf29f2fc6
---
When a Jira project's permission scheme excludes a user from being assignable (or `lookupJiraAccountId` doesn't find them by display name), do NOT jump to "create a new placeholder user". The user may already exist in the org directory and just needs to be added to the project's role / permission scheme.

**Why:** On 2026-04-29, while clearing the BADASS backlog, I told Robert he needed to create an "AP Dev" placeholder user in Atlassian Admin to handle 11 BX issues that referenced "Gaizka Pueyo (needs BX project access)" in their descriptions. Robert pushed back ("the BADASS PM have had access in their Jira"). On retest: Gaizka's account *was* active in the directory (`712020:07f771b9-...`) — he just wasn't assignable in the BX project specifically. The previous Claude session interpreted the migration error as missing user, when it was actually a project-scoped permission exclusion. Robert's pushback caught the misdiagnosis.

**How to apply:**
1. Before recommending "create a new user" for a Jira project: run `lookupJiraAccountId` AND check `project = X AND assignee was "displayName"` AND fetch a known issue in another project where they were assigned to find their accountId.
2. If accountId exists: try `editJiraIssue` with that accountId. If the error is `"User '...' cannot be assigned issues"` → it's a permission scheme exclusion, not a missing user.
3. The fix is `Project settings → People → add user to assignable role`, NOT `Atlassian Admin → Users → create new user`.
4. When in doubt: ask before sending Robert into admin UI work that may not be needed.
