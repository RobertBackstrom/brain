# Hooja - Project Instructions

## What this is
Aurora Punks F2P mobile auto-runner built on the "Hooja" music-artist IP (Banan Melon Kiwi & Citron). Released 2023, live on Google Play (`com.AuroraPunks.Hooja`) and App Store (`id1659828753`). AP did full dev + live service.

## Repos
- **Game:** `Aurora-Punks/Hooja` (private, C#, Unity). Runtime engine as of 2026-07: Unity 2021.3.45f2.
- **Web:** `Aurora-Punks/hooja-web` (JS landing/PR site).

## Stack
- Engine: Unity (Built-in RP, IL2CPP Android), custom AP packages `aurora-audio` / `aurora-scriptable-values` / `aurora-save`.
- Ads: ironSource **LevelPlay** mediation, rewarded-only (as of 2026-07 on 7.3.0.1, pre-upgrade).
- Backend: **PlayFab** (anonymous login, leaderboards, Title Data, telemetry). No catalog/VC/inventory in use.
- IAP: none yet (design spike done 2026-07).

## Model policy
Coding work runs on **Fable 5** (`config.json` project_model_policy.projects.hooja = "fable"). Set by Robert 2026-07-13.

## Prefix
`hoj` (set by Robert 2026-07-13). Tickets: `hoj-NNN`.

## Current initiative
SDK modernization + ad-funnel update + IAP - see `hooja_modernization_brief.md` and `output_log.md`. Engine upgrade + LevelPlay 8.x migration are mandatory to ship any new store update (target API 35 / 16 KB / Xcode 16 gates).

## Rules
- Standard project rules from the root `CLAUDE.md` apply (writing voice, no em-dashes, numbered lists, confirm before external changes, security defaults).
- Never modify store listings, PlayFab title config, or ad dashboards without Robert's approval.
- Engine spikes/builds run on a Unity-Hub dev machine, not the VPS.
