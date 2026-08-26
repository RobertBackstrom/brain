# Curveball: P2P + Steam-Ready Development Plan

| | |
|---|---|
| **Date** | 2026-08-04 |
| **Author** | Fable (claude-fable-5) via the GameDev planning pass |
| **Source state** | BBA_dev.zip, Drive 1uFgqh4vX3PgEqWBDdJZrAYfwPmQNmplT, delivered 2026-06-04 |
| **Project** | BladeBallArena (module Mogadishu), UE 5.3, The Gang Studio AB, ProjectVersion 0.22.0 |
| **Local tree** | `/home/assistant/projects/code-corpus/repos/curveball-bba/` |
| **Goal** | (a) P2P multiplayer over Steam networking, (b) Steam-ready shippable PC build, (c) transport and identity abstracted so EOS/console drops in later |

## 1. Summary and verdict

1. The game's netcode is standard UE server-authoritative replication (GAS abilities, replicated ball as an `ACharacter`, NetMulticast RPCs). That is good news: it runs unmodified on a listen server. The P2P conversion is not a gameplay-netcode rewrite, it is a **services replacement**: GameLift session placement, The Gang's matchmaking/party backend, and the trusted-server LootLocker grant path all have to be replaced or relocated.
2. The plan below is 14 work packages in 4 phases, sequenced so a playable LAN listen-server build exists in week 2 and a Steam-transport build by roughly week 5, not a big-bang cutover.
3. **Honest estimate: 285 to 445 hours, central 350 h, roughly 9 to 11 calendar weeks for one full-time senior UE developer**, confidence medium until the Blueprint export (WP0.3) is reviewed, then re-estimated at the Phase 0 checkpoint.
4. Against the pitch frame: **the ~2 months calendar is reachable but tight**, and only for P2P + Steam PC. **The 100K SEK figure does not cover this work at market rates** (350 h at 100K implies ~285 SEK/h effective), **and it definitely does not also cover the mobile port** that the original commercial target folded into the same number. Recommendation in section 11: renegotiate scope so 100K = P2P + Steam EA, price mobile separately after EA data.
5. Biggest unknown, flagged throughout: most gameplay and all menu flow lives in 5,469 binary .uasset Blueprints that no one can currently read. WP0.3 (one-time export to text) is deliberately first. Everything marked "cannot determine until Blueprints are exported" in this document is exactly that, not a guess.

## 2. Current-state architecture map

How a match gets created and played today, verified from `Source/`, `Config/`, `Plugins/` and `Saved/Logs`:

```
Player clicks Play (Blueprint UI, GM_MainMenu / WB_* widgets)
  |
  v
UMatchmakingSubsystem (C++, GameInstance subsystem)
  POST {BackendBaseURL}/... with region_latency map + matchmaking_configuration_key
  BackendBaseURL = https://mlc-backend-dev.thegang.io  (Config/DefaultGame.ini:131)
  region latency measured by GameLiftRegionLatency plugin pinging
  eu-central-1, ap-southeast-1, us-east-1, us-west-1, sa-east-1
  |
  v
The Gang backend brokers a GameLift FlexMatch ticket
  (party's gamelift_matchmaking_configuration: FFA / PRACTICE / DUEL)
  |
  v
Status polls until MATCH_FOUND; FStatusUpdateEvent fires with
  IP, Port, PlayerSessionId  ->  Blueprint opens connection to the
  GameLift-hosted dedicated server (targets MogadishuServer /
  MogadishuGameliftServer / MogadishuGameliftServerAnywhere)
  |
  v
Dedicated server (trusted):
  - AMogadishuGamemode (PreLogin/Logout) + ULootLockerServerCacheGameMode
  - ULootLockerServerLoadoutValidator: pulls player data with the
    LootLocker SERVER key, validates/fixes loadouts
  - GAS: MogadishuAbilitySystemComponent, abilities server-authoritative
  - AGameBall (ACharacter subclass, replicated counters/flying mode)
  - UServerHeartbeatSubSystem reaps disconnected players on a 5 s tick
  - ULootLockerServerGranter: grants assets/currency/progression
    (soft currency cap 6000) via the SERVER key at match end
  - UMLCAC strike system (10 strikes / 60 s window -> kick) + TGEAC (EAC)
```

Parallel client-side services:

1. **LootLocker (game key, `a86igukp`)**: guest login or `StartSteamSessionUsingTicket` (both already implemented in `LootLockerLocalPlayerSubsystem.cpp`), inventory, store, progression, persistent storage (loadout keys), friend list.
2. **UBackendMessagePump + UGamePartySubsystem** (thegang.io): party create/invite/ready-state, presence, queue-state toasts, 3 s poll interval.
3. **GameAnalytics** telemetry, **Tolgee** localization (staged to disk), **CommonUI** input routing.

What each backend dependency is load-bearing for:

