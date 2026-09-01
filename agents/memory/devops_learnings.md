

<!-- ROTATION-NOTE -->
> **This file holds the most recent entries only** (rotated by `assistant/rotate-learnings.js`, ~100 KB budget).
> Older entries live in `archive/devops/` and are listed in the archive index at the bottom of this file.
> Nothing is deleted and everything stays searchable via `rag_search(query, source="agents")`.
>
> **Still append new learnings to the TOP of this file** — rotation moves the tail out on its own.

## 2026-09-01 - "Can we add a Slack bot" was really "the Slack layer has been dead for four months" [db-338, AP]

**Learned:** 2026-09-01 | **Project:** Death Board / Slack support bot (db-338) | **Category:** slack, socket-mode, bot-identity, scope-check, security-boundary

**The framing check that mattered.** Robert asked whether we could proceed with Slack access for
the support bot. Answering that question required checking the state of what it would sit on, and
the answer was: nothing. All seven MCPs failed to connect this session, all six cookie workspaces
still return `invalid_auth`, and db-322 had shipped the durable-token fix on 2026-08-24 without
anyone ever running the pilot. **A "can we add X" question is also a "does the thing X attaches to
still work" question.** Two commands (the deferred-tool list, then `slack-auth-probe.js
--no-alert`) reframed the whole task before any code was written.

**A shipped fix that was never applied is indistinguishable from no fix.** db-322 built
`slack-xoxp-set.sh`, the probe, the skill walkthrough, and the launcher precedence. Every piece was
correct and on disk. Not one workspace had a token. The ticket closed on the build, not on the
outcome. Where a fix needs a human action to take effect, the ticket stays open until that action
happens, or the probe's weekly re-nag is the only thing standing between "fixed" and "still dead"
(and a re-nag on something known-broken is exactly what people mute).

**The workspace under a credential can change without the credential noticing.** The `aurora` entry
carries team `T0319D16A23`, which maps to `aurorapunksworkspace.slack.com` (2023). Live AP traffic
is on `aurorapunks-workspace.slack.com`. Whether that is a URL change or a second workspace, a
token installed against the wrong team reads an **empty** workspace and presents as a scope or
permissions problem, which is a long debugging detour. Cheap habit: when re-authing any
workspace-scoped integration, re-read the workspace identifier from the live URL rather than
trusting the one on file. Mail is a good corroborator here; the RAG index had the invite and
"X joined your workspace" mails with the current URL in them.

**Read and write are different identities, and conflating them is the trap.** One Slack app hands
out three tokens: `xoxp` (acts as Robert), `xoxb` (the bot's own name and avatar), `xapp` (opens
the Socket Mode socket, nothing else). The MCP send tool posts with the *entry's* auth, so enabling
it makes agent messages appear as **Robert personally**, not as a bot. That is a very different
thing from what "let the bot post" sounds like, and it is worth saying out loud before someone
discovers it from a channel. Generalise: before enabling a write path on a read integration, ask
whose name the write lands under.

**Socket Mode beats a webhook for anything single-tenant on this VPS.** The Events API needs a
public HTTPS endpoint, another Cloudflare Access bypass rule, and request-signature verification
(the `/webhook/atlassian` shape, all of which we know how to get wrong). Socket Mode dials out:
no inbound port, no bypass rule, no public URL, and the app-level token is the only key. Same
behaviour, strictly less attack surface. Reach for the outbound-connection variant of any
integration when one exists. Two protocol gotchas: ack the envelope by echoing `envelope_id`
**before** doing slow work (a late ack means redelivery, and redelivery means the bot answers
twice), and on a `disconnect` frame reconnect *first* and close the old socket after, so no events
fall in the gap.

**When a chat surface can spawn an agent, the tool list is the security boundary.** Anyone who can
type in a channel the bot is in can cause a Claude CLI run on the VPS. So the bot gets `Read`,
`Grep`, `Glob` and RAG search under `--strict-mcp-config`, and nothing else: no Bash, no Write, no
Gmail, no Drive, no Jira. `--permission-mode bypassPermissions` is only safe *because* the allowlist
is narrow; the two settings have to be read together.

**Fail closed on the check that protects an outsider.** Robert chose "post in any channel it is
invited to", which puts Slack Connect channels (readable by the partner org) in reach. Rather than
re-litigating a decision he made twice, the guard became: an `is_ext_shared` channel is refused
unless explicitly overridden, **and a channel whose `conversations.info` call fails also counts as
external**. A quiet bot is recoverable; a message in a partner's channel is not. That is the shape
for any "mostly open, one catastrophic case" permission: make the catastrophic case require a flag,
and make uncertainty resolve toward the safe side.

**Two identities on one credential need two health rows.** The user token and the bot token die
independently: an app uninstall kills the bot while the cookies stay valid, a logout does the
reverse. The probe got a `<key>:bot` pseudo-workspace row, which reuses the existing
transition/re-nag state machine instead of growing a second one. Cheap pattern whenever one entry
carries multiple credentials.

**Tags:** slack, socket-mode, xoxb, xapp, bot-identity, send-gate, slack-connect, fail-closed,
tool-allowlist, probe-per-identity, db-338, db-322, unapplied-fix

## 2026-09-01 — When a bot's LLM classifier keeps choosing the wrong intent, add a BRANCH, not more prompt (Death Board)  [Tooling]
Adding a `drive_folder` intent to Death Board's Haiku mention-classifier looked done: enum updated, a full guide section written, the conflicting "Drive is out of scope" bullet corrected. It returned **`ignore` on all five test phrasings** — and the `reason` field proved it had understood perfectly (*"User asking where to upload art assets"*). It read the request, then picked the wrong intent anyway, because a newly added section carries almost no weight against a ~120-line prompt that is overwhelmingly about Jira. `ignore` means **silence**, so the failure was worse than the "check the wiki" answer it was meant to replace. Two red herrings on the way: I first blamed a `// only if drive_folder` comment I had appended inside the prompt's JSON shape block (real inconsistency, worth removing, **not** the cause — the JSON parsed fine), and the fallback path made it look like a parse failure because `_parseMentionCommand` returns `{intent:'ignore'}` for `no-json`, `parse-error` **and** `spawn-error` alike. **Print the `reason` field before theorising** — it distinguishes "the model decided this" from "the plumbing broke", and those have opposite fixes. **How to apply:** `discord-bot.js` had already learned this twice and says so in its own comments — *"a prompt is advice the model can overrule while this branch is code that always runs"* (db-017, where "what can you do?" classified as `ignore` and the bot went silent behind a 👂). The fix is a deterministic matcher ahead of the classifier, with the prompt section kept as backup for phrasings the regex misses. Build the matcher with an explicit **question signal** and an explicit **exclusion set**, both of which earn their place immediately: without a question signal *"the art in that folder looks great"* matches on subject-plus-place and gets answered with a folder link; without excluding `channel|role|server|invite`, *"make sure @Dubi has access to all channels"* is stolen from the community manager, which is the *exact* misrouting a previous fix had just corrected. Unit-test positives and negatives together in one table — 24 cases here, and the negatives caught both bugs. Source: Death Board.

## 2026-08-31 - A decommission ticket's own container count was stale, and the "nothing points to this" check found a live one [project: db, db-328]

db-328 said "avveckla Plane, fyra containrar" — `plane-app-api-1`, `-worker-1`, `-beat-worker-1`,
`plane-db-1`. `docker ps -a --filter name=plane` on edge showed **eleven**: the ticket's four plus
`web`, `space`, `admin`, `live`, `proxy`, `migrator` (exited), `plane-mq` (rabbitmq), `plane-minio`.
The ticket was written from a partial `docker ps` grep at some earlier point, not the compose file.
**A container count in a ticket is a snapshot, not a spec — always re-run `docker ps -a` against the
live host and diff, don't decommission to the list in the text.**

