# Curveball: what The Gang's backend does, and what replaces it

| | |
|---|---|
| **Date** | 2026-08-04 |
| **Author** | The Assistant, read directly from `code-corpus/repos/curveball-bba/Source/Mogadishu/` |
| **Scope** | The `mlc-backend-dev.thegang.io` service only. LootLocker, GameAnalytics and Tolgee are separate and stay. |
| **Companion to** | [dev_plan_p2p_steam.md](dev_plan_p2p_steam.md) sections 5 and 6 (Fable) |

The service source was not in the delivered zip and has been asked for. Everything below is
reconstructed from the **client side**, which is enough to specify a replacement because the client
is the only consumer. Where the server's internal behavior matters and cannot be inferred, it is
marked **[ASK]**.

## 1. The complete API surface

Base URL comes from `UMLCDeveloperSettings::BackendBaseURL`, set in `Config/DefaultGame.ini:131`.
Eleven endpoints, three groups.

### 1.1 Matchmaking (`MatchmakingSubsystem.cpp`)

| Endpoint | Verb | Request | Response fields consumed |
|---|---|---|---|
| `/api/v1/start-solo-matchmaking` | POST | `{ region_latency: {region: ms}, matchmaking_configuration_key }` | status |
| `/api/v1/get-solo-matchmaking-status` | POST | none | `Status`, `IP`, `Port`, `MatchmakingStartedAt`, `EstimatedWaitTime`, `PlayerSessionId`, `QueuedPlayerCount` |
| `/api/v1/stop-solo-matchmaking` | POST | none | status |

Polled on a timer from `UMatchmakingSubsystem::Tick` while `bIsRunning`. The status response is the
GameLift session placement: the client is handed an `IP:Port` of a spun-up dedicated server plus a
`PlayerSessionId` to present on connect.

`EMatchmakingConfiguration` is a three-value enum: `FFA`, `PRACTICE`, `DUEL`. The configuration key
sent to the backend is a string; `UMatchmakingData::GetMatchmakingConfigurationFromMatchmakingData`
reverse-maps by substring-matching `"duel"` / `"practice"` inside a GameLift
`MatchmakingConfigurationArn`, defaulting to FFA.

### 1.2 Party (`GamePartySubsystem.cpp`)

| Endpoint | Verb | Body |
|---|---|---|
| `/api/v1/parties/create` | POST | none |
| `/api/v1/parties/{partyId}/invite/{playerUlid}` | POST | none |
| `/api/v1/parties/{partyId}/join` | POST | none |
| `/api/v1/parties/{partyId}/leave` | POST | none |
| `/api/v1/parties/{partyId}/kick/{playerUlid}` | POST | none |
| `/api/v1/parties/{partyId}/setreadystate` | POST | `{ is_ready, region_latency }` |
| `/api/v1/parties/{partyId}/loadoutupdated` | POST | loadout payload |
| `/api/v1/parties/{partyId}/setpartygamemode` | POST | `{ gamelift_matchmaking_configuration }` |

Party state comes back as `FPartyResponse`: `id`, `pending_invites[]`, `players[]` (each with
`player_ulid`, `name`, `is_leader`, `is_ready`), `ticket_id`, `gamelift_matchmaking_configuration`.

### 1.3 Message pump (`BackendMessagePump.cpp`)

| Endpoint | Verb | Body | Cadence |
|---|---|---|---|
| `/api/v1/messages/pop?ignoreLastReadFilter=<bool>&apiVersion=2` | POST | `{ check_presence_player_ulids[], party_id }` | every **3.0 s** (`MESSAGE_POP_INTERVAL`) while listening |

This is the push channel, implemented as polling. It returns `messages[]` (`message_type`,
`message`, `message_data`, `sender_name`, `sender_player_ulid`, `id`, `created_at`) and
`player_ulid_is_online` (a presence map for whichever players the client registered interest in).

Message types (`EPumpMessageType`):

- Server-originated: `PARTY_INVITE`, `PARTY_UPDATED`, `PARTY_READY_STATE_UPDATED`,
  `PARTY_PLAYER_LOADOUT_UPDATED`, `PARTY_YOU_LEFT`, `TOAST_MESSAGE`, `GAME_UNAVAILABLE`,
  `PARTY_ENTERED_QUEUE`, `PARTY_LEFT_QUEUE`
- Client-local, injected via `PushLocalMessage`: `FRIEND_REQUEST_RECEIVED`

`TOAST_MESSAGE` and `GAME_UNAVAILABLE` are operator broadcast channels: The Gang could push a banner
or take the game offline remotely. Nothing in P2P replaces those, and nothing needs to, but note
that **`GAME_UNAVAILABLE` is a remote kill switch on a service we are told to stop depending on**.
Worth confirming no Blueprint treats its absence as an error state. **[ASK / WP0.3]**

## 2. Three findings that change the design

### 2.1 Identity is LootLocker ULID, not Steam ID

Every party operation is keyed on `player_ulid`, a LootLocker identifier. Steam lobbies are keyed on
`SteamID64`. A Steam-lobby-backed party therefore needs a **bidirectional ULID ↔ SteamID64 mapping**,
maintained per party member, or every consumer of `FPartyPlayerResponse.player_ulid` breaks. This is
not mentioned in the Fable plan's section 6 and it is the single most likely source of silent
breakage in WP1.3.