| Dependency | Load-bearing for | Evidence |
|---|---|---|
| GameLift + awsSDK plugin | Session placement, server fleets, region latency | `Plugins/GameLiftBlueprintPlugin/awsSDK.uplugin` (AWSCore, GameLift, GameLiftServerSDK), EC2 metadata calls in logs |
| mlc-backend-dev.thegang.io | Matchmaking tickets, party, presence, invites, queue states | `MatchmakingSubsystem.cpp`, `GamePartySubsystem.h`, `BackendMessagePump.h` |
| LootLocker game key | Accounts, inventory, store, progression, friends | 1309 calls in logs; `LootLockerLocalPlayerSubsystem` |
| LootLocker SERVER key | Item/currency/progression grants, loadout validation | `LootLockerServerGranter.h`, `LootLockerServerLoadoutValidator.h`; server SDK is stripped from client targets (`DisablePlugins` in `BladeBallArenaClient.Target.cs`), so the key never ships to players today |
| TGEAC (EAC) + MLCAC | Anti-cheat; EAC assumes a trusted dedicated server | `Plugins/TGEAC/` (EACServer/EACClient); note `TGEAC.uplugin` force-enables `OnlineSubsystemEOS`, which is why EOS artifact credentials sit in `DefaultEngine.ini` |
| OnlineSubsystemSteam | Identity only (auth ticket for LootLocker), `CustomConfig=Steam` per-target config | `Config/Windows/Custom/Steam/WindowsEngine.ini`: `DefaultPlatformService=Steam`, `SteamDevAppId=2981120`, `bUseSteamNetworking=false` |
| IpNetDriver, 30 Hz | Transport (plain UDP, server tick capped) | `DefaultEngine.ini` NetDriverDefinitions + `NetServerMaxTickRate=30` |

Findings not in the original assessment, discovered while verifying:

1. **App ID mismatch.** Config says `SteamDevAppId=2981120`; the live Steam page for Major League Curveball is app **2805120**. One of these is a playtest/second app or stale. Must be resolved with The Gang before any Steam upload (open question 1).
2. **Broken packaging reference.** `DefaultGame.ini` sets `BuildTarget=MajorLeagueCurveball` but no `MajorLeagueCurveball.Target.cs` exists in the delivered Source (logs show it ran once, so the target existed and was not handed over, or was renamed). Packaging will fail until pointed at `BladeBallArenaClient`.
3. **Secrets in tree.** LootLocker dev SERVER key in `DefaultGame.ini`, EOS ClientSecret + encryption key in `DefaultEngine.ini`, GameAnalytics keys. All dev-tier, but they need scrubbing and prod replacements before shipping (WP3.2).
4. **The Epic path exists as a pattern.** `BladeBallArenaEpicClient.Target.cs` with `CustomConfig="Epic"` and `Config/Windows/Custom/Epic/WindowsEngine.ini` switching `DefaultPlatformService=EOS`. The per-target CustomConfig mechanism is exactly the right seam for our abstraction layer and we will reuse it.
5. **Bots exist** (`BotManagerV2`), which gives us a lever for making sparsely-populated EA matches playable (backfill), and a practice mode that works fully offline.

## 3. Target P2P architecture

### 3.1 Decisions

1. **Listen server, not mesh.** UE replication is client-server; GAS assumes a single authority; a true mesh would be a rewrite of every replicated system for zero benefit at this player count. One player hosts, others connect. This is not up for debate given the codebase.
2. **Transport: SteamSockets plugin** (`SteamSocketsNetDriver`), not the legacy `bUseSteamNetworking` path and not raw `IpNetDriver`. Reasons: NAT traversal and relay fallback come free via Valve's SDR relay network, connections address peers by Steam ID (no IP exposure, no port forwarding support tickets), and encryption is built in. The legacy `bUseSteamNetworking=false` stays false; that flag governs the old deprecated ISteamNetworking path, which we are not using.
3. **Sessions: OnlineSubsystemSteam sessions (lobbies)** for discovery, join, and invites. Quick match = FindSessions filtered by game mode, join best result, else create a session and host. No skill-based matching for EA; with an EA-sized population, skill matching against an empty queue is worse than instant lobbies.
4. **Host selection:** the party leader hosts; for solo quick match, the searching player who finds no session becomes host. Optional later refinement (ping-based selection inside a party) is out of scope for step 1.
5. **Host migration: not supported in step 1, deliberately.** What that costs the player: if the host quits or drops mid-match, the match ends for everyone; remaining players return to the menu with a "host left" message. Mitigation: match results are reported at round boundaries (not only at match end), so progression earned up to the last completed round is still granted, and the post-match party is preserved so the group can requeue in one click. Full seamless migration under GAS + a physics-driven ball is a multi-week feature with brutal edge cases; it is the single easiest place to silently lose a month. Revisit post-EA with real disconnect telemetry.
6. **Tick rate:** keep `NetServerMaxTickRate=30` initially (the game was tuned for it), evaluate 60 on host hardware once the Steam build is playable. Host upload bandwidth at FFA player counts is an open measurement task (open question 2: max players per mode is configured backend-side, not visible in client code).

### 3.2 Config vs C++: exactly what changes

Config only (no code):

1. `BladeBallArena.uproject`: add `"SteamSockets": Enabled` (engine plugin, ships with 5.3).
2. `Config/Windows/Custom/Steam/WindowsEngine.ini`:
   - `[/Script/Engine.GameEngine]` NetDriverDefinitions override: `DriverClassName="/Script/SteamSockets.SteamSocketsNetDriver"`, fallback `/Script/OnlineSubsystemUtils.IpNetDriver` (keeps LAN/dev workflow working outside Steam).
   - `[OnlineSubsystemSteam]` correct `SteamDevAppId` (pending open question 1), keep `bInitServerOnClient=true` (required for SteamSockets listen servers).
3. `DefaultGame.ini`: fix `BuildTarget` to `BladeBallArenaClient`.

C++ (new code, all inside the abstraction layer of section 6):

