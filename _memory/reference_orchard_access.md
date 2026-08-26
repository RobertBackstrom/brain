---
name: reference_orchard_access
description: VPS has headless API access to The Orchard (CZP music distribution) via orchard-api.js
metadata: 
  node_type: memory
  type: reference
  originSessionId: 599156e2-cc4f-484e-b9ff-6e708011a0c6
---

The VPS has durable, self-refreshing **headless API access to The Orchard Workstation** (CZP music-distribution account), set up 2026-06-05. Shared by the Assistant, Analytics, and CorpBot agents.

- **Use it:** `const orchard = require('./assistant/orchard-api')` → `orchard.allProducts()`, `orchard.searchCatalog()`, `orchard.gql(op, query, vars)`. CLI: `node assistant/orchard-api.js catalog|find "<artist>"`. Token mgmt: `node assistant/orchard-auth.js token|status`.
- **How it works:** VPS owns its own Auth0 (`login.distroauth.com`) refresh-token grant, independent of Robert's browser; mints access tokens with no Turnstile. GraphQL gateway = `ows-grass.theorchard.io/graphql-gateway/graphql`, which needs a per-call `grass_token` from `/login/startsession` (handled in the client).
- **Login is behind Cloudflare Turnstile** so interactive headless login is impossible — never try to script the login form. If the refresh grant ever dies (`invalid_grant`), re-auth via `orchard-auth.js authurl` + `exchange` (Robert opens the URL once).
- **Takedowns** at The Orchard are done by emailing UPCs to clientservices@theorchard.com (not via a known API mutation).

Full guide: `assistant/ORCHARD_ACCESS.md`. Secrets: `orchard.workstation-oauth` / `orchard.workstation-login` in [[feedback_secrets_registry]]. Account = personal Gmail login, profile 56318 (LabelProfile/Administrator).
