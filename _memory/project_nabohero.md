---
name: project_nabohero
description: "Nabohero — client services-marketplace build (TippTapp-style); phase 1 = app-level auth + personal-data DB (GDPR), NOT CF Access."
metadata: 
  node_type: memory
  type: project
  originSessionId: 327ca70c-5888-41f3-af81-150ccc678524
---

**Nabohero** is a new client website build — a Scandinavian two-sided **services marketplace** ("nabo" = neighbour; TippTapp / Nextdoor-services category). Public self-signup, stores personal data, later a buy/sell-services front end. **Front-end page live at https://www.nabohero.com/ but no signup/data layer yet** — auth + backend is greenfield. **Stack confirmed: Supabase** (Postgres+Auth+RLS) with **Swedish BankID** sign-in (no native Supabase provider → OIDC broker like Criipto/Signicat/ZignSec/Scrive or server-side RP flow; watch the RP-agreement holder + personnummer/data-minimisation, Lawyer's call). Prefix `nab` (registered in `config.json`). Project home `nabohero/` (CLAUDE.md + START_PROMPT.md + output_log.md). Kickoff ticket `nab-001` (auth + personal-data foundation, phase 1).

Owner: DevOps agent (run via `nabohero/START_PROMPT.md`, model opus, Plan-Confirm-Execute first). Lawyer consulted on the GDPR data model.

Key architecture call: grew out of the [[reference_runatyr_domains]] `internal.aurorapunks.com` portal, which uses **Cloudflare Access** (SSO for known invited users, no user DB). Nabohero is the opposite — public self-signup + personal data — so it needs an **app-level auth stack** (recommended: **Supabase** = Postgres + Auth + Row-Level Security), not CF Access. The transferable piece is the *pattern* (verified identity → ownership → scoped access, fail closed), not the mechanism. Deal structure TBD (confirm before billing). See [[feedback_security_defaults]].
