# Nabohero — CLAUDE.md

## Engagement
- **Type:** Client website build (external). Robert = product/biz-dev + delivery lead.
- **What it is:** A two-sided **services marketplace** ("nabo" = neighbour). Users sign up, a profile with **personal data** is stored, and a front end lets them **buy and sell services** (TippTapp / Nextdoor-services / Neighborly category). Scandinavian market.
- **DB prefix:** `nab`
- **Status:** Kickoff (2026-07-15). Phase 1 = auth + personal-data foundation.
- **Agent owner:** DevOps (build), with Lawyer consulted on the GDPR/personal-data layer.
- **Live site:** https://www.nabohero.com/ — a front-end page is live but **there is no signup / data layer behind it yet**. The auth + backend is genuinely greenfield; inspect the page only to match the existing front-end stack/host.
- **Stack: Supabase — CONFIRMED** (Robert, 2026-07-15). Postgres + Auth + RLS.
- **Sign-in: Swedish BankID required** (alongside/instead of email+password — confirm the mix). BankID has no native Supabase provider; integrate via an OIDC **broker** (Criipto / Signicat / ZignSec / Scrive) or a server-side BankID flow that mints Supabase sessions. Two dependencies: (1) a BankID **relying-party agreement** held by a legal entity — procurement lead time, and *who is the RP* (client vs. an AP/Runatyr entity) is open; (2) BankID returns the **personnummer** — store an opaque subject id, not the raw number, unless there's a documented lawful basis. Lawyer owns that call.
- **Deal structure:** TBD — confirm with Robert (retainer / flat-fee / rev-share) before logging billable time. Bill to `projects/time_log.csv` once confirmed.

## Origin
Grew out of the `internal.aurorapunks.com` portal build (2026-07-15). That portal taught the **transferable pattern** — verified identity → role → scoped access, failing closed — but it uses Cloudflare Access (SSO for a *known, invited* set of people, no user DB, no passwords). Nabohero is the **opposite shape**: public self-signup by strangers, storing personal data. That needs a real application auth stack, not CF Access. See `START_PROMPT.md` for the full brief.

## Hard constraints (carry into every task)
1. **Personal data = GDPR from day one.** Scandinavian users. Consent, lawful basis, data-at-rest handling, right-to-erasure, minimal collection. Loop in the Lawyer agent for the data model + privacy policy. Per [[feedback_security_defaults]].
2. **Auth is app-level, not CF Access.** Self-serve signup into a user store on **Supabase** (confirmed) with **Swedish BankID** sign-in via an OIDC broker or server-side flow. RLS maps cleanly onto per-user marketplace data. See the Engagement block for the BankID integration + RP/personnummer dependencies.
3. **Plan-Confirm-Execute.** Any spawned agent restates the goal + asks 1-3 scoping questions before building. No blank-slate drafting.
4. **The front-end page is live but the auth/backend is greenfield** — no signup or data layer exists yet at https://www.nabohero.com/. Match the existing front-end stack/host when you inspect the page; build the auth + DB fresh. Production host may be the client's own infra; VPS is the runtime only for what we host. Don't assume Robert's laptop.

## Scope phasing
- **Phase 1 (this kickoff, `nab-001`):** Sign-in + personal-data DB foundation. Auth flow, user/profile schema, GDPR-compliant data model, session handling. No marketplace features yet.
- **Phase 2:** Front end — service listings, buy/sell flow, search, messaging.
- **Phase 3:** Payments, reviews/trust, disputes.

## Conventions
- Deliverables + design docs live here (`nabohero/`), drafts in `drafts/`.
- Log significant deliveries to `output_log.md` before committing.
- Code repo: GitHub is source of truth (create a private repo when the stack is confirmed).
