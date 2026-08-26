---
name: badass-jira-connection-details
description: "Atlassian cloud ID, project keys, and site URL for BADASS Studios Jira instance"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 401f4055-5048-4da4-b947-f8015c62c96d
---

- **Site:** badass-studios.atlassian.net
- **Cloud ID:** db8f98b2-4e5a-4d37-bba5-787aa3219f58
- **Projects (live, verified 2026-07-08 — 7 total):** BX (BADASS XR Platform), CUST (BADASS Customisation — consolidates the old per-client/season projects), MO (Master Overview — product_discovery/JPD), OPS (Badass Internal Ops), PE (Platform Enhancement), P4TEST (Perforce Test), SJ (PJL - Show Jumping). The old E12026/BMS/PFL/IUB projects were migrated into **CUST** (2026-05 restructure) and no longer exist standalone.

**How to apply:** Use the cloud ID when calling Atlassian MCP tools. **The generic `mcp__atlassian-jira__*` MCP resolves to the K2C/KAN site — for BADASS reads/writes use the Rovo MCP with the explicit cloudId above** (or the badass REST token). Client/season slicing now lives inside CUST via components + labels, not separate projects.
