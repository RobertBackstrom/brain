# CM Agent — Cross-Project Learnings

## 2026-08-19 — Discord cannot force-add a user by ID, and a failing invite is usually not the invite (k2c)

Robert supplied an external contractor's Discord user ID and asked for him to be invited.
**There is no API route to add a user to a guild by ID.** `PUT /guilds/{id}/members/{user}`
requires an **OAuth2 access token for that user with the `guilds.join` scope**, which means the
user has to authorise it. With a bot token alone, a link is the only route. The ID is still
worth having: `GET /users/{id}` confirmed the account was real and matched the person.

**Diagnose before reissuing.** The invite Robert had shared was reported as "Invalid Invite /
Unknown Message", and it turned out to be **completely valid** — it resolved via
`GET /invites/{code}` with a month left to run. Checks worth running, in this order:

1. `GET /invites/{code}` — does it resolve at all?
2. `GET /guilds/{id}` — `verification_level` (4 = needs verified phone) and `features` for
   `MEMBER_VERIFICATION_GATE_ENABLED`. Both were clear here.
3. `GET /guilds/{id}/bans/{user}` and `/members/{user}` — banned, or already a member?

All clear meant the failure was **client-side**, and the useful advice was: paste the URL in a
browser rather than clicking the embed, restart the client, check the 100-server limit, check
the account's email is verified. Note "Unknown Message" is error **10008**, which is about a
*message* reference rather than an invite, so it points at a stale client embed.

**Invite hygiene found in passing:** the guild had **two channels both named `general`** with
different invites pointing at each, which is a real hazard when onboarding an external
contractor. Prefer a **fresh single-purpose invite** with an expiry and low max-uses over
reusing a long-lived unlimited one.


This file accumulates knowledge from Aurora Punks Discord community management — onboarding, role-based access, and invite hygiene — across all CM work.

## 2026-08-17 — "Give X access to all channels" resolved to one bot-only channel; resolve the ask to concrete deltas before touching anything (K2C)

**Context:** Robert asked the bot in Discord to "make sure @Dubi has access to all channels". The
phrasing sounds like a broad grant. Enumerating it first turned it into a decision about a single
channel, and then into no change at all.

**1. Enumerate the delta before proposing a mechanism.** Dubi already saw **11 of 12** channels. The
whole request reduced to `#brief`. Had I reached for `provision`/`grant` on the phrasing alone, I
would have built a role scheme for a problem that was one channel wide. **Compute "what does this
person see today vs. what would change" and lead with that number.**

**2. The gated channel was gated *against everyone*, not just the newcomer.** `#brief`
(`1493262512693575750`) has `@everyone` DENY and exactly one ALLOW: the Death Board bot itself. No
human is in it; Robert only sees it through owner permission bypass. It carries morning briefings,
Daily Catch-ups, Gemini standup notes, and new-ticket alerts. **A channel with a single bot ALLOW is
an output sink, not a private team room** — granting a human there is a disclosure decision, and it
makes them the first human in the room. Read the overwrite list before assuming "gated" means "gated
to a group".

