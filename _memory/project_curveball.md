---
name: curveball-the-gang-studio
description: "Hybrid AP deal on The Gang's game Curveball — co-dev (P2P + mobile port via Robin/Eternal Minds) + AP publishing; prefix cvb"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6ff24d51-123e-43dc-8ba9-131be7b2dcf0
  modified: 2026-08-04T18:36:11.348Z
---

# Curveball — The Gang Studio

Hybrid AP engagement, scaffolded 2026-06-22. Prefix `cvb`. Project folder `curveball/`, deal wiki [[the-gang-studio]] under project pipeline `curveball`.

**Shape (Robert, 2026-06-22):**
- Part 1 — **co-dev ~1.5 months**: ship Curveball with P2P multiplayer + a **mobile port**. Done by subcontractor **Robin Hofström** ("Robin") invoicing via **Eternal Minds AB**. See [[project_eternal_minds]] (Robin is sole director/VD there).
- Part 2 — **AP publishing services**: Robert/AP take it to market; **remaining publishing costs recoupable**.
- Commercial target: **≥100K SEK paid for development** (incl. mobile port) up front, then recoupable publishing. Split TBD in the pitch.

**The game:** *Curveball*, internal name "bodybreakerabs"/**BBA**. UE **5.3**. Built by The Gang, never properly shipped. Delivered as `BBA_dev.zip` (Drive `1uFgqh4vX3PgEqWBDdJZrAYfwPmQNmplT`, 2026-06-04). No version control (was Perforce, never moved to Git).

**Tech, verified 2026-08-04** by pulling the zip onto the VPS. It is a **full UE project tree**, not a cooked build: `BladeBallArena.uproject`, C++ module **Mogadishu**, `EngineAssociation 5.3`. Unpacked to `code-corpus/repos/curveball-bba/` and indexed (`source=code`, `project=curveball`, 190 files). Backend stack:
- **AWS GameLift** dedicated servers. `GameLiftBlueprintPlugin` (AWSCore + GameLiftServerSDK + GameLiftClientLibrary), `GameLiftRegionLatency` on, `UGameLiftClientComponent`; the matchmaking delegate returns IP/Port/PlayerSessionId and the logs call `169.254.169.254` (EC2 metadata), so it ran on real fleets.
- **The Gang's own service** `https://mlc-backend-dev.thegang.io` (`BackendBaseURL`, Config/DefaultGame.ini:131) driving `MatchmakingSubsystem`, `BackendMessagePump`, `GamePartySubsystem`.
- **LootLocker** (game id `a86igukp`) for accounts/progression/store/inventory/friends, **server-authoritative** via `LootLockerServerGranter` + `LootLockerServerLoadoutValidator`. This is the part naive P2P breaks: a peer host would grant its own items.
- **TGEAC** (Easy Anti-Cheat wrapper) + `MLCAC`; **GameAnalytics**; **Tolgee** (en/sv/zh-Hans/pt).
- **`OnlineSubsystemSteam` already enabled**, but NetDriver is plain `IpNetDriver`. Steam is identity, not transport, so the switch to Steam sockets is config + C++, not a rewrite.
- **`EOSIntegrationKit` present but `Enabled: false`** plus a `BladeBallArenaEpicClient.Target.cs`. An EOS path was started and dropped, which is half the cross-platform scaffolding already there.
- **Gameplay is in Blueprints**: only 94 `.h` + 88 `.cpp` (~1 MB) against 5,469 binary `.uasset` + 304 `.umap`. Abilities run on **GAS**, which assumes an authoritative server. A text index cannot read any of it, so the plan includes a one-time Blueprint-to-text export (T3D/JSON) on a machine that can run the editor. See [[project_baremetal_migration]].

**Caveat on the commercial frame:** the pitched **under 100K SEK / ~2 months** was set before anyone read the code. Server authority runs deep and gameplay is blueprinted, so the honest estimate may differ. Flagged to Robert 2026-08-04; his call.

**Client (The Gang Studio, Stockholm):** Joel Edström (CEO), Olle Brännström (producer, owns build, thin June availability), Gustav Linde. **AP side:** Robert, Oskar Hansen, Robin.

**Pitch:** public title is **Curveball** (BBA/bodybreakerabs is internal-only). **Built 2026-06-29 — live at pitch.aurorapunks.com/curveball** (HTML living-doc, [[feedback_html_pitch_living_doc]]). Audience = **Light Up Games** as marketing/funding partner (AP+The Gang = the package). Angle: finish + ship as **sub-$10 PC paid Early Access**, P2P replacing dedicated servers, smooth PC, AP co-dev + lite publishing, no paid marketing initially; AP/LUG commercial terms (LUG-style 70/30 net after recoup, per Everything Is Crab template). Source material: The Gang's **"Curveball - NetEase" deck** (Slides `1CrK-Fhk_cdaoOuaRDn0J6MzLGxSgFRGdIX2-V931Hy4`, shared by Joel 2026-06-25) + **RankOne Blade Ball intel** (`curveball/drafts/rankone_bladeball_intel.md`, pulled via [[reference_rankone_agent]]). Iconography = custom inline SVG in the deck's spirit (real deck/Steam art swappable into `pitches/curveball/assets/`).

**Game is already on Steam:** **Major League Curveball** (app 2805120, dev/pub The Gang, "Coming soon" / not released; Action+Sports PvP+Co-op; 4 arenas, 38 weapons, 11 skins, 14 abilities). Blade Ball (Roblox) reference: 15-25M MAU, mobile ~72% / PC ~20% (PC over-indexes for power users), core age 9-24.

**Open decision (flagged to Robert 2026-06-29):** RankOne's data recommends **$14.99-19.99** ("reaction-brawler" positioning) over sub-$10; sub-$10 kept per Robert's brief and justified via the Knockout City paywall-failure lesson. Robert to confirm final price.

**Deal progress (2026-06-30):** Robert sent the pitch to The Gang thread (Joel/Gustav/Olle + Oskar) proposing LUG as funding + marketing partner, framed as his idea, citing AP's board-mandated "strict profitable mode". The Gang is positive: they know LUG well, **LUG just raised money** (good timing to fund), and **Magnus + Anthony at LUG already know the game** and were keen during the original dev. Joel confirmed the split: after AP+LUG recoup 100% of expenses, **The Gang's rev-share = 70%**; Robert agreed it sounds reasonable (consistent with the pitch's 70/30 net). The Gang offered to help. New LUG contact: **Anthony** (Robert coordinates Magnus + Anthony via a LUG-AP Discord).

**Magnus/LUG status (WhatsApp 1-on-1, chat `122561371349051@lid` = +852 9377 7249):** Robert sent the pre-warm pitch 2026-06-29; Magnus acknowledged (travelling, "svarar snart"); Robert nudged 2026-07-02 with "Joel positiv till trepartssamarbete, vad tror du, ni har väl kikat på det förut?". **Magnus replied positive (~2026-07-07):** "Väldigt intressant och vi har kikat på det! ... konceptet och spelet är riktigt nice. Gillar planen och du får gärna skicka över. Vad är er timeline?" (his read: The Gang shipped the demo a bit early with some problems, but concept + game are nice). **Magnus asked for the material + our timeline.** Robert (on holiday in Crete) first said he'd send it when home, then told the Assistant to send now - **pitch link + login + timeline SENT to Magnus 2026-07-07** (Robert-approved). **Timeline given: start after the summer vacations, ~2 months of work.** Next: Magnus + Anthony review, then a call. Pitch gated at pitch.aurorapunks.com/curveball.

**Cost framing in the pitch (Robert, 2026-07-07):** the pitch's commercial section now states the **dev finishing cost as under 100K SEK (~$9K)** and frames it as a low-capital advantage - the game is done, so most of the budget goes to marketing, not development risk. Robert's rationale: LUG (like everyone) is cash-short, so a low dev cost is a strong selling point. (Supersedes the older "≥100K SEK" internal framing for outward-facing use.)

**Other flags:**
- MNDA with Robin before sharing IP-specific build detail ([[feedback_scrub_ip_until_mnda]]).

Next: receive pitch material from The Gang → Robin's technical assessment of the build → client pitch (≥100K SEK dev + recoupable publishing) → Robin subcontract + client agreement.
