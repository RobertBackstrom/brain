# Curveball grant service (WP2.1)

| | |
|---|---|
| **Date** | 2026-08-27 |
| **Work package** | WP2.1 service half, moved forward from Phase 2 per [execution_plan_agent_build.md](../drafts/execution_plan_agent_build.md) Lane A1 |
| **Runtime** | Node 22 on the AP VPS, zero dependencies (`node:sqlite`, `node:http`, `node:crypto`) |
| **Status** | Runs against the LootLocker mock, 26 tests green. Not deployed, not yet pointed at real LootLocker. |

## Why this exists

In the shipped build, the question "is this player allowed to be granted this" is answered by
`UHelperLibrary::IsWorldDedicatedServer`. The machine asking was The Gang's, so it was trusted, and
`ULootLockerServerGranter` calls LootLocker directly with the server key.

Under P2P the machine asking is a player's PC. Handing it the LootLocker server key would let any
host grant themselves the entire catalogue. So the server key moves here, to a service Aurora Punks
runs, and the host asks this service instead of LootLocker. Trust gets replaced by two things:

1. **Authentication**, so we know which Steam account is asking.
2. **Plausibility rules**, so a compromised host is bounded in what it can take, and the ledger
   records what it took.

This service is the only part of the P2P conversion that has no Unreal dependency, which is why it
was pulled forward and built before the build machine exists.

## API

All endpoints are POST, all bodies JSON, all responses `{ ok, result }` or `{ error, detail }`.

| Endpoint | Body | Notes |
|---|---|---|
| `GET /health` | | No auth. Reports auth mode and whether the mock is in use. |
| `/v1/matches` | `{ matchId, mode?, players: [{ playerId, ulid?, steamId? }] }` | Host opens a match and declares who is in it. Grants outside this roster are refused. |
| `/v1/matches/close` | `{ matchId }` | Closes the match. Grants after close are refused. |
| `/v1/grant/assets` | `{ requestId, matchId, playerId, assetIds: [int] }` | Replaces `GrantAssetsToPlayer`. |
| `/v1/grant/currency` | `{ requestId, matchId, playerId, walletId?, currencies: [{ currencyId, amount }] }` | Replaces `AddCurrencyToPlayer`. Negative amounts debit, positive credit, same currency twice is summed. |
| `/v1/grant/progression` | `{ requestId, matchId, playerId, progressionKey, amount }` | Replaces `AddProgressionForPlayer`. Zero is refused, as in the original. |

`requestId` is the idempotency key. The game's `ULootLockerApiQueue` retries failed server calls, so
the same grant will arrive more than once; the second call returns the first call's result and
grants nothing further.

## Auth

Signed request. Canonical string is `METHOD\nPATH\nTIMESTAMP\nNONCE\nsha256(body)`, HMAC-SHA256,
sent as `X-MLC-Signature` with `X-MLC-Timestamp`, `X-MLC-Nonce` and `X-MLC-Steam-Id`. A 60 second
timestamp window bounds replay, a nonce cache blocks replay inside the window.

**Why the shared secret is not enough.** In `hmac` mode the secret lives in the game client, so a
determined player can extract it and sign their own grants. The rules below still bound the damage,
but the identity is asserted rather than proven, and the ledger records that per grant
(`identity_proven`). Early Access should run `steam` mode, which additionally verifies the caller's
Steam session ticket through `ISteamUserAuth/AuthenticateUserTicket`.

**That needs a Steam Web API publisher key for app 2805120, which we do not have.** The ticket
verifier is injected (`SteamVerifier`), so the mode is wired, tested and reviewable now, and turning
it on is a config change plus a key. This is the first genuine access requirement the build has
surfaced, which is exactly what "build first, see what we actually need" was for.

## The rules

Ported from `LootLockerServerGranter.cpp` and `LootLockerServerLoadoutValidator.cpp`, plus what P2P
newly requires. All limits are environment-configurable, see `src/config.js`.

1. **Soft-currency cap**, `SOFT_CURRENCY_CAP = 6000` on currency `01HSX2NNRWJWXBP89K9Z78VJKC`.
   Reads the live wallet balance and clamps the credit to `max(cap - balance, 0)`, identical to
   `CreditCurrencyToPlayerCapped`.
2. **Roster check.** A grant must name a player who was declared in the match.
3. **Match must have been played.** Grants against a match younger than 30 seconds, already closed,
   or older than an hour are refused. This is what stops open-and-harvest.
4. **Per-match caps** per player: currency, asset count, progression points.
5. **Rolling window caps** per player across matches, so opening fresh matches does not reset the
   budget. Debits do not buy back headroom, otherwise credit-debit-credit walks past the cap.
6. **Allow lists** for currency ids, progression keys and asset ids. Empty by default because the
   real key set is a WP0.3 question (the Blueprints hold it). Configure to lock down.

Caps are evaluated against the ledger, not against the request, so splitting a grant into pieces
hits the same ceiling as asking for it all at once.

## Running

```bash
node --test "test/*.test.js"   # 26 tests, no network, no LootLocker access needed
npm start                      # mock backend unless LOOTLOCKER_SERVER_KEY is set
```

With no `LOOTLOCKER_SERVER_KEY` the service uses `MockLootLocker`, an in-memory wallet, inventory
and progression store. That is deliberate: the whole service is exercisable end to end while the
LootLocker access request sits unanswered.

## What is unverified

The LootLocker request paths in `src/lootlocker.js` (`ENDPOINTS`) are written from the shape of the
calls the UE server SDK makes and **have not been checked against the LootLocker API reference**,
because we have no access to game `a86igukp`. They are isolated in one object so confirming them is
a single edit. Nothing else in the service depends on them, and no test does.

## Not done here

1. Deployment. A systemd user unit is drafted in `grant-service.service` but not installed, and
   nothing is exposed publicly yet.
2. The client half of WP2.1: the UE side that calls this instead of `ULootLockerServerGranter`.
   That needs the build machine and belongs to Lane B.
3. Match result reporting. `IMatchResultReporter` in `../drafts/online_interfaces/` is the intended
   caller, so grant plausibility can later be checked against a reported scoreline rather than only
   against caps.
