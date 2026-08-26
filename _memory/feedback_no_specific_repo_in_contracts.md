---
name: feedback_no_specific_repo_in_contracts
description: "Contracts use generic \"source repositories\"; never name a specific repo/branch unless the client specifically requests it"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 745f5972-f904-487b-b194-f39b7cb21d94
---

In subcontractor / client contracts, the access clause must stay **generic** — "access to needed documentation, planning tools and source repositories" — and must **never** name a specific repository or branch (e.g. a GitHub branch like `egypt/dlc-setup`) unless the client has specifically requested that the named repo be in the contract.

**Why:** a hard-coded repo/branch name is volatile operational detail that goes stale (the K2C subs named `twocrowns/next-dlc`, which was wrong — the real branch was `egypt/dlc-setup`), leaving an error sitting in a doc heading for signature. The generic wording conveys the same obligation with zero maintenance burden. (On K2C, Imi's and Oskar's contracts were already generic and never had the problem; the other four had to be corrected then genericized — 2026-06-04, Robert direction.)

**How to apply:** when drafting or reviewing any contract access/equipment clause, strip named repos/branches/servers/tool-versions and use the generic form. Internal docs (CLAUDE.md, project plans, tech-risk notes) may still reference the specific branch — this rule is for **client-facing contracts** only. Relates to [[feedback_proofread_round_before_esignature]] and [[feedback_share_for_signature]].