**3. The K2C guild has no member roles at all.** The only role is the bot's own managed `Death
Board`. Access there is per-channel user overwrites. The `role_channel_map.json` keys (`board`,
`ap-finance`) are **AP-guild-only** — and note `cm-channel-admin.js list --guild <k2c>` still prints
those AP entries, because `list` echoes the map rather than reading the target guild. That output is
misleading on any non-AP guild; enumerate channels directly instead.

**4. Identify the person before widening access in a client guild.** "Dubi" (`dubi2583`,
`860463384847712266`) appears nowhere in the wiki — not in the K2C people lists (Niclas/Ishani/Alan
at Raw Fury, Tim, Imi, Oskar, Fredrik). Robert confirmed **external**. In a co-dev guild that
contains the publisher and external partners, an unidentifiable name is itself a reason to stop and
ask. Now recorded in `k2c_sands_of_duat/CLAUDE.md`.

**Outcome:** no Discord change. The team channels are ungated, so the request was already satisfied.

**Tags:** k2c, discord, channel-access, overwrites, enumerate-first, external-partner, cm-channel-admin

## Agent stood up (2026-06-18, Aurora Punks)

**Context:** Created the CM agent and wired guild onboarding into the existing always-on bot. No separate bot — everything runs through `discord-bot.js` (the `DeathBoardBot` in `deathboard.service`).

**Architecture decisions worth remembering:**
1. **Config-over-code.** Onboarding and access are driven by two JSON files under `aurora_punks/` (`pending_discord_access.json`, `role_channel_map.json`), re-read on every event. Adding a person or granting access = a JSON edit, no bot restart. Only intent/event-wiring changes need a restart.
2. **Pending entries are consumed on grant.** `_onGuildMemberAdd` deletes the matched entry after assigning roles, so a rejoin doesn't silently re-grant. If you need a re-grant, re-add the entry.
3. **`grantChannelAccess(userId, roleKey)` is the access API.** Other agents call it instead of touching `member.roles`. It only assigns the role — the *channel's permission overwrite on that role* is what grants visibility, so a new role-channel pair must have the overwrite in place (deny `@everyone` ViewChannel, allow the role) before it's added to the map.
4. **No Administrator perm.** Guild role-assign + per-channel overwrites cover everything. Don't reach for admin.
5. **Stale-invite cleanup is a separate oneshot** (`cm-invite-cleanup.js`) on a systemd timer, not bot-internal — keeps the sweep observable per-run and off the always-on bot's hot path. Only needs the non-privileged `GuildInvites` intent; the bot itself needs the privileged `GuildMembers` intent for `guildMemberAdd`.

**Known IDs (AP guild `616345869490454593`):**
- Board role `1517102080655888394` → #board `1511348246558019705`
- AP-Finance role `1517103637887844413` → #ap-finance `1517103667030003783`

**Gotcha:** the `GuildMembers` intent is privileged — it must be enabled in the Discord dev portal *and* declared in the bot's `Client` intents. If the portal toggle is off, the bot fails login with a disallowed-intents error and crash-loops. If onboarding silently stops working, check both.

**Open follow-up:** Alexander has no Discord ID yet (not in guild) — parked in `pending_no_id`. Move him into `pending` keyed by ID once he joins / the ID is known. Ali (`199282124501680128`) and Daniel (`363008257310064640`) are live in the pending list for the Board role.

## Deployment findings (2026-06-18, Aurora Punks)

1. **Invite cleanup needs the `Manage Guild` permission — the bot doesn't have it yet.** `guild.invites.fetch()` returned `Missing Permissions` on the first timer run. Guild-wide invite fetch/delete requires `MANAGE_GUILD` (a specific permission, NOT Administrator). The timer is installed and scheduled (daily 04:30) but will keep failing until someone grants the bot Manage Guild in the AP guild. Member-watch + role-assignment are unaffected (they use Manage Roles, which the bot already has from managing the OPS category). **Action for next time:** confirm the bot's role in the AP guild includes Manage Guild before relying on invite cleanup; verify with `node cm-invite-cleanup.js --dry-run`.
2. **AP-guild bot is denied ViewChannel on ~50 channels** (confirmed via `cm-diagnose.js`). It can see #board and #ap-finance (so CM onboarding works) but NOT most community channels (talk-with-the-devs, gametester-bugs, off-topic, etc.) — nor its own OPS category (`agent-relay`/`alerts`/`brief`), which is the source of the startup `Missing Access` line (a pre-existing db-088 bug: @everyone ViewChannel deny was never paired with an explicit allow for the bot's role). Any Discord coverage for the needs-response watch requires granting the "Death Board" role ViewChannel on the target channels first. Diagnostic tool: `node assistant/cm-diagnose.js`.
3. **Restarting the bot is non-trivial — watch for a port squatter.** The bot lives in `server.js` (`deathboard.service`). On 2026-06-18 the systemd unit had been crash-looping ~1117 times on `EADDRINUSE :3777` because a manually-started `node assistant/server.js` was squatting the port and holding stale code. Clean restart = `systemctl --user stop deathboard.service` → kill the manual PID holding 3777 (`ss -ltnp | grep 3777`) → `systemctl --user start deathboard.service`. systemd then binds and loads fresh code. Expect one transient EADDRINUSE on the first start attempt as the port frees; the auto-restart binds cleanly. The `GuildMembers` privileged intent was already enabled in the dev portal (login succeeded without a disallowed-intents error).

## Community Bot ownership + needs-response watch (2026-06-18, all forums)

**Context:** Robert asked CM to "catch all unanswered questions or threads that look like they should be answered by me, across all forums, like a webscrape." This already had an architecture — don't rebuild it.

1. **The Community Bot (db-065) already exists and is `done`.** Four trackers (Discord scanner in `discord-bot.js`, `reddit-tracker.js`, `steam-forum-tracker.js`, `youtube-tracker.js`) write normalized events to `assistant/community-events/<source>-<date>.jsonl`. The orchestrator (`community-bot-orchestrator.js`) opens a reply-draft ticket per event under db-065 using KEYWORD heuristics (its `classify()` literally says "v1 — no LLM"). Per-project config lives in `<project>/community_config.json`.
2. **The new "skill" = an LLM layer on top, not a rebuild.** `cm-needs-response-digest.js` reads the same event store, LLM-judges "unanswered + waiting on a dev?" (conservative), and emits ONE digest (disk + a single `gen` ticket when flagged) instead of N tickets. Daily 08:00 Stockholm via `cm-needs-response-digest.timer`. Skill doc: [[community_needs_response_watch]].
3. **LLM access pattern on this VPS = shell out to the `claude` CLI** (`/home/assistant/.local/bin/claude --model <id> -p <prompt>`), NOT the SDK/API key. Copied from `gmail-triage-unread.js`. Model `claude-sonnet-4-6` works via the CLI (verified). Parse JSON out with `out.match(/\[[\s\S]*\]/)`.
4. **CM owns community-management routing.** toa-016 caught Community Bot tickets mis-routing to Analytics because no agent owned the domain. That's now CM.
5. **Verified live:** dry-run against the real Steam events correctly flagged a crafting-bug (HIGH) and a quest-drop question (MED) with sensible reply angles. Pipeline (read → CLI classify → digest) works end-to-end.
6. **v1 limitation:** answered-state is judged from the event snippet, not a reply chain (trackers emit posts, not thread state). True answered-detection needs the trackers to capture replies — a DevOps enhancement under db-065. Acceptable for a safety net.

## Channel/role self-service CLI + the Discord bootstrap invariant (2026-06-19, Aurora Punks)

**Context:** Robert wanted CM to handle channel/role assignments itself ("full lifecycle, everything auto") so he never clicks Discord. Built `assistant/cm-channel-admin.js` (standalone on-demand CLI, same pattern as cm-invite-cleanup/cm-diagnose). Verified live: `create-channel --gate-role` created + gated a new channel correctly.

1. **The capability works fully for anything CM *creates*.** create-role, create-channel, gate, provision (role+channel+gate+map in one shot) all succeed because the bot owns the permission overwrites at creation time. `provision` writes `role_channel_map.json`, which the always-on bot re-reads per event → `grantChannelAccess(userId, '<key>')` works instantly, no restart.

2. **HARD Discord invariant — the bootstrap problem.** The bot **cannot grant itself (or any role) ViewChannel on a pre-existing channel it is already denied** — every `permissionOverwrites.edit()` on the ~50 locked AP channels returned **`Missing Access` (50001)**. ManageRoles + ManageChannels guild-wide are NOT enough: you cannot manage a channel you cannot see. **Only Administrator bypasses a ViewChannel deny** — and the CM charter forbids Administrator. So retrofitting the bot into existing locked channels needs a ONE-TIME admin action from Robert (add the Death Board role ViewChannel-allow on the categories — synced children inherit — or a momentary Administrator toggle to run the batch, then revoke). After bootstrap, CM self-serves everything. This is *the* reason earlier "give it global view" couldn't be done short of admin.

3. **Death Board role ID = `1501135236300406947`** (bot's top role @ position 4 in the AP guild). Use it as the `--role` for granting the bot itself view on channels.

4. **Public categories to grant the bot into (for needs-response Discord coverage):** 1993 Space Machine `636197034478665728`, Aurora Punks `668838326802972700`, Robot Lord Rising `768750759838875678`, Giveaways and Competitions `778912863430508574`, Ark Gametesting `1326896106130374717`. Plus the bot's own **OPS** category `1501135625405862040` (agent-relay/alerts/brief) — granting Death Board view+send there fixes the long-standing db-088 startup `Missing Access` line. **DONE (2026-06-19):** Robert toggled Administrator on the Death Board role briefly; CM laid down explicit ViewChannel overwrites on all community channels (view) + OPS (view+send) via `cm-channel-admin.js grant`, then Admin was toggled back off. Verified post-Admin: the bot now sees all of them; db-088 startup Missing Access is fixed; ManageGuild invite-fetch works (11 invites). Still denied (deliberately, least-privilege): Admin section, moderator-only, friend-control-panel, keys, log, bot-test, Beta-test, Bot Stuff, and the internal dev-team channels (rlr-*-internal, uefn-internal, ark-*-internal, ark-eod, art/design/programming, ARK ART, Design, Meeting).

5. **`clientReady` not `ready`.** discord.js now deprecates the `ready` event in favour of `clientReady`; new standalone scripts should listen on `clientReady` to avoid the warning (cm-invite-cleanup.js still uses the old name).

## grant-read command + read-only coverage policy (2026-06-24, Aurora Punks + cross-guild)

**Context:** Robert wanted the CM agent to manage channel permissions itself, "only approvals here," to unblock Discord→RAG ingestion (which had emitted ZERO events: `rag-discord-indexer.js --stats` = 0 docs, no `community-events/discord-*.jsonl`, no `community-state/discord.json`). Root cause was channel visibility, not config/code (config loads fine: `[Community] Loaded configs for 2 guild(s)`; capture is wired `onMessage`→`_onCommunityMessage`).

1. **New tool: `cm-channel-admin.js grant-read --channels <id|key[,...]> [--role <id|key>] [--guild <id>]`.** Grants the bot itself (default) or a role ViewChannel + ReadMessageHistory on existing channels. Never touches @everyone/SendMessages, so it's read-only coverage, not member access. Added `--guild` so it targets K2C/Deathboard too. This is the standing-policy-safe action (see cm.md Rules).

2. **Standing policy (Robert approved 2026-06-24):** CM may run grant-read on watched-project `community_config.json` channels WITHOUT per-change approval; member-access changes (gate/ungate, @everyone, roles, create/delete) still need in-session approval. Always --dry-run first.

3. **Per-guild bot permission reality (verified via `GET /users/@me/guilds`):** AP `616345869490454593` = Manage Channels + Manage Roles, NO Admin (correct, least-privilege). Deathboard `1483101431111094464` + K2C Sands of Duat Dev `1492150019833467010` = **Administrator** (Robert chose 2026-06-24 to leave Admin as-is despite the db-190 HIGH finding — note stays open). Admin is what lets grant-read bypass a ViewChannel deny in those two guilds.

4. **The bootstrap invariant still bites in AP only.** Confirmed live: of the 12 AP watched channels, 11 already have the Death Board role ViewChannel-allow (from the 2026-06-19 grant) and are ready; only **#board `1511348246558019705`** is `@everyone deny, no role allow` → grant-read returns Missing Access 50001, needs a one-time Admin toggle. Reason: Manage Channels+Roles is NOT enough to manage a channel you can't see; only Administrator bypasses (the documented invariant). #board is the GDPR-sensitive board channel — gate its ingestion on the visibility-scoping decision, don't just toggle it on.

5. **Why "zero events" with 11 visible channels:** those are low-traffic community sub-channels; seeding emits nothing on first sight (flood prevention), and no qualifying message has arrived since the bot's last restart. Plumbing is correct, just starved of input. The high-value channel (#board) is the denied one.

6. **RAG ingestion privacy gap (still open, DevOps):** `indexContent()` does NOT honour the `visibility` field — every `source='discord'` doc is searchable by all agents, and discord docs have no retention TTL. Decide a visibility model before ingesting external-party channels (#board: Amer/Mattias; K2C: Raw Fury). See `rag-discord-indexer.js` header + `devops/db-190_discord_ingestion_plan.md`.

## Community response drafting — player "can't find X in new version" (2026-07-11, Tears of Adria)

**Context:** Player asked "can't find garrison in the new version?" after ToA's March 2026 visual overhaul + UI rework. Community Bot's initial draft was generic ("reading through, will come back"). Improved it by:
1. Acknowledging the recent update ("got some love in the March update")
2. Explaining the relocation ("moved during the UI overhaul")
3. Guiding to likely new location (town screen, settlement, tavern menu)
4. Inviting follow-up if still stuck

**Pattern:** When players report "can't find X after the update," search the wiki for recent major patches. UI/visual overhauls often relocate familiar mechanics. Better response = acknowledge change + guide to likely new location, rather than generic deferral. If exact new location is unknown, draft should still be helpful (guide to menu category) while flagging for Robert to refine with specifics.

## Tears of Adria: Stance toggle (ranged/melee mode) (2026-07-17, Tears of Adria)

**Context:** Steam forum player confused: "I equipped a bow but my hero still punches enemies — how do I use ranged attacks?" Community member answered: it's a **stance toggle in the character screen** (switches combat mode independently of equipment).

**Mechanic:** Ranged vs melee mode is controlled by a stance toggle, NOT equipment alone. A player can equip a bow and still be in melee stance (= punches), or equip a sword and be in ranged stance (= bow/spell attacks if equipped). The UI for this toggle lives in the character screen.

**FAQ pattern:** If more "bow/ranged doesn't work" posts appear, this is the answer. The doc gap: the character screen / tutorial doesn't make the stance→mode connection obvious. If UI redesign happens, spotlight the stance toggle prominently.

**Response template:** "Ranged vs melee mode is controlled by a stance toggle in your character screen — separate from what gear you have equipped. Switch stance and you'll see your character's attack style change."

## Achievement description discrepancies — Tears of Adria Hard Winner / Hardcore Hard (2026-08-26, Tears of Adria)

**Context:** Player Beaghan reported a discrepancy: "Hard Winner" achievement has conflicting descriptions — Steam page says "win on hard" (no mention of saves), but in-game text says "without saving." This creates confusion because "Hardcore Hard" is explicitly the no-saves variant, making Hard Winner redundant if both require no saves.

**Finding:** This is a real bug — either the Steam description is outdated OR the in-game description is wrong. A player can legitimately complete the requirement (win on hard) and not know if they also need to avoid saving. The issue is legit, not player confusion.

**Response pattern:** Achievement discrepancies are reportable bugs. CM should (a) acknowledge the discrepancy as valid, (b) ask the dev to clarify which description is correct, (c) offer manual unlock as a goodwill remediation while the fix is in progress. This is escalation-appropriate (the player did the work, confusion was legit).

**Gotcha:** Don't dismiss "description mismatch" reports as user error. Achievement descriptions being inconsistent across the game + Steam is a real UX problem.

## Community needs-response digest workflow + reply approval gate (2026-07-19, Tears of Adria / all forums)

**Context:** 4am CM sweep on gen-268 surfaced 3 Steam forum issues (1 HIGH ring bug, 2 MED achievement sync). Attempted to draft replies, hit MUST-ASK boundary.

**Pattern:** Player bug reports + design complaints flagged by the needs-response watch MUST go through Robert for reply approval before posting. Even low-complexity replies (acknowledge + ask for clarification) need Robert's voice OK — it's the brand boundary. CM can (a) research, (b) draft reply options, (c) surface context (is it known? design intent?), but cannot proceed to publication without Robert's explicit OK.

**Workflow:** CM triage → draft reply(ies) with context + questions → set ticket to `needs_input` → Robert reviews → Robert posts manually (CM never publishes to external forums per cm.md rule). If Robert provides guidance on reply direction, CM can iterate drafts in follow-up activity.

**Why this matters:** Needs-response watch is a triage tool, not a reply automation. Robert owns community voice and design decisions. CM's job is "catch what's waiting on Robert," not "answer for Robert."
