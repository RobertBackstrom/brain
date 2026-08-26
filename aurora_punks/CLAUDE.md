# Aurora Punks — CLAUDE.md

## Engagement
- **Role:** Founder/CEO, board-facing governance, cap table owner, shareholder comms
- **DB prefix:** `apb` (AP Board)
- **Status:** active
- **Agent owner:** CorpBot (admin) — cap table, emissions, investor comms, governance

## Entities
- **Aurora Punks AB** — 559256-9718 (live entity, contracting entity going forward)
- **Aurora Punks Development Services AB** — konkurs 12/12/2025 (do NOT use in new contracts)

## Key People

### Board (5 ledamöter, korrigerat 2026-05-03)
- **Mattias Wiking (ordf)** — mattias@mattiaswiking.com / mattias@turborilla.com
- **Alexander Bergendahl** — alexander@lootlocker.com
- **Andreea Chifu** — **andreeachifu@gmail.com** (preferred, för signering/kontakt; tidigare andreea@aurorapunks.com) (avgick som VD under 2025, kvar i styrelsen)
- **Karl-Magnus Troedsson** — km@behold.vc
- **Robert Bäckström** — robert@aurorapunks.com (inofficiell ställföreträdande VD efter Andreeas VD-avgång)
- **Firmateckning:** två i förening (förslagsvis Mattias + Robert)
- **Konkursförvaltare APDS AB:** Nils Åberg, Carler (Ulrika Mattsson handläggare; ulrika.mattsson@carler.se)

### Shareholders (fully diluted, post WISE 2 conversion)
- Behold Ventures 0 AB — 127 811 (32,26%) — Karl Magnus Troedsson (km@behold.vc), Brynjólfur Erlingsson (binni@behold.vc), Magnus Kenneby (magnus@behold.vc)
- Creation Zero Point Holding AB — 119 411 (30,14%) — Robert's holding
- Alexander Bergendahl — 47 816 (12,07%)
- Loot Spawn AB — 45 136 (11,39%)
- Gyllenberg Invest — 16 438 (4,15%)
- DekoDu — 13 636 (3,44%)
- Jens Lundqvist — 10 138 (2,56%)
- Mattias Wiking Development AB — 8 263 (2,09%)
- Byberg & Nordins Busstrafik — 5 170 (1,30%)
- Sundquist Konsult i Umeå AB — 1 887 (0,48%)
- Kenny Carvalho — 467 (0,12%)
- **Total: 396 173 aktier**

### Legal / Accounting
- **Marc Harris** — marc.harris@dangoor-associates.com (Dangoor Associates, corporate legal)
- **Henrik Franzén** — henrik@sifferradet.se (accounting, AP)
- **Christine Lef** — christine.lef@parameterrevision.se (revision)

## Infrastructure / Resources
- **Jira/Confluence:** aurorapunks.atlassian.net (BADASS project and others)
- **Atlassian site hosts BADASS tickets** — apb-* are DB tickets (internal), not Jira
- **Fortnox:** accounting system (Christine has access)
- **Bolago.app:** aktiebok / shareholder register
- **GDrive:** CZP Drive for board/finance docs, see DB epic apb-000 for sheet IDs

### Key sheets
- **AP P&L 2026 LIVE board sheet**: GDrive `1ml7BaJaVDTZwDp-CKFd6LPPaJ0HzaQsLQm96rt0-yiU` (Google Sheet — single source of truth as of 2026-04-29)
- **CZP Projects_2 → AP Board → Financials** (`_financials`): `1sfWNlGWSxXMSLU8sEkmtJSa6IEMasJCI`

### AP Board Drive tree (Shared Drive)
- **Aurora Punks Board** (root): `15JWcx2V4lcOd9fz9RloDiUwVfijeGLSH` — children: `_deliverables`, `_financials`, `_legals`, `Meeting Notes`, `_deliverables_working`
- **`_deliverables_working`**: `1TmSqmdwPY115LXwlFHNDyCniQkEzxGCh` — shared working folder for 2025 bokslut (Wiking/Amer/Jacob). Working docs live here as Google-native (per Robert: always Drive/Sheets for working docs)
- **2025 Årsbokslut**: going-concern Sheet `1dmokSjTvdx3ptlgbmEt9WSKaNjp37AjN2wsfNVjlP28`; förvaltningsberättelse Gdoc `1RlboFA5PNTWSCJhJN-lbMuISjhyCYwO3I4prFL2ZlKE`; 2024 bokslutsbilagor zip `1Ehy8DSp-4F_9FnWpip8XcouEb7KJJaVb`; 2024 ÅR `1Zk8q8KP8j_QMqYgmn_132hZmRMqEld56`

## Cap Table Conventions
- Model convention: **EV = pre-money** (verified: 45M EV / 294 709 shares = 152 SEK matches)
- **No anti-dilution in the default model** — if ratchet triggers it must be read from actual AA/WISE agreements
- **No liquidation preferences** — proceeds split pro-rata on common equity
- WISE 2 converted 2024-07-01 at floor 40M (Behold added 46 101 shares)
- Most recent xlsx: `uploads/Calculations AP Issuances and Conversions (2024-05-20 - additional discount version).xlsx` (from Marc 2024-06-18, the corrected-for-Byberg version)

## Why
Aurora Punks is Robert's operating company for game publishing, the primary vehicle for partnerships (K2C, Shosha, BADASS), and holds the biggest investor relationship (Behold ~32%). All board governance and cap table work flows through this project.

## Conventions
- Deliveries logged to `output_log.md`
- Drafts in `drafts/` before going out
- Cap table source of truth: `uploads/` (most recent Marc/Dangoor version), never overwrite
- Investor comms must follow [[writing_voice_robert]] — professional but not stiff corporate
- Never modify Bolago, DocuSeal, or send investor emails without Robert's approval
- Child tickets: [apb-000-epic](../assistant/followups/apb-000-epic.md), [apb-002-pnl](../assistant/followups/apb-002-pnl.md) (apb-001 was folded into apb-002 on 2026-04-29)

## Related
- [[project_badass]] — BADASS Studios XR work invoiced via AP
- [[project_k2c_sands_of_duat]] — K2C intercompany flows land here via apb-001
- [[project_czp_finances]] — AP-scoped P&L lives in master CZP model