1. A session provider (create/find/join/destroy session, invites, connect-string resolution `steam.<SteamID64>`).
2. Rewired internals of `UMatchmakingSubsystem` and `UGamePartySubsystem` (public Blueprint-facing API kept, see section 6, so Blueprint UI edits are minimized).
3. Match-result reporting client (section 4).
4. Removal/guarding of GameLift and backend HTTP code paths.

Blueprint (unavoidable, scope known only after WP0.3):

1. The travel step after MATCH_FOUND (today Blueprint opens `IP:Port`; the same delegate will carry a `steam.<ID>` connect string, so this may be zero-change if the Blueprint just calls Open Level with the string it is handed; cannot confirm until export).
2. Host-side UI states ("waiting for players", start-match countdown) that dedicated servers never showed.
3. Party UI widgets that reference backend-specific fields (`WB_InvitePlayerButton`, `WB_KickPlayer`, `WB_LeaveParty`, `WB_FriendList`, ready-state flow).

## 4. The server-authority problem, solved concretely

With a player hosting, everything in section 2's "Dedicated server (trusted)" box runs on a player's machine. Three separate problems, three separate answers.

### 4.1 LootLocker grants and loadout validation

Today `ULootLockerServerGranter` and `ULootLockerServerLoadoutValidator` use the LootLocker SERVER key, which has write access to every player's inventory, wallet, and progression for the whole game. The client targets strip the server SDK precisely so this key never reaches a player's machine. A listen-server host is a player's machine. **The server key must not ship, full stop.** Options:

| Option | Mechanics | Verdict |
|---|---|---|
| A. Thin AP-hosted grant service | Host and clients POST signed match results to a small HTTPS service (Node, on existing AP VPS). Service holds the server key, sanity-checks results (currency caps, per-match maximums, rate limits, cross-report agreement between host and clients), then performs the grants and progression writes via LootLocker server API. | **Recommended.** Keeps the key off clients, keeps the anti-fraud caps (`SOFT_CURRENCY_CAP=6000` logic moves here), costs effectively nothing to run. |
| B. Server key in the host build | Ship LootLockerServerSDK in the client. | Rejected. Key extraction from a shipped binary is trivial and compromises the entire player database, not just the cheater's account. |
| C. Client self-grant via game-key session | Let each client write its own progression through the player-session API. | Rejected as primary: LootLocker's player session correctly cannot grant arbitrary assets, and what it can write is spoofable per-player anyway. Note store purchases (spending soft currency) already run through the player session and continue to work unchanged. |
| D. Accept-the-risk | No validation, host reports, trust it. | Fallback only. Viable for a premium EA with a cosmetic-leaning economy, but it converts every host into a potential economy faucet. Keep as the de-scope valve if WP2.1 slips, not the plan. |

Does option A undermine the "no server cost" commercial driver? No. The driver is removing **per-match simulation servers** (GameLift fleets billed per instance-hour). A stateless grant endpoint serving a few HTTPS calls per match is noise, it can live on infrastructure AP already pays for, and it is orders of magnitude below any dedicated-server bill.

**Loadout validation** moves to the host using data the players themselves present: each client submits its loadout claim on join; the host runs the existing `CheckAndFix`/`MakeSafeServerData` logic (that code is plain C++, reusable as-is) against the client's public LootLocker profile, which is readable without the server key. Stakes are low (wearing an unowned cosmetic), so host-side checking is proportionate. The grant service can spot-audit claims server-side as a backstop.

### 4.2 GAS ability authority

Nothing changes structurally: on a listen server the host's engine instance is the GAS authority, all `AbilitiesV2` code and Blueprinted `GA_*` abilities run exactly as on the dedicated server, and `UServerHeartbeatSubSystem` keeps working. The honest part: **the host is a player and can cheat with authority** (memory editing, speedhacks on their own sim). There is no P2P architecture where nobody owns the simulation. Mitigations that are actually worth their cost for EA: `UMLCAC` keeps running on the host against remote clients; the grant service's cross-report check (4.1) catches a host inflating results, because non-host clients independently report what they observed; and a premium price tag is itself the strongest anti-cheat economics available (banned = buy again). State this plainly in the store FAQ rather than pretending otherwise.

### 4.3 Anti-cheat: TGEAC / EAC under P2P

EAC's deployment model here assumes a trusted server doing attestation of clients (`EACServer.cpp`/`EACClient.cpp`). Under P2P there is no trusted machine to anchor it, and keeping EAC kernel-level protection on a small premium EA title also carries real support cost (false positives, Linux/Proton friction on Steam Deck). Decision: **compile TGEAC out for step 1** (disable the plugin per-target), keep `UMLCAC` (host-side behavioral strikes, 10 strikes in 60 s then kick) and the grant-service validation as the cheat surface. Consequence to note: disabling TGEAC also removes the thing that force-enables `OnlineSubsystemEOS`, so the EOS settings block goes dormant, which is fine until step 2. Revisit in step 2: EOS Anti-Cheat has a peer-to-peer mode (client-to-client attestation) that fits the EOSIntegrationKit path naturally.

## 5. Keep vs cut