Recommended: publish the ULID as Steam lobby member data (`SetLobbyMemberData("ulid", ...)`) at join
time, and have `IPartyProvider` present the same `FPartyResponse` shape it does today. The mapping
then lives entirely inside the provider, and no caller changes. Requires that the LootLocker session
is established before the lobby is joined, which it is today (Steam auth ticket to LootLocker session
already exists in `LootLockerLocalPlayerSubsystem`).

### 2.2 GameLift-shaped fields are Blueprint-visible and must stay populated

`FPartyResponse` exposes `ticket_id` and `gamelift_matchmaking_configuration` to Blueprint. Freezing
the struct (the plan's load-bearing trick) is not enough: if Blueprint logic branches on those being
non-empty, leaving them blank under Steam breaks the flow just as surely as deleting them.

Recommended: populate `gamelift_matchmaking_configuration` with the same key strings today's backend
uses (so the `"duel"`/`"practice"` substring reverse-mapping keeps working untouched) and
`ticket_id` with the Steam lobby ID. Cheap, and it keeps the existing parsing honest. Confirm actual
Blueprint usage at WP0.3 before relying on this.

### 2.3 `region_latency` dies, and it is sent from two places

The GameLift region-ping map is a parameter of both `start-solo-matchmaking` and `setreadystate`.
Under Steam, routing is Valve's problem and the field is meaningless. Both call sites drop it, and
`GameLiftRegionLatency` comes out of the plugin list. Low risk, but it is two removals, not one.

## 3. What replaces what

| Backend capability | Replacement | Notes |
|---|---|---|
| Solo matchmaking start/status/stop | Steam session search, create-if-none-found | `FStatusUpdateEvent` keeps its exact 7-param signature; `IP` carries `steam.<SteamID64>`, `Port` unused or `"0"` |
| `EstimatedWaitTime`, `QueuedPlayerCount` | Local estimates | No queue exists any more. Return search-elapsed and result count, or fixed placeholders. Cosmetic, but the UI reads them **[WP0.3]** |
| Party create / join / leave / kick | Steam lobby create / join / leave / kick | Leader = lobby owner |
| Party invites | Steam overlay invites + lobby invite API | Replaces `pending_invites[]` semantics; the invite-timeout path (`BlockInvitesUntil`, `OnPartyInviteTimeout`) has no Steam equivalent and becomes client-local |
| Ready state | Lobby member data flag | Push-updates arrive via Steam lobby callbacks, not the 3 s poll |
| Party game mode | Lobby data field, leader-writable | |
| Loadout sharing between party members | Lobby member data, or keep the existing LootLocker public-profile fetch | `FetchOtherPlayerLoadout` already reads other players' loadouts from LootLocker; simplest path is to keep that and drop the pump message |
| Presence (`player_ulid_is_online`) | Steam friends presence | Only works for Steam friends. Non-friend party members lose presence. Recommend accepting for EA (open question 4 in the Fable plan) |
| `TOAST_MESSAGE` | Nothing, or a static remote JSON | Optional. A file on the AP VPS behind the same domain as the grant service costs nothing |
| `GAME_UNAVAILABLE` | Nothing | Deliberately dropped. Confirm no Blueprint depends on receiving it **[ASK]** |
| `FRIEND_REQUEST_RECEIVED` | Unchanged | Already a local message; `PushLocalMessage` stays, the pump shrinks to a local bus |

The message pump does not survive as an HTTP client. It becomes a **local event bus** with the same
`OnMessageReceived` delegate signature, fed by Steam lobby callbacks and local pushes instead of a
3-second poll. Every Blueprint subscriber keeps working. This is a better outcome than the plan's
"retire or reduce" phrasing suggests: the pump's *interface* is exactly the right shape for a
callback-driven implementation, it was just wired to a poll.

## 4. What this means for the estimate

The party rewire (Fable's WP1.3, 40 to 60 h, the largest single band) gets a little more predictable
with this mapping done: the endpoint list is closed, the state shape is known, and the pump keeps its
delegate surface. What stays unknown is purely how many **widgets** touch these fields, which is a
WP0.3 question, not a backend question.

The one item that grew: the ULID ↔ SteamID64 mapping in 2.1 is real work that was not previously
called out. Small (it rides on lobby member data) but it is on the critical path for every party
feature, so it belongs in WP1.1 with the identity provider, not in WP1.3.

## 5. Open items for The Gang

Already asked in the 2026-08-04 mail: whether the service source or a spec exists, and how long the
dev instance stays up. Additionally:

1. What are the actual `matchmaking_configuration_key` strings per mode? The client sends a key it
   receives from party state; the enum reverse-map only pattern-matches on the returned ARN.
2. Max players per configuration (also Fable's open question 2). Backend-side, not in the client.
3. Does anything other than the game client call this API (a web dashboard, an ops tool)? Affects
   whether The Gang cares about keeping it alive.

## 6. Incidental observation

`BackendMessagePump.h` carries an author comment: `NOTE(Robin): Set by the party system so the
message pump can query the party_id ... I cannot be bothered to break up the message pump into two
parts`. Checked with Robert 2026-08-04: **not Robin Hofström**, a different Robin at The Gang. Noted
only because the comment is a useful signal that the pump's party coupling was a known shortcut
rather than a design decision, which supports collapsing it to a local event bus in section 3.