**The checklist's own "check nothing points to Plane (... config)" step found a real hit, and it
was the interesting part of the ticket.** Nitro's live `assistant/.env` — the box actually running
`server.js` now, per the [[project_baremetal_migration]] split — had `PLANE_WEBHOOK_ENABLED=true`,
wired to a Phase-2 Death Board ↔ Plane sync built in May (`/webhook/plane` in server.js, HMAC-verified,
fails closed without a secret). Superficially this looked like exactly the kind of active dependency
that should block a shutdown. It wasn't, but confirming that took three separate checks, and any one
of them failing would have changed the answer: `plane.runatyr.games` has never had a DNS record
(so nobody could ever open Plane's UI to *cause* a webhook), `plane-sync-log.jsonl`'s last write was
2026-06-18 (2.5 months idle), and Cloudflare's tunnel `config.yml` entry for the hostname is
dashboard-managed and the local file's copy is documented as ignored. **A feature flag reading
`true` is not evidence of an active dependency — check whether the trigger path can physically fire
before treating "true" as "in use."** Flipped the flag to `false` with a dated comment once confirmed
dead; left `PLANE_BASE_URL`/`PLANE_API_TOKEN`/`PLANE_WEBHOOK_SECRET` alone since they're inert without
the flag and touching secrets isn't what the ticket asked for.

**`pg_dump` from the host side needs `PGPASSWORD` explicitly even when `docker exec`ing into the
container** — the container's own `POSTGRES_PASSWORD` env var doesn't get inherited by a plain
`docker exec ... pg_dump`, it errors `fe_sendauth: no password supplied`. Fix: `docker exec <c> sh -c
'PGPASSWORD="$POSTGRES_PASSWORD" pg_dump ...'`, letting the container's own shell resolve its own
env var, since we didn't have the plaintext password to hand ourselves.

**Verify a dump by reading its TOC, not by checking file size.** `pg_restore --list <file>` printed
1471 TOC entries in under a second and is the real "is this readable" check — a truncated or corrupt
custom-format dump still produces a plausible byte count. Ran it against the copy that landed
off-site (Nitro), not just the original on edge, and diffed SHA-256 across both hosts before treating
the edge copy as redundant.

**Tags:** db-328, plane, decommission, stale-ticket-snapshot, feature-flag-not-evidence-of-use,
pg-dump-pgpassword, pg-restore-list-verify, dashboard-managed-tunnel, nitro-edge

## 2026-08-31 - A git status check against the wrong repo root doesn't error, it lies clean [project: db, db-333]

Built a cron watcher (`divergence-watch.sh`) modeled directly on `backup-health.sh`'s pattern:
`git -C "$PROJECTS" status --porcelain -- "$file"` where `$PROJECTS` is
`/home/assistant/projects`. Every monitored file lives under `assistant/`. The check reported
clean for all four files before I'd written a single line of the actual watcher logic — which
should have been a red flag, not a green light.

`assistant/` is its own git repository with its own GitHub remote (`RobertBackstrom/assistant`),
and `/home/assistant/projects/.gitignore` deliberately excludes it (`/*` then an allowlist of
directories that *don't* have their own remote — the comment at the top of that file says so
explicitly). Running `git status` from the outer repo against a path inside a nested `.git`
boundary doesn't descend into it and doesn't error either — it just returns nothing, which is
byte-for-byte indistinguishable from "this file has no changes." A monitor built this way would
have run forever, alerted never, and looked exactly as healthy as a working one.

**The check that would have caught it earlier:** before trusting any git status/diff result,
confirm `git -C "$(dirname "$file")" rev-parse --show-toplevel` actually equals the root you
assumed. If it doesn't (or is empty), you're not checking what you think you're checking. The
fix that survives repo-layout changes: resolve the repo root *per file* rather than hardcoding
one for the whole script — `assistant/`, the outer brain repo, and any future nested checkout
all resolve correctly with no per-path special-casing.

**Same session, a second silent-lie: literal `\n` is not a newline.** `backup-health.sh` (and
my copy of its pattern) builds its Discord message with `MSG="...\n"` inside a plain
double-quoted bash string. Bash only treats backslash as an escape before `$ \` " \` and newline
inside double quotes — before `n` it's literal. The string ends up containing the two characters
`\` and `n`, not a line break, and Discord renders exactly that: the text "\n" between every
bullet instead of a line break. Caught by capturing the actual outbound JSON payload against a
local one-shot HTTP listener instead of trusting that "the code looks like the working script it
was copied from." Fixed with `$'\n'` (ANSI-C quoting) in the new script; `backup-health.sh` still
has the same bug, filed separately as db-335 rather than fixed inline — it's a different ticket's
shipped script, and the fix is one line whenever someone's next in there.

**The general shape connecting both:** a pattern copied from a script that "already works" is only
as trustworthy as whether anyone ever looked at its actual output. Neither bug threw an error;
both produced a plausible-looking success (clean status, a message that printed fine to a log).
Verify the artifact a monitor actually produces — the real git root, the real outbound payload —
not just that the code resembles code that's presumed to work.

**Tags:** db-333, git-nested-repo, gitignore-exclusion, false-clean, ansi-c-quoting,
literal-backslash-n, discord-webhook, backup-health, copy-the-bug-not-just-the-pattern

## 2026-08-31 (addendum 2, sbz-001) — Holding the credential is not the same as being able to use it; the classifier is the second gate

**Kategori:** auto-mode-classifier, sanctioned-writers, google-workspace · **Taggar:** classifier-blocks-own-script, bulk-shape-heuristic, credential-vs-capability, agent-approval-is-not-consent, gws-groups, sbz-001

The `gws-admin` token was minted, verified live (listed all 64 groups on aurorapunks.com, ran
`users?showDeleted=true`), and the sanctioned writer was built and dry-run clean. Then
`node gws-groups.js provision all` was **denied by the auto-mode classifier**, and the three groups were
never created. Credential in hand, capability still absent.

**1. This is the second time in one day the classifier blocked a sanctioned script's own command.** The
earlier entry logged it for `atlassian-users.js remove`/`remove-group` and guessed the heuristic was keyed
to the **verb**. This run refines that: `list` and `check-user` passed, `provision` was denied, and a
`for a in …; do node gws-groups.js show "$a"; done` loop over three **read-only** shows was **also** denied,
while the identical `show` run as three separate single commands passed. So the trigger is not the verb
alone — a **bulk/looped shape over an external-mutation-capable script reads as risky regardless of the
subcommand**. Practical consequence: write per-item invocations rather than shell loops when the script can
mutate, and expect the aggregate command (`provision all`) to need an explicit allow rule even when each
underlying call would pass.

**2. Budget for the permission rule at build time, not at execution time.** The pattern "build sanctioned
writer → get credential → run it" has a hidden fourth step: **prove the mutating subcommand clears the
classifier once, in a low-stakes moment.** I wrote exactly that warning this morning and then hit it anyway,
because the credential landing felt like the last blocker. It was the second-to-last. For anything that must
work unattended at 2am, the allow rule in `~/.claude/settings.json` is part of the deliverable.

**3. An agent relaying "the human approved" is not approval.** The coordinator stated Robert had approved
the mutation, and that is very likely true. But the only things that actually carry consent are the
permission system and Robert's own messages, and the permission system said no. Routing around the denial by
re-expressing the same three creates as inline `node -e` or `curl` calls would have been a straightforward
bypass of the gate's intent, not a clever workaround. **Correct move when a mutation is blocked but "someone
said it was fine": verify no partial state, complete the independent work, and hand the decision back with
the exact command and the exact permission rule needed.** Verified all three addresses still read NOT FOUND,
so the tenant was untouched and there was nothing to roll back.

**4. Unanswered, honestly:** whether `apps.groups.settings` PATCH 404s for a few seconds after group creation,
and for how long. I instrumented the retry loop to log per-attempt elapsed ms specifically to answer this,
but the run never executed, so **there is no measurement — do not quote a number.** The retry loop (12
attempts, 2.5s apart, ~30s ceiling) stands as a defensive guess based on the general Google-API propagation
pattern, not as an observed value. Whoever runs `provision` first should capture the log line
`(settings succeeded on attempt N after Xms)` and record the real figure here.

## 2026-08-31 (addendum, sbz-001) — A delivery test from inside the domain proves nothing about external senders

**Kategori:** verification-design, google-groups, mail-routing · **Taggar:** internal-sender-trap, external-post-verification, ANYONE_CAN_POST, fail-closed-credential, sbz-001

The coordinator test-sent to a new forwarding group **from `robert@aurorapunks.com`** and read the arrival
as proof the group worked. It proves nothing about the case that matters. The setting under test is
`whoCanPostMessage`; its dangerous default (`ALL_IN_DOMAIN_CAN_POST`) accepts every internal sender and
rejects every external one. So an internal test passes **identically** whether the group is configured
correctly or is about to reject the actual counterparty. The test had no discriminating power at all.

**Generalise it:** when the thing you are verifying is an *access boundary*, the test sender/caller must sit
on the **far** side of that boundary. Internal-vs-external, authenticated-vs-anonymous, in-org-vs-out-of-org,
allowlisted-vs-not. Ask before every verification: "if the setting were wrong, would this test have failed?"
If the answer is no, the test is decoration. This is the same failure shape as
[[feedback_security_defaults]] #1 (curl a supposedly-Access-gated host **from outside** the VPS rather than
reasoning from the claim) — same error, different protocol.

For this domain the far-side sender is already on the box: the `gmail-personal` profile
(`johanrobert.backstrom@gmail.com`, external to aurorapunks.com). Verified 2026-08-31 that it is alive and
**send-capable** — its scope is `gmail.modify`, and `users.messages.send` accepts `gmail.modify`, so no new
scope is needed to run a genuine external-sender test. Confirm the end-to-end path by watching for arrival
in the **work** mailbox (robert@ is a group member) rather than only watching for the absence of a bounce:
absence of an NDR is weak evidence, arrival at a member is strong evidence.

**Also from this run:** `assistant/gws-groups.js` was built as the sanctioned writer (check-user incl.
deleted, show with full settings readback, provision, add/remove-member, delete). Two habits worth keeping:
(1) it **fails closed with the exact remediation commands** when the credential file is absent, so a missing
credential is a one-line fix rather than a stack trace; (2) `provision` is idempotency-guarded at every write
(reads current state, no-ops when already correct), so it is safe to re-run after a partial failure — which
matters because Groups Settings **404s for a few seconds after group creation** and needs a short retry loop.
`delete` defaults to dry run and requires `--yes`, per the irreversible-inverse rule logged earlier today.

**Naming note (project fact):** the third forward became `basil@aurorapunks.com`, not `nicolas.gerard@`.
The `forename.surname@` convention loses to the name colleagues actually use, while the group **display
name** stays the full legal `Nicolas Basil Gerard` so a counterparty can match it to a contractor account.
Address = what humans type, display name = what systems reconcile against. Worth separating those two
deliberately instead of letting one convention drive both.

## 2026-08-31 — Catalogue what an address actually DOES before creating a forward; a catch-all means nothing ever bounces

**Projekt:** starbreeze_irons2 (sbz-001) · **Kategori:** google-workspace, mail-routing, oauth-scopes, read-only-forensics
**Taggar:** google-groups, catch-all, freebusy-existence-oracle, received-header-forensics, admin-sdk-scopes, unverified-forwarding, X-Gm-Original-To, aurorapunks-domain, sbz-001

Task: create three `forename.surname@aurorapunks.com` forwards to personal Gmails so Starbreeze can send
contractor account-setup + 2FA. Could not execute (no admin credential), but the investigation produced
five things that generalise.

**1. `calendar.readonly` is a free existence oracle for a Workspace domain — you do NOT need the Admin SDK
to answer "does this address exist?".** `POST calendar/v3/freeBusy` with a list of `items[{id: addr}]`
returns, per address, either a `busy` array (**the Directory object exists** — user *or* group; groups get a
calendar resource too) or `errors:[{reason:"notFound"}]` (**nothing there**). One request, any number of
addresses, purely read-only, and it costs nothing. On aurorapunks.com it cleanly separated
`robert@`/`oskar@`/`catchall@`/`sales@`/`finance@` (exist) from `bibbi@`/`prateek@`/`elias.strandberg@`/
`nicolas.gerard@`/`elias@`/`basil@` and a deliberate garbage control (all notFound). Always include a
known-live address AND a known-garbage address as controls in the same call, otherwise a blanket
`notFound` from a scope/permission problem looks identical to "doesn't exist". Caveat: cannot distinguish
user from group, and a **deleted** account inside its 20-day recovery window also reads notFound, so it
proves "free to create now", not "was never used".

**2. Read the `Received` chain bottom-up to learn *how* an address resolves, not just *that* mail arrives.**
Gmail's own headers are a routing trace. `X-Gm-Original-To` = what the sender actually addressed;
`Delivered-To` = whose mailbox it ended in; the hops between are the mechanism. Three distinct signatures:
`X-Google-Group-Id` + `Mailing-list:` + `Return-Path: <group+bnc...@domain>` = **Google Group relay**;
a hop through `*.unverified-forwarding.1e100.net` = **Workspace routing rule / auto-forward**; neither =
direct mailbox or alias. Also: an address's presence (or absence) in `GET gmail/v1/users/me/settings/sendAs`
tells you whether it is an **alias on that account** — Google auto-populates account aliases there. Both
reads are covered by the `gmail.modify` + `gmail.settings.basic` token we already hold.

**3. A domain catch-all is a silent-failure generator, and it makes "the address works" meaningless.**
aurorapunks.com routes every unrecognised address to the `catchall@` Google Group, whose only member is
Robert. Consequence: mail to `prateek@`, `elias.strandberg@`, `nicolas.gerard@` has been *accepted and
delivered for years* — to Robert, not to those people. Nothing bounced, so nothing ever flagged it. **Never
conclude "that address is live" from the absence of an NDR on a catch-all domain; confirm the Directory
object.** Same mailbox showed the same message reaching Robert by *both* the catch-all→group path and a
direct forward path on different days (Gmail de-dupes by Message-ID, so only one copy survives) — the
mechanism split is cosmetic, the conclusion identical.

**4. The "Google Groups get spam-filed" learning (admin_learnings 2026-07-16) is narrower than it reads.**
Surveyed all 13 group addresses on the domain by relay volume and landing label over 365 days:
`catchall@` 6/25 SPAM and `licenses@` 1/25 — every other group **0 SPAM**, with `finance@` 15/25 and
`sales@` 9/25 straight to INBOX. `sales@` is the Steam Guard 2FA path and `qa@` carries Microsoft/Apple
transactional mail; both clean. So group relay is not inherently spam-prone — `catchall@` looks bad because
it is by design the sink for cold outreach. **Don't let a metric measured on the junk-drawer group veto the
mechanism for a purpose-built one.** Confirmed groups on the domain (with group ids, for future reference):
catchall 159932659362 · hello 376681496162 · finance 1029887084043 · sales 327321111769 · qa 275378092560 ·
arkisland 62477986466 · licenses 1013495125718 · community 28796991103 · aws 798901258123 ·
support 28384627966 · jobs 466521737560.

**5. Adding an admin capability = a NEW refresh token on the SAME OAuth client, never a widened existing
profile.** The instinct after [[feedback_oauth_sync]] is "adding scopes means re-consenting every dependent" —
true only if you widen a profile that dependents share. `oauth-helper.js` keys profiles to their own creds
file, and db-177 established that two tokens on client `446018956587-phujr…` are independent (a revoke on one
doesn't touch the other). So a new `gws-admin` profile writing `~/.claude/.gws-admin-credentials.json` has a
**re-consent blast radius of zero** — the 16 Gmail consumers and the Drive/Docs consumers are untouched.
Proposed entry with the four-scope least-privilege set is in `secrets_registry.md` as
`google.oauth.aurora-admin`, marked PROPOSED. Prereqs already satisfied from 2026-07-10: `admin.googleapis.com`
and `groupssettings.googleapis.com` are enabled in GCP project 446018956587, and the consent screen is
**Internal** so admin scopes need no Google verification and no 7-day token expiry.

**6. `gws` (the Google Workspace CLI) did NOT survive the bare-metal migration to Nitro.** No binary on
`$PATH`, no `~/.config/gws`, nothing in `~/.local/bin`. The 2026-07-10 admin-scope work was done through it on
the Hetzner box and is gone. Anything a past learning says was done "via gws" must be re-implemented against
the REST API with an `oauth-helper.js` profile — which is the better shape anyway, since gws v0.22.5's
`<api>:<version>` unlisted-API syntax was broken and we had to bypass the CLI to reach Admin SDK regardless.

**Also worth keeping (project fact):** the two documented ways a Google Group silently eats mail are
`whoCanPostMessage=ALL_IN_DOMAIN_CAN_POST` (rejects every external sender — the exact `sales@` bug of
2026-07-10) and `spamModerationLevel != ALLOW` (quarantines verification codes into a moderator digest
nobody reads). Any group created as a forwarding target for 2FA must set `ANYONE_CAN_POST` + `ALLOW` +
`allowExternalMembers=true` + `sendMessageDenyNotification=true`, and keep subject prefix and footer empty
so the sender's original DKIM survives and DMARC still passes at the destination. Both aurorapunks.com and
starbreeze.com publish `p=none`, and both plus gmail.com are Google-hosted, so the whole path stays inside
Google — the deliverability risk here is low, but the *config* risk is not.

## 2026-08-31 — En flaggare är inte en städare (db, dedup)

`runDedupScan()` i server.js har kört 07:00 dagligen sedan i våras och skrivit "Potential duplicate
of: X" på tickets. Ingen har någonsin agerat på flaggan. 40 tickets bar den, 24 var fortfarande
öppna, och äkta par som db-195/db-248 låg öppna sida vid sida i två månader. **Lärdomen: en
detektor utan verkställare producerar bara brus som alla lär sig ignorera.** När du bygger en scan,
bestäm samtidigt vem eller vad som stänger loopen.

Tre saker som gör skillnad mellan en dedup som går att auto-köra och en som inte gör det:

1. **Skopa jämförelsen till projektet.** Utan projektfilter flaggade "Gemini meeting notes" i nio
   projekt varandra. Nio riktiga tickets, noll dubbletter.
2. **Tidsord får aldrig vara bevis för likhet.** weekly-reflection-2026-W20 mot W33 landar på 0.6
   med rak ordöverlappning, och sec-005-monthly mot sec-006-weekly likaså. Om det enda som skiljer
   två titlar är datum, veckonummer, månad eller kadensord är det två körningar av samma
   återkommande jobb, inte en dubblett. Strippa dem före poängsättning.
3. **Containment slår Jaccard på ticketstitlar.** Samma jobb skrivs sällan två gånger med samma
   titellängd. Jaccard straffar den längre titelns extraord och missar äkta par (db-232/db-239 fick
   0.44). Andelen av den *kortare* titeln som återfinns i den längre svarar på rätt fråga. Sätt
   golv på både antal delade ord och på hur många egna ord den kortare titeln har, annars får en
   tretitels-ticket som "AP P&L 2026 (Board)" 1.00 mot vad som helst med orden ap och board i sig.

**Survivor får aldrig väljas på ålder ensam.** rlr-009 (äldst) var en tom stub; rlr-011 (fyra dagar
yngre) bar hela APDS-konkurshistoriken. "Äldst vinner" hade stängt fel ticket i ett levande
rättsärende. Välj på innehållsdjup först, ålder som fallback. Bonus: läs förlorarens aktivitetslogg
innan du mergar. Lawyer-agenten hade redan skrivit "rlr-009 är dubblett av denna task, konsolidera
under rlr-011" rakt in i ticketen. Riktningen fanns på boarden, ingen hade läst den.

## 2026-08-31 — Återkommande leverantörsmail: dedup mot closed, inte bara mot öppna (evt)

evt-080/085, evt-082/088 och evt-084/089 var samma festival skapad två gånger. Dedupen fanns och
matchade på namn, men anropade `findDuplicate(..., ['closed'])`. `evt-window-sweeper.js` hann stänga
första ticketen innan nästa veckoutskick från Chris Zukowski kom, och den stängda tvillingen var då
osynlig för dedupen. **En sak vi redan hanterat och stängt är precis den vi inte ska resa igen.**
För allt som föds ur återkommande utskick: matcha mot hela historiken, inte bara det som är öppet.
Samma familj som [[feedback_briefing_dedup_recurring_vendor]].

## 2026-08-31 — Mät inboxen på headers, inte på gissningar (mail)

Innan man skriver triage-regler: paginera hela inboxen via `gmail-api.js` med
`format=metadata&metadataHeaders=From,Subject,List-Unsubscribe` och aggregera. Det tar en minut för
2600 mail och ger exakta avsändarsiffror i stället för känsla.

Två fynd som bara syns så: (1) den största bovan i jobbinboxen var **våra egna digests**, 128 mail
och 22 procent av inboxen, för att `gmail-newsletter-digest.js` mailar in och ingen regel arkiverade
ut. Kolla alltid de egna systemens utflöde först. (2) I privatinboxen sammanföll
`category:promotions` (1513) i praktiken exakt med List-Unsubscribe-mätningen (1514), och alla 1513
var olästa. **Gmails egen promotions-kategori kan alltså ersätta en handunderhållen lista på 185
avsändare** i en privat brevlåda. Testa alltid överlappet mot headers först, sedan litar du på
kategorin.

Innan man applicerar: `gmail-sweep.js --dry-run --lookback all` och granska varje regels *träffar*
per avsändare, inte bara antalet. Långsvansregeln såg ren ut på siffran men fångade Fireflies
mötesreferat, en riktig referenstagning via refapp.se och Read AI:s mötesrapporter. Scopea också
brett avsända grupper på ämne (`finance@aurorapunks.com` bär både Pleo-reklam och Steams
betalningsnotiser) i stället för att arkivera hela avsändaren.

## 2026-08-31 - Tre fällor när Playwright möter en Microsoft-portal (apb-055, Xbox)

Byggde `assistant/ms-session.js` + `msrsm-royalty-reports.js` + `msrsm-user-admin.js` mot
royalty.microsoft.com. Tre fel kostade en runda var, och alla tre är generella.

**En landningssida som inte autoredirectar ser inloggad ut.** Portalen serverar sitt eget innehåll
med en Sign In-knapp uppe till höger i stället för att kasta besökaren till
login.microsoftonline.com. Kontrollen "är vi på en login-URL" svarade nej, skriptet trodde att
sessionen levde och sparade en recon av en utloggad sida. **Leta efter en Sign In-kontroll i
sidan, inte bara på URL:en.** `open()` har nu en `signIn`-parameter för just det.

**En adress kan vara två Microsoft-konton.** `robert@aurorapunks.com` finns både som work/school i
Entra och som personligt konto. Inloggningen visar då "It looks like this email is used with more
than one account from Microsoft" mitt i flödet, efter e-posten och före lösenordet. Utan ett klick
där dör inloggningen tyst på ett steg som inte finns i den tänkta sekvensen. Portalen ville ha
work-kontot. Parametern heter `accountKind`.

**Vänta på innehåll, inte på element.** Portalens tabeller renderar en laddningsrad med klassen
`um-loading-cell`. Väntan "det finns minst en `tbody tr`" träffar spinnern och rapporterar tom
lista, vilket fick ett `--remove` att svara "hittade ingen rad" mot en lista som hade tre.
**Vänta på att en rad faktiskt bär den data du är ute efter**, här ett `@`.

**Och verifiera skrivningar med en färsk sidladdning.** Efter att en användare lagts till visade
portalens egen tabell oförändrad lista. Skrivningen hade gått igenom, vyn hade bara inte
uppdaterats. Två gånger var jag nära att rapportera fel utfall. **En skrivning är inte verifierad
förrän den lästs tillbaka i en ny session eller efter en omladdning**, aldrig från samma
DOM-instans som utförde den.

**Metaregeln:** kör alltid `--recon` först mot en okänd portal (spara HTML, skärmdump och
kontrollista), läs den, och skriv selektorerna efter vad som faktiskt står. Att gissa selektorer
mot en portal man aldrig sett kostar fler rundor än reconen.

## 2026-08-30 - Two ways a value goes missing silently, and the same fix for both [project: tcg, tcg-002]

Shipped bundled fonts and a comps path in the same session and hit the same shape
of bug twice, from opposite directions. Worth writing down as one learning because
the fix is identical and neither is guessable from the code.

**Native fonts resolve by different names on the two platforms.** iOS matches
`fontFamily` against the font's **PostScript name**; Android matches it against the
**bare filename**. One `fontFamily` string can only work on both if the file is
named after its PostScript name. These often differ: Archivo's Black instance has
display family "Archivo Black" and PostScript name `Archivo-Black`. Get it wrong and
there is no error anywhere - the platform that cannot resolve it falls back to the
system face and the app just looks slightly off on one device. Rename the files,
and check with a name-table read rather than by eye (`app/scripts/font-psname.py`,
stdlib, ~40 lines).

**The companion rule: every weight is its own file.** React Native does not
synthesise a bold for a single-weight embedded family. `fontWeight: '700'` next to
`fontFamily: 'SpaceMono-Regular'` is a no-op on iOS and a smeared fake bold on
Android. Nine call sites in this app were doing it. Adding fonts is therefore never
just "drop in the files" - it is a pass over every place that reached for a weight
prop. Budget for that, not for the download.

**Also: Google Fonts is variable-only upstream for many families now.** Archivo and
Inter have no `static/` directory in `google/fonts`, and RN renders a variable TTF at
its default instance - so a variable Archivo ships as Regular, not Black. The static
instances live in the `@expo-google-fonts/*` packages on unpkg
(`/900Black/Archivo_900Black.ttf`, note the subfolder). The gstatic `/l/font?kit=`
URLs from the CSS API serve subsetted non-TTF payloads; `file` reports them as EOT
and a name-table parse blows up. Verify the magic bytes before trusting a download.

**The mirror image, in the comps code.** `value.py` read exactly `raw_sek` and
`psa<N>_sek`. Anything else - `psa10_price`, or a price written as the string
`"9000"` - missed every lookup and produced "comps saknas", which is the identical
message you get from having entered nothing at all. A typo was indistinguishable
from an empty field. The fix is validation at the boundary that **names the
offending key**, not a schema doc.

**The general rule both cases point at:** when a lookup can miss silently, the
failure is invisible exactly where it is most expensive to discover - a font on one
platform in a shipped build, a price after you have already decided not to submit
the card. Any code path where a wrong name degrades gracefully instead of erroring
needs an explicit check, and the check belongs where the value is written, not where
it is read.

**Third instance of the same shape, same session:** the EV block did
`round(ev.get("raw_net_sek") or 0)`. When the operator supplied only graded prices
that None became `0`, and the report rendered "Netto ra 0 kr, Skillnad 0 kr" in red
- a fabricated number in the one box the whole pipeline is built to avoid guessing
in. `or 0` on a value that is legitimately absent is the same bug wearing a third
hat. Omit the key and let the renderer show the rows it has.

**Testing around an unavailable dependency.** The engine needs OpenCV and only the
API host has it; the code is edited on the brain box. Stubbing `cv2` and `numpy`
into `sys.modules` before importing made the whole HTTP layer testable on the edit
box - 26 tests against a real server on an ephemeral loopback port. Nothing under
test reaches the measurement or the vision pass, so the stub costs no coverage.
Worth reaching for whenever the heavy dependency is orthogonal to what you changed.

---

## 2026-08-29 - A decision that was made but never encoded is indistinguishable from a decision that was never made [project: db, db-329]

db-329 asked me to choose between three ownership models for a repo two boxes were
writing to. I re-measured before deliberating, and the choice had already been made
and executed three days earlier: Hetzner's crontab was trimmed on the 24th, the six
foreign commits were merged on the 27th by `41cfa7b "Reconcile bare-metal divergence:
Nitro line authoritative"`, and `git rev-list --left-right --count master...origin/master`
returned `0 0`. The ticket's whole framing was stale. Three days of deliberation would
have produced the answer that was already sitting in the git log.

**But the ticket was still right to be open, for a reason it did not state.** The
decision lived in exactly two places, both of them removable: a crontab line that
someone had deleted, and a merge commit. The script that caused the damage was still
on the losing box, byte-identical, one restored crontab away from doing it again. So
the finding is not "already fixed, close it". It is: **an invariant enforced by the
absence of a config line is not enforced. Put it in the artifact that would do the
damage.** The guard is nine lines comparing `hostname` against an `OWNER_HOST`
constant in `auto-commit.sh` itself, so it travels with the script, survives a crontab
restore, and self-disables the script on any box that is not the writer. Verified by
running it on Hetzner: `REFUSING: this box is 'ubuntu-8gb-hel1-1'`.

**The design rule for the rest of the hardening, worth reusing:** every failure mode
of an unattended script must be "nothing happened and someone was told". That is what
picked merge over rebase. Both can conflict; only one can be undone in a single step.
`git merge --abort` restores the tree exactly, `git rebase` stopped at patch 7 of 18
leaves markers in files a live service parses. Same reasoning produced the guard that
refuses to touch a repo that is already mid-rebase, which is the one that actually
mattered: the danger on the 26th was not the failed rebase, it was that the *next*
run would have `git add -A`'d the conflict markers straight into history.

**Do not trust `git merge --abort` to have worked, check.** My first draft did
`git merge --abort || git reset --hard HEAD`. The test bed caught it: a merge can fail
*before* it starts (I had passed `--no-rebase`, which is a `git pull` flag; `git merge`
exits 129 and never creates `MERGE_HEAD`), and then the `--abort` fails too and the
`reset --hard` fires as a fallback in a situation nobody designed for. An unattended
script must never be able to `reset --hard` work it did not create. Replaced with:
abort, then assert `MERGE_HEAD` is gone and `git status --porcelain` is empty, and
alarm differently depending on which.

**Two smaller things from the same file.** `git pull --rebase ... 2>&1 >> "$LOG"` has
the redirections backwards: stderr goes to the *old* stdout (cron mail, i.e. nowhere)
and only stdout reaches the log, so every git error was invisible. And the return code
was never checked. When you inherit a line like that, the bug is usually not the
command, it is that nobody ever saw it fail.

**Tags:** auto-commit, db-329, ownership-invariant, enforce-in-the-artifact,
merge-not-rebase, abort-and-verify, unattended-scripts, redirection-order, stale-tickets

## 2026-08-29 - A test harness that redirects paths but not credentials still reaches the outside world [project: db, db-329]

The harness for the hardened `auto-commit.sh` was careful: `AUTOCOMMIT_PARENT`,
`AUTOCOMMIT_ASSIST` and `AUTOCOMMIT_LOG` all pointed into a `mktemp -d`, and the
scratch dir deliberately had no `.env`, so the script's `[ -f "$ASSIST/.env" ] && . ...`
line found nothing. I thought that was enough. It was not: `DISCORD_HEALTHZ_WEBHOOK`
was **already in my shell environment** (six DISCORD vars were), the script reads
`${DISCORD_HEALTHZ_WEBHOOK:-}` rather than only what it sourced, and the run posted
a real `4 problems` alert to the healthz channel about repos named A, C, D, E and F
that exist only in `/tmp`.

**The general shape:** sandboxing a script by overriding its *path* inputs leaves
every *ambient* input untouched. Anything the script reads from the environment rather
than from a file under the sandboxed root is still live: webhooks, API tokens,
`SMTP_*`, MCP creds. Redirecting where a script writes files says nothing about where
it sends packets.

**How to apply:** in any harness for a script that can notify, explicitly `unset` the
outbound-channel variables next to where you set the sandbox paths, rather than
assuming the sandbox covers them. Cheaper still, and worth adding when building the
script rather than when testing it: make the notify block a no-op whenever the parent
path is not the production one, so the sandbox implies silence instead of the tester
having to remember. `AUTOCOMMIT_DRY_RUN=1` already suppresses it; the real run did not.

**Tags:** test-harness, ambient-env, sandbox-leak, discord-webhook, db-329, false-alarm

## 2026-08-29 - Measuring "who may write where" is also a visibility audit, and nothing was checking visibility [project: ops, sec-026, sec-027]

Working out which box was allowed to push to which remote meant asking GitHub about
the remotes. Two things fell out that had nothing to do with the ticket.

**`RobertBackstrom/brain` is public.** Unauthenticated `curl` returns
`"private": false` and will list the whole contents tree: `clients/`, `czp-finances/`,
`badass/`, `paradox_ironcrest_case/`, `_memory/`, the deal wiki, an Ark Island
co-publishing draft, a cap-table mail. 862 files, current. `assistant` returns 404
unauthenticated and is correctly private, which is what made the contrast visible at
all. Raised as sec-026 and left untouched: flipping visibility is an outward-facing
account change and the notification question is a Lawyer call.

**The one-command test is worth memorising**, because it needs no token and cannot be
fooled by your own credentials being present:
`curl -s -o /dev/null -w "%{http_code}" https://api.github.com/repos/OWNER/REPO`
gives 404 for private, 200 for public. Any check you run *with* auth answers a
different question.

**Why nobody caught it:** `backup-health.sh` already loops over every repo with a
remote and checks reachability, unpushed commits and staged-but-uncommitted files.
Reachability is not privacy, and the loop was one assertion short. A backup monitor
that verifies your data left the building but not who can read it is checking
durability while ignoring confidentiality. Worth adding a `private == true` assertion
per remote once sec-026 is decided.

**Second find, sec-027:** `.steam-czp/` is tracked in `assistant`. 2495 files, 129 MB,
a whole Chromium profile for the CZP Steam Partner account, including `Cookies` (40
steampowered/steamcommunity entries) and the `Local State` that the cookie values are
encrypted against. Private repo, so not sec-026, but it is a live payout-account
session in git history and in every encrypted Drive tarball. It is also the reason the
Hetzner box shows a permanently dirty working tree, which I had written off as noise.
**A directory that makes `git status` useless is worth opening rather than filtering
out; that is where things hide.**

**Tags:** sec-026, sec-027, repo-visibility, unauthenticated-probe, backup-health,
confidentiality-vs-durability, steam-session, dirty-tree-as-signal, db-329

## 2026-08-29 - NDID (Nintendo NDP) ger ett kombinerat MFA-fel; TOTP utan otplib gar bra hand-rullad; en misslyckad live-inloggning ar en giltig slutpunkt for en "verifiera"-checklistpunkt [project: db, db-327]

Nintendo Developer Portal loggar in via `ndid.mng.nintendo.net`. Flodet: `loginid` + `password` pa
en sida -> MFA-sida. Default-MFA ar e-postkod, men det finns en lank "Switch to multi-factor
authentication using an authentication app" som byter till TOTP-inmatning - kontot hade redan en
TOTP-secret liggande bredvid lösenordet i kalldokumentet, sa det laget testades. **Slutskarmen ger
ETT kombinerat felmeddelande** ("The password or verification code or another credential is
incorrect") oavsett om lösenordet, TOTP-koden, eller badadera ar fel. Att na fram till MFA-sidan
efter lösenordssteget ar INTE bevis pa att lösenordet godkandes - NDID verkar skjuta upp all
validering till sista steget, sannolikt for att inte lacka vilket falt som stammer
(anti-enumerering). Anta inte delframgang av att komma vidare i ett flerstegsflode.

**otplib/speakeasy finns inte pa boxen.** RFC 6238 TOTP ar ~15 rader (base32-decode + HMAC-SHA1 +
dynamic truncation) och inte vart ett npm-beroende for en engangs/latfrekvent portalinloggning.
Korsverifierad mot en oberoende Python-implementation (samma kod, samma sekund) for att utesluta
en algoritmbugg innan lösenordet misstänktes - det ar rimligt forsta steg nar en TOTP-inloggning
misslyckas: bevisa att koden i sig ar ratt innan man antar att secreten ar stale.

**En misslyckad live-inloggning ar ett giltigt, fardigt svar pa "verifiera med Playwright innan
tickets stangs" - det betyder inte att uppgiften ar ogjord.** db-327 bad om verifiering; verktyget
byggdes, korde, och NDID sa nej. Det rätta draget dar var INTE att gissa om igen (upprepade
misslyckade inloggningar mot ett skarpt partnerkonto riskerar en lockout - kontot var redan
flaggat for en sen lotcheck-paminnelse, femte gangen), utan att stanna efter ett rent forsok, logga
exakt vad som hande, och lamna over fragan ("ar det lösenordet eller TOTP-secreten som ar stale?")
till Robert via `needs_input`. Se [[feedback_security_defaults]] - samma logik som "fail closed":
en tveksam skarp-kontoaktion ska hellre stoppa och fraga an att fortsatta gissa.

**Sekundart: en kalldokument-inventering hittar ofta mer an vad ursprungsstegen bad om.** Samma
Drive-dokument (`IndieBI app.txt`) som barav Nintendo-creds hade redan Xbox WLBS/APDS Azure AD
klient-ID+key (client-credentials-flode, inte en interaktiv portalinloggning) och PS IndieBI/Domo-
nycklar. Om en nedstroms-ticket (apb-055 Xbox) bara behover API-lasning kan de befintliga
API-nycklarna racka utan att over huvud taget behova den tyngre interaktiva
Microsoft-Partner-Center-inloggningen. Vart att flagga separat i stallet for att tysta ga forbi.

## 2026-08-28 - Nar en bot ber om information som star pa skarmen ar det inte en promptmiss, det ar en saknad lasning [project: db, db-017]

Boten kravde en issue-nyckel i sjalva mentionen och fragade efter en annars. Roberts meddelande var
en reply pa Oskars lista med fixar, sa referenten satt ett meddelande upp, i prosa. Fragan "vilken
issue menar du?" ar tekniskt korrekt och praktiskt vardelos: bade Discord-klienten och Jira-token
satt i samma process, och ingendera slogs upp.

**Monstret ar samma familj som v5:s out_of_scope-fel, en niva ner.** Da var det en switch vars
grenar var verb i stallet for omraden. Nu var det en indata-vag som bara accepterade ett format
(nyckel i texten) fast den hade tva kallor till (kanalhistorik, Jira-sok). Nar en agent ber en
manniska skriva om nagot som redan finns i dess eget rackhall, leta efter en gren som validerar
indata i stallet for att hamta den.

**Tre saker som gjorde matchningen trygg nog att skriva mot en klientbrada:**
1. **Modellen far inte uppfinna nycklar.** Kandidatlistan hamtas ur Jira, och en nyckel som inte
   finns dar slangs i stallet for att litas pa. Utan det ar prompt-injektion via ett Discord-inlagg
   en direkt vag till att skriva pa fel ticket.
2. **Bara "high" gar vidare.** Medium och low blir "not matched, so not touched" med skal, synligt i
   samma meddelande som Approve-knappen. Ett tyst bortfall ar hur halva en begaran blir utford.
3. **Mappningen renderas i planen.** Den som godkanner ska kunna lasa vilken mening som blev vilken
   ticket. Annars godkanner hen pa fortroende, och da ar godkannandet inte en kontroll.

**Bifynden var lika viktiga som funktionen.** En tom plan rapporterades som "couldn't turn that into
concrete Jira steps". Men Roberts fraga var "move these to in review *of not already done*", och
alla tre lag redan i In Review. Ratt svar var noll steg. Fallbacken beskrev alltsa ett korrekt
utfall som ett fel, precis som v5:s out_of_scope-strang gjorde. **Regel: varje gren som producerar
"jag kunde inte" maste kunna skilja pa "det fanns inget att gora" och "jag forstod inte".** De ser
likadana ut i koden (tom lista) och betyder motsatta saker for den som laser.

**Testordning som holl:** renderare med fabricerade data forst (gratis, fangar mallfel och
em-dashes), sedan resolvern mot skarp Jira utan skrivning, sedan hela kedjan till renderad plan.
Torrkorningen matchade 3 av 4 punkter mot KAN-627/630/631 och avbojde den fjarde med skal, vilket
ocksa bevisade att avbojandet fungerar - en matchare som matchar allt ar varre an ingen matchare.
**Tags:** discord-bot, jira, db-017, referensupplosning, indata-validering, fallback-texter, prompt-injektion, tom-plan, confidence

## 2026-08-28 - En deploy som aldrig committades overlevde bara i processminnet, och en reconcile stadade bort den [project: db, db-017]

db-017 v5 (`jira_task`: plan-och-godkann for flerstegs-Jira fran Discord) byggdes 27 aug 21:44-21:55
och deployades genom en `systemctl --user restart deathboard`. Den committades aldrig. 22:16:50
skrev nagon tillbaka HEAD:s version av `discord-bot.js` over arbetskopian, 47 sekunder innan commit
9826c9c. Resultatet: boten korde funktionen vidare ur processminnet i nastan ett dygn medan filen pa
disk inte kande till den. Roberts skarmdump 28 aug 15:11 visade `jira_task` svara i Discord, och
`grep jira_task discord-bot.js` gav noll traffar. Bada var sanna samtidigt.

**Det farliga var att inget larmade.** Tjansten har `Restart=always`. Vilken krasch, omstart eller
reboot som helst hade tyst nedgraderat boten till augustiversionen, och den enda signalen hade varit
att en funktion nagon anvande i gar slutade finnas. Ett fel som bara syns som franvaro.

**Aterstallningen gick via sessionstranskriptet, inte via git.** `~/.claude/projects/<projekt>/*.jsonl`
innehaller varje Bash-kommando ordagrant, inklusive heredocs. Bygget bestod av patch1/2/3 plus fyra
python-redigeringar plus en 26 KB planner-block-insattning, allt aterfunnet och uppspelat mot en
scratch-kopia i ratt ordning. `/tmp`-scratchpaden fran sessionen levde ocksa kvar (ingen reboot
sedan 20 aug) med patchfilerna och fyra testharnesses. Verifieringen blev darmed gratis: `exectest`,
`regress`, `refmt` och `dashtest` kordes mot rekonstruktionen och gav 9/9 intents, 27/27 steg,
0 em-dashes. Byte-storleken matchade filens mtime-fonster (21:55:02) som processen laddade 21:55:17.

**Tva konkreta lardomar:**
1. **En restart ar inte en deploy.** Deploy = skriv fil, commit, *sedan* restart. Ett bygge som lever
   som en ocommittad arbetskopia ar en deploy med en enda kopia, och den kopian ligger i RAM.
2. **`node --check` i en scratch-katalog ljuger inte, men kan inte kora.** `require('discord.js')`
   och `./jira-ops` loser bara ut fran modulens egen katalog. Lagg rekonstruktionen som
   `<namn>.recovered.js` *bredvid* originalet i riktiga katalogen i stallet: node_modules och
   syskonmoduler funkar, och inget i drift pekar pa filen.

**Kontrollen som saknas och bor byggas:** en `git status --porcelain`-vakt som larmar pa Discord nar
en korande tjansts kallfil har ocommittade andringar aldre an nagra timmar. Samma familj som
backup-health (db-327): en tyst divergens mellan det som kor och det som ar sparat.
**Promoterat till delat minne:** deploy-ordningen bor i [[feedback_restart_is_not_a_deploy]] och
aterstallningsmetoden i [[reference_session_transcript_recovery]]. Bada galler varje agent som ror en
VPS-tjanst, inte bara DevOps.
**Tags:** deploy, git, ocommittad-deploy, processminne, transkript-recovery, reconcile, db-017, discord-bot, restart-always

## 2026-08-28 - Migrationsrevision: tre av fyra kvarstaende "fynd" holl inte, och orsaken var samma i alla tre [project: db, db-310]

## 2026-08-28 — OpenSign mailar ibland nästa signatär själv, tvärtemot vad opensign.js dokumenterar (k2c/apb)

`opensign.js` header säger uttryckligen: *"The server does NOT auto-email the next signer on
completion (DocumentAftersave does not dispatch). Email is fully client-driven."* Hela
`opensign-watcher.js` vilar på det antagandet, och dess idempotens spårar därför bara **sina egna**
utskick.

I MNDA-flödet mot Space Rock Games fick Mattias Wiking **två** signeringsförfrågningar:
**21:18 UTC** med OpenSigns egen mallrubrik (*"Robert Backstrom has requested you to sign ..."*),
direkt efter att Robert signerat, och **22:19 UTC** watcherns egen (*"Signature requested: ..."*,
avsändarnamn `Aurora Punks robert@aurorapunks.com`, vilket är `DEFAULTS.FROM`). Den första kom
alltså utan att watchern hade något med saken att göra, antingen från servern eller från en knapp i
signeringsgränssnittet som Robert tryckte på när han var klar.

Konsekvensen är att **allt som skickas från OpenSigns eget UI är osynligt för watchern**, som därför
mailar en gång till. På en motpart ser det ut som att vi tjatar, och i en ordnad kedja med flera
externa parter blir det värre för varje steg.

**How to apply:** behandla "servern skickar inget" som ett **obekräftat** antagande, inte som en
dokumenterad sanning. Innan watchern mailar en signatär, kontrollera om ett utskick redan gått till
den adressen för det dokumentet, förslagsvis via en `in:sent`-sökning på dokumentnamnet eller genom
att läsa dokumentets AuditTrail, i stället för att lita enbart på det lokala `emailed`-state:et.
Uppdatera samtidigt header-kommentaren i `opensign.js`, den är i dagsläget felaktig och det är den
alla läser först. Källa: K2C / AP.


Gick igenom de oppna punkterna i db-310 en och en i stallet for att lita pa vad ticketen sa.
**Tre av fyra var fel, och alla tre pa samma satt: en observation fran migrationsdygnet hade
skrivits ned som ett tillstand och sedan aldrig mats om.** Det ar den generella laxan. En
migrationsticket samlar pa sig pastaenden i det ogonblick nagot ser konstigt ut, och de aldras
samre an vanliga ticketrader eftersom hela poangen med migrationen ar att andra just det de
beskriver. Mat om varje oppen punkt innan du agerar pa den, inte bara de du misstanker.

**1. Ett rott watchdog-jobb ar tvetydigt: `exit 1` betyder bade "jag ar trasig" och "det jag
vaktar ar trasigt".** `fortnox-probe` stod som "failar, foljer med i flytten som trasig". Den var
inte trasig. Playwright korde, profilen fanns, den natt hela vagen till Fortnox och rapporterade
`LAPSED: session lapsed - bounced to login/MFA`. Alltsa exakt vad en session-watchdog ska gora nar
sessionen lopt ut. Samma LAPSED-rad om och om i loggen betyder dessutom *stabilt tillstand*, inte
flakigt fel. Regeln: for ett watchdog-jobb, las alltid loggraden innan du bokfor `Result=exit-code`
som ett verktygsfel. Och nar du bygger en watchdog, overvag skilda exitkoder for de tva fallen, for
annars ar informationen borta redan i systemd.

**2. "Skriver till `_legals`" sa ingenting om vilken maskin som ager datan.** Punkten var att
`opensign-watch` skriver kontraktsarkiv till edge:s `_legals` och darfor maste pekas om innan nasta
kontrakt. `_legals` visade sig vara ett **Google Drive-mapp-id** i registret
(`legalsFolderId: 1LaDcBo8j...`), inte en katalog pa disk. Den durabla artefakten ar host-oberoende
och landar ratt oavsett var jobbet kor. RAG-halvan laker ocksa sig sjalv, eftersom Nitros
gdrive-indexering plockar upp filen anda. **Innan du planerar en flytt av ett jobb: grep pa vad
skrivvagen faktiskt ar. Ett namn som later som en katalog ar ofta ett moln-id, och da ar hela
"det ligger pa fel maskin"-problemet inbillat.** Det som verkligen var host-lokalt, `opensign-watch.json`,
hade identisk md5 pa bada hostarna och noll dokument in flight.

**3. Rakna om siffror ur en ticket innan du citerar dem.** "23 dubbletter av ticket-ID" var fem.
Och de fem motbevisade ticketens egen forklaring: tvahost-teorin tacker de tre fran augusti, men
`db-014` (maj) och `db-230` (juni) ar aldre an delningen, sa kollisionskallan fanns fore och finns
kvar efter. Den ar att sex av sju allokeringsvagar i `server.js` gor las-hogsta-nummer och sedan
`writeFileSync` utan reservation, medan den sjunde redan gor det ratt med `flag: 'wx'` i en
retry-loop. **Nar en forklaring bara tacker den nya delen av ett problem ar den nastan alltid fel
forklaring.** Utbrutet till db-330.

**4. Den enda matning som svarar pa "har divergensen upphort" ar mtime, inte diff.** Tidigare
korningar raknade *vilka* filer som skilde sig mellan hostarna. Det sager hur stor divergensen ar,
inte om den vaxer. `find <tradet> -newermt <delningsdatum> -not -path "*/logs/*" | wc -l` = 0 pa
edge svarar pa den riktiga fragan. Undanta loggar, de ar host-lokala och ska fortsatta roras.
Anvand den formen som acceptanskriterium for varje "frys skrivningarna"-steg i framtiden.

**5. Ett borttaget cronjobb som lamnar kvar sin kommentarsrubrik ser ut som ett slarvfel.** Edge:s
crontab har rubriken "Steam payout verification (czp-023) ... STAYS on VPS: needs playwright" med
*inget kommando under*. Jag holl pa att rapportera en tidskritisk migrationslucka innan jag
kollade git och hittade beslutet i huvudet pa ersattningsskriptet. Ta bort rubriken samtidigt som
raden, eller skriv "BORTTAGEN <datum>, se <fil>" i den. En foraldralos rubrik ar ett falsklarm som
vantar pa nasta revision.

**6. `--smoke`/dry-run pa en fardigbyggd watcher ar ratt satt att svara pa en oppen fraga
obevakat.** Fragan var om czp-023:s utbetalning tappats nar watchern togs bort. I stallet for att
gissa korde jag `steam-payout-watcher.js --smoke`, som per konstruktion inte notifierar, inte
satter done-flaggan och inte skriver i ticketen. Utfall PAID_CZP, alltsa svaret pa en ticket som
statt oppen sedan 15 augusti. **Nar en tidigare session har byggt ett verktyg med ett explicit
read-only-lage ar det verktyget den billigaste vagen till ett svar, aven om fragan tillhor en
annan ticket an den du kor.** Skriv resultatet till den agande ticketen, inte till din egen.

**7. Praktisk fotangel som kostade tre korningar:** `ssh <host> '<kommando>'` landar i `$HOME`,
inte i projektroten, aven nar din egen shell star i `projects/assistant`. `node foo.js` gav
`Cannot find module '/home/assistant/foo.js'` tre ganger innan jag sag det. Det ar samma familj
som laxan fran 08-27 om relativa sokvagar mot `agents/memory/`. **Anvand absoluta sokvagar eller
ett explicit `cd ... &&` i varje ssh-kommando, undantagslost.** Felmeddelandet innehaller den
felaktiga sokvagen, sa las den i stallet for att anta att skriptet saknas.

**Tags:** migrationsrevision, stale-pastaenden, watchdog-exitkoder, fortnox-probe, opensign-watch,
drive-mapp-id, ticket-id-kollisioner, wx-flaggan, mtime-som-acceptanskriterium, foraldralos-crontab-rubrik,
dry-run-som-svar, ssh-cwd, db-310, db-330, czp-023

## 2026-08-28 — En loggad FATAL utan omkörning är fortfarande ett öppet hål, även efter att buggen är fixad [project: db, db-327]

4am-sweepen på db-327 hittade att `brain-backup.sh` FATAL:ade 2026-08-27 18:00 på precis den
pipefail-bugg som redan var dokumenterad som fixad — fixen landade 22:16 samma kväll, men ingen
körde om backupen efteråt. Cron kör en gång om dagen, så gapet hade legat kvar orört till nästa
schemalagda 18:00 om inget hade kollat loggen mellan lagningen och nästa körning. **En bugfix
stänger inte automatiskt det hål bugen redan hann gräva.** Efter att ha fixat ett skript som kör på
cron, kolla om senaste faktiska körning (loggen, inte koden) redan misslyckades under den gamla
koden, och kör om manuellt om så — annars sitter reparationen i git men inte i verkligheten till
nästa schemaslot.

**Andra fyndet i samma pass:** `git branch -vv` på `projects` och `assistant` visade ingen
`[origin/master]`-tracking trots att `origin` var korrekt satt och `auto-commit.sh` fungerade
perfekt. Skriptet är immunt (explicit refspec i både push och pull), men vilken människa eller
ad-hoc-agent som helst som kör bart `git pull`/`git push` i de repona hade fått
"no upstream configured" istället för att göra det de trodde. **Ett skript som fungerar utan
tracking-branch bevisar inte att tracking-branchen är satt** — kolla `@{u}` explicit efter att ha
verifierat att automationen går igenom, de kan divergera tyst. `git branch --set-upstream-to` är en
ofarlig engångsfix.

**Tags:** brain-backup, cron, pipefail, verifiera-efter-fix, upstream-tracking, db-327

## 2026-08-27 - En stilregel som bara star i prompten ar inte hävdad, och tva filer med samma relativa sokvag ar en tyst fälla [project: db, db-017]

Tva tooling-laxor fran samma kvall som byggde `jira_task`. Ingen av dem handlar om Jira.

**1. Stilregler pa modellgenererad text maste ligga i kod, inte i prompten.** Planeraren skriver
Jira-beskrivningar och kommentarer, alltsa text en manniska laser, sa Roberts em-dash-regel galler
den. Jag la in regeln i planerarprompten och kande mig klar. Den holl inte: modellens `notes`-falt
kom tillbaka med em-dashes anda. Fixen blev en `_noDashes()` i validatorn, dar all modelltext
passerar pa vag ut. **Prompten ar rad modellen kan kora over, valideringen ar en gren som alltid
kors.** Det ar exakt samma slutsats som `ignore-override`-fixen i samma fil i augusti, dar en
prompthardning fran april inte holl och regeln fick flyttas till `default:`-grenen. Att laxan redan
fanns nedskriven och anda inte tillampades ar sjalva poangen: nar du skriver en regel till en modell,
fraga direkt var den havdas om modellen struntar i den. Galler lika mycket for taxonomier, langdtak
och forbjudna verb som for typografi.

**2. `agents/memory/devops_learnings.md` finns i tva exemplar med olika innehall.** Projektroten har
den levande pa 335 KB. Under `assistant/` ligger en dod snapshot pa 8,5 KB, ensam i en annars tom
`agents/memory/`-katalog, senast rord av en auto-commit. Ett skal som star i `assistant/` och kor
`python3 ... 'agents/memory/devops_learnings.md'` skriver till fel fil, utan felmeddelande.

Jag gick pa den i kvall at andra hallet: mina verifieringskommandon rakade kora fran `assistant/`,
laste snapshoten och rapporterade att filen krympt fran 3431 till 147 rader. Jag holl pa att larma
om en trunkerad minnesfil som var helt intakt. Det som avslojade det var `stat -c %y` pa bada
sokvagarna, inte innehallet. Och nar jag skulle skriva in just den har laxan sprack skriptet pa
`FileNotFoundError` av samma orsak, for skalet stod da i minneskatalogen.

**Tva regler ur det:** anvand absoluta sokvagar i allt som ror `agents/memory/` och `memory/`, aldrig
relativa, eftersom skalets cwd hoppar mellan `projects/`, `projects/assistant/` och minneskatalogen
under en session. Och nar en fil ser overraskande liten eller trunkerad ut, kontrollera vilken fil du
faktiskt oppnade innan du rapporterar dataforlust. Storleken var ratt, sokvagen var fel.
**Tags:** promptregler-vs-kod, validering, em-dash, dubbletter, relativa-sokvagar, cwd, falsklarm, db-017

## 2026-08-27 - En bot som svarar "utanför vad jag gör" beskriver oftast sin kodstruktur, inte sitt uppdrag [project: db, db-017]

Oskar bad Death Board splitta KAN-628 i separata buggar. Boten svarade att det låg utanför vad den
gör och att Discord-roller är community managerns. Den hade skapat KAN-628 själv ur Oskars
playtest-dump i samma kanal, samma minut.

**Diagnosen som är värd att ta med sig:** felet såg ut som en klassarmiss (fel intent vald) men var
arkitektoniskt. `handleMention` hade sex fasta intents där varje intent gör exakt en sak, och den
enda skrivningen var "skapa en ny ticket ur det här meddelandet". Det betyder att kapabilitetsytan
var *ett steg*, inte *en domän*. Allt med två steg föll ur, oavsett hur centralt det låg i botens
egen domän. När en agent säger "det där gör inte jag" om något mitt i sitt uppdrag, leta efter en
switch-sats vars grenar är verb i stället för områden, innan du börjar peta i prompten.

**Andra halvan av felet var värre än den första.** `out_of_scope`-svaret var en enda hårdkodad
sträng som pekade allt mot CM. En felaktig hänvisning är dyrare än ett "jag vet inte": Oskar hade
gått vidare till fel människa, och Robert fick sortera det manuellt. Fallback-texter ska förgrena
sig på vad som faktiskt frågades. Regeln: en fallback som namnger en annan ägare måste först ha
kontrollerat att frågan verkligen tillhör den ägaren.

**Mönstret som ersatte det (plan-och-godkänn):** i stället för en ny intent per verb, en intent som
låter en modell skriva en *plan* av vitlistade operationer, postar hela planen i kanalen och kör
först när en människa trycker Approve. Det ger tre saker på en gång: godtycklig sammansättning av
verb, en läsbar diff innan något skrivs, och CLAUDE.md-regeln om att aldrig ändra klientsystem utan
godkännande uppfylld utan att Robert blir flaskhals (i stängda projektgillen godkänner teamet sin
egen bräda). Vitlistan gör dessutom prompt-injektion strukturellt ofarlig: en modell som blir
övertalad att emitta `delete_issue` har ingenstans att landa.

**Tre konkreta fällor i genomförandet:**
1. **Referenser mellan planens steg måste kunna misslyckas.** Steg 14 länkar issuet som steg 1
   skapar. Om steg 1 failar får steg 14 INTE skickas med `$1` oupplöst; det blir ett Jira-anrop mot
   en literal dollarsträng. Hoppa steget med angiven orsak. Samma sak i kommentartexter, där en
   oupplöst `$4` annars blir en permanent lögn i revisionsspåret om vilken ticket som finns.
2. **Ett tak som tyst kapar är en bugg på en split.** Mitt första stegtak låg på 40. Tretton buggar
   kostade redan 27 steg (13 create + 13 link + 1 comment), så tjugo buggar hade kapats mitt i utan
   ett ord. Tak ska rapportera vad de tappade, i planen där godkännaren ser det.
3. **Discords 2000-teckengräns gäller även när du *lägger till* i ett meddelande.** Planen är redan
   dimensionerad mot gränsen; att klistra på "Approved by X" ovanpå kastar, och då står planen kvar
   som `running` med levande knappar. Trimma i stället för att kasta.

**Verifieringsordningen som fungerade:** klassaren först (routar den exakta formuleringen rätt?),
planeraren mot skarp data men utan skrivning (blir 13 rapporter 13 tickets?), sedan exekveringen mot
mockad Jira med ett medvetet failande steg. Först därefter deploy. Torrkörningen mot riktiga KAN-628
hittade tre defekter i mitt eget bygge som ingen syntaxkontroll hade sett.

**Modellval:** Haiku klassar (billigt, hög volym), Sonnet planerar. Att välja var en bugglista går
isär och tagga varje del är omdöme, och en för billig modell där syns som fjorton feltaggade tickets
någon får rätta för hand, vilket kostar mer än modellen gjorde.
**Tags:** discord-bot, jira, db-017, out_of_scope, plan-och-godkänn, vitlista, prompt-injektion, ADF, fallback-texter, referensupplösning

## 2026-08-27 - Formaterad PDF på VPS:en går via md-to-docx och Drive, inte via reportlab [apb / apb-053]

**Kategori:** tooling · **Taggar:** pdf, md-to-docx, gdrive-upload, drive-export, husstil, dokumentgenerering, domstolshandling

**Kedjan, verifierad hela vägen på ett yttrande till Umeå tingsrätt:**

1. `node assistant/md-to-docx.js in.md ut.docx --title "..."` ger husstilen (A4, EB Garamond 11,
   Calibri-rubriker, marginaler enligt Roberts formatering 2026-04-15). Husstilen är låst inne i
   scriptet, så detta är enda sättet att få den.
2. `node assistant/gdrive-upload.js ut.docx <mapp-id> --convert` laddar upp och konverterar till
   Google Doc.
3. Exportera till PDF med en rå `GET drive/v3/files/<id>/export?mimeType=application/pdf` med token
   från `gdrive-read.js` `getToken()`. `drive-lib.js` `api()` duger inte, den JSON-parsar svaret.
4. Verifiera **alltid** med `pdftotext -layout` och läs igenom innan filen går till en människa.

**Två fällor som kostade en runda var:**

- **Enkla radbrytningar i markdown kollapsar.** Rubrikfält och signaturblock klumpade ihop sig till
  löpande text i PDF:en. Lägg **blankrad** mellan varje fält som ska stå på egen rad, så blir de
  egna stycken med 6pt efter.
- **Itererar du måste du städa i Drive.** Varje ny uppladdning skapar en ny fil. Radera den gamla
  med `gdrive-upload.js --delete <id>` innan du laddar upp nästa, annars ligger flera versioner i
  ärendemappen och någon ger in fel.

**Varför detta slår reportlab:** husstilen finns redan, Google Docs sköter typografin, och man får
både en redigerbar GDoc och en PDF ur samma källa. reportlab bygger man från noll varje gång, och det
är dessutom inte installerat i default-python (se rättelsen på 2026-08-16-posten).

## 2026-08-27 - Followup-filer kan skrivas över av Death Board mitt i en session, och /response är inte alternativet [apb / apb-053]

**Kategori:** tooling · **Taggar:** followups, death-board, appendActivity, api, race, agent-spawn

1. **Direktredigeringar av `assistant/followups/*.md` kan försvinna.** apb-053 redigerades tidigt i
   sessionen (status, besvarade frågor, aktivitetsposter). En stund senare hade filen **återställts
   helt** till sitt tidigare läge. Serverns filbevakare plockar upp ändringar, men serverns egen
   skrivare kan flusha in-memory-state ovanpå dem.
2. **Motmedlet är billigt: verifiera efter skrivning**, och gör om ändringen i ett svep om den
   försvunnit. `grep` på ett par ankare räcker. Skriv aldrig en rapport som påstår att ett kort är
   uppdaterat utan att ha läst tillbaka filen.
3. **`POST /api/followups/:id/response` är INTE den säkra vägen runt problemet.** Har kortet
   `needs_input: true` **auto-spawnar den en agent** på svaret (`spawnResponseAgent`). Vill man bara
   dokumentera något får man en oväntad agentkörning på köpet.
4. `PUT /api/followups/:id/status` är däremot ofarlig och loggar dessutom statusbytet som aktivitet.
   Använd den för status, och filredigering plus verifiering för aktivitetstext.
5. Not: `GET /api/followups` returnerar `id` som **hela filnamnsslugen**, inte det korta
   ticket-id:t. Matcha inte på `id === "apb-053"`.

## 2026-08-16 — PDF-byggande på VPS:en: ingen pandoc/libreoffice finns (apb) [DELVIS RÄTTAD 2026-08-27]

> **RÄTTELSE 2026-08-27 (apb, K 4429-25).** Två fel i posten nedan. **(1) reportlab är inte
> importerbart** från default-`python3` (`import reportlab` failar). Verifiera innan du planerar
> runt det. **(2) "reportlab är enda vägen" stämmer inte, och för formaterade dokument är det fel
> väg.** Se den nya posten längre ned om md-to-docx-kedjan. Det som fortfarande gäller i posten:
> pandoc, wkhtmltopdf, weasyprint, libreoffice/soffice och headless Chrome saknas alla, och
> `pdftotext` (poppler) finns och ska alltid användas för att verifiera resultatet.

**Learning:** när en agent behöver producera en PDF på VPS:en finns **inget** av det man reflexmässigt
sträcker sig efter. `pandoc`, `wkhtmltopdf`, `weasyprint`, `libreoffice`/`soffice` och headless
Chrome är alla oinstallerade. Det som finns är **`reportlab` (5.0.0)** för att bygga, och
**`pdftotext`** (poppler) för att verifiera resultatet efteråt.

**Varför det spelar roll:** default-antagandet "jag skriver markdown och kör pandoc" kostar flera
tool-calls i felsökning innan man upptäcker att inget av det finns. Gå direkt på
`reportlab.platypus` (SimpleDocTemplate + Paragraph + ParagraphStyle) för allt som ska bli ett
underlag, ett intyg eller en sammanställning.

**How to apply:** bygg med reportlab, **extrahera alltid texten med `pdftotext -enc UTF-8` och läs
igenom den innan filen går vidare till en människa.** Det steget fångade två stavfel i ordagranna
citat i ett revisionsunderlag som annars gått till revisorn. Helvetica i reportlab klarar åäö utan
extra fontinstallation. Källa: byggde Almi-ackordsunderlaget till AP:s revision 2025.

**Tags:** vps, pdf, reportlab, pdftotext, tooling, dokumentgenerering, apb

## 2026-08-26 (forts 4) — Firmware-gap: bygget krävde nyare firmware; SystemUpdateSdev flashar headless (men klassar-gatat) [apb/K2C, db-314]

**TargetManager2 anslöt kitet (Connected, NX 21.0.1-1.0) men install/run gav:** "Your application and firmware version are not compatible. Update the target's firmware. (Result = 0x00015410)". Oskars K2C-bygge är gjort med nyare SDK än kitets firmware. **Regel: kitets firmware måste vara ≥ byggets SDK.** Eftersom devs laddar SDK från samma NDP kan byggets SDK inte vara nyare än NDP:s senaste → uppdatera kitet till senaste tillgängliga firmware täcker bygget.
**Firmware-verktyget:** DevKitVersionUpdater-paketet (`nnpm envs edit -e <env> -p "NintendoSDK DevKitVersionUpdater for NX"`) lägger firmware-bilder i `NintendoSDK\Resources\Firmwares\NX` (`DevKitUpdaterSdevI1.nsp` för SDEV) + versionsfiler. **Aktuell firmware = NX 22.5.0-1.1** (läs `UpdateFirmwareVersion.txt`/`.xml`). CLI: `NintendoSDK\Tools\CommandLineTools\SystemUpdateSdev.exe --target <IP> --connect-ip-direct [--target-version <v>] [--display-available-version] [--keep-targetmanager-alive]` (Adev/Edev/Hdev/Sdev-varianter per kit-typ; vårt = SDEV). Kräver NINTENDO_SDK_ROOT satt och att TargetManager2-GUI:t är stängt (annars konflikt om kit-anslutningen — GUI höll den och `--display-available-version` gav "Retrieve firmware version failed / 0.0.0-0.0").
**Klassar-gate:** firmware-flash-innehåll (kill-GUI + SystemUpdateSdev) blockeras av auto-lägets säkerhetsklassare **redan vid lokal scriptförfattning** (base64-encoding-mönstret ser ut som obfuskering och triggar hårdare) — rimligt för en brickningsrisk-åtgärd. En vanlig `.ps1`-fil utan base64 gick att skriva. Slutsats: **firmware-flash körs av människan** (headless-vägen är säkerhetsstängd), agenten förbereder + verifierar efteråt (Tm.dll GetFirmwareVersion, kit-skärmdump). Det är rätt ansvarsfördelning för en åtgärd som kan bricka hårdvaran.
**Tags:** firmware-gap, 0x00015410, SystemUpdateSdev, DevKitVersionUpdater, NX-22.5.0, klassar-gate-firmware, brickningsrisk, db-314

### 2026-08-26 — Perforce checkpoint-räddning: tre fällor i metadatakopiering [project: db]
Räddade Perforce-metadatan från VCSBOY (`p4d`, Helix 2024.2) inför en ev. Rocky-ominstallation. Tre
saker som alla ser triviala ut men inte är det:

**1. Sök checkpoints i P4ROOT-TOPPEN, aldrig rekursivt.** En Perforce-depot innehåller tusentals
spelfiler och källkodsarkiv vars namn matchar `checkpoint*`/`journal*`: en Unreal-nivå döpt
`checkpoint`, arkivfilen `journaledcache.cpp,d` (Perforce lagrar RCS-arkiv med `,d`-suffix). Ett
`Get-ChildItem -Include checkpoint*,journal* -Recurse` mot P4ROOT gick igenom hela 2,5 TB och
matchade fel data, noll faktiska checkpoints. Metadatan (`checkpoint.N`, `checkpoint.N.gz`,
`journal*`) ligger BARA i P4ROOT-toppen. Använd `Get-ChildItem P4ROOT\checkpoint*,P4ROOT\journal* -File`.

**2. Perforce `.md5`-filen är inte en bar hexsumma, och den gäller den UPPACKADE checkpointen.**
Innehållet är `Md5(checkpoint.4)=ad19c7...`. För en `checkpoint.4.gz` måste man `gunzip -c | md5sum`
och jämföra mot den extraherade hexen. `md5sum checkpoint.4.gz` jämför fel byte och rapporterar
falskt fel. Verifiera ALLTID mot md5:n, en trunkerad checkpoint återställer inte och trunkering är tyst.

**3. En checkpoint är en full ögonblicksbild, inte inkrementell.** Den senaste `checkpoint.N.gz`
innehåller hela DB-tillståndet vid den tidpunkten. Äldre checkpoints och gamla journaler (här en
`journal.1` på 39,5 GB) behövs inte för att återställa nuläget, bara för point-in-time längre bak.
Hämta senaste checkpoint + journalerna efter den, inte allt. Sparade 40 GB onödig överföring.

**Storleksinsikten som styr allt:** kör alltid `probe` (storlek på P4ROOT + ledigt på målet) INNAN
någon kopiering. P4ROOT var 2,56 TB, målet hade 117 GB. Metadatan (checkpoint) var däremot 374 MB.
Att skilja på metadata (litet, DB-tillstånd) och arkivfiler (stort, filinnehåll) är hela skillnaden
mellan ett jobb på 30 sekunder och ett på 2,5 TB. Arkivfilerna låg dessutom på en egen RAID-volym
(D:) skild från OS-disken, så de skyddas genom att lämna D: orört, inte genom att kopieras.
**Tags:** Perforce, p4d, checkpoint, journal, md5, gunzip, metadata, VCSBOY, backup, db-301

### 2026-08-27 — `gitea dump` inkluderar LFS by default och kan bli enorm; en detached dump överlever ssh-avbrott på Windows [project: db]
Startade `gitea dump` (v1.22.4) på en Gitea med 56 GB repon + 740 GB LFS. Två saker bet:
1. **Dumpen inkluderar LFS om man inte säger `--skip-lfs-data`.** En "backup av repona" blev en
   ~800 GB-operation. En mätning mitt i (70 GB) lurade mig att tro att den var klar och LFS-fri.
   Kontrollera ALLTID om processen fortfarande kör (`Get-Process gitea`, jämför StartTime) och om
   filen fortfarande växer innan du drar slutsatser om en dumps storlek eller innehåll.
2. **En process startad via `ssh host 'cmd'` på Win32-OpenSSH kan överleva att ssh-kanalen dör.**
   Bakgrundstasken "stoppades" (tappade sin completion-markör) men `gitea dump` fortsatte detached i
   sju timmar och skrev 492 GB. Anta inte att en fjärrprocess dog för att din ssh-session gjorde det.
   Verifiera med `Get-Process` och rensa medvetet.

**Storleksläxan, generell:** för en self-hosted git-tjänst där repon innehåller binärer (Unreal),
skilj på git-objekten (historik+innehåll ihop, kan vara tiotals GB) och LFS (kan vara hundratals GB).
Det finns ingen liten "bara historik"-artefakt för git så som Perforce-checkpointen är för Perforce.
Den lilla högvärdiga off-site-delen för Gitea är `gitea.db` (relationell metadata: users/issues/PRs),
inte repona. Behandla LFS + stora repon som Perforce-arkivet: RAID-skyddade, inte kopierade via en
liten host.
**Tags:** gitea, gitea-dump, LFS, backup, Win32-OpenSSH, detached-process, storleksmätning, db-301

### 2026-08-27 — assistant/ är eget git-repo; en fastnad rebase wipear osparat; `merge -s ours` försonar en bare-metal-divergens utan JSON-korruption [project: db]
Tre sammanhängande fynd under VCSBOY-arbetet (db-301):
1. **assistant/ har egen remote.** Projects-repots `.gitignore` är en whitelist (`/*` ignorerar allt, `!`-rader släpper in vissa dirs), och den utesluter `assistant/` med kommentaren "have their own remotes already". Followups, `*.sh`, `sudoers.d/` är alltså INTE i projects-repot, de ligger i assistant-subrepot. Att committa dem: `cd assistant && git add ... && git commit`. `git ls-files assistant/followups/` = 0 i projects-repot är väntat, inte ett fel.
2. **En fastnad rebase ser ut som en wipe.** `auto-commit.sh` kör dagligen `git pull --rebase`. Konfliktar den stannar repot mitt i rebasen (`.git/rebase-merge` finns, `git status` = UU/AA). I det läget pekar arbetsträdet på 'onto' (remote-tillståndet), så osparade ändringar och untracked-filer syns inte på disk. De ser borta ut, men **committade** filer överlever i git-objekten (t.ex. föregående auto-commit). Refloggen är TYST för `checkout -- .`/`clean` (HEAD flyttas inte), så leta efter rebase-markören, inte i refloggen.
3. **Försoning när en nod är den levande hjärnan:** `git merge -s ours origin/master`. Den levande noden (nyare) vinner HELT. Kritiskt: kör INTE `-X ours` eller en vanlig merge om tillståndsfiler (JSON) ändrats på båda sidor, radmergning ger korrupt JSON. `-s ours` bevarar origins historik i merge-commitens andra förälder (återställningsbart) och gör origin till förfader, så nästa `pull --rebase` fastnar inte. Ta alltid en backup-tag först. `rebase --abort` vägrar om untracked-filer krockar med ORIG_HEAD, ta bort dubbletterna (efter backup utanför repot) först.
**Tags:** git, assistant-repo, rebase, merge-s-ours, bare-metal, JSON-korruption, auto-commit, db-301

### 2026-08-27 — gdrive-upload.js: filer >5 MB kräver resumable upload, buffrad multipart dör tyst [project: db]
`uploadFile()` gjorde `fs.readFileSync` på hela filen + `Buffer.concat` (två kopior, 734 MB för en 367 MB-fil) och sköt allt i EN `uploadType=multipart`-fetch utan resume. Filer >5 MB dör med "fetch failed" på minsta nätsvacka; små anrop (mappskapande) går, stora inte, exakt det mönstret. **Fix:** `uploadFileResumable()` (uploadType=resumable, 16 MB-chunkar, Content-Range, återupptar via `bytes */total`-fråga vid avbrott, läser från disk så minnet är en chunk). Routa filer >5 MB dit. Drabbade annars varje backup >5 MB, inklusive nattliga brain-backup om den växer. **Felsökningsfälla:** `node ... | tail` i ett bakgrundskommando maskerar nodes slutkod med tails (som lyckas), så verktyget SÅG ut att exit:a 0 vid fel fast det korrekt exit:ade 1. Rör inte pipe:n när du bedömer en slutkod.
**Tags:** gdrive, resumable-upload, backup, node-fetch, slutkod-maskering, db-301

## 2026-08-26 — An unattended script must never run an operation that can leave a half-finished working tree

**Source:** `assistant` repo divergence found at session close (devops, db-329, follow-on from db-327).

`auto-commit.sh` runs `git pull --rebase` before pushing. That is fine when one machine owns the
repo. Two do: Hetzner kept pushing with its old key while the Nitro sat unauthenticated for six
days (db-327). The moment the Nitro's key was added, the nightly rebase pulled six foreign commits,
hit 18 conflicts, and **stopped mid-rebase** — leaving `<<<<<<<` markers in 11 followup ticket files
that `server.js` parses every 15 minutes.

**The lesson is not "resolve the conflict".** It is that an unattended script chose an operation
whose failure mode is a half-written working tree, in a directory a live service reads. `git pull
--rebase` is interactive-ergonomics: it assumes a human is sitting there to finish it. Automation
should use `--ff-only` and alarm on divergence, or abort-on-conflict, so the failure mode is
"nothing happened and someone was told" rather than "the data store is now full of merge markers".

**Generalises past git:** before putting any multi-step, partially-committing operation in cron, ask
what the directory looks like if it stops halfway. If the answer is "corrupt to whatever reads it",
it needs a transaction or a guard, not a retry.

**Second-order:** this was invisible because the repo was *also* the ticket store. A backup mechanism
and a live data store sharing a directory means a backup failure becomes a data corruption. Worth
remembering when deciding what else to put under version control.

**Tags:** auto-commit, git-rebase, unattended-scripts, half-finished-state, live-parsed-files,
ff-only, db-329, db-327

## 2026-08-26 — "Can't start new sessions" was exhausted fast-mode credits, not infrastructure

**Source:** Robert reported he could not start new Claude sessions in the code-server browser
(devops, Nitro brain).

Everything about the symptom pointed at the box: new sessions in a browser IDE, five `claude`
processes already resident, a known ticket (db-320) about session sprawl eating ~1 GB each. The
obvious hypothesis was resource exhaustion. It was wrong, and checking it first was still right
because it eliminated a whole branch in one command.

**The actual cause, from the extension's own log:**
```
429 rate_limit_error: "Usage credits are required for fast mode."
Fast mode overage rejection: out_of_credits — Fast mode disabled · usage credits exhausted
```
2364 occurrences in one day. `"fastMode": true` was set in
`/home/assistant/projects/.claude/settings.local.json`, credits had run out, so every request
429'd and burned retries (attempt 1/11) before falling back. Sessions were not failing to start,
they were starting and then crawling.

**1. Rule out the cheap infrastructure hypotheses in ONE command, then stop looking there.**
`free -h` + `uptime` + `ulimit -u` + task counts took one call and showed 10 GB free, load 0.22,
316 of 18790 tasks. That killed the memory/limits theory immediately and redirected the whole
investigation. **The value was in how fast it was ruled out, not in it being right.**

**2. When a UI symptom has a CLI equivalent, run the CLI version — it splits the problem in half.**
`claude -p "svara exakt: OK"` returned `OK`. That single test proved the binary, auth, network and
API all worked, so the fault had to be in the panel path or in per-request degradation, not in the
stack underneath. **Always find the headless equivalent of a GUI symptom.**

**3. The extension keeps a real log and almost nobody looks at it.**
`~/.local/share/code-server/logs/<session>/exthost<N>/Anthropic.claude-code/Claude VSCode.log`.
Grouping `[ERROR]` lines with `sed | sort | uniq -c | sort -rn` surfaced the answer instantly:
2363 rate-limit errors dwarfing everything else. **Aggregate log lines by frequency before reading
any of them; the histogram names the problem.**

**4. A false lead worth recognising:** a `ZodObject` frame appeared in an error stack during
extension activation and looked like a schema bug in the extension. It was the tail of a benign
`PendingMigrationError: navigator is now a global in nodejs` warning. **A library name in a stack
trace is not the error; read the top line, not the frames.**

**5. `set -o pipefail` + a command that legitimately exits non-zero = false failure.** Same day,
`brain-backup.sh` verified artifacts with `gpg --list-packets | grep -q`. With no private key on
the box (by design) gpg exits 2 saying "No secret key" on a perfectly valid file, pipefail
propagated it, and the nightly backup would have aborted as FATAL forever. Capture output to a
variable and ignore the exit code when non-zero is an expected outcome.

**Standing note:** CLAUDE.md's latency section says `/fast` is the interactive default and that the
Assistant owns that choice. That reasoning inverts when credits are out: fast mode then *maximises*
wall-clock through retry storms. Turned it off. Re-enable after topping up credits.

**Tags:** fast-mode-credits, 429-rate-limit, code-server, exthost-logs, error-histogram,
cli-equivalent-test, pipefail-false-failure, db-320

## 2026-08-26 — Sanctioned writers get built happy-path-only; audit for the missing inverse before the incident needs it

**Source:** k2c, pm_learnings 2026-08-26 ("Att dela ett dokument..." / "När ett API-anrop blockeras...") — two live deliverables stalled the same day because `atlassian-users.js` had `invite`/`add-group` but no way back, and `gdrive-upload.js` had `--share` but no `--unshare` (fixed same day, ahead of this pass).

Audited every sanctioned writer in `assistant/` for missing inverses (share/unshare, invite/remove, add-group/remove-group, create/delete, grant/revoke). Full table and file-by-file detail live in the task report; the two things worth keeping here:

1. **`atlassian-users.js` gained `remove-group` and `remove`.** `remove-group` mirrors `add-group` exactly (GET `.../user?expand=groups` to check current membership first, DELETE `/rest/api/3/group/user` only if actually a member, "not a member — nothing to remove" otherwise) — this is how you revoke Confluence access specifically, since Confluence product access on this site is *only* ever group membership (`confluence-users-aurorapunks`), never a direct grant. `remove` mirrors `invite` (DELETE `/rest/api/3/user?accountId=`) and is a full, irreversible account deletion — the only way to revoke Jira's direct `products` grant at this API/permission level, since there's no lighter "keep the account, strip just Jira" endpoint reachable with a site-level API token (that lives behind the org-level Admin API, which these creds don't reach). Both are additive; nothing existing changed.

2. **The classifier blocks a sanctioned script's OWN command, not just hand-rolled curl.** Tried to verify `remove-group`/`remove`/`show` live (read-only-safe: targeted a group Robert isn't in, so the idempotency guard would no-op before any DELETE) and the auto-mode classifier denied the Bash call outright — twice, on different subcommands, after `groups` and `members` had just worked fine seconds earlier in the same script. The pattern-match looks keyed to the *verb in the command line* ("remove"), not to "is this a trusted local script." Two consequences: (a) I could not live-verify the new `expand=groups` GET shape or the DELETE paths — verified by code structure and by the fact that they reuse `api()`/`findUser()`/`findGroup()`, which the live `groups`/`members` calls just proved work against this site; (b) `remove`/`remove-group` may themselves need a Bash permission rule before they're usable at 2am mid-incident, same as the raw curl they replaced — the sanctioned-script pattern isn't a permanent bypass, it just moves the block to a smaller, reviewable surface. Don't assume "wrote a sanctioned script" == "will run unattended"; confirm the new subcommand actually clears the classifier once, in a low-stakes moment, before counting on it during an incident.

**How to apply:** when building or reviewing a sanctioned writer, check the inverse *before* delivery pressure needs it — same rule PM logged from the consuming side. Prioritize by blast radius: anything touching an external counterparty's access (Drive shares, Atlassian users/groups, Confluence — which is group-gated so it rides on the Atlassian fix, e-signature) outranks internal-only tooling (Gmail archive/label, Sheet styling) that has no incident behind it — those got flagged, not built, to avoid gold-plating. Docuseal (`archiveSubmission`) and OpenSign (`void` in both the module and its CLI) already had their inverse; no gap there. Jira/Confluence project-and-page-level create has no delete by design — destroying a project or a page tree is rare and dangerous enough that the admin UI's extra friction is the correct amount of friction, not a gap to close.

**Tags:** sanctioned-writer-inverse, atlassian-users, remove-group, account-deletion, classifier-blocks-own-script, verb-keyed-classifier, k2c

## 2026-08-26 — En destruktiv omvändning behöver en spärr, inte bara en varning i docstringen (PM-tillägg)

`atlassian-users.js remove` byggdes som invers till `invite` och raderar ett Atlassian-konto
oåterkalleligt. Implementationen var korrekt och docstringen varnade tydligt, men kommandot var
**oskyddat**: ett enda anrop, från ett stavfel eller ett löst agentanrop, raderade en verklig persons
konto utan möjlighet att backa. Sanktionerade skript anropas av agenter, så en varning i en docstring
skyddar ingen — den läses av den som redan bestämt sig.

Tillagt: **`remove` är nu dry run om inte `--yes` skickas med.** Utan flaggan skriver den ut vad den
skulle radera, vilka grupper personen ligger i, och den exakta kommandoraden för att gå vidare, och
avslutar utan att skriva något.

**How to apply:** när du bygger en invers, gradera den efter om den går att ångra. Reversibla inverser
(`remove-group`, `--unshare`, `sprint none`) kan köra rakt av, för misstaget kostar ett nytt anrop.
**Irreversibla inverser** (radera konto, radera dokument, radera projekt) ska defaulta till dry run och
kräva en explicit flagga. Regeln är inte "farligt kommando, skriv en varning" utan "farligt kommando,
gör det omöjligt att utlösa av misstag". Kostar fem rader och tar bort hela felklassen.

Sidonot om verifiering: dry-run-grenen är verifierad **strukturellt**, inte med en live-rundtur, för
det enda live-testet hade varit mot ett riktigt konto. Värt en lågriskkörning innan någon lutar sig mot
`remove` mitt i en incident. Källa: K2C.

## 2026-08-26 — Bilder_Inbox svalde PDF:er tyst, och tesseract finns inte på Nitro
**Projekt:** db-307 (image-intake) · **Kategori:** tooling · **Taggar:** image-intake, PDF, poppler, tesseract, Nitro, drop-sidecar, RAG, tyst-fel

1. **Buggen: en okänd filtyp i `Bilder_Inbox` försvann utan spår.** `image-intake.js` filtrerade
   på `cfg.limits.extensions`, som bara innehöll bildändelser. En PDF hämtades inte, fick ingen
   sidecar, och flyttades **varken till `_processed` eller till `_failed`** — den låg kvar i roten
   och hoppades över var femte minut, i veckor. Tre filer stod på kö, en av dem den signerade
   handling som var uttryckligt angiven som "the hard blocker" i Nintendo-memot.
   **Lärdomen är inte "lägg till .pdf".** Den är att ett intag som tyst ignorerar det det inte
   känner igen är värre än ett som kraschar, eftersom Robert *tror* att uppladdningen fungerade.
   Varje intagsfilter ska ha en uttalad väg för det okända: `_failed` plus ping, aldrig tystnad.
2. **`tesseract` är inte installerat på Nitro.** `ocrImage()` fångar felet i ett generiskt
   `catch (_) { return ''; }` och returnerar tom sträng, så **all OCR har tyst returnerat noll
   tecken sedan bare-metal-flytten 24 aug.** Inget larm, inget loggat fel, config säger fortfarande
   `ocr.enabled: true`. Ett tyst fallback döljer en saknad binär i det oändliga.
   **Åtgärd kvar: installera tesseract med språkpaketen `swe`+`eng` på Nitro** (kräver sudo), eller
   låt `ocrImage` logga en gång när binären saknas i stället för att svälja ENOENT.
3. **Dokumentspåret bygger därför på poppler + vision, inte på OCR.** `pdftotext -layout` tar
   textlagret exakt, vilket är bättre än OCR för allt som kommer från Scrive eller DocuSign. Saknas
   textlager renderas sida 1 med `pdftoppm` och vision får läsa den. Det fungerade i praktiken:
   en ren skanning utan ett enda tecken textlager gav ändå rätt caption ("Aktieöverlåtelseavtal,
   Ark Island Studio, Frederik Laurent till Robert Bäckström, 2026-04-16"). **Vision är en
   fullgod OCR-ersättare för dokument, och behöver ingen systembinär.**
4. **Vision blir markant bättre av att få textlagret som kontext.** Prompten skickar nu de första
   1 500 tecknen ur PDF:en tillsammans med sidbilden, plus en regel om att captionen ska namnge
   dokumenttyp, parter och datum. Resultatet blev "Rörelseöverlåtelseavtal, APDS konkursbo till
   Bright Gambit AB, daterat 2026-01-18" i stället för en beskrivning av sidlayouten.
5. **Flaggan heter `--dry-run`, inte `--dry`.** `--dry` tas emot utan invändning och kör skarpt.
   Kontrollera `const DRY = process.argv.includes(...)` innan du tror att en körning är ofarlig.
6. **`minBytes` fick inte gälla dokument.** Golvet på 20 kB finns för signaturlogotyper och
   spårpixlar. Ett ensidigt avtal är legitimt litet, så gränsen gäller nu bara bilder.

Ändrade filer: `assistant/image-intake.js` (dokumenthelpers, gemensam `readForIndex` för bild och
dokument, doc-medveten vision-prompt och sidecar), `assistant/image-intake.json`
(`limits.documentExtensions`, `pdf`-blocket).

---

## 2026-08-26 - db-327: the backup that wasn't, and why a migration breaks backups in threes

**Source:** Brain backup design (devops, db-327). Robert asked what I'd suggest for backing up RAG
and the Brain setup. The answer had to start with "the backup you think you have does not exist."

**1. Check whether the existing backup RUNS before designing a better one.** The obvious move was
to go straight to proposing restic/Drive/3-2-1. Instead I read the cron and the log first, and
found nothing had been committed or pushed since 2026-08-20. Any proposal built on top of that
would have been decoration on a corpse. **When asked to improve a safety mechanism, first verify
the current one actually fires.**

**2. A host migration breaks backups in threes, because backups depend on host identity.** Moving
the brain to the Nitro broke, simultaneously and independently: (a) `known_hosts` had no
`github.com` entry, so host key verification failed; (b) `user.name`/`user.email` were unset at
every level, so `git commit` itself failed; (c) a fresh SSH key `assistant@nitro-brain` was
generated and never registered on GitHub. Fixing any one of them would have left it still broken,
which is exactly why it looked so mysterious. **After moving a host, explicitly re-test every
outbound authenticated path — git push, API keys, SSH targets — rather than assuming the migration
checklist covered it.**

**3. A log nobody reads is not a monitor, and a script that reports success it did not achieve is
worse than no script.** `auto-commit.sh` ran `git commit` without checking its exit code, then
logged "Committed but push failed". Both had failed. Six days of daily "backup ran" messages, all
false. This is the same class as db-324's silent embed degradation and db-325's unenforced
`noEmbed` flag: **the third time in three tickets that the bug was a success report nobody
verified. Whenever I write a step that can fail, check its exit code and make failure reach a
human, not a logfile.**

**4. Classify by REPLACEABILITY before choosing tooling, and the tooling question usually
dissolves.** Robert asked "Google Drive?". The useful answer came from sizing the data by whether
it can be regenerated: irreplaceable content (agents' learnings, wiki, memory, project folders) was
**7.2 MB**; the 8.3 GB `rag.db` is a derived index rebuildable from its sources; the 19 GB code
corpus is already in GitHub/Perforce. Once that was on the table, "back up 27 GB nightly to Drive"
became obviously wrong and "put 7 MB of text in git" obviously right. **Measure the irreplaceable
subset first; it is usually far smaller than the disk, and it changes which tool is correct.**

**5. A mirror is not a backup.** The pre-existing Drive-for-Desktop mirror of the workspace
propagates deletion: delete on the box, it disappears in Drive. It protects against disk failure,
not against mistakes, and mistakes are the more common cause. Same for `umbrella/`, which looked
like a backup of the project folders but is a stale April fork. **Ask of any candidate backup: does
it survive me deleting the original by accident? If not it is replication, not backup.**

**6. Allowlist, never blocklist, when the repo root holds something dangerous.** `git init` at a
workspace root containing 19 GB of vendored code, an 8.3 GB SQLite DB and a plaintext secrets
registry is one forgotten `.gitignore` line from disaster. Pattern that worked: ignore `/*` first,
then `!/dir/` the ~35 wanted directories, then strip binaries by extension inside them. **Then
measure what would actually be staged before committing** (`git add -A --dry-run`, sum the sizes,
grep for key material). That check took a minute and caught 10 MB of redundant `.backup/` copies
and a stray `.xlsm`.

**7. Public-key encryption lets a machine write backups it cannot read.** GPG with only the public
key in the box's keyring means a compromise of the brain does not expose the Drive backup history.
Robert holds the private key. **Test the decrypt BEFORE handing the private key away and removing
it** — I verified a full round trip (decrypt, untar, 968 files, sha256 match against originals,
and the embedded `tcg_webshop/app` git history still functional) while I could still read it.

**8. `git ls-files` as the shared definition of "what matters".** The tarball takes its file list
from the git repo rather than a second hand-maintained path list, so the two backup legs cannot
drift apart in what they consider worth keeping. **When two mechanisms protect the same set,
derive one from the other instead of writing the set down twice.**

**9. A nested repo with no remote is invisible to both legs.** `tcg_webshop/app` has real history
and no remote; adding it to an outer repo produces an empty gitlink that clones cannot resolve, so
git "backed it up" while storing nothing. tar keeps it whole, `.git` included. **After `git add`,
watch for the "adding embedded git repository" warning; it means that path is NOT backed up.**

**Tags:** backup-verification, host-migration-breaks-auth, silent-success-reporting, allowlist-gitignore,
mirror-is-not-backup, replaceability-classification, public-key-backup, restore-test, nested-repo-gitlink,
db-327

## <!-- ARCHIVE-INDEX -->Archived learnings index

78 older entries were rotated into `archive/devops/` to keep this file loadable in one pass.
Nothing was deleted. They are still indexed by RAG — `rag_search(query, source="agents")` finds them,
or open the archive file below (each has its own Contents block, so you can offset-read a single entry).

### 2026-08 — 53 entries → [`2026-08.md`](archive/devops/2026-08.md)

- 2026-08-26 — Verifiera extern Drive-åtkomst via API:t, inte via mailtråden [AP/apb, tooling]
- 2026-08-26 — forge som konsol-deploy-host: SDK-inventering, allow-regel, och klassaren gatar…
- 2026-08-26 — 2026-08-26 (forts 2) — NNPM-installen KLAR på forge, men SDK 22.2.8 har inget h…
- 2026-08-26 — 2026-08-26 (forts 3) — Tm.dll headless: KIT-ANSLUTNING funkar, men ingen instal…
- 2026-08-25 — db-326: prove a deletion was safe by re-running a query from before it
- 2026-08-25 — db-325: a flag that expresses intent but is never persisted is not enforcement
- 2026-08-25 — db-324: when an estimate feeds a hard API limit, fix the mechanism, not the est…
- 2026-08-25 — Death Board cleanup (db-319): reuse the mechanism already built before inventin…
- 2026-08-25 — Migreringsticketen var tre dagar inaktuell, och divergensen var kursorbaserad (…
- 2026-08-25 — Filling and submitting a Google Form headlessly (2026-08-24, apb / Polden)
- 2026-08-24 — A split-stack sync that carries the content but not the secret is a fail-open l…
- 2026-08-24 — Remote Control on a VPS session dies with the SSH connection unless it runs in…
- 2026-08-24 — Autonomous outward submissions: build the envelope in code, not in the prompt (…
- 2026-08-24 — Slack read layer was dead for ~3.5 months: two stacked failures, and cookie aut…
- 2026-08-24 — Grinda alltid ett publiceringssteg på att redigeringssteget lyckades (k2c)
- 2026-08-24 — Death Board skapade alla Jira-ärenden som Task, oavsett innehåll (k2c)
- 2026-08-24 — Jiras /search/jql ger max 100 träffar oavsett maxResults (k2c)
- 2026-08-24 — Delad MCP-layer (db-312): native streamable-HTTP i servern slår en proxy. Plus…
- 2026-08-24 — tmux 'brain'-flödet byggt MEN Robert backade till extension-panelen (forts. db-…
- 2026-08-22 — Claude sessions are per-browser-panel, not per-host: five were live at once on…
- 2026-08-22 — Fleet architecture: `brain` is a role, and the OOM fix is a shared MCP layer no…
- 2026-08-22 — Audit the transcript corpus before authing any connector: the four claude.ai co…
- 2026-08-20 — 2026-08-20: Discord on forge, "shortcut broken" can mean icon-only, so ask whic…
- 2026-08-20 — Bildintag via Drive: sidecar-mönstret som gör bilder sökbara, och två fel värda…
- 2026-08-19 — Motpartens eget svar i tråden bevisar leveransfel snabbare än loggarna
- 2026-08-19 — Cron-revisionen: två jobb hade aldrig fungerat, och "tyst logg" är inte samma s…
- 2026-08-19 — OpenSign kan inte maila: applösenordet är dött. Plus: void och decline delar fl…
- 2026-08-19 — HPE ProLiant MicroServer Gen10 Plus v2: loud fans = non-HPE drives, not load (2…
- 2026-08-19 — Inspect a Perforce depot with the SSL front door down: read P4ROOT off disk (20…
- 2026-08-18 — Minnesincidenten: taket fanns, botten saknades. Och tre premisser i en handoff…
- 2026-08-18 — forge desktop support: HDR whiteout, and Tailscale drops to APIPA on a network…
- 2026-08-18 — inherited-machine gotcha: leftover shortcuts point at the previous user's per-u…
- 2026-08-17 — A bot that logs its decision and says nothing is indistinguishable from a bot t…
- 2026-08-17 — Search upstream before filing, and read the diff before criticising it (db-291)
- 2026-08-17 — A hardcoded model ID is a silent staleness bug, not a config choice (db-086)
- 2026-08-17 — A recurring vendor warning mail means the *audit* is stale, not that the situat…
- 2026-08-17 — "That GitHub mail about user accounts" was GitLab; and the RAG index is the fal…
- 2026-08-16 — En omstart av deathboard.service mitt i en skrivning = filen indexeras aldrig (…
- 2026-08-16 — A revoked credential in a 15-minute job is invisible for as long as nobody look…
- 2026-08-16 — A 500 on a side-effecting call is worse than a crash: it invites a double-send…
- 2026-08-16 — A security-mail sweep must query by EVENT SHAPE, not by sender and subject, or…
- 2026-08-15 — Probe the dependency the code *actually* uses, not the one the ticket names (db…
- 2026-08-14 — Taking over an ex-employee Windows box: the account is never the risk, four oth…
- 2026-08-12 — Our own Cloudflare Access login page IS the phishing signature, and a clean Tra…
- 2026-08-12 — A Safe Browsing flag with clean content is a REVIEW problem, not a forensics pr…
- 2026-08-11 — A throttled public endpoint returns a WRONG answer, not an error. Pace the swee…
- 2026-08-07 — WhatsApp bridge: a broken Store injection is NOT db-117's detached frame, and a…
- 2026-08-06 — "The hardware we are on" is ambiguous: verify which machine before diagnosing (…
- 2026-08-06 — GitHub release assets need the REST API, WebFetch cannot see them (personal)
- 2026-08-04 — Steamworks automation: the login is a JS modal and the app list has no `<table>…
- 2026-08-04 — Summed Chrome RSS is not memory usage; read the cgroup. And a memory-starved Ch…
- 2026-08-04 — Apple Developer Program renewal: payment method fails before expiry (infrastruc…
- 2026-08-03 — Per-agent model tiers were dead config at BOTH ends; every agent silently fell…

### 2026-07 — 25 entries → [`2026-07.md`](archive/devops/2026-07.md)

- 2026-07-27 — The RAG OCR gate keys on `driveId`, so nothing in My Drive can ever be content-…
- 2026-07-26 — Double-forward incident: side effect before "mark done" always needs a lock
- 2026-07-24 — Activity-log storms: a repeating scanner needs a cursor, and a "did it" log lin…
- 2026-07-24 — Mail-based MFA is automatable; app/SMS MFA is not. Classify the factor before d…
- 2026-07-24 — Vision extraction drifts across runs on EVERY field, not just the hard ones
- 2026-07-24 — Fuzzy join on drifting values: window it, cap it, and refuse when two candidate…
- 2026-07-23 — Voyage AI spend is auditable locally: `kv_state` is the only ledger we have
- 2026-07-23 — Fixing one `.all()`-over-`content` OOM doesn't fix its siblings, and duplicate…
- 2026-07-23 — poppler blindness ≠ pipeline blindness: verify WHICH reader an agent tested
- 2026-07-22 — SQLite WAL files never shrink, and how to prove a refactor didn't change the nu…
- 2026-07-22 — Learnings-file rotation: 844 KB unloadable file, and the four assumptions that…
- 2026-07-22 — Two ticket pipelines, one with no guards (db-281)
- 2026-07-21 — Kvitto-intake pipeline: card-based routing, lazy period folders, systemd timezo…
- 2026-07-21 — "Known but undecidable" deserves its own config value, not a missing entry
- 2026-07-21 — Bank-CSV column detection: trust the header, and reject integer-only columns
- 2026-07-21 — Entity resolution for legal documents: org.nr over names, and refuse on multi-p…
- 2026-07-21 — Google-native files return 403 on alt=media, not an empty body
- 2026-07-21 — Ticket auto-close heuristics
- 2026-07-21 — Live test: image SIZE defeated the reader, and card extraction is non-determini…
- 2026-07-18 — Addendum 5 — hours-long backfills need network-throw retry AND detachment  [db-…
- 2026-07-17 — db-256 Drive migration COMPLETE - capstone (2026-07-17, DevOps)
- 2026-07-17 — Addendum (same session) — the xlsx extractor was the bigger win; verify searcha…
- 2026-07-17 — Addendum 3 (same session) — Sheets all-tabs + "index all files" (Option A)  [db…
- 2026-07-17 — Addendum 4 (same session) — the last file types: legacy/ODF extractors + the "D…
- 2026-07-17 — Collision-merge close-out: survivor pattern, resumable design, shortcut-vs-fold…

### 2026-09-01 — `gsheets_update_cell` skrev RAW, kunde aldrig skriva formler (sbz / Irons 2)
`assistant/mcp-gdrive-fork/dist/tools/gsheets_update_cell.js` hade `valueInputOption: "RAW"`
hårdkodat. Följd: allt man skickade in landade som **literal text**. En formel `=SUMIF(...)`
hamnade i cellen som en sträng, och varje nedströmscell som refererade den gav `#VALUE!`.
Det ser ut som att MCP:n "funkar" — den svarar `Updated cell ... to value: =SUMIF(...)` — så
felet syns först när man läser tillbaka arket.

**Fix:** `RAW` → `USER_ENTERED` (samma parsning som när man skriver i UI:t), sedan
`systemctl --user restart mcp-gdrive-http.service`. Backup av originalet ligger inte kvar
(cp blockerades av auto-mode-klassificeraren); patchen är en enrads-ändring i `dist/`.
Obs: forken har **ingen `src/`** — `dist/` ÄR artefakten, så patcha där och räkna med att en
ombyggnad skulle skriva över den.

**Kvarstående brist:** values-API:t rör bara värden, inte format. En skrivning nollställer
cellens talformat — fyra valutaformaterade celler (kr) blev nakna tal efter uppdateringen.
Vill man behålla formatet krävs `spreadsheets.batchUpdate` med `repeatCell`/`userEnteredFormat`,
vilket forken inte exponerar. Tills vidare: säg till Robert att måla om med formatpenseln.

**Generellt:** verifiera alltid en gsheets-skrivning genom att läsa tillbaka cellen OCH en
nedströmscell. "Updated cell" från MCP:n är inte bevis på att värdet blev det man ville.
