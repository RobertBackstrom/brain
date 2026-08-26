# Nabohero — Output Log

## 2026-07-15 — Project kickoff scaffolded
Created `nabohero/` project (CLAUDE.md, drafts/, this log) + kickoff ticket `nab-001` (auth + personal-data foundation) + `START_PROMPT.md` for a separate DevOps agent. Grew out of the internal.aurorapunks.com portal build — carries the verified-identity → role → scoped-access pattern, but correctly diverges to an app-level auth stack (public self-signup + personal-data DB, GDPR) rather than CF Access. Stack recommendation (Supabase) pending Robert's confirm. No code yet.

## 2026-07-15 — Scaffold completed + live site noted
Registered `nab` prefix + `nabohero` folder in `assistant/config.json` (were missing); added `drafts/.gitkeep`. Robert flagged a sign-up front end is **already live** at https://www.nabohero.com/ — threaded that through CLAUDE.md, START_PROMPT.md, nab-001, and the memory pointer. Reframed the DevOps kickoff from greenfield to "inspect what's deployed first."

## 2026-07-15 — Stack decided + BankID + DevOps kicked off
Robert: nabohero.com has **no signup yet** (front-end page only → auth/backend is greenfield). **Supabase confirmed** as the stack. **Swedish BankID** added as a required sign-in method — threaded through CLAUDE.md, START_PROMPT, nab-001, memory (no native Supabase provider → OIDC broker or server-side RP flow; RP-agreement holder + personnummer minimisation flagged for Lawyer). Spawned the DevOps agent (opus) on `nab-001` to Plan-Confirm-Execute.
