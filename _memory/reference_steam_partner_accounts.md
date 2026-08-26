---
name: reference_steam_partner_accounts
description: "Steamworks partner-account & login registry — which login reaches which PartnerID, AA holders, the Valiant default trap."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2696e915-aed2-4d9b-91bd-9c4365a7f6b5
---

Canonical map of Steamworks logins → partner accounts, for any Steam backend work (transfers, store pages, announcements, financials). Touches ToA, BlockEm, RLR, Vessels of Decay/Headup, Eternal Minds, and the APDS→CZP transfer ([[reference_vessels_of_decay]], apb-026).

## Logins → accounts
- **`naturenistockholm_2`** (Robert's PERSONAL Steam account) is **admin across many partner orgs**: Valiant 53109, Headup 69688, Red Marmoset 169300, Feral Flame 200248, Duck Tape 210499, **Ark Island 229086** (Tears of Adria), Windup 235971, **APDS 301411**, Eternal Minds 350400. So its account-wide app list **MIXES other studios' titles** — authoritative ownership = **package-admin per partner** (`/pub/packageadmin/<pid>`), NOT the store publisher string. Uses **mobile 2FA** (Robert's phone) → cannot be driven headless.
- **`aurorapunks_user`** (email sales@aurorapunks.com) = **Creation Zero Point Holding AB, PartnerID 418393**. Actual Authority = 1 (verify via publisher-wide permissions CSV `/pub/downloadalluserscsv/418393`). Uses **email Steam Guard** → codes are agent-readable, but they arrive via the sales@ Google Group and get spam-filed, so fetch with **`in:anywhere`** and timestamp-gate (see [[admin_learnings]] 2026-07-16; helper `assistant/steam-guard-code.js`). Password in `.env` STEAM_CZP_PASS.
- **`ap_hektor`** = Hektor Andreasson = Actual Authority on **APDS 301411**.
- **`stagisaurus`** = another admin login with APDS backend access.

## Traps
- **Account selector defaults to "Valiant Game Studio AB"** (top-right on partner.steamgames.com AND in Steamworks Support). ALWAYS switch to the intended entity before filing/editing — filing under the wrong account points Valve at the wrong company.
- **Steamworks sessions are per-domain:** `partner.steamgames.com`, `store.steampowered.com`, `help.steampowered.com` are separate logins; a partner login does not carry to store/help.
- **A zero-app partner account is inert:** CZP 418393 (no apps yet) is locked out of BOTH the finance/onboarding domain AND Steamworks Support (`/wizard/HelpWithPublishing` silently redirects it to the consumer tree). File support about 418393 from **APDS 301411** until the transfer lands.
- **Announcements/events are dashboard-only** (no API) on every account — automation = Playwright form-driving, not an API call.

## Appids (quick ref)
Tears of Adria = **2561500** (dev+pub Ark Island Studio; NOT 1516680 — that's an unrelated game). Full APDS→CZP transfer list (18 appids / 10 products): see apb-026.
