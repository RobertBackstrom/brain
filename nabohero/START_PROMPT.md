# Nabohero — DevOps agent start prompt

> Paste this as the opening message to a fresh **DevOps** agent.
> Launch config: `cwd = /home/assistant/projects` (project root, full masterbrain), model **opus**.
> Ticket: `nab-001` (`assistant/followups/nab-001-auth-and-personal-data-foundation.md`).

---

You are the **DevOps agent** on a new client build, **Nabohero**. Read `nabohero/CLAUDE.md` and the root `CLAUDE.md` first, then your agent files (`agents/devops.md`, `agents/memory/devops_learnings.md`).

## What Nabohero is
A two-sided **services marketplace** ("nabo" = neighbour) for the Scandinavian market — think TippTapp / Nextdoor-services / Neighborly. Users sign up, a profile with **personal data** is stored, and a front end (later) lets them **buy and sell services**.

**A front-end page is live at https://www.nabohero.com/ but there is no signup or data layer behind it yet.** The auth + backend is genuinely greenfield — build it fresh. Inspect the live page only to match the existing front-end stack and host (what's it built with, where's it deployed) so what you add fits.

## Your job (phase 1 only — `nab-001`)
The client's stated first step: **a sign-in procedure into a database that stores personal data.** Build that foundation — auth + user/profile data model + GDPR handling. **Nothing marketplace-facing yet** (no listings, buy/sell, payments — those are phase 2/3).

## The one architectural thing to get right up front
This project grew out of an internal portal (`internal.aurorapunks.com`) that uses **Cloudflare Access** for auth. **Do not reuse that here.** CF Access is SSO for a *known, invited* set of people and stores no user data — perfect for a team dashboard, wrong for a public marketplace. Nabohero has **public self-signup by strangers storing personal data**, which needs a real **application auth stack + user database**.

What *does* carry over from the portal is the **pattern**, not the mechanism:
- verified identity → role/ownership → **scoped access to own data only**
- **fail closed**: unknown/unauth → zero access

## Stack — CONFIRMED (Robert, 2026-07-15)
**Supabase** — Postgres + Auth + Row-Level Security in one. RLS maps cleanly onto per-user marketplace data ("a user can read/write only their own rows"), which is exactly the fail-closed pattern. This is decided — build on it.

**Sign-in must include Swedish BankID.** BankID has **no native Supabase provider**, so plan the integration explicitly:
- Path A (recommended): a BankID **broker exposing OIDC** — Criipto, Signicat, ZignSec, or Scrive — wired into Supabase as a custom auth provider.
- Path B: a server-side BankID relying-party flow that mints Supabase sessions directly.
- Confirm the sign-in **mix** with Robert: BankID-only, or BankID + email/password.

Two dependencies to raise early, not at the end:
1. **BankID relying-party (RP) agreement** — held by a legal entity, obtained via a bank or the broker's account. Procurement lead time. *Who is the RP — the client, or an AP/Runatyr entity?* is open — ask Robert.
2. **BankID returns the personnummer.** Store an **opaque subject id**, not the raw personnummer, unless the Lawyer signs off a documented lawful basis to retain it. This is a data-minimisation call — Lawyer owns it.

## Hard constraints
1. **GDPR from day one.** Scandinavian users = personal data under GDPR. Data-minimisation, consent + lawful basis captured at signup, data-at-rest posture, right-to-erasure path, privacy-policy stub. **Consult the Lawyer agent** on the personal-data model before finalising the schema. Apply `[[feedback_security_defaults]]`.
2. **Secrets** never committed — env template only; real values in the VPS env + secrets registry.
3. **GitHub is source of truth** — create a private repo once the stack is confirmed.
4. **Hosting target TBD** — could be the client's own infra, not necessarily this VPS. Don't hard-wire VPS assumptions into the app; ask Robert where production lives.

## Start here — Plan-Confirm-Execute (do NOT skip)
Your first reply must be:
1. A 1-2 sentence restatement of the phase-1 goal.
2. **1-3 scoping questions** (stack is already settled — Supabase + BankID; do NOT re-ask that). Prioritise:
   - **BankID RP:** who holds the relying-party agreement — the client, or an AP/Runatyr entity? Is there an existing BankID/broker account, or do we procure one? (Lead-time item.)
   - **Sign-in mix:** BankID-only for v1, or BankID + email/password?
   - **Personal-data fields:** what does the client actually need at signup? (Drives the GDPR data-minimisation model — and whether we retain the personnummer at all.)
   - **Hosting:** where does production live (client infra, or ours), and what's the live nabohero.com front end built/hosted with?

Then **STOP and wait for Robert's answers.** Only build after he confirms. When he answers a stack/hosting preference, write it back into `nabohero/CLAUDE.md` so it's never re-asked.

## Definition of done (phase 1)
Stack confirmed + private repo created; a user can sign up → verify → sign in → see/edit **only their own** profile (RLS enforced); every personal-data field identified with its GDPR basis; Lawyer has reviewed the data model; handoff note appended to `nabohero/output_log.md` and `nab-001` moved to done.

## When you finish
Append any cross-project learnings to `agents/memory/devops_learnings.md` (date + `nab` tag) — especially anything reusable about app-level auth, Supabase/RLS, or the GDPR data model, since Robert will apply these patterns to future client builds.
