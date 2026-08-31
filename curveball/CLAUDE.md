# Curveball (The Gang Studio) — CLAUDE.md

## Engagement
- **Role (omarbetad 2026-08-31):** AP finishes and publishes The Gang's game *Curveball* on its own dime, in exchange for a revenue share. No cash changes hands from The Gang.
  1. **Färdigställande**: P2P instead of dedicated servers, the server-authoritative LootLocker calls moved to an AP-run service, launch polish. **Utförs av Robert + GameDev-agenten**, inte längre av Robin/Eternal Minds.
  2. **Utgivning**: AP is publisher of record. Steam app 2805120 transfers to AP's Steamworks account. Zero paid media.
  3. **Mobilporten ligger utanför** det här avtalet, liksom konsol. AP har förhandlingsföreträde.
- **DB prefix:** `cvb`
- **Status:** active — pre-contract / pitch stage (build received, assessment + commercial pitch in progress)
- **Agent owner:** BizDev (deal + client pitch), GameDev (co-dev execution oversight), CorpBot/Lawyer (Robin subcontract + client agreement)

## Commercial Target (Robert, 2026-08-31 — ersätter 2026-06-22)
Term sheet: `drafts/term_sheet_2026-08-31.md`. Den gamla målbilden (≥100K SEK kontant upfront) gäller inte längre.
- **Alternativ 1, AP:s förstahandsval:** ingen recoup, **50/50 i perpetuitet**. Motiv mot The Gang: samma incitament över hela livslängden, mindre administration.
- **Alternativ 2:** **100 000 SEK recoup**, därefter **30 % AP / 70 % The Gang** i perpetuitet. Det är strukturen Joel bekräftade 30 juni ("blir vår rev-share 70%?" / "låter rimligt"), då med LUG i bilden.
- **Brytpunkt 350 000 SEK nettointäkt.** Därunder tjänar The Gang på alt 1, däröver på alt 2. AP:s kurva är spegelvänd, samma brytpunkt. Båda alternativen visas öppet för dem.
- **Med LUG:** AP + LUG recoupar faktiska kostnader 100 %, därefter 70 % The Gang / 30 % AP+LUG. Magnus (LUG) tyst sedan 16 juli.
- **Steam:** app 2805120 överförs till AP. Önskelistor och följare följer med, finansiell historik gör det inte. Vid avtalets slut går appen tillbaka inom 30 dagar.

## Key People
**Client — The Gang Studio** (www.thegang.io, Slakthusplan 3, 121 62 Stockholm)
- **Joel Edström** — CEO, joel.edstrom@thegangstudio.com, +46 793 5343 71
- **Olle Brännström** — Producer, olle@thegangstudio.com (owns the build, low availability in June — big-project deadline)
- **Gustav Linde** — gustav@thegangstudio.com

**AP side**
- **Robert Bäckström** — Founder / Exec Producer, robert@aurorapunks.com
- **Oskar Hansen** — oskar@aurorapunks.com (looked at an earlier mobile version)
- **Robin Hofström** — co-dev subcontractor, invoices via **Eternal Minds AB** (org.nr 559527-5719; Robin is sole director/VD). See [[project_eternal_minds]].

## Infrastructure / Resources
- **Build:** `BBA_dev.zip` — Google Drive `1uFgqh4vX3PgEqWBDdJZrAYfwPmQNmplT` (delivered 2026-06-04 by Olle). It is a **full UE project tree**, not a cooked build.
- **Source on the VPS:** `code-corpus/repos/curveball-bba/` (Source, Config, Plugins, Saved/Logs; 466 MB). Indexed in RAG as `source=code`, `project=curveball`. Content's 5,469 `.uasset` + 304 `.umap` are **not** extracted — they are listed by name in `_ASSET_MANIFEST.txt`.
- **Engine:** Unreal Engine **5.3**. Project `BladeBallArena.uproject`, C++ module **Mogadishu**.
- **Internal name:** "bodybreakerabs" / **BBA** (the title is *Curveball*)
- **Version control:** confirmed by Olle 2026-08-19 that **no Perforce remains** (The Gang moved to GitHub, MLC was never ported). The 4 June zip is the only copy outside Olle's own workspace. **AP owns version control**: private repo `Aurora-Punks/curveball-mlc` with Git LFS, vendor baseline tagged `vendor/bba-zip-2026-06-04` (Robert's call 2026-08-27). See `drafts/plan_update_2026-08-27.md`.

