# `Online/` interface design, for review

| | |
|---|---|
| **Date** | 2026-08-04 |
| **Author** | The Assistant |
| **Item** | A4 of [execution_plan_agent_build.md](../execution_plan_agent_build.md); implements section 6 of [dev_plan_p2p_steam.md](../dev_plan_p2p_steam.md) |
| **Status** | Headers only. No implementation, deliberately, until the build machine exists. |
| **Destination** | `Source/Mogadishu/Public/Online/` once we have a repo |

These six headers are the surface EOS drops into at step 2 and a console OSS drops into at step 3.
They are far cheaper to argue about now than after two implementations sit on them, which is why
they come before anything else.

## The six files

| File | Replaces |
|---|---|
| `MLCOnlineTypes.h` | shared types, no platform includes |
| `IPlatformIdentityProvider.h` | Steam auth ticket path currently inside `LootLockerLocalPlayerSubsystem` |
| `IMatchSessionProvider.h` | GameLift placement: `start/stop/get-solo-matchmaking-status` |
| `IPartyProvider.h` | the eight `/api/v1/parties/*` endpoints + the party half of the message pump |
| `IMatchResultReporter.h` | `LootLockerServerGranter`, the trusted-server write path |
| `MLCOnlineSubsystem.h` | the holder; picks implementations from CustomConfig |

## Five decisions worth pushing back on

**1. `FMLCPlayerHandle` carries both identities, and every API takes it.**

The backend keys everything on LootLocker ULID; Steam lobbies key everything on SteamID64. Rather
than converting at call sites, the handle carries both and providers take the handle. The mapping
then cannot be forgotten, because if you can name a player you have both halves. Cost: a slightly
heavier value type passed around, and `IsFullyResolved()` checks in party paths. I think that is a
good trade; the alternative is a class of bug that only shows up with a real second player on a real
network, which is the most expensive place to find it.

**2. Plain C++ interfaces, not `UINTERFACE`.**

No reflection, no Blueprint exposure, no `UObject` lifetime. `UMLCOnlineSubsystem` is the only
`UObject` and it owns the providers by `TSharedPtr`. Blueprint keeps talking to the existing
subsystems, which keep their exact signatures. If we ever genuinely need a Blueprint-implementable
provider this decision has to be revisited, but nothing suggests we will.

**3. `FindOrHost` is one call, not `Find` then `Create`.**

Every caller wants "get me into a match". Splitting it pushes the find-failed-so-host race onto the
caller, which is exactly where that bug would live. `HostSession` stays separate for the party-leader
case, where searching would be wrong because the group has already decided who plays together.

**4. Failure degrades, it does not crash.**

Accessors never return null. When a provider cannot be built (no Steam client, offline dev build) a
null-object implementation is installed: calls complete with `NotReady`, queries return empty. This
is mostly so PIE without Steam running keeps working, since that is how most iteration happens.

**5. Result reporting is per round and comes from clients too, not only the host.**

Both follow from decisions already taken. Round-boundary reporting is what stops a host quitting
mid-match from also costing everyone their earned progression, given no host migration in step 1.
Clients reporting independently is what makes the grant service's cross-report check possible; a
host reporting alone proves nothing about a host that cheats.

## What these headers deliberately do not do

1. **No implementation.** Writing `FSteamSessionProvider` against `IOnlineSubsystem` and
   `SteamSockets` without a compiler would produce plausible code that has never been checked, which
   is worse than no code. Implementation starts after B1.
2. **No platform SDK includes anywhere in `Public/`.** If a compile error ever names Steam outside
   `Private/Online/`, an abstraction has leaked. Worth treating as a build rule, not a convention.
3. **No opinion on max players per mode.** `MaxPlayers` is a parameter because those numbers lived in
   backend config and The Gang has not given them to us yet (open question 2 in the Fable plan).

## Open items this surfaces

1. ~~Copyright headers.~~ **Settled (Robert, 2026-08-04): keep The Gang's existing header unchanged
   on new files.** Applied to all six. If the co-dev agreement lands somewhere else on IP, a header
   sweep is one commit, so this costs nothing to revisit.
2. **Invite timeouts have no Steam equivalent, and the standard answer is not to build one.** Steam
   lobby invites do not expire server-side; an invite stays valid while the lobby exists and has
   room, and joining a dead one simply fails. What shipped games actually do: a **client-local
   send-cooldown** to stop invite spam (which is exactly what `BlockInvitesUntil` was doing), a
   pending-invite list that is UI state only, and a graceful "lobby no longer available" on a failed
   join. So `BlockInvitesUntil` survives as-is on the client, `OnPartyInviteTimeout` becomes a local
   timer for greying out a row, and nothing needs a server. Confirm the UI wiring at WP0.3.
3. **Presence narrows to Steam friends.** The backend answered presence for any player the client
   registered interest in. `IsPlayerOnline` returns false-for-unknown rather than guessing offline,
   so the UI can distinguish. Whether that is acceptable for EA is Fable's open question 4, and I
   recommend yes.