| System | Decision | Replaced by |
|---|---|---|
| awsSDK plugin (AWSCore, GameLift, GameLiftServerSDK) | **Cut** | Steam sessions + listen server |
| GameLiftRegionLatency plugin + region ping config | **Cut** | Steam handles routing; session search can filter by ping natively |
| MogadishuGameliftServer / Anywhere / MogadishuServer targets | **Cut** (keep `MogadishuServer` compiling if cheap, as a future LAN/dedicated escape hatch; do not maintain it) | Listen server in the client target |
| mlc-backend-dev.thegang.io: matchmaking | **Cut** | Steam session search behind the existing `UMatchmakingSubsystem` API |
| mlc-backend: party, invites, ready state | **Cut** | Steam lobby + overlay invites behind the existing `UGamePartySubsystem` API |
| mlc-backend: presence, message pump, toasts | **Cut** | Steam friends presence where surfaced; in-game LootLocker friend list keeps working for list/add, loses live presence in step 1 (open question 4) |
| LootLocker game-key side (accounts, inventory, store, progression, persistent storage) | **Keep unchanged** | n/a (platform-agnostic, already the system of record for the economy) |
| LootLocker SERVER-key usage (granter, validator) | **Relocate** | AP-hosted grant service (4.1) + host-side validation (4.1) |
| TGEAC / EAC | **Cut for step 1** | MLCAC + grant-service validation; EOS AC P2P mode in step 2 (4.3) |
| MLCAC | **Keep** (runs on host) | n/a |
| ServerHeartbeatSubSystem | **Keep** (runs on host) | n/a |
| GameAnalytics | **Keep** (client-side; swap dev keys for prod) | n/a |
| Tolgee localization | **Keep** (files staged to disk; verify offline behavior and account status, open question 7) | n/a |
| Bots (BotManagerV2) | **Keep**, optionally promote to match backfill (WP3.5, stretch) | n/a |
| OnlineSubsystemSteam | **Keep and extend** (identity today, + sessions + transport) | n/a |
| EOSIntegrationKit (disabled) + EpicClient target + Epic CustomConfig | **Keep dormant** | Step 2 implementation slot |
| GameLiftClientComponent, MLCMatchmakingHandler internals | **Cut/rewire** (handler's Blueprint node signature kept, see section 6) | Session provider |

Note on the thegang.io backend: this plan never depends on it, which also de-risks the scenario where The Gang turns the dev instance off mid-project. We should still ask them to keep it up through Phase 1 as a behavioral reference.

## 6. The abstraction layer

Goal: EOS (step 2) or a console OSS (step 3) drops in without touching gameplay or UI. The project already has the right seam: per-target `CustomConfig` ("Steam" / "Epic") selecting different `WindowsEngine.ini` stacks. We extend that pattern into code.

New folder `Source/Mogadishu/Public/Online/` (+ Private mirror):

1. **`IMatchSessionProvider`** (pure C++ interface): `CreateSession(Mode, MaxPlayers)`, `FindAndJoin(Mode)`, `LeaveSession()`, `GetConnectString()`, `SendInvite(PlayerId)`, plus status delegates. Step 1 implementation `FSteamSessionProvider` (wraps OSS Steam session interface + SteamSockets connect strings). Step 2: `FEOSSessionProvider`. Selected at startup from config (`[MLCOnline] SessionProvider=Steam`), which lives in the per-target CustomConfig files.
2. **`IPlatformIdentityProvider`**: `GetAuthTicket(Callback)` + `GetPlatformUserId()`. Step 1 `FSteamIdentityProvider` (the auth-ticket code already exists inside `LootLockerLocalPlayerSubsystem`; this extracts it). Step 2 EOS Connect token. LootLocker session bootstrap consumes this interface instead of calling Steam directly, so cross-platform accounts arrive with zero LootLocker rework.
3. **`IPartyProvider`**: party create/invite/ready behind the delegate surface `UGamePartySubsystem` already exposes to Blueprint (`FOnPartyUpdated`, `FOnGamePartyInviteReceived`, etc.). Step 1 maps parties onto Steam lobbies.
4. **`IMatchResultReporter`**: `ReportRoundResult(...)` / `ReportMatchEnd(...)` posting signed payloads to the grant service. Kept as an interface so a future platform (console cert, or a return to dedicated servers if the game blows up) swaps the sink, not the callers.

**The load-bearing trick: the Blueprint-facing API does not change.** `UMatchmakingSubsystem::StartMatchmaking/StopMatchmaking` and `FStatusUpdateEvent(Status, IP, Port, ...)` keep their exact signatures; the `IP`/`Port` strings simply carry a `steam.<SteamID64>` connect string, and `UMLCMatchmakingHandler` (the async Blueprint node the menus call) is untouched at the surface. Same for `UGamePartySubsystem`. This confines changes to C++ internals plus whatever Blueprint edits WP0.3 proves genuinely necessary, instead of rewiring every menu widget.

## 7. The Blueprint problem

Source C++ is 94 headers / 88 cpp (~1 MB) and readable. The game is not there: it is in 5,469 binary `.uasset` + 304 `.umap` (5.2 GB, unextracted; names listed in `_ASSET_MANIFEST.txt`). Nobody on our side has read the match flow, the grant call sites, or the menu wiring. Plan:

1. **One-time export to text, on a Windows machine with UE 5.3 + the project** (WP0.3): run the editor headless (`UnrealEditor-Cmd.exe <project> -run=pythonscript -script=export_blueprints.py`) with a Python script that iterates Blueprint/WidgetBlueprint/AnimBlueprint assets via the asset registry and writes each through `unreal.AssetExportTask` + the T3D object exporter (graphs, nodes, pins, default values, all human-readable). Commit exports to the repo under `/BlueprintExports/` and index into RAG so every later agent can grep them. Data-only assets (DataTables like `DT_MatchMakingConfigurationNames`) export to JSON/CSV.
2. **Priority order for export review** (from the manifest, the ones that gate replication and services work):
   - `Blueprints/GameInstance/BP_GameInstance` (session bootstrap, subsystem wiring, kick handling)
   - `Blueprints/Gamemodes/GM_MogadishuBasic`, `GM_Tutorial`, `BP_TestGamemode`, `Levels/MainMenu/GM_MainMenu` + `GM_MainMenu_Rework` (match lifecycle, where grants are triggered)
   - `Blueprints/Ball/BP_Ball_New` (+ `_FX`) and `Blueprints/Characters/BP_PlayerCharacter` (replication-sensitive gameplay)
   - `Blueprints/Matchmaking/DT_MatchMakingConfigurationNames` + `S_MatchMakingConfiguration`
   - Party/menu widgets: `HUDMenu/Widgets/Party/WB_*` (InvitePlayerButton, KickPlayer, LeaveParty, GamemodeButton), `HUDMenu/Widgets/Friends/WB_FriendList` + `WB_AddFriendPopup` + `WB_GameMode`
   - `GA_*` ability Blueprints and `Blueprints/Characters/BP_RemotePartyMemberCharacter`
   - Match-end flow: `HUD/Widgets/LocalHud/Popups/W_NewMatchOverPopup`, `W_MatchStat`
3. Every estimate in section 10 carries a **Phase 0 checkpoint**: after the priority exports are reviewed, WP1.2/1.3/2.1 get re-estimated with stated confidence before Phase 1 work starts. That is the honest way to handle 5 GB of unread logic.

## 8. Work packages

Ground rules for every WP: implemented by the GameDev agent (Robin executing / agent supporting per the co-dev split), each WP ends with a **code-review gate** (reviewing agent reads the diff against acceptance criteria before merge; Robert does hands-on QA on the build), work lands on a feature branch per WP, and `output_log.md` gets a line per merged WP.

### Phase 0: Foundations (week 1 to 2)

**WP0.1 Version control and project hygiene**
- Goal: the project exists in Git before anyone edits anything.
- Touches: new GitHub repo (AP org), Git LFS for uasset/umap (5.2 GB; check LFS quota/cost, consider Azure DevOps free LFS if GitHub quota is a problem), `.gitignore`/`.gitattributes` for UE, scrub `Saved/` except kept reference logs.
- Acceptance: fresh clone + `Setup` doc reproduces the tree byte-identical to the zip; secrets inventoried in a SECRETS.md (not the values, the locations).
- Review gate: repo structure + attributes review; confirm no secret values in README/docs.
- Estimate: 8 to 12 h.

**WP0.2 First build**
- Goal: `BladeBallArenaClient` (CustomConfig Steam) compiles and packages on a Windows machine with UE 5.3.
- Touches: `DefaultGame.ini` (`BuildTarget=MajorLeagueCurveball` reference is dead, point at `BladeBallArenaClient`), plugin binary rebuilds (`awsSDK`, `UINav3Plugin`, `CPathfinding`, `TolgeeSDK`, `GameLiftRegionLatency` all ship in `Plugins/` with source, so this is compile-time work, not procurement), possible engine-version friction.
- Acceptance: packaged Development build reaches the main menu; editor opens the project without fatal load errors.
- Review gate: build log review; list of every warning/deviation recorded for later.
- Estimate: 16 to 32 h (widest Phase 0 band; no one has built this outside The Gang).

**WP0.3 Blueprint export to text**
- Goal: section 7 executed; priority Blueprints reviewed and summarized.
- Touches: `export_blueprints.py` (new, in repo `/Tools`), `/BlueprintExports/` committed, RAG index refresh.
- Acceptance: all Blueprint classes exported; a written 1 to 2 page summary of (a) the exact match-flow wiring, (b) every call site of ServerGranter/LoadoutValidator/MatchmakingHandler/PartySubsystem in Blueprint, (c) confirmation or correction of the section 3.2 Blueprint-edit list.
- Review gate: **the Phase 0 checkpoint.** Re-estimate WP1.2, WP1.3, WP2.1 against the export findings; Robert signs off on the revised numbers before Phase 1 starts.
- Estimate: 12 to 20 h.

**WP0.4 LAN listen-server smoke test**
- Goal: prove gameplay survives a listen server before touching Steam.
- Touches: launch scripts only (`?listen` on an arena map, second client `open <ip>`), backend calls stubbed/ignored via a dev flag if they block match start (cannot fully predict until WP0.3; `BP_TestGamemode` and PRACTICE mode are the likely path of least resistance).
- Acceptance: two machines on LAN complete a match round on IpNetDriver: movement, ball deflection, at least one GAS ability each, scoring. Defect list captured, not necessarily fixed.
- Review gate: recorded session + defect list review.
- Estimate: 8 to 16 h.

### Phase 1: Steam P2P core (weeks 2 to 5)

**WP1.1 Abstraction layer + Steam sessions + SteamSockets transport**
- Goal: section 6 interfaces exist; a session can be created, found, and joined over SteamSockets between two real Steam accounts on different networks.
- Touches: new `Source/Mogadishu/Public|Private/Online/` (interfaces + `FSteamSessionProvider`, `FSteamIdentityProvider`), `BladeBallArena.uproject` (SteamSockets), `Config/Windows/Custom/Steam/WindowsEngine.ini` (NetDriver, appid), `Mogadishu.Build.cs` (add `SteamSockets`, `OnlineSubsystem` deps as needed).
- Acceptance: console-driven proof (no UI yet): host creates session, remote peer on a different NAT finds and joins via `steam.<ID>`, character replicates. Relay fallback verified (block direct route, confirm SDR path connects).
- Review gate: interface design review is the important one here (this is the surface EOS lands on later); then connection-matrix test evidence.
- Estimate: 24 to 40 h.

**WP1.2 Matchmaking rewire behind the existing API**
- Goal: `UMatchmakingSubsystem` internals swap HTTP-to-thegang.io for `IMatchSessionProvider`; quick match works from the real UI.
- Touches: `MatchmakingSubsystem.cpp`, `MLCMatchmakingHandler.cpp` (internals only, signatures frozen), removal of `GameLiftRegionLatency` calls, Blueprint travel step if WP0.3 showed it needs edits.
- Acceptance: from the packaged build's main menu, player A clicks Play and hosts; player B clicks Play and joins A within one search cycle; FFA/PRACTICE/DUEL selection maps to session filters; cancel works; `FStatusUpdateEvent` states drive the existing UI without widget rework.
- Review gate: diff review confirming zero Blueprint-facing signature changes; playtest by Robert.
- Estimate: 24 to 40 h (confidence low until WP0.3; re-estimated at checkpoint).

**WP1.3 Party and invites on Steam lobbies**
- Goal: `UGamePartySubsystem` runs on Steam lobbies; overlay invites work; `BackendMessagePump` consumers weaned off.
- Touches: `GamePartySubsystem.cpp` internals, `BackendMessagePump` (retire or reduce to a local-message bus for the FRIEND_REQUEST_RECEIVED path), party widgets per WP0.3 findings, ready-state over lobby member data, party-leader-hosts flow into WP1.2's session creation.
- Acceptance: two players form a party via Steam overlay invite, ready up, leader starts quick match, both land in the same listen-server match; leave/kick paths work; solo flow unaffected.
- Review gate: state-machine review (party edge cases: invite declined, member disconnects while queued) + Robert playtest.
- Estimate: 40 to 60 h (largest single unknown; presence/toast UI depth is Blueprint-buried).

**WP1.4 Listen-server gameplay hardening**
- Goal: the match plays correctly and fairly-enough with a player host on real internet latency.
- Touches: whatever WP0.4's defect list + Steam-latency testing surfaces; likely candidates: host-quit handling (clean session teardown + "host left" UX per 3.1.5), `ServerHeartbeatSubSystem` on host, spectate/respawn flow, ball feel at 60 to 120 ms (deflection windows are server-adjudicated; may need lag-compensation tuning in `GA_DeflectBall`/ball Blueprint), the experimental `PhysicsPrediction=(bEnablePhysicsPrediction=True, bEnablePhysicsResimulation=True)` flags in `DefaultEngine.ini` (verify what actually consumes them; consider disabling if they were dedicated-server experiments).
- Acceptance: 3+ player match across real networks completes; host quit mid-match fails gracefully; defect list from WP0.4 closed or explicitly deferred with Robert's sign-off.
- Review gate: netcode-focused review of every change touching replication; Robert QA across two match types.
- Estimate: 30 to 50 h.

### Phase 2: Authority and persistence (weeks 5 to 7)

**WP2.1 Grant service + result reporting**
- Goal: section 4.1 option A live: progression/currency/asset grants work without the server key on any client.
- Touches: new small service (Node/Fastify on AP VPS, HTTPS, HMAC-signed payloads keyed per build, LootLocker server API calls, plausibility rules ported from `LootLockerServerGranter.cpp` including the currency cap); in-game `FMatchResultReporter` (new, `Online/`); `ULootLockerServerGranter` call sites rerouted (call sites enumerated by WP0.3); round-boundary reporting per 3.1.5.
- Acceptance: match end grants XP/currency exactly once per player with the service as the only writer; replayed/forged payloads rejected (signature, nonce, per-match caps); host/client report divergence beyond threshold flags and withholds; service deployed with monitoring on the VPS.
- Review gate: security-focused review (this is the economy's front door): signing, replay, caps, idempotency. Second reviewer pass warranted here.
- Estimate: 30 to 40 h (20 to 26 service, 10 to 14 game side).

**WP2.2 Loadout validation on host**
- Goal: section 4.1 host-side validation: `CheckAndFix`/`MakeSafeServerData` logic runs on the host against client-presented public profiles.
- Touches: `LootLockerServerLoadoutValidator` (rework to game-key/public data), `LootLockerServerCacheGameMode`, join-flow handshake.
- Acceptance: client claiming an unowned weapon/skin gets defaulted (existing ForceDefault path); legitimate loadouts pass; no server-key references remain in any client-linked module.
- Review gate: diff review + a deliberate spoof test.
- Estimate: 8 to 16 h.

**WP2.3 Anti-cheat decision implemented**
- Goal: section 4.3: TGEAC compiled out cleanly, MLCAC verified on host.
- Touches: `.uproject`/target files (disable TGEAC per client target), guard any Blueprint calls into `EAC_BlueprintFunctions` (WP0.3 tells us where), confirm OnlineSubsystemEOS dormancy causes no startup errors, MLCAC strike/kick path tested host-side.
- Acceptance: build boots and plays with no EAC modules loaded; MLCAC kicks a strike-accumulating client.
- Review gate: standard review.
- Estimate: 8 to 12 h.

### Phase 3: Strip, ship, harden (weeks 7 to 10)

**WP3.1 Remove GameLift, AWS, and thegang.io remnants**
- Goal: dead services out of the build entirely (binary size, attack surface, license hygiene, no accidental calls to a backend The Gang may switch off).
- Touches: disable/remove `awsSDK`, `GameLiftRegionLatency` plugins; delete/strip `GameLiftClientComponent`, GameLift server targets from the build matrix; remove `MLCDeveloperSettings.BackendBaseURL` consumers (`MatchmakingSubsystem` HTTP paths, `BackendMessagePump` remnants); config cleanup (region lists, `[OnlineSubsystemEOS]` stale block decision).
- Acceptance: packaged build makes zero network calls to AWS or thegang.io (verified with a network capture over a full session: boot, menu, party, match, grants); no GameLift symbols in the binary.
- Review gate: capture evidence + dead-code diff review.
- Estimate: 16 to 24 h.

**WP3.2 Identity, keys, and Steam plumbing**
- Goal: production-ready identity chain and clean secrets.
- Touches: resolve app ID (open question 1) and set it everywhere; LootLocker **production** game key + guest-vs-Steam-session policy (Steam ticket path already implemented, make it the default on Steam builds, keep guest for dev); scrub dev secrets from shipped configs (LootLocker server key line, EOS artifact secret, GameAnalytics dev keys) and extend `IniKeyDenylist` (`LootLockerServerKey` is not currently denied); `steam_appid.txt` handling for dev vs shipping.
- Acceptance: shipping-config audit shows no secret material; fresh Steam account logs in, gets a LootLocker account bound to Steam identity, progression persists across reinstall.
- Review gate: secrets audit checklist signed.
- Estimate: 8 to 16 h.

**WP3.3 Build pipeline and Steam delivery**
- Goal: repeatable one-command path from Git to a Steam branch.
- Touches: UAT/BuildGraph script (BuildCookRun for `BladeBallArenaClient` Shipping), steamcmd depot scripts (app build config, depot layout, `default` + `beta` branches), versioning from `ProjectVersion`, upload doc; runs on whatever Windows build machine Robin uses (a VPS-triggered flow is a later nicety, not step 1).
- Acceptance: tagged commit produces a Shipping build uploaded to the beta branch and installable through Steam by Robert.
- Review gate: pipeline dry-run reviewed end to end.
- Estimate: 16 to 24 h.

**WP3.4 QA cycles and Steam-readiness closure**
- Goal: the section 9 checklist closed; EA-shippable candidate.
- Touches: fix queue from Robert's QA passes (2 to 3 structured cycles: fresh-user flow, party flow, match flows per mode, disconnect matrix, store/progression), localization spot-check (4 languages stage correctly), min-spec pass, overlay/invite/Big Picture check, optional Steam Deck/Proton smoke (no EAC anymore, so odds are decent).
- Acceptance: zero known crash/progression-loss/blocker bugs; checklist in section 9 all green or explicitly waived by Robert.
- Review gate: release-candidate review meeting (Robert + agent) against the checklist.
- Estimate: 40 to 60 h (defect-driven; the honest number depends on Phases 1 to 2 quality).

**WP3.5 (Stretch, only if timeline holds) Bot backfill**
- Goal: quick match never leaves a solo EA player staring at an empty lobby: host fills with `BotManagerV2` bots, humans replace bots as they join.
- Estimate: 12 to 20 h. Cut first if anything above slips; PRACTICE mode already covers the offline case.

## 9. Steam-ready checklist (beyond networking)

1. App ID resolved (2981120 config vs 2805120 store page) and Steamworks admin access to the app confirmed via The Gang's partner account.
2. Store package: EA questionnaire, pricing (note the standing open item: RankOne comparables read favored $14.99 to 19.99 vs the sub-$10 brief), depot + launch config, system requirements honest against min-spec pass.
3. VCS live (WP0.1), pipeline live (WP3.3), tagged RC build on beta branch.
4. Secrets scrubbed, production keys in (WP3.2); LootLocker account ownership/billing agreed with The Gang (open question 3).
5. Steam identity: auth ticket -> LootLocker Steam session as default; guest path fenced to dev builds.
6. Achievements/stats: none found wired in C++ (no OSS achievements interface usage); confirm none hide in Blueprints after WP0.3. Decision: ship EA without achievements, add post-EA. Steam does not require them.
7. Overlay, invites, and Join Game via friends list verified; controller + CommonUI navigation pass (project already targets gamepad seriously: CommonInput config, UINav).
8. Localization: en/sv/zh-Hans/pt stage and render; Tolgee account status confirmed (open question 7).
9. GameAnalytics: prod keys, and a privacy-policy line for the store page (analytics + LootLocker = personal data processing; needs a privacy URL on the Steam page).
10. Crash visibility: `IncludeCrashReporter=False` today; enable or accept blindness, decide consciously.
11. Network capture proof of no AWS/thegang.io traffic (WP3.1 acceptance).
12. Disconnect matrix documented behavior: host quit, client quit, Steam offline mid-match.

## 10. Risks, ranked (timeline killers first)

1. **Blueprint opacity.** The match flow, grant call sites, and party UI wiring are all in unread binary assets. Any estimate touching them (WP1.2, WP1.3, WP2.1) carries ±40% until WP0.3. Mitigation: WP0.3 is front-loaded and gated with a mandatory re-estimate; nothing in Phase 1 starts before that checkpoint.
2. **First-build risk.** No VCS provenance, a packaging config pointing at a missing build target, plugins needing local recompiles, and a project no one outside The Gang has ever built. If WP0.2 uncovers missing pieces (the `MajorLeagueCurveball` target, engine patch mismatches), day-one becomes a scavenger hunt with The Gang's availability (Olle: low) on the critical path. Mitigation: WP0.2 in week 1, escalate missing-file asks to The Gang immediately.
3. **Party/social replacement breadth.** `BackendMessagePump` feeds invites, presence, ready state, toasts, and queue states into an unknown number of widgets. WP1.3 has the widest band for a reason; the de-scope valve is dropping in-game presence/friend features to Steam-native only for EA.
4. **Listen-server game feel.** Tuned for 30 Hz dedicated servers with symmetric latency; now the host has 0 ms and peers have real internet. Deflection-timing fairness is the core mechanic. Risk of a tuning tail in WP1.4. Mitigation: test on real cross-network setups from week 5, not at the end; keep the experimental physics-prediction flags under suspicion.
5. **Host upload bandwidth at FFA sizes.** Max players is backend-configured and currently unknown (open question 2). If FFA is 8 to 10 players, a poor host's upstream becomes the match quality ceiling. Mitigation: measure in WP1.4, cap player count for EA accordingly, party leader (usually the most invested player) hosts.
6. **Grant service = new operated surface.** Small, but AP now runs a service the economy depends on, with security exposure if the signing scheme is sloppy. Mitigation: WP2.1's second-reviewer security gate; option D (accept-risk) documented as the explicit fallback rather than a silent slip.
7. **Third-party account handovers.** LootLocker (prod keys, billing), Steamworks app admin, GameAnalytics, Tolgee: all currently The Gang's. Any of these stalling blocks WP3.2/3.4 late in the schedule. Mitigation: request all four accesses in week 1, not week 7.
8. **Cheating in a premium EA without EAC.** Accepted consciously (section 4.3). Residual risk is host-side cheating in pub matches; the grant service caps economy damage. Revisit with EOS AC P2P in step 2.
9. **Perforce history is gone.** One zip, no history, no blame, no prior-version diffs. Every archaeology question costs a Gang round-trip. Nothing to do but note it.

## 11. Estimate and the 100K SEK / 2-month frame

| Phase | Hours (low to high) |
|---|---|
| Phase 0: Foundations | 44 to 80 |
| Phase 1: Steam P2P core | 118 to 190 |
| Phase 2: Authority + persistence | 46 to 68 |
| Phase 3: Strip, ship, harden | 80 to 124 |
| **Total (without WP3.5 stretch)** | **288 to 462, central ~350 h** |

Calendar: one full-time senior UE developer, **9 to 11 weeks** including Robert's QA cycles. Confidence: **medium** on shape and sequencing, **low-to-medium on Phase 1/2 hours until the WP0.3 checkpoint**, at which point this section gets revised with named confidence per WP.

Against the pitch frame, plainly:

1. **Timeline.** "~2 months starting after summer" is the optimistic edge of this estimate, reachable only if Phase 0 comes up clean and the party scope takes the de-scope valve (Steam-native social only). Planning reality is 2.5 months. I would tell LUG "8 to 10 weeks" now rather than walk back "2 months" later.
2. **Budget.** 100K SEK over ~350 h is ~285 SEK/h effective. That is well under market for senior UE networking work, so either Robin's arrangement absorbs it or the number is thin. That is a commercial call, not a technical one, but the plan should not pretend the work is 150 h.
3. **The mobile port is not in this plan and cannot fit the same envelope.** The original commercial target (100K including the mobile port) predates reading the code. P2P + Steam consumes the whole 2-month window on its own. Recommendation: rescope 100K to cover P2P + Steam PC EA, price the mobile port separately once EA data justifies it (it also stacks on this work: the abstraction layer and the removal of dedicated-server cost are prerequisites the port inherits for free).
4. What the money buys either way: after this plan, per-match infrastructure cost is zero, the only recurring backend is a trivially cheap grant endpoint plus LootLocker's existing bill, and the codebase has a provider seam where EOS (already scaffolded in the project: EOSIntegrationKit, EpicClient target, Epic CustomConfig) drops in for cross-platform as step 2 without touching gameplay. The assumed sequence (Steam PC first, mobile second, Epic/console capable via EOS) survives contact with the code; nothing in the tree argues for a different order, and going EOS-first instead would trade the lowest-risk Steam path for day-one crossplay nobody asked for in step 1.

## 12. Open questions (blocked on The Gang or on Blueprint export)

1. Which Steam app is real: config `SteamDevAppId=2981120` vs store page 2805120? (The Gang)
2. Max players per matchmaking configuration (FFA/DUEL/PRACTICE): lived in backend/GameLift config, not in the client. Need the numbers to size host bandwidth and session limits. (The Gang)
3. LootLocker account: production keys, ownership, billing going forward. (The Gang)
4. Does the in-game friend list (LootLocker friends + backend presence) need to survive step 1, or is Steam friends/invites acceptable for EA? Cost difference lands in WP1.3. (Robert/The Gang; recommend Steam-only for EA)
5. Exact match-end grant flow and every Blueprint call site of ServerGranter/LoadoutValidator: cannot determine until Blueprints are exported (WP0.3).
6. Whether any achievements/stats logic hides in Blueprints: cannot determine until WP0.3.
7. Tolgee account status and whether localization files are fully static at package time. (The Gang)
8. GameAnalytics account access + prod keys. (The Gang)
9. Is the `MajorLeagueCurveball` build target recoverable from The Gang, or renamed remains? Affects WP0.2 only mildly, but worth one ask. (The Gang)
10. How long does mlc-backend-dev.thegang.io stay up? Not a dependency of this plan, but useful as a behavioral reference during Phase 1. (The Gang)