## Tech Stack (verified 2026-08-04 from the source, not from the deck)
- **Networking today:** AWS **GameLift** dedicated servers. `GameLiftBlueprintPlugin` (AWSCore + GameLiftServerSDK + GameLiftClientLibrary), `GameLiftRegionLatency` enabled, `UGameLiftClientComponent`. `UMLCMatchmakingHandler` returns IP/Port/PlayerSessionId; runtime logs hit `169.254.169.254` (EC2 instance metadata).
- **Matchmaking + party** go through The Gang's own service, `BackendBaseURL="https://mlc-backend-dev.thegang.io"` ([Config/DefaultGame.ini:131](../code-corpus/repos/curveball-bba/Config/DefaultGame.ini#L131)), via `MatchmakingSubsystem`, `BackendMessagePump`, `GamePartySubsystem`.
- **Accounts / progression / store / inventory / friends:** **LootLocker**, game id `a86igukp`. **Server-authoritative** — `LootLockerServerGranter` and `LootLockerServerLoadoutValidator` run on the dedicated server. This is the core problem P2P has to solve.
- **Anti-cheat:** `TGEAC` (Easy Anti-Cheat wrapper) enabled + `MLCAC` in `Source/Mogadishu/*/AntiCheat/`. EAC assumes a trusted server.
- **Abilities:** GAS (`GameplayAbilities`, `AbilitiesV2/`, `MogadishuAbilitySystemComponent`), which also assumes an authoritative server. `ServerHeartbeatSubSystem` reaps disconnected players on a 5s tick.
- **Also:** GameAnalytics (telemetry), Tolgee (localization; en, sv, zh-Hans, pt), CommonUI, UINavigation, CPathfinding.
- **Steam:** `OnlineSubsystemSteam` is already enabled, but the NetDriver is plain `IpNetDriver`. Steam is used for identity, not transport.
- **Cross-platform, half-started:** `EOSIntegrationKit` is in the project but `Enabled: false`, and `BladeBallArenaEpicClient.Target.cs` exists.
- **Gameplay lives in Blueprints.** 94 `.h` + 88 `.cpp` (~1 MB) of C++ against 5,469 binary assets. The C++ is matchmaking, backend glue and GAS helpers. Any agent reasoning about gameplay logic must say so rather than guess; the fix is a one-time Blueprint-to-text export on a machine that can run the editor (see [[project_baremetal_migration]]).
- **Discord:** The Gang server "bodybreakerabs"; Robin to be added, thread being set up
- **Email thread:** Gmail thread `19e889144ac3e56a` ("Curveball")
- **Pitch URL:** pitch.aurorapunks.com/curveball (to be created — nothing published yet). Public title is **Curveball**; "bodybreakerabs"/BBA is internal-only.

## Why
The Gang built Curveball but "never got it out the right way." Robert offered to assess what it takes to ship with P2P multiplayer. That assessment converts into a paid co-dev + AP publishing deal — recurring AP revenue on a near-finished asset, plus a deepened relationship with The Gang.

## Conventions
- Pipeline lives in the deal wiki: company [[the-gang-studio]], project pipeline `wiki/deals/projects/curveball.md`. Update via `/ingest-deal-email` after every touch.
- **Scrub IP / keep generic in any contractor-facing material until an MNDA is in place** with Robin — see [[feedback_scrub_ip_until_mnda]] and [[feedback_no_specific_repo_in_contracts]].
- Robert's voice on all drafts — [[writing_voice_robert]], no hype, no em-dashes.
- Deliveries logged to `output_log.md`; local drafts (incl. the client pitch) to `drafts/`.
- Pitch as styled HTML living-doc per [[feedback_html_pitch_living_doc]] at **pitch.aurorapunks.com/curveball**. **Built 2026-06-29** (audience = Light Up Games as marketing/funding partner). Source material: The Gang's "Curveball - NetEase" deck (Slides `1CrK-Fhk_cdaoOuaRDn0J6MzLGxSgFRGdIX2-V931Hy4`, shared by Joel 2026-06-25) + RankOne Blade Ball intel (`drafts/rankone_bladeball_intel.md`). Public Steam page exists: **Major League Curveball** (app 2805120, "Coming soon"; 4 arenas / 38 weapons / 11 skins / 14 abilities). Open item: RankOne pricing data favours $14.99-19.99 over the sub-$10 brief.
