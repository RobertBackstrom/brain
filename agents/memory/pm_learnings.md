

<!-- ROTATION-NOTE -->
> **This file holds the most recent entries only** (rotated by `assistant/rotate-learnings.js`, ~100 KB budget).
> Older entries live in `archive/pm/` and are listed in the archive index at the bottom of this file.
> Nothing is deleted and everything stays searchable via `rag_search(query, source="agents")`.
>
> **Still append new learnings to the TOP of this file** — rotation moves the tail out on its own.

## 2026-08-31 — Embedding a Drive video in a K2C Confluence delivery page (k2c)

Milestone playthrough videos: upload to the K2C shared `_deliverables/ms<N>` Drive folder, then embed in that milestone's Confluence delivery Legend page. The embed is a plain Confluence macro pointing at the Drive file URL, copied verbatim from the MS3 page (125566978):
`<ac:structured-macro ac:name="embed" ac:schema-version="1" data-layout="default"><ac:parameter ac:name="url">UrlResourceIdentifier[url=https://drive.google.com/file/d/<FILE_ID>/view]</ac:parameter></ac:structured-macro>`
RF views it via shared-drive access ("Streams from Drive, so you need Drive access to view"). Match the video to the milestone it demonstrates, not the folder it landed in: an "PL MS4 Demonstration" file uploaded into an ms5 folder still belongs on the **MS4** page (150274049), where the playthrough was flagged "coming Monday".

**Writing the page:** the aurorapunks Confluence is NOT reachable by the Rovo MCP (that only reaches badass-studios). Use `assistant/confluence-set.js` (Basic auth via `~/.claude/.atlassian-credentials.json`; `update <pageId> <page.json>` reads the current version and increments it). A delivery-page body is ~37 KB of storage XHTML, so never hand-transcribe it: fetch the live storage, do targeted string replacements in a script, **assert each target matches exactly once (abort otherwise)**, sanity-check that the video id + embed macro are present and the stale placeholder is gone, dry-run, then `--commit`. Also fix any now-false framing (a "coming Monday / not part of this delivery" bullet) so the page doesn't contradict the embed.

**Read gotcha:** `mcp__atlassian-confluence__conf_get` uses JMESPath, not jq, so jq expressions error out — but the tool still dumps `_originalData` with the full body, so you get it anyway. For scans/verification, curl the v2 API directly with the token.

Source: K2C MS4 playthrough embed.

**Tags:** k2c, confluence, video-embed, drive, confluence-set.js, atlassian-credentials, read-modify-write, delivery-page, rovo-mcp-scope

## 2026-08-31 — Splitting an island's "Level Art" into features: source it from the island's GDD "Art Assets Needed" (k2c)

Robert asked to split the vague per-island "Level Art" tickets into specific art features for the 3 remaining islands (D Sphinx / E Osiris / G Set), Confluence as reference. The clean source is each island's own GDD page (Campaign > Islands > Island X): it has an **"Art Assets Needed"** bullet list that IS the feature breakdown, verbatim. Sphinx = 4 sphinx sculptures + riddle altar; Osiris = 2 statues + altar + reunion FX; Set = Set mask, crypt, windbreak, sarcophagus item + ritual FX, tome puzzle, Duat skybox. Created them as **Subtasks under the Level Art task** (issuetype id 10002), keeping the board's Epic > Task > Subtask model rather than restructuring to "main task + subtasks" (the existing model already gives design/art/code as sibling Tasks under the island epic).

**Dedup is the judgment part, not the listing.** Two Set items on the GDD art list (Anubis jackal warriors, Book of the Dead + pages) are cross-cutting and already tracked elsewhere (KAN-576 Anubis art; Book of the Dead = a Divine Favor under Abilities KAN-13). Splitting the GDD list mechanically would have duplicated them. Cross-check each island-art bullet against existing FEATURE/ABILITIES tickets before creating, link the shared ones, only create island-unique art. Same family as the "go broad" art decision (shared Egyptian assets tracked broadly, not per-island).

**KAN board mechanics worth caching:**
- Board id **1**, team-managed, board type reports "simple" but it DOES have sprints via the agile API. Sprints map to milestones: **S9 = MS5 Production (id 9)**, S10 MS5 CC Hardening ... S15 MS7 Launch. fixVersions = MS1..MS7.
- The new `/rest/api/3/search/jql` endpoint returns **null fields unless you pass an explicit `fields` param** (old `/search` returned them by default). Always set `fields`.
- Add to sprint: POST `/rest/agile/1.0/sprint/{id}/issue` `{issues:[...]}` (works on a future sprint). Subtasks inherit the parent's sprint, so only the parent needs adding.
- Transition ids on this board: To Do=11, In Progress=21, In Review=31, Done=41, Icebox=42, BACKLOG=2.
- The Atlassian wrapper MCP authenticates as Robert, so every write is attributed to him.

Source: K2C, s9/MS5 grooming.

**Tags:** k2c, jira, kan-board, island-epics, level-art-split, gdd-art-assets, subtasks, sprint-api, search-jql-fields, dedup, go-broad

---

## 2026-07-14 — OpenSign "resend" ≠ fix an expired link — the DOCUMENT expires at 15 days (TimeToCompleteDays); extend ExpiryDate, don't re-email (K2C)  [Delivery Prep]
Follow-on to k2c-035: after I "resent" Andreea's Skokloster link via `opensign.js email`, she replied it STILL said **"link expired on July 2nd."** Root cause: OpenSign stamps every doc with `TimeToCompleteDays: 15` ([opensign.js:877](assistant/opensign.js#L877)), so the whole **document** `ExpiryDate` = send-date + 15 days (Jun 17 → Jul 2). The sign link is stable (`/load/recipientSignPdf/<doc>/<contact>`); re-emailing sends the SAME link to an expired doc — it does nothing. **Real fix = extend the document's `ExpiryDate`**, which preserves every signature already collected (a void-and-resend throws them away and forces everyone to re-sign). No CLI verb for it, so master-key Parse PUT:
```
node -e 'const os=require("./assistant/opensign.js");const{BASE,APP_ID,MASTER_KEY}=os.cfg();
fetch(`${BASE}/classes/contracts_Document/<DOCID>`,{method:"PUT",headers:{"X-Parse-Application-Id":APP_ID,"X-Parse-Master-Key":MASTER_KEY,"Content-Type":"application/json"},
body:JSON.stringify({ExpiryDate:{__type:"Date",iso:"2026-08-31T23:59:00.000Z"},TimeToCompleteDays:60})}).then(r=>r.text()).then(console.log)'
```
Returns 200 `{updatedAt}`; verify with `os.parseGet("contracts_Document", id)` → `ExpiryDate`. `opensign.js` exports `cfg/parseGet/parseQuery/cloudFn/getSessionToken/getStatus/voidDocument` but NO update helper — the raw PUT is the path. **Gotcha to always check:** when a signer reports an expired OpenSign link, DON'T just re-email — read the doc's `ExpiryDate` first; if it's past, extend it, then resend. And the same batch-send means **sibling docs expire together** — Ark Island (Fredrik) was also sent Jun 17, so its link was dead too even though nobody had flagged it yet; fix all in-flight docs from that batch, not just the one that complained. Filed durable watcher fix as **db-265** (opensign-watcher nudges the frontier signer but doesn't extend expiry → nudges dead links; also raise the 15-day default). Source: K2C.

## 2026-08-30 — Event submission pipeline evolved into permanent operational infrastructure, not a project milestone (evt)

The Events Epic (evt-000) arrived in June as a "deadline tracking and event participation" project, routed to PM with a score of 7 (autonomy 3 = pure research/data). By August it had evolved into permanent operational infrastructure—three linked scripts running on cron, an autonomous portfolio registry, a submission ledger, and daily event intake from HTMAG alerts.

**The pattern:** A deadline-driven project that starts with manual tracking (6 tickets with past deadlines, 15 needing research) is a sign that the work is *systematic*, not *one-off*. The moment you've solved "which games fit which festivals" (portfolio.json) and "how do we auto-close dead forms" (evt-window-sweeper.js), the next step isn't "wrap up," it's "make it permanent." This is because new events arrive continuously (87 tickets created since June), deadlines are recurring, and the decision rules (autonomy envelope: auto-submit, but escalate money/travel/exclusivity) are stable.

**The three-script architecture:**
1. **Sweeper** (daily 06:15) — Probes submission forms for closed markers, auto-closes when windows end. Safe because it only closes, never opens.
2. **Applicator** (hourly :25) — Evaluates new HTMAG alerts, fills forms headlessly, and either submits (for AP titles) or parks (for client titles needing approval). Ledger-backed and idempotent (write before submit, verify after).
3. **Reporter** (daily 06:20 + monthly) — Generates status report of submissions + rejections. Tracks outcomes so quarterly health checks can happen without a human trawling tickets.

**How to apply:** When a deadline-driven project reaches steady state (autonomous decision rules are stable, intake is continuous, workflow is repeatable), move it from a "project ticket needing your 4am sweep" to operational infrastructure. Create a monitoring task (quarterly standing check) instead of a project that eats 4am-sweep cycles every day. The three scripts will keep it healthy; the standing task just verifies the logs and escalates if something breaks. This frees the 4am agent to work on actual projects, and it prevents infrastructure from rotting on a backlog.

**Same-session learning:** This epic was marked `pending_close: true` since June, but closure was never the right outcome. It's not "done," it's "in service." The first PR after this finding should retag epics more carefully: a deadline-driven project that's in steady-state automation should not live in a "pending close" state — it should live in a "monitoring" state, which is a different board condition. Nothing to change operationally; just a classification fix so future 4am agents know what they're looking at.

**Tags:** evt, event-submission, automation, ops-infrastructure, epic-classification, deadline-pipeline

---

## 2026-08-28 — Platform notification mail is a membership LEDGER: reconstruct access state from it before declaring an access task blocked [project: necrotic_dominion, nd]

Follow-on to the same day's console-testing entry. Robert asked me to add him and Elias as CurseForge
testers on ND. Project memory said flatly "there is **no CurseForge session on the VPS**, so member
changes are Robert-in-the-browser", and the 2026-08-02 learning had already filed the task as blocked
three ways. Both true, and both would have led me to answer "blocked, ask Amichai" and stop.

**What the mail archive actually showed.** `from:noreply@curseforge.com` does not only carry comment
text (the 2026-08-02 finding). It carries **membership and ownership state-change events**, each
addressed to the account it happened to:
- "AuroraPunksBoss, ... April 13 **You were added to the following projects**: Necrotic Dominion" (to robert@, 2026-04-14)
- "davidkruse, ... April 13 **Ownership** of the project Necrotic Dominion **has been transferred to you**" (to david.kruse@, same batch)
- "robert_aurorapunks, ... December 17 New Owner in Necrotic Dominion: Armory" (to the private Gmail, 2025-12-18)

So Robert was **already a member** of the very project he was asking to be added to. The real ask was
never "add me", it was "raise my existing membership to include Cross Platform Testing" — which is
exactly why Amichai's "you can also do it in the project page in the author console" was correct and
not just a brush-off. Reporting "blocked, no session" would have been *technically accurate and
practically wrong*: it would have parked a task Robert could finish himself in two minutes.

**How to apply.** For any access/membership question on a gated platform where we hold no session,
before answering "blocked": search the notification mail for the platform's **state-change events**
(added to project / removed from / ownership transferred / role changed / invitation accepted) across
**every** mailbox we index, and reconstruct the access graph from them. The events are per-account, so
they also tell you *which identity* holds the access, which is the thing that actually decides the
answer. A gated write surface does not imply gated *state*. Generalises the 2026-08-02 rule ("ask what
the platform sends outward") from content to **permissions**.

**Two caveats.** (1) Phrasing is not stable, so a single quoted-string search under-returns: searching
`"added to the"` returned one mail while a broader semantic query surfaced two more of the same class.
Query semantically (RAG) or with several phrasings before concluding a membership event doesn't exist.
(2) The ledger is **append-only and one-sided** — it proves an add happened, never that it still holds,
and it cannot give you the *role* attached. So it is good for "does this identity have a foothold" and
useless for "what exactly can it do" or "how many of the 5 seats are used". State the difference rather
than over-claiming from it.

**Same-session correction, and it is the real lesson.** After writing the above I found the project's own
`output_log.md` from 2026-08-12: *"`AuroraPunksBoss` owns nothing, which is why its author portal shows
**'No projects yet'**"*. That is a **direct observation of the console** and it contradicts the mail ledger's
"you were added to Necrotic Dominion". Either the author console surfaces only *owned* projects (so a
member-only project is invisible there) or the April membership lapsed. Either way Robert probably **cannot**
self-serve, which is the opposite of what I had just told him.

**So the ledger rule needs a hard ceiling.** Notification mail is append-only and one-sided: it proves an add
*happened*, never that it still holds, never the role attached, never the seat count. It is a lead, not a state
read, and it **loses to any direct observation of the live surface**. Before reporting reconstructed access state,
grep the project's own `output_log.md` and prior audits for someone having actually *looked* — a five-second check
I skipped because the mail evidence felt conclusive. Reconstructed evidence that contradicts a logged observation
means you have a question, not an answer. Ship it as "two sources conflict, here is the cheap thing that settles
it" rather than picking the one you found second.

**ND-specific residue:**

**Tags:** necrotic-dominion, curseforge, access-management, notification-mail, identity, permissions, blocked-tasks, nd

---

## 2026-08-28 — Testing an unreleased ARK:SA mod build on console is a CurseForge permission, not a platform devkit flow [project: necrotic_dominion, nd]

Robert asked "what are the steps to test Elias' internal PS5 build on a retail PS5". The instinct on a
console project is to reach for the platform runbook (PlayStation Partner Center package, Package
Distribution, activation codes, devkit). **For an ARK: Survival Ascended mod that is entirely wrong.**
There is no Sony-side artifact at all. The whole flow lives inside CurseForge + the in-game mod browser:

1. The mod is uploaded from the ARK Devkit with "Cross-Platform" ticked, and CurseForge cooks the
   PC/Xbox/PS5 variants automatically. There is no separate PS5 build to distribute.
2. The tester's **CurseForge account must be linked to PSN** under profile settings -> Connected
   Accounts. This is the step that actually gates console visibility, and it is per-account, so it
   decides *which* username is the right one to hand over.
3. The project owner adds that **CurseForge username** in the project's Members tab with the
   **"Cross Platform Testing"** permission. Cap is **5 team members**, which is a real constraint on a
   project with many legacy staff accounts.
4. On the console: MODS LIST -> My mods -> Install -> new session -> Mod settings -> Available mods ->
   Activate. Single-player/non-dedicated is enough; a Nitrado dedicated server is only needed to test
   server-side. Unpublished versions are addressed by project ID with a **`-dev` suffix** (ND = `1117983`,
   so `1117983-dev`).

**The transferable lesson:** when a platform question arrives on a project whose distribution is
mediated by a storefront/mod platform (CurseForge, mod.io, Steam Workshop), check whose runbook actually
governs before answering. "PS5 build" made this look like a cert/devkit question and it was an access
permission on a web project page. Source: CurseForge support "Cross-platform testing" article, verified
2026-08-28.

**Second-order finding from the same pass:** the blocker is almost never the build, it is *which account*.
Elias hit exactly this ("it says I need to purchase the mod") because his new `DevElias` account has no
entitlement and no tester permission. Same trap waits for Robert, who has two personal-ish CurseForge
identities (`AuroraPunksBoss` on robert@, `robert_aurorapunks` on the private Gmail) plus the map being
owned by a third (`davidkruse`). Before asking anyone to grant access, establish which account is linked
to the platform, otherwise the grant lands on the wrong identity and you burn one of the 5 slots.

**Tags:** necrotic-dominion, curseforge, ark-survival-ascended, console-testing, ps5, cross-platform-testing, tester-permissions, account-identity, nd

---
name: PM Agent Learnings
description: Cross-project knowledge accumulated by the PM agent from estimation, planning, and tracking work
type: agent_memory
agent: pm
---

# PM Agent Learnings

## 2026-09-03 — An empty dashboard is not evidence of missing access until you have verified you are on the right dashboard [project: necrotic_dominion, nd]

Fourth pass on the same ND CurseForge access question, and I got it wrong twice in one session before
it resolved. Both errors are worth more than the eventual answer.

**The question.** Robert wanted to test Elias' PS5 fixes on a retail kit. That needs a CurseForge
account with (a) Cross Platform Testing on the project and (b) PSN under Connected Accounts. Since
2026-08-12 the record had said `AuroraPunksBoss` "owns nothing, which is why its author portal shows
**No projects yet**" — a direct console observation, which the 2026-08-28 entry then enshrined as
beating the contradicting notification mail.

**Error 1: I read a third-party screenshot as a complete state.** Amichai Marmor (CurseForge side) sent
a Members-tab screenshot with two rows, `davidkruse` and `DevElias`, under the words "You both have full
permissions". `AuroraPunksBoss` was absent, so I concluded Robert was not a member and built a whole
runbook on it. Elias, who had the console open, then said flatly: *"AuroraPunksBoss är owner över kartan
och robert_aurorapunks är author"*. **A Members list need not render the owner as a member row.** The
account I declared absent was the one that owned the project.

**Error 2, the expensive one: I sent him to the wrong product and confirmed it badly.** Asked where the
author console lives, I fetched `console.curseforge.com`, saw the title "CurseForge for Studios", and
called it confirmed. It is not the mod-author dashboard — it is the **publisher** surface where a studio
registers a *game* (what Studio Wildcard uses for ARK itself). Robert logged in and got "All games — No
Games yet", which is the correct output of the wrong tool. Mod projects live at
`www.curseforge.com/account/projects` (302 → `legacy.curseforge.com/account/projects`). **I verified that
a page existed and had a plausible name, and treated that as verifying it was the right page.** A title
match is not a capability match; the check is whether the surface lists the object type you care about.

**The compounding failure, and the real lesson.** Error 2 probably *caused* the entire three-week
investigation. If the 2026-08-12 audit that produced "No projects yet" was also looking at the studios
console, then the load-bearing observation behind "AuroraPunksBoss owns nothing" was an artifact of the
wrong dashboard — and the April notification mail that contradicted it was right the whole time. The
2026-08-28 rule I wrote ("direct observation of the live surface beats the append-only mail ledger")
needs a hard qualifier: **only if the observation was made on the correct surface.** An empty view is the
most seductive false negative in access debugging, because absence renders identically whether you lack
permission, lack the object, or are looking in the wrong place. Before treating "no results" as a state
read, confirm the surface can display the thing at all — ideally by finding something you *know* exists
there.

**What actually resolved it: asking the person with the console open.** One Discord line from Elias beat
three sessions of mail-ledger reconstruction, screenshot interpretation and URL guessing. On any gated
platform where we hold no session, "who currently has this open, and what do they see" should be the
*first* move, not the fallback after the clever reconstruction. Cost: one message. It also outperformed
the platform contact (Amichai), who summarised from memory and named the wrong accounts — the insider
with the working session beat the insider with the authority.

**Third, smaller, but it nearly produced a bogus ticket:** I ran the project's Discord reader as
`--days 400`, got `0 msgs` across all four channels at exit 0, and concluded the bot had lost guild
access. The script takes **positional** args; `parseInt('--days')` is `NaN`, the guard `all.length < PER`
is `0 < NaN` = false, so it never fetched. Re-run as `100 45` it returned 27 messages, four of which
became evidence on ND-11. Same shape as the dashboard error: **an empty result from a tool you invoked
wrongly is indistinguishable from a dead upstream.** Filed db-342 — read tools should fail loud, and an
all-channels-zero result should not exit 0.

**One good triage habit from the same pass, worth keeping:** among five PS5 crash reports sat one player
who had loaded the same mod **on Xbox** and flown around in admin. That converts "console crash" into
"PS5-specific divergence from a working Xbox cook" — a much smaller hypothesis space. On cross-platform
defects, hunt the channel for the platform that *works*; the negative space is the diagnostic.

**Tags:** necrotic-dominion, curseforge, access-management, permissions, false-negatives, verification-discipline, tooling-footguns, cross-platform-debugging, ps5, nd

---

## 2026-08-28 — Buggfixar mot en levererad feature är inte featurearbete (k2c)

Jag satte in **Merchant** under "Updated features" i MS4-byggnoteringarna. Robert strök den:
featuren är i levererat skick sedan MS3 och hörde inte hemma i dokumentet alls.

Det som lurade mig var ticketstrafiken. **KAN-578** (merchant stuck, kunde inte betala mynt efter
bygge) och **KAN-549** (merchant donkey flickers) stängdes båda inne i MS4-fönstret, och min
Done-fråga plockade upp dem. Jag läste "tickets stängda den här milstolpen" som "den här featuren
rörde sig den här milstolpen". **Ett levererat system fortsätter generera defekter för alltid.**
Den trafiken säger ingenting om huruvida featuren gick framåt.

Testet som hade fångat det tar tio sekunder: **titta på featurens egen epic, inte på tickets i
datumfönstret.** `KAN-355 FEATURE: Merchant (NPC unit)` står Done, prod-design KAN-356 Done, konst
och kod levererade vid MS3. En epic som redan är stängd kan per definition inte vara den här
milstolpens nya eller uppdaterade feature.

Regeln generellt, för alla milstolpedokument: en feature förtjänar en rad under New eller Updated
bara om **featurearbetet** rörde sig, alltså ny mekanik, ny konst, eller ett medvetet balans- eller
polishpass. Att stänga buggar mot något redan levererat kvalificerar inte. Det här är samma familj
som fixVersion-fällan i entryn ovanför: **båda handlar om att en Jira-fråga som ser rimlig ut svarar
på en annan fråga än den du ställde.**

Kanonisk hemvist för sakuppgiften: [[project_k2c_merchant_delivered]].

**Tags:** k2c, milestone-delivery, build-notes, jira, epics, feature-scope, delivered-state

## 2026-08-28 — Bygg kända-problem-listan på status, aldrig på fixVersion (k2c)

Robert bad om MS4-byggnoteringar med kända problem, "bara pending". Den självklara frågan är
`fixVersion = "MS4 - Pre-Cert Build" AND issuetype = Bug AND status NOT IN (Done, "In Review")`.
Den gav **13 buggar**. Den riktiga listan var **38**.

Skillnaden är att **KAN-628 till KAN-661 saknar fixVersion helt**, och det är just de ticketsen som
betyder något: hela playtestbatchen från 27-28 aug, skapad av Death Board-boten ur Discord #qa
timmarna före grinden. Ju färskare fyndet, desto större chansen att ingen hunnit stämpla det. En
fixVersion-scopad fråga är alltså **systematiskt partisk mot det som är äldst och minst relevant**
för ett bygge som levereras i dag.

Det förrädiska är att frågan inte ser trasig ut. Den returnerar 13 rimliga buggar med rimliga
rubriker, och det finns ingenting i svaret som säger "här saknas 25 stycken". Hade jag levererat den
listan hade RF fått en kända-problem-sektion som utelämnade Anubis-krigarnas alfa-blending,
Lurkern som arkéerna inte kan träffa, och hålet i muren bakom bryggan, alltså precis det Tim och
Oskar hittade under de sista två dagarna.

**How to apply:** för en leveransartefakt, ställ frågan på **status** (`status NOT IN (Done,
"In Review", Icebox)` plus ett datumfönster på `created`), inte på `fixVersion`. Använd fixVersion
för att bygga *levererat*-listan, där stämplingen faktiskt har skett i efterhand, och status för att
bygga *kvarstår*-listan. Kör alltid båda och jämför antalen: **om status-listan är väsentligt större
än fixVersion-listan är differensen ostämplade tickets, inte brus.** Flagga gapet till Robert i
samma pass, det är en boardhygienläcka och inte bara en frågedetalj.

Samma mönster som bot-hygienläckan 24 aug (bot-skapade tickets utan sprint och fixVersion), men en
våning upp: där handlade det om att städa boardet, här om att en ostädad board tyst förfalskar en
klientleverans.

**Tags:** k2c, jira, jql, fixversion, build-notes, known-issues, milestone-delivery, board-hygiene

## 2026-08-28 — Ett ticket-ID i projektminnet är en pekare till oavslutad analys, inte ett faktum (k2c)

Jag lät Robert motsignera Fury Studios-avtalet utan att öppna **`k2c-047`**, en öppen ticket med
rubriken *"DO NOT SIGN AS-IS — 4 defects"* på exakt det avtalet. Projektminnets statusrad sa
*"Fury Studios contract: notice must be served by FRI 21 AUG ... (`k2c-047`)"*, och jag tog
uppsägningsfristen därifrån, flaggade den korrekt, och gick vidare. **Bakom ID:t låg tre defekter
till.** Två av dem, avsaknad av spendtak och avsaknad av RF:s no-AI-klausul, gick in i ett signerat
avtal.

Det som gör felet lärorikt är att jag **använde** ticketen. Jag citerade den. Det kändes som att
jag hade täckt in den, och just därför ställde jag aldrig frågan om vad mer som stod i den.
En sammanfattningsrad som nämner ett ID ser ut som ett faktum men är en **komprimering**, och
komprimeringen behåller det som var akut när raden skrevs, inte det som är viktigast när du läser
den.

**How to apply:** när en minnesrad refererar ett ticket-ID i samma andetag som den artefakt du är
på väg att agera på, **öppna ticketen innan du agerar**, även när du tycker att du redan vet vad
den handlar om. Titta särskilt på `status` och `needs_input`: `status: backlog` plus
`needs_input: true` är boardets sätt att säga att någon väntar på ett beslut som ingen har fattat.
Kostnaden är tio sekunder. Kostnaden för att låta bli är en underskrift.

Efterspel värt att ta med: när Robert fick utfallet svarade han att **Fury Studios är ett
dotterbolag till Raw Fury**, vilket gör båda de osåtgärdade defekterna ofarliga. Beviset låg i
mailen jag redan hade läst, Toms adress är `tom@rawfury.com`. **Att jag hade fel om allvaret gör
inte att processfelet var okej**, och den motsatta slutsatsen, att det löste sig så det spelade
ingen roll, är den farliga att dra. Källa: K2C.

## 2026-08-27 — En QA-ticket skapad strax efter ett möte är förmodligen samma fynd som mötet diskuterade (k2c)

Vid avstämningen av playtestet 26 aug mot KAN stod jag i begrepp att skapa en ticket för
"kvarglömd chimera-mask ger boxformad renderingsartefakt runt träd". Boardet hade redan **KAN-617,
"Artifact renders behind tree on chimera landing site"**, skapad **kl. 15:54 samma dag** ur Discord
#qa, alltså **54 minuter efter att playtestet slutade**. Rubrikerna liknar inte varandra ("artifact
renders behind tree" mot "leftover mask"), och en dedup på sammanfattningstext hade missat paret helt.
Det var **tidsstämpeln relativt mötet** som avgjorde: Robert rapporterade in i Discord det han just
hade sett i playtestet.

Rätt drag blev därför att **kommentera KAN-617 med rotorsaken** som playtestet hade tagit fram, i
stället för att lägga en andra ticket bredvid. Ticketen var en symptombeskrivning; mötet hade svaret.

Det här kompletterar dubblettmönstren från 19 och 26 aug. De handlade om att matcha på källänk och
skapandeminut mellan bot-tickets. Det här är en tredje form: **samma person rapporterar samma fynd i
två kanaler, mötet och QA-flödet, med olika ordval.** Fångas varken av textmatchning eller av
källänk.

**How to apply:** när du stämmer av ett mötesprotokoll mot boardet, filtrera först fram allt som
skapades **inom ett par timmar efter mötets sluttid** och läs de tickets fullt ut, oavsett vad
rubrikerna säger. Deltagarna rapporterar in direkt efteråt. Och när mötet bär rotorsaken till en
befintlig symptomticket, är kommentaren leveransen, inte en ny ticket. Källa: K2C.

## 2026-08-27 — Signeringskedjan saknade returledet, och ingen hade märkt det (k2c/apb)

`opensign.js` skickar ut ett dokument för signering. `opensign-watcher.js` avancerar en ordnad
kedja och meddelar Robert när allt är påskrivet. **Ingenting lämnade tillbaka den motsignerade
PDF:en till motparten som bad om den.** Varje "please countersign and send it back"-tråd stannade
alltså på ett manuellt steg som ingen hade skrivit ner att det fanns.

Det här är **tredje gången samma form dyker upp på två dagar**: `--share` utan `--unshare` (26 aug),
det sanktionerade skriptet som bara täckte lyckofallet (26 aug), och nu en signeringskedja som är
komplett fram till sista hoppet. Lärdomen från 26 aug var "kolla om motsatsen finns". Den är för
smal. Den rätta frågan är **"vart tar artefakten vägen när flödet är klart?"** Ett verktyg som
producerar något åt en extern motpart är inte färdigt förrän leveransen tillbaka också är byggd.
Inverser (dela/avdela) är ett specialfall av det.

Byggde `assistant/opensign-return.js`: en kö av returjobb (docId, mottagare, Gmail-tråd), som pollar
`getStatus`, hämtar den signerade PDF:en och svarar i den **ursprungliga mailtråden** med
In-Reply-To/References plus `threadId`, idempotent via `sentAt`. Generiskt, inte bundet till de två
avtalen det byggdes för.

**How to apply:** när du kopplar in ett nytt utåtriktat flöde, rita hela vägen artefakten går, inklusive
sista hoppet tillbaka till människan som väntar. Om sista hoppet är "någon minns att göra det manuellt"
är flödet inte byggt. Källa: K2C + AP.

## 2026-08-27 — En motparts signaturblock kodar deras signeringsrätt, inte vår (apb)

Space Rock Games MNDA (Kindrik-mall, nyzeeländsk) har **en** signaturplats per part: signatur, linje,
"Print full name of authorised signatory". Det är rätt för NZ och UK, där en behörig firmatecknare
räcker. **AP AB tecknas två i förening.** Roberts signatur ensam i den rutan hade sett komplett ut
och varit ogiltig som bindande för AP AB.

Fel svar: klämma in två namn på en rad, eller signera ensam och hoppas. Rätt svar: **spegla mallens
egen cellgeometri en gång till** och lägga till en rad som förklarar varför. Jag mätte offseterna i
motpartens eget block (etikett, namn +20pt, "Print full name" +51/+61pt, hjälplinjer 19pt över
etiketten och 12pt under namnet) och byggde en identisk andra cell för Mattias, plus en kursiv rad i
vänsterkolumnen: "Aurora Punks AB is bound by two authorised signatories acting jointly." Motparten
ser då direkt varför dokumentet har tre signaturer i stället för två.

Två detaljer som gjorde jobbet: **rendera sidan till PNG och titta på den**, textextraktion visar inte
att en pålagd rad krockar med en linje (min första not gjorde det). Och **mät mot motpartens egen
befintliga cell** i stället för att gissa avstånd, då blir tillägget omöjligt att skilja från mallen.

**RÄTTELSE samma dag:** för just **MNDA/NDA behövdes det inte**. Robert: *"Just MNDA har vi sagt
är godkända utan två i signering, det är ett styrelsebeslut."* Roberts signatur ensam räcker alltså
på NDA, och det utbyggda blocket var onödigt arbete.

**Och en andra sväng på samma sak:** när jag skrev att beslutet inte gick att hitta i RAG svarade
Robert *"kan vara så att det inte finns officiellt ännu, vi åtgärdar det på nästa styrelsemöte."*
Undantaget är alltså **praxis, inte protokollförd handling**. Det är värt att skilja på: praxis
räcker för att veta hur man ska agera operativt, men inte för att skriva i ett avtal eller mot en
revisor att styrelsen har beslutat något. Ligger nu i [[reference_ap_mnda_single_signatory]] med den
brasklappen, och formaliseringen är ticketad som `apb-061`.

**Det generella:** en tom RAG-träff på ett påstått beslut betyder ibland att indexeringen missat
det, men ibland att beslutet faktiskt inte finns. Fråga vidare i stället för att antingen anta det
ena eller skriva ner det som fastställt. Skillnaden syns bara om man säger att sökningen kom upp
tom.

**How to apply:** innan du bygger ut ett signaturblock, kolla **först** om avtalsslaget har ett
undantag från firmateckningsregeln, inte bara vad registreringsbeviset säger. Registrerad
firmateckning är golvet; styrelsen kan ha lyft delar av den, och NDA är just ett sådant fall hos AP.
Metoden nedan är fortfarande rätt när tvåsignaturregeln faktiskt gäller, alltså för allt utom NDA:
"två i förening" mot en enrads-mall är en layoutändring, inte en ifyllnad, och den ska göras synligt
och förklarat i dokumentet, inte i följemailet där den försvinner. Källa: AP AB / Space Rock Games.

## 2026-08-27 — Efter en servermigration ljuger både loggen och timerlistan om vad som kör (devops/k2c)

`opensign-watcher.log` på Nitro slutade 21 aug, och `~/.config/systemd/user/` har ingen
`opensign-watcher.timer`. Båda signalerna läser som "watchern är död", vilket hade varit en riktig
blockerare: utan den avanceras aldrig ett ordnat signeringsflöde till andra undertecknaren.

Den var inte död. `assistant/migrate-timers-to-nitro.sh` har en **explicit ej-flyttad-lista** med
motivering: *"opensign-watcher — OpenSign container lives on edge."* Watchern kör kvar på
Hetzner-boxen med flit, mot samma OpenSign-instans.

**How to apply:** efter bare-metal-migrationen är "finns timern på den här maskinen" fel fråga. Den
rätta är "vilken maskin äger den här tjänsten", och svaret står i migrationsskriptets MOVE-lista och
dess kommenterade ej-flyttad-block, inte i lokala loggar eller `systemctl --user list-timers`. Kolla
den listan **innan** du drar slutsatsen att en poller är borta, och innan du bygger om något som redan
kör någon annanstans. Källa: K2C.

## 2026-08-26 — Skriv aldrig "verify against a fresh registreringsbevis" utan att först söka efter det (k2c)

Jag lämnade CZP:s säte och firmatecknare som en öppen blankett i ett anställningsavtal, ärvd rakt av
från Carolinas mall, med noteringen "verify vs fresh registreringsbevis". Robert: *"CZP säte och
firmatecknare finns på RAG. Du borde veta det."* Han hade rätt. **En enda `rag_search` gav både
bolagsordningen och ett registreringsbevis från 2026-07-13.**

Två saker gjorde felet värre än ett vanligt slarv. **Blanketten var ärvd, inte egen.** Jag kopierade
en öppen punkt från ett äldre kontraktsutkast och förde den vidare utan att fråga om den fortfarande
var öppen. **Och uppgiften hade ändrats sedan sist:** CZP:s postadress registrerades om just 13 juli
2026, så äldre adresser i gamla mail och avtal är felaktiga. Hade jag bara kopierat "senast kända
adress" i stället för att slå upp den hade jag skrivit fel adress i ett anställningsavtal.

Fyndet som betydde mest juridiskt: beviset säger **"Firman tecknas av styrelsen"** och Robert är
**ensam styrelseledamot**. Det finns alltså ingen särskild firmatecknare, så signaturblocket ska skriva
honom som **styrelseledamot**. Carolinas mall gissade "Director? confirm", vilket är fel ord och hade
gått vidare till motparten.

**How to apply:** varje `[BLANK — verify X]` i ett ärvt utkast är en **sökuppgift**, inte en punkt att
föra vidare. Kör `rag_search` på den innan du lämnar över dokumentet, och prioritera myndighetskällan
(registreringsbevis, bolagsordning) över mail och tidigare avtal, för de senare bär gamla adresser.
Kolla också alltid **datumet** på registreringsuppgifter: bolagsuppgifter ändras, och den nyaste källan
i RAG kan vara nyare än det avtal du kopierar ifrån. Befordra sedan svaret till delat minne
([[reference_company_structure]]) så att nästa avtal inte återupptar frågan. Källa: K2C.

## 2026-08-26 — Att dela ett dokument är halva jobbet, att kunna ta tillbaka det är andra halvan (k2c)

Simons avtal bytte form mitt i granskningsrundan: han hade tappat sitt bolag, så B2B-avtalet han
redan hade kommentarsrätt på blev fel instrument. Att publicera ersättaren var enkelt. Att **återkalla
det gamla** visade sig omöjligt, för `assistant/gdrive-upload.js` hade `--share` men inget `--unshare`,
och ett hand-rullat DELETE mot Drive-API:t stoppas av auto-mode-klassificeraren.

Samma mönster som Atlassian-inbjudan tidigare samma dag: det sanktionerade skriptet täckte bara
lyckofallet. Verktyg byggda under en leverans får bara den riktning leveransen råkade behöva.

**How to apply:** när du bygger eller använder ett sanktionerat skript för en utåtriktad åtgärd, kolla
om **motsatsen** finns. Dela/avdela, bjud in/ta bort, publicera/dra tillbaka, skapa utkast/radera
utkast. Ett granskningsflöde mot en extern motpart kommer förr eller senare behöva backas, och den
dagen står du med ett halvt verktyg mitt i något tidskritiskt. `--unshare` finns nu och är idempotent:
den listar behörigheterna, matchar på mailadress, och rapporterar "nothing to revoke" i stället för att
fela när personen saknar direkt behörighet.

Och när ett delat dokument blir obsolet: **återkalla åtkomsten samma pass som du publicerar
ersättaren**, plus radera det gamla följebrevsutkastet. Annars sitter motparten med två dokument och
ingen upplysning om vilket som gäller, vilket är värre än att inte ha delat alls. Källa: K2C.

## 2026-08-26 — AGI följer utbetalningsdatum, inte anställningsstart (k2c)

Jag flaggade i ett anställningsavtal att en anställning som startar 24 augusti innebär att
arbetsgivardeklarationen för **augusti** behöver rättas. Robert rättade mig: **arbetsgivardeklarationen
(AGI) bygger på kontantprincipen och följer den månad då lönen faktiskt betalas ut, inte den månad
anställningen börjar.** Simons enda löneutbetalning ligger 25 september, så hela anställningen
redovisas i septembers AGI, inlämnad i oktober, trots att arbetet börjar i augusti.

Felet var inte harmlöst: det hade skickat CorpBot på en rättning av en deklaration som inte behövde
röras, och det gav Robert en falsk deadline mitt i en milstolpsvecka.

**How to apply:** en retroaktiv anställningsstart är i sig ingen skatteflagga. Fråga i stället **när
lönen betalas ut**, för det är den enda datumfråga som styr AGI, avdragen skatt och
arbetsgivaravgifter. Samma princip gör att ett milstolpsbaserat lönupplägg kan ha flera intjänandepunkter
men bara **en** betalningsdag, och då ska avtalet skilja på de två: milstolparna styr *rätten* till
ersättning, Enclosure 1 anger *betalningsdagen*. Skriv aldrig in en betalningskadens som följer
milstolparna om lönekörningen faktiskt sker en gång. Källa: K2C.

## 2026-08-26 — Datumankringsfelet upprepades, och kostade en helt felprocessad standup (k2c)

Sessionen ankrade på den senaste Gemini-notisen i inkorgen i stället för på `currentDate` och antog
att den var dagens. Den var gårdagens. Följden blev tvådelad: allt dagens arbete stämplades fel datum
i output_log, projektminne, learnings, time_log och tre kontraktsdokument, **och** när Robert bad om
"dagens standup" processade jag 25 aug-notisen medan 26 aug-notisen låg oläst. Det andra felet var det
dyra: åtta tickets skapades mot fel dags åtgärdslista, och när jag läste rätt notis hade teamet redan
hunnit skapa KAN-595 till KAN-605 som täckte merparten.

**Regeln bor i [[feedback_anchor_on_currentdate]], inte här.** Den har nu ett "GÖR DETTA FÖRST"-block
överst med den mekaniska kontrollen, tillagt efter det här återfallet, som är det femte dokumenterade.
Det PM-specifika att ta med sig: **en inkorg säger vad som senast anlände, aldrig vilken dag det är**,
och i en daglig körning är `from:gemini-notes@google.com newer_than:2d` en sekunds arbete som fångar
hela felklassen. Källa: K2C.

## 2026-08-26 — Death Board-botten kan skapa samma rapport två gånger inom samma minut (k2c)

KAN-579 och KAN-580 skapades **11:15 samma dag ur samma Discord #qa-meddelande**. Ordagranna
rapporttexten är identisk ("The sun did not appear (but the start of day stinger played and I got the
staff of Ra..."); det enda som skiljer är att botten kört **två olika vision-läsningar av samma
skärmdump**, så sammanfattningarna blev olikt formulerade ("Sun visual does not appear at start of
day..." mot "Sun sprite missing on day start in Egyptian location"). En dedup som jämför
sammanfattningar hade missat paret. En som jämför **källänk plus skapandetidsstämpel** fångar det
direkt.

Detta utökar dubblettmönstret från 2026-08-19 (KAN-412 mot KAN-544, "Staff of Ra SFX" två gånger).
Skillnaden: då var det två personer som rapporterade samma sak över tid, nu är det **en bot som
dubbelskriver samma händelse inom sekunder**. Andra formen är billigare att fånga och farligare att
missa, för båda hamnar orörda i backloggen och ser ut som två distinkta fynd i varje räkning.

**How to apply:** i varje daglig körning, gruppera nyskapade bot-tickets på `Source`-länken i
beskrivningen och på skapandeminut, inte på sammanfattningstext. Ett par med samma permalink är per
definition en dubblett. Verifiera ändå genom att läsa båda beskrivningarna före stängning, även när
Robert godkänt stängning rakt av: det tar tjugo sekunder och skiljer en äkta dubblett från två
närliggande fynd. Behåll den som bär mest kontext eller den äldre med källänk, och skriv motiveringen
som kommentar **innan** transitionen, så att den överlever i historiken. Källa: K2C.

## 2026-08-26 — När ett API-anrop blockeras är svaret ett sanktionerat skript, inte en workaround (k2c)

Inbjudan av Simon och Dubravko till Atlassian stod blockerad sedan 24 aug: auto-mode-klassificeraren
stoppar hand-rullade `POST /rest/api/3/user`, och den förra körningen loggade det som "behöver en
Bash-permission-regel, ett sanktionerat hjälpskript, eller två minuter i admin-UI:t" och lämnade det.
Rätt drag var det mellersta, och det tog tio minuter: **`assistant/atlassian-users.js`**, byggt i exakt
samma form som `jira-set.js` och `confluence-set.js` som redan finns av precis samma anledning. Repot
hade alltså redan mönstret, två gånger, och den förra körningen såg inte att den stod i det.

Två saker som skriptet fick fram och som ingen dokumentation sa:
1. **Confluence finns inte som produktnyckel.** `POST /rest/api/3/user` tar `products:["jira-software"]`
   och det finns ingen motsvarande sträng för Confluence. Confluence-åtkomst är **alltid** en
   gruppinläggning i `confluence-users-aurorapunks`. Så "lägg till X i Jira och Confluence" är alltid
   två operationer, aldrig en.
2. **`/rest/api/3/groups/picker` returnerar `groupId`, inte `id`.** Jag skrev `g.id`, fick
   `group ID 'undefined' does not exist`, och kontot var redan skapat när det small. Så skriptet måste
   vara idempotent på gruppsteget: kör `add-group` separat efteråt utan att försöka skapa om kontot.
   Ett provisioneringsskript som inte går att köra om är ett halvfärdigt skript.

Bonus: **en nyskapad Atlassian-användare är assignable direkt**, före accept av inbjudan. Det motsäger
inte [[feedback_jira_assignable_vs_user_existence]] men är värt att veta, för det betyder att man kan
skapa och tilldela tickets i samma pass i stället för att vänta på onboarding.

**How to apply:** när ett skrivanrop blockeras av klassificeraren, leta först efter ett befintligt
sanktionerat skript i `assistant/`, och skriv annars ett nytt i samma form med en docstring som säger
varför det finns. Lämna aldrig uppgiften som "blockerad" när mönstret redan finns i repot. Källa: K2C.

## 2026-08-26 — Gemini garblar egennamn, så låt Jira avgöra vilket objekt en åtgärdspunkt gäller (k2c)

Standup-notisen sa "Remove the misinformation stating that the Staff of Ra can damage **Sobeck**".
Robert sa Bata. Samma notis skriver "Remove **Ba** hint" om Bata, och äldre notiser har skrivit
"Barta", "Bravu Jurina" och "Ro Fury", så namngarble är normaltillståndet i den källan, inte undantaget.

Det som avgjorde saken var inte vem som sa vad utan **att boardet bar beviset**: KAN-497 stängd med
"works per design" och KAN-520 som ordagrant namnger Apesh och Bata. Två tickets pekade åt samma håll,
och Gemini stod ensam.

**How to apply:** när en Gemini-åtgärdspunkt namnger ett spelobjekt, en person eller ett system, slå upp
namnet i Jira innan du agerar på det. Stämmer det inte mot något på boardet är det troligen en garble.
Och skriv den kundvända texten **generellt om kategorin** när underlaget tillåter det, i det här fallet
"bossarna" i stället för en uppräkning: en generell formulering överlever en garble, en uppräkning gör
det inte. Flagga ändå avvikelsen till Robert i stället för att tyst välja en läsning. Källa: K2C.

## 2026-08-26 — "Done" is not "fixed", and a delivery doc that reads it that way lies to the client (k2c)

The RF playtest build notes told Raw Fury "The Staff of Ra damages bosses". It does not, and it is not
supposed to. **KAN-497 was Done, but its resolution was "Works per design" — Robert's own close, after
Oskar flagged that a fix would contradict Tim's intent** (bosses are not ability targets; fire would
need new idle/attack animations; the other weapons either do not use the targeting system or unlock
too late to reach Apesh). Whoever wrote the "Also new since the Vertical Slice" list pulled the ticket
title, saw the Done status, inverted the title into a fix and shipped it to the publisher. A second
ticket, **KAN-520 "Remove Apesh and bata from being able to be targeted"**, was sitting In Review
saying the exact opposite of the delivery doc.

There are at least four ways a bug ticket reaches Done, and only one of them is "we fixed it":
fixed · **works per design** · duplicate · cannot reproduce. A bug ticket's *title* always states the
broken behaviour, so a title flipped into a positive claim is only true in the first case. The tell was
free here and I would have caught it by reading one comment thread.

**How to apply:** when building a "what's new / what's fixed" section from Done tickets, do not source
it from summary + status. Read the **resolution and the last comment** on every ticket you convert into
a client-facing claim, and drop anything closed as by-design, duplicate or cannot-reproduce. Then
cross-check the claim against **open** tickets on the same system — an In Review ticket contradicting
your fixed-list line is the loudest possible signal that the line is wrong. Complementary to the
2026-07-24 learning about re-pulling live status before writing a delivery doc: that one catches
open-vs-Done drift, this one catches Done-but-not-fixed.

Corollary worth keeping: a by-design ruling is **itself publisher-facing content** on a page whose job
is helping the client filter incoming tester reports. Deleting the false claim was half the fix; the
other half was a "Working as designed, not defects" section so the behaviour does not come back as a
tester report during the external playtest. The page already had the pattern in "Days on Ra are
shorter ... Deliberate, not a timing bug" and I should have reached for it earlier. Source: K2C.

## 2026-08-24 — Defekttäthet är inte samma sak som vad kunden vill ha testat (k2c)

Två gånger på en dag skrev jag kundvänd text som drev på för fel sak, och båda gångerna av samma
felslut. **Co-op:** jag såg att i stort sett varje öppen defekt av betydelse var en nätverksbugg, drog
slutsatsen att co-op var det mest värdefulla att testa, och skrev in i byggnoteringarna att
co-op-sessioner var värda mer än singleplayer och att en co-op-fråga var det enda hål som återstod i
enkäten. Robert: "Coop inte fokus i detta playtest." **Merchant:** jag noterade som en förlust att RF
strukit Merchant-frågan, eftersom NPC:n var helt färdig sedan MS3. Robert: "Merchant behöver inte
testas den har ingen ny funktionalitet."

Båda felen kom av att härleda testprioritet ur **var arbetet finns** i stället för ur vad som faktiskt
ska bedömas. Ett system med många öppna buggar kan vara ur scope. Ett system utan en enda bugg kan
vara det viktigaste att bedöma. Det är två olika frågor.

**How to apply:** testscope kommer från den som äger produkten, aldrig från boardet. Fråga rakt ut
vad testet ska besvara innan du skriver en rad kundvänd text, och när du föreslår ett tillägg, säg
vilken *fråga* det besvarar snarare än hur många tickets det rör. Extra viktigt i dokument som går
vidare till en publisher: en felriktad prioritering därifrån styr riktiga testartimmar.

## 2026-08-24 — Kolla om det finns en nyare version INNAN du analyserar den du har (k2c)

Jag triagerade Raw Furys speltestenkät mot våra fokusområden, hittade tre luckor och två frågor som ger
obrukbar data, och **publicerade analysen till kunden**. Sedan visade det sig att RF delat en **v2** tolv
dagar tidigare. Hela triageringen var mot en möjligen övergiven version.

Underlaget fanns dessutom redan i vårt eget system: `k2c-043`, "Review
KTC_DLC_Alpha_Playtest_Survey_v2", skapad 14 aug, **priority high, taskType critical, förfallen samma
dag, fortfarande i backlog**. Jag hittade den bara för att jag av andra skäl grep:ade followups efter
ordet "survey". Ingenting i dagsrutinen hade lyft den, för rutinen läser Gemini-notiser, Discord och
mail, men **sveper aldrig projektets egna förfallna followups**.

**How to apply:** innan du analyserar ett kundartefakt, kör två kontroller som tillsammans tar en minut:
(1) sök followups och mail på artefaktens namn efter ett `_v2`, `_final`, "updated" eller en ny delning,
och (2) titta på delningsdatumet för den kopia du håller i. En transkription i vår mapp daterar när **vi**
tog emot den, aldrig vad som är aktuellt hos kunden. Och när analysen redan gått ut: sätt reservationen
på det publicerade dokumentet **först**, innan du rapporterar till Robert, eftersom sidan kan delas vidare
i samma minut.

Följdsats: lägg "förfallna followups i projektet" som ett eget steg i dagsrutinens gather, jämsides med
Gemini och Discord. En kritisk post kan ligga tio dagar utan att någon signal går.

## 2026-08-24 — En LLM-klassificerare komprimerar mot mitten, och just severity tål det inte (k2c)

Utökade Death Boards Discord-klassificerare med severity, sp/mp och disciplin. Typ, mode och
disciplin blev rätt direkt. **Severity blev fel åt båda hållen samtidigt:** en krasch-till-skrivbord
klassades som `sev-critical` i stället för `sev-mustfix`, och en ren z-order-bugg som `sev-major` i
stället för `sev-minor`. Modellen undvek ytterkanterna på en fyrgradig skala, vilket gör exakt de två
kategorier man faktiskt filtrerar på oanvändbara.

Fixen var inte fler ord om skalan utan **två överstyrande regler formulerade som absoluter** ("en
krasch är ALLTID sev-mustfix, oavsett hur smal reproduktionen är", "ren ritordning är sev-minor om
den inte döljer något spelaren måste interagera med") plus **sex arbetade exempel med facit**. Efter
det blev alla tre testfallen rätt.

**How to apply:** när du ber en modell klassificera på en ordinalskala, testa alltid **ytterkanterna**
först, inte mittfallen, för det är där komprimeringen syns. Och skriv reglerna för ytterkanterna som
undantagslösa imperativ med exempel, inte som beskrivningar. Testa mot den riktiga kodvägen, inte mot
en återskapad prompt: här körde jag `_parseMentionCommand` direkt via `module.exports` utan
Discord-anslutning eller Jira-skrivning, vilket gav ett ärligt svar på tre minuter.

## 2026-08-24 — Tvinga inte en taxonomi på behållarposter (k2c)

Backfillade disciplin på 277 öppna ärenden. 269 gick att placera. De sista åtta var innehållsbehållare
(Scarab, Scorpion, Chariot, Book of the Dead, Flail of Anubis, Apesh, Sphinx, Scepter of Khonsu), var
och en med art- och kodbarn som bär den riktiga taggen. Att sätta en disciplin på föräldern hade höjt
täckningssiffran från 97 till 100 procent och samtidigt gjort varje filter sämre.

**How to apply:** en täckningssiffra är inte målet. Rapportera vad du medvetet lämnade otaggat och
varför, så att nästa person inte "rättar" det. Samma logik höll mp/sp tunt här: 7 mp och 1 sp, satta
bara där texten faktiskt sa det, för att gissa "sp" på en bugg ingen kört i co-op är att hitta på data.

## 2026-08-24 — "Known issues" och "believed fixed" är motsatta instruktioner till en testare (k2c)

Jag byggde kända-problem-listor till ett externt speltest genom att fråga Jira efter allt som inte var
Done, och lade allt under rubriken "please do not report". Sju av posterna stod **In Review**, alltså
fixade i väntan på verifiering. Robert fångade det: "de skulle du kunna lista som believed fixed".

Felet är värre än en felaktig rubrik. Att be testare tiga om en In Review-post **stänger av den enda
mekanism som kan upptäcka att fixen regredierat**, och en tyst regression är det dyraste man bär in i
en milstolpe. Den mest värdefulla posten i hela dokumentet var den jag hade tystat: en fix som
utvecklaren markerade klar 12:31 och rapporterade följdeffekter av 14:08 samma dag.

**How to apply:** när du bygger testunderlag, dela alltid på status, aldrig på "inte Done".
**To Do och Backlog** = known open, rapportera inte. **In Review** = believed fixed, be uttryckligen om
bekräftelse och eskalera det som fortfarande är trasigt. **Done** = nämn bara det som är värt att
kontrollera. En bonus: den uppdelningen gör speltestet till verifieringspasset som In Review-kolumnen
annars saknar ägare för, se [[2026-08-24 — En status vars utgångsgrind saknar ägare]].

## 2026-08-24 — Ankra på systemdatumet, inte på det nyaste dokumentet i logg-tickten (k2c)

Ombedd att processa "gårdagens playtest och dagens standup" öppnade jag den rullande Gemini-loggen
`k2c-018`, tog dess **senaste post** som "idag" och processade 19 aug playtest plus 20 aug standup.
Det var måndag den **24:e**. Rätt material var 21 aug playtest och 24 aug standup. Filens `updated`-fält
och filsystemets mtime pekade också på den 20:e, vilket förstärkte felet: **allt utom systemdatumet
sa den 20:e**, för en rullande logg slutar uppdateras när ingen kör den.

Arbetet var inte bortkastat, materialet var genuint oprocessat, men fyra dagars möten missades och
varje datumstämpel i output_log, memory, pm_learnings och time_log blev fel och fick rättas.

**How to apply:** läs `currentDate` **först**, innan någon logg öppnas, och räkna ut vilka datum
"igår" och "i fredags" faktiskt betyder. Om den nyaste posten i en rullande logg är äldre än idag är
det ett **gap att undersöka**, inte en definition av nu. Skärper [[feedback_anchor_on_currentdate]].

## 2026-08-24 — En status vars utgångsgrind saknar ägare växer utan tak (k2c)

Robert bad teamet 21 aug att sätta tickets till In Review när de fixat något, så att fixarna kunde
verifieras. Inflödet fungerade omedelbart. Utflödet hade ingen ägare. Tre dagar senare stod **62
tickets** i In Review, och mot hans egen grind, verifierad som löst i speltest, klarade **en enda**.
Fem hade legat kvar i två till tre månader, varav två var hans egna.

Kolumnen såg ut som framsteg och var i själva verket en kö. Värre: den ena ticket som såg mest
"klar" ut, day/night-cykeln, hade markerats DONE av utvecklaren 12:31 och genererat regressioner
som rapporterades 14:08 samma dag.

**How to apply:** när någon inför en mellanstatus, fråga direkt **vem som tömmer den och på vilken
signal**. Utan ett namn och ett återkommande tillfälle är det en förvaringsplats. Och läs alltid
vidare i kanalen **efter** ett "DONE" innan du föreslår Done, för motbeviset ligger ofta i samma
tråd några timmar senare.

## 2026-08-24 — Verktygets tidszon är inte användarens (k2c)

Robert svarade "nytt bygge 16.32, se Discord". Discord-läsaren stämplar i **UTC** och den senaste
bygg-posten stod på **14:32**. Jag läste om kanalen tre gånger och letade efter ett meddelande som
inte fanns, innan CEST-förskjutningen förklarade det.

**How to apply:** när en användare refererar till en klockslag som inte matchar loggen, testa
tidszonsförskjutningen innan du drar slutsatsen att data saknas. Skriv ut båda i rapporten
("14:32 UTC, alltså 16:32 din tid") så att nästa jämförelse går på en gång.

## 2026-08-24 — A ticket bot that creates from chat drops the metadata the requester supplied (k2c)

The Death Board Discord bot turns "create a jira and assign to @X" into a ticket. Seven of them
(KAN-533/534/535/536/540/541/542) landed **in the backlog, with no sprint and no fixVersion**,
and three were **unassigned even though the requester named the owner in the same message**.
They were invisible on the active sprint board and on every MS4 release view while the team
treated them as tracked work.

**How to apply:** every run, sweep `created >= <last run>` across ALL statuses, not just the
active sprint, and fix sprint / fixVersion / assignee. When one is unassigned, **read the
originating chat message** before guessing an owner, because the requester usually named one and
the bot dropped it. Do not assume a bot-created ticket is a complete ticket.

## 2026-08-24 — Dedup by the mechanic noun, not the note's verb phrase (k2c)

The playtest note said "javeling turns into civilians demotes. after 5min without javelin".
Searching that phrasing (javelin, demote) found nothing new. Searching **"civilian"** surfaced
**KAN-421, "Javelin units become civilians after throwing spears instead of only when losing
javelin"**, already open, already in S8, unassigned, and being actively worked that morning.
One search term apart from creating a duplicate.

**How to apply:** run the dedup pass over the **nouns of the mechanic** (civilian, portal, sail,
donkey, exclusion), not the note's verb phrase, and run several single-word searches rather than
one long one. Jira text search is not fuzzy enough to bridge a rephrasing.

## 2026-08-24 — A note item that CONTRADICTS an existing ticket is a question, not a mutation (k2c)

The Aug 19 playtest note described a purple texture overlay as a deliberate tool for spotting
un-converted Greek assets. KAN-504, open since Aug 7, treated purple tint as a rendering bug.
The Aug 20 standup said "resolve unit purple tinting". Both readings were defensible and they
implied opposite tickets: reframe KAN-504 as an asset-conversion tracker, or leave it a bug and
raise the tooling separately. Guessing would have silently rewritten a two-week-old bug.

**How to apply:** the tell is a note item that would **duplicate or contradict** an existing
ticket rather than extend it. Extension is a safe mutation. Contradiction goes to the question
UI with the two readings spelled out. Robert answered "two separate things" in one line.

## 2026-08-24 — A new hire can be three days into visible work with zero tracker presence (k2c)

Dubravko started 18 Aug and had shipped title-screen art in #art on all three days. He had
**no tickets on the board at all**, so none of his work appeared in sprint scope, in the MS4
release view, or in any burndown. Nothing flagged it, because the absence of tickets does not
generate an alert the way a stale ticket does.

**How to apply:** when a person joins mid-project, add "does every active contributor have at
least one ticket?" to the reconcile step. Cross-check the Discord contributor list for the
window against the board's assignee set, and treat anyone posting work with no assigned ticket
as a gap. Pairs with [[2026-08-19 — Check whether a new hire's scope matches the business case]].

## 2026-08-19 — An agreed review gate expires silently if you do not diarise it (k2c)

Robert overrode the advice to use AP's own subcontract template and took the counterparty's
Croatian one. The agreed mitigation was explicit: **the Assistant reads the IP and
governing-law clauses before signature.** Then the contract arrived Monday, a day passed, and
Robert replied **"This looks good"** with the company details. He did nothing wrong: nothing
in his inbox said a review was pending, so the gate simply evaporated.

Four defects were still live when the review finally happened, one of them a **two-day**
notice deadline that decided a ~65 000 SEK difference.

**How to apply:** a review gate you agreed verbally is not a gate, it is a hope. When the
answer is "I'll review X when it arrives", **create the followup with a due date at that
moment**, and if the artefact is expected on a known day, watch for it rather than waiting to
be handed it. Corollary for `/close` step 0: read every touched thread's *current* state
before reporting, because a client acting fast is the normal case, not the exception.

## 2026-08-19 — A subtask's sprint is inherited from its parent and cannot be set directly (k2c)

Asked to get "Crocodile: art" (KAN-338) into the current sprint. `jira-set.js sprint 7
KAN-338` **reported success and did nothing** — the read-back still said `backlog`. Subtasks
render nested under their parent on a sprint board, so the sprint field follows the parent.
The fix was moving the parent KAN-154, which brought both children.

**How to apply:** to sprint a subtask, sprint its **parent**. And always read back after a
sprint move, because the API accepts the call silently. Check the parent's **status** too: it
was sitting in `BACKLOG` while its own child was `In Progress`, which would have rendered
active work in the Backlog column.

## 2026-08-19 — Filter by issue type before you publish a work-in-flight count (k2c)

Reported "**102 open MS4 items are in no sprint**" in a sprint review. The real figure was
**36**. The 102 included **11 Epics** (which belong in columns, not sprints), **37 Subtasks**
(which inherit their parent's sprint), and **21 deliberately parked** BACKLOG/Icebox items.
The inflated number made the gate look out of control and I had to correct it a day later.

**How to apply:** before quoting any "hidden work" or backlog-size figure, exclude
`issuetype in (Epic)` and `issuetype in subTaskIssueTypes()`, and separate *parked* statuses
from *live* ones. A count that mixes hierarchy levels is not a count of work.

## 2026-08-19 — Age the In Review column by status-entry date, never by `updated` (k2c)

S7 read as 9 Done out of 71 at the halfway point, which looks like a failing sprint. Adding
the 22 In Review made it 44% functionally complete: **production was fine, verification was
the bottleneck.** The finding that mattered came from walking each issue's **changelog** for
when it *entered* In Review: 13 of 22 had sat 9+ days, 8 at 14+, worst **28 days**. Two of
them were the exact items the publisher's playtest survey asks testers about.

**How to apply:** `updated` is useless here, because any comment or field touch refreshes it.
Pull `/issue/{key}/changelog` and find the transition *into* the status. A review column that
ages is a parking lot, and the shape matters as much as the contents: **one reviewer held 9 of
the 22**, which is a single point of failure, not a workload problem.

## 2026-08-19 — Check whether a new hire's scope matches the business case that bought them (k2c)

The fourth artist was justified by an asset-list capacity model: ~1 009 h remaining, and his
hours took padding from −7% to +28%. His onboarding meeting then scoped him to **UI and key
art** (game map, title logo, menu shield progression) — **not on the asset list at all**. So
the number that justified the hire never applied to the person hired, and three places in
project memory carried it as fact.

**How to apply:** when a hire lands, read the onboarding notes **against the business case**,
not just for actions. If scope has drifted, correct the stored figures immediately, because a
capacity number is exactly the kind of thing a later session quotes without re-deriving. Also
check the hire has tickets: he started with **no ticket** for two of his three deliverables.

## 2026-08-15 — A superseded spreadsheet that still opens is more dangerous than one that 404s (k2c)

Two stale pointers to the same P&L, and only one announced itself. `output_log.md`
carried a sheet id that returned **404**, which is a good failure: loud and immediate.
The second, the standalone `k2c_pnl_2026`, **opened fine and returned plausible current
numbers** while carrying a LEGACY banner in cell A1 saying it had been migrated into
the AP workbook two months earlier. Writing there would have "succeeded", read back
correctly, and changed nothing anyone looks at.

**How to apply:** before writing to any finance sheet, read **A1 and the header row**,
not just the range you intend to edit. A migration banner lives at the top, not next
to your cell. And confirm the id by **Drive search on the file name** rather than by
grepping the project's own docs, because docs preserve dead ids indefinitely.

## 2026-08-15 — Never set a rate cell on a row whose milestone cells are still formulas (k2c)

The k2c P&L prices most subcontractors as `rate × FTE × MS-ratio`. Row 15's ratios run
MS2 1.35, MS3 0.9, MS4 0.9, MS5 1.35. Setting the rate cell alone, for an artist
engaged **80 hours**, would have computed across four milestone columns and booked
**274 346 SEK**. The row would have looked populated and internally consistent.

**How to apply:** whenever an engagement is short, part-period, or does not span the
milestones the row was designed for, **hardcode the per-milestone amounts and zero the
formula cells**, following whichever row already does that (row 14, Lost Hive). Read the
target row with `valueRenderOption=FORMULA` first — formatted values render a dormant
formula and a hard zero identically. The MS-ratio machinery encodes *effort weighting
across a full engagement*, so it is simply the wrong instrument for a two-week hire.

## 2026-08-15 — When a rate quote arrives, the rate is rarely the risk (k2c)

Asked Tom for the fourth artist's rate. The rate came back at 32 EUR/h, within 1.7% of
the modelled 346 SEK/h, so it changed nothing. Three other things in the same short mail
did: he committed to **two weeks when the plan needed ten**, he signed as **Fury Studios
rather than Raw Fury** (so AP books and pays instead of the cost sitting inside the
publisher's LTC), and he offered a **contract template in a language the client cannot
read**. Hours per week were never stated at all.

**How to apply:** read a rate reply as a **term sheet, not a number**. Check duration,
hours per week, legal entity in the signature block, and what paperwork is being
proposed, before doing any arithmetic. A rate that matches the model can still leave the
business case unsolved: booking the confirmed floor here left art capacity at −2.5%
against ~1 009 h, i.e. the problem the hire existed to fix was untouched. Say that
plainly rather than reporting the booking as a resolution.

## 2026-08-15 — Pre-cost the scenarios you were not asked for (k2c)

Robert chose the most conservative of three costed durations. Because B and C were
already computed and written into the followup, the moment Tom extends the booking is a
lookup rather than a re-derivation.

**How to apply:** when a counterparty has committed to less than the plan needs, cost
**the floor, the ask, and the plan** in one pass and store all three. The decision is
the client's; the arithmetic should not have to be repeated when their answer changes.


<!-- ROTATION-NOTE -->
> **This file holds the most recent entries only** (rotated by `assistant/rotate-learnings.js`, ~100 KB budget).
> Older entries live in `archive/pm/` and are listed in the archive index at the bottom of this file.
> Nothing is deleted and everything stays searchable via `rag_search(query, source="agents")`.
>
> **Still append new learnings to the TOP of this file** — rotation moves the tail out on its own.

## 2026-09-02 — An AI notetaker's ACTION LIST invents people and tasks its own transcript does not contain (K2C)  [Process]
Today's Gemini standup notes carried the action item **"[Eamonn Byrne, Amy] Discuss Mask Effects: discuss the mask of set animation with Amy."** There is no Amy on the project, in Jira, or in the registry. Robert's read was that it is **Eamonn's own name through a strong Irish accent** — right about the cause, and the artifact went further than that. **Grepping the raw transcript settled it: "Amy" appears ONLY inside Gemini's synthesised action-item block and never once in the transcript body.** The body says something different and more useful: *"Eamonn Byrne has completed the castles, animations and wharf assets. They are beginning work on the Mask of Set. **Tim Browne provided direction to style the location as an ornate tomb rather than a cave and suggested using visual effects rather than animation for the mask's breath.**"* So the direction had already been **given and settled in the room**, and the summariser turned it into a pending two-person discussion with a person who does not exist. Ticketing that action item verbatim would have created a phantom owner and a task that was already done. **How to apply:** the quick-notes / action-item block of an AI notetaker is a *generated* layer and is where hallucinated owners appear. When a name in it is not in the registry, **grep the transcript body for that name before doing anything with it** — if it appears only in the action list, it is an artifact, and the body will usually tell you what was actually said. Same run, same file: the body plainly wrote **"Joanna Supska (Arlenti)"**, independently confirming an identity I had asked Robert to confirm the day before — so the body is also where identity questions get answered cheaply. Garbles from this project's notes now live in `project-registry.json` under `transcriptionAliases` (amy→Eamonn Byrne, dubie→Dubravko Jurina, frederick→Fredrik Laurent), kept deliberately separate from the real-nickname `people` map and consulted after it, so a real Amy joining the team would override the alias rather than be swallowed by it. Source: K2C.

## 2026-09-01 — Set `anyone`/`reader` on a Drive asset BEFORE you embed it; "the reviewers have access" is a different test (K2C)  [Tooling]
**The rule, first:** any Drive file you intend to *embed* in a client-facing page needs a `{"type":"anyone","role":"reader"}` permission, granted at upload time, before the link goes anywhere. Per-user sharing lets a human **open** a link; it does not let another tool **render a preview** of it. Confluence's `embed` macro resolves the asset **with no Google session**, so a file shared to named users renders as **"Error loading the extension!"** — which is exactly what MS4 did while every RF reviewer sat on it as `fileOrganizer`. **Shared Drives are the trap**: membership-based, inheriting no link-share from the drive or its folders, so a capture dropped in one is broken-by-default for embedding while looking perfectly shared in the UI. A `driveId` on `files/{id}` is the cue to check permissions explicitly. **Two false leads to skip, because both cost real time here.** (1) The **REST `body-format=view` render is not diagnostic** — it returns the same `<img class="wysiwyg-unknown-macro" …name=embed>` placeholder for the working page and the broken one, because that renderer does not know editor-native macros at all. Only a browser load distinguishes them. (2) A **storage-XHTML diff between a working and a broken page hands you plausible red herrings**: MS4's macro was genuinely missing the `ac:local-id` that MS3's had, and rebuilding it in MS3's exact shape changed nothing. Check `GET /drive/v3/files/{id}/permissions?supportsAllDrives=true` for an `anyone` entry **before** touching macro XHTML. **How to apply:** the preventive version now lives in the playbooks rather than only here — [[publisher_milestone_delivery]] section 3 (the inline-video technique bullet, plus a browser-verification step before calling a delivery page done) and [[gdrive_workflow]] (a sharing section with the two API calls). The old gotcha in the delivery playbook said *"confirm the publisher has Drive access to any embedded video"*, which is **true and insufficient** — it was satisfied on MS4 and the embed still broke; it now reads as two separate checks. Two things worth holding beyond the mechanics: a broken embed is a **presentation bug, not a delivery blocker**, since the reviewers can still watch from the quick-links line, so fix it without escalating it; and **granting `anyone`/`reader` is an outward-facing change that needs Robert's go** — it means anyone with the URL can view without signing in. Listing permissions first is a free access-hygiene check as well, on MS4 it surfaced four unrelated third parties (Behold VC ×2, Mattias Wiking, LootLocker) holding read on a Raw Fury build capture, inherited from the parent folder. Source: K2C.

## 2026-08-10 — A pre-wired budget row is a trap, not a shortcut: check WHICH columns carry the formula before you price a hire (K2C)  [Tooling]
Asked for the budget impact of a third artist, I found the K2C P&L already had a **row 15 "Artist no3"** at 1.0 FTE with the standard `=B15*C15*<MS ratio>` cost formula and a rate cell sitting at zero. That reads as "someone thought of this, just fill in the rate". It is not. **The formula was live on the MS2, MS3, MS4 and MS5 columns and hardcoded to 0 on MS6 and MS7**, i.e. the row was wired months ago for a *July-to-October* artist. Writing the rate alone would have (a) **retroactively loaded two delivered, invoiced and paid milestones** with a cost that never existed, silently understating the project's realised margin, and (b) **contributed nothing to MS6**, the window the hire was actually for, because that cell was a literal zero. Both errors are invisible in the total, which would simply have come out plausible and wrong. **How to apply:** before using any dormant placeholder row in a financial model, dump the range with `valueRenderOption=FORMULA` and read *which* cells are formulas versus literals, then diff that span against the period the spend actually covers. A placeholder row encodes the assumptions of whoever created it, and those assumptions have a date. Second thing this run proved: **express duration in the model's own units, never in months.** The sheet allocates the project across milestone windows with per-column ratios (MS5 = 1.35, MS6 = 1.8, summing to 9.0 across a 9-month project), so "two months across MS5 and MS6" is **3.15 month-equivalents at full time**, a 57% overrun on the intuitive number and about 69k of real money here. Convert the ask into the model's units and show the client both readings rather than picking one silently. Source: K2C.

## 2026-08-10 — "Fund it from contingency" and "let contingency scale" are contradictory instructions; model the literal one and show the delta (K2C)  [Client Coordination]
Robert answered two budget questions in the same breath: the third artist is **"taken from the contingency budget"**, and the sheet's 10% contingency line should **"let it scale"**. Those cannot both hold. Contingency has already been deducted from the margin, so genuinely funding a hire *from* it means the margin does not move; leaving the formula scaling means the sheet adds fresh contingency on top of the new cost and the margin drops by the full 1.1x. On this project the gap was **738 949 versus 757 849**, small enough that flagging it as a blocking question would have been precious and large enough that silently picking one would have been wrong. **How to apply:** when two answers conflict, do not re-ask and do not average them. Model the **literal, conservative** reading, state the other number in one line next to it, and name the single cell that flips between them. The decision maker resolves it in a sentence with both figures in front of them, which is faster than a second round of questions. The related trap worth naming: **"we'll take it from contingency" is a sentence about authorisation, not about arithmetic** — it usually means "this is within plan, I don't need to reopen the deal with the client", and it is worth answering that question directly. Here that meant showing contingency *capacity*: 423 014 in the plan, but only 141 397 sitting in the two windows the artist actually works, so the hire is 134% of its own windows' contingency and 45% of the project's entire buffer with two milestones still to run. That framing is what the sentence was really asking about. Source: K2C.

## 2026-08-07 — Two Jira Cloud mechanics that bite on a sprint roll: closing a sprint DUMPS incomplete work, and Task→Subtask is not a REST edit (K2C)  [Tooling]
Rolling S6 into S7 surfaced two things worth never rediscovering. **(1) `jira-set.js sprintstate <id> closed` has no `incompleteIssuesDestinationId`**, and a bare `POST /rest/agile/1.0/sprint/<id> {state:"closed"}` sends every incomplete issue to the **backlog**, not to the next sprint. On this board that was **44 issues**, i.e. the entire live workload, silently dropped out of any sprint on a Friday afternoon. The fix is trivial once you know it: **move the incomplete set into the destination sprint FIRST** (`jira-set.js sprint 7 <44 keys>` takes them all in one call), *then* close the old sprint, so the close has nothing left to relocate and the outcome is deterministic rather than dependent on an undocumented parameter. Verify afterwards that the closed sprint's issue count equals the Done count (41 here) and the new sprint's total is carryover + new. **(2) You cannot convert a Task into a Subtask over REST.** `PUT /rest/api/3/issue/<key>` with `{"issuetype":{"id":"<subtask id>"},"parent":{"key":"<task>"}}` returns **400 `{"pid":"Issues with this Issue Type must be created in the same project as the parent."}`** even when both issues are in the same project — the message is misleading, the real cause is that the type change is a UI **Move** operation. When an instruction is "file X under Y" and Y is a Task, the executable path is to **create a fresh Subtask under Y carrying the content across, then close the original pointing at the replacement**. Cheap here because the orphan Task had no description; check that first, and say in the comment *why* it was re-created rather than moved so it does not read as churn. KAN subtask type id is **10002** (Epic 10001, Task 10003, Story 10004, Feature 10005, Bug 10006). **How to apply:** treat "close the sprint" as a two-step operation with an explicit destination, and check whether a reparent instruction crosses the Task/Subtask boundary before promising it. Source: K2C.

## 2026-08-07 — A client's survey/test plan is a set of CLAIMS ABOUT BUILD STATE — diff every question against the tracker before answering it (K2C)  [Client Coordination]
Raw Fury sent a 19-question alpha playtest survey and asked what we thought. Read on its own it is a clean, well-structured document and the honest answer is "looks good". Joining each question to the live board changed the answer completely: **four questions were wrong about the build and two more pointed straight at known-broken features.** Q15 offered the **Chariot** as a selectable mount when it is Island E / MS5 (KAN-162 BACKLOG, art + code subtasks both To Do) and cannot appear in an A+B build. Q13 told testers to ignore the Merchant's art because "final art isn't in yet" when the Merchant shipped **complete at MS3** (epic KAN-355 plus all three children Done), so the caveat would have thrown away the art feedback we most want. Q11 asks testers directly about *friction paying for and mounting the Large Black Cat* — which is **KAN-463, the only open Critical on the board**, triple-confirmed and including RF hitting it themselves; ship that survey unfixed and every tester returns the same bug instead of an opinion. Q8 asks how the Ra puzzle *feels* while **KAN-467 (days stay shorter until Ra is freed) is still BACKLOG**, so the mechanic supplying that puzzle's entire pressure is absent from what they would play. And the **Lurker**, the one genuinely new enemy behaviour in the DLC and a Phase 1 focus area in RF's *own* strategy deck, had **no question at all**. **How to apply:** treat every question in a client-authored test plan, survey or QA script as an assertion about what is in the build, and resolve each one against the tracker — content items against the island/chapter map, "final art isn't in yet" style caveats against the delivering epic's children, and any question naming a specific interaction against the open bug list for that interaction. The high-value finding is never a badly-worded question; it is a well-worded question aimed at something that does not exist yet or is already known broken. Corollary that paid off twice here: the survey's own scope line ("both Island A and Island B playable start to finish") is a **verbatim description of a build we had already delivered and they had already approved**, which turned "which build do you want?" into "you have described the Vertical Slice, use that one". Clients routinely describe your own deliverable back to you without realising it. Source: K2C.

## 2026-08-07 — Check a client's proposed test/event date against the MILESTONE calendar, not against team availability (K2C)  [Client Coordination]
Mia (RF, covering for Ishani) asked to start the external playtest "somewhere around the end of August" and Robert offered a stable build a few days before it starts. Both reasonable in isolation. Against the calendar it is not: **MS4 Pre-Cert is due Fri 28 Aug and S8 (Aug 24–28) is the hardening sprint into it**, so "a stable build a few days before" means cutting and stabilising a *second* build in the same week as a **560 000 SEK payment gate**, using the same three people. The conflict is invisible from inside the request, because a publisher asking for a build in week 35 has no idea week 35 is the gate week. **How to apply:** whenever a client proposes a date for anything that consumes build or QA capacity (playtest, capture session, press build, showcase demo), overlay it on the milestone and sprint ladder *before* replying, and if it collides say so immediately with two concrete alternatives rather than a warning. Here: run the alpha on a build derived from the already-approved Vertical Slice, or move the test to the first week of September. A named alternative reads as production control; a raised risk with no option reads as an excuse. Also worth carrying: **a new counterpart covering for someone on leave has none of the schedule context the regular contact had**, so the calendar collision is more likely, not less, and the reply should state the milestone date explicitly instead of assuming they hold it. Source: K2C.

## 2026-08-07 — One word in a dev's own Discord list can invalidate a board status — grep the playtest report for "still" before trusting In Review (K2C)  [Process]
Fredrik's post-demo list opened with "staff of ra on client there is no beam ... i see ball on client **STILL**". KAN-485 was sitting in **In Review**, assigned to him, moved there two days earlier. The single word "STILL" is the whole finding: the assignee is reporting that the ticket he moved to In Review is not fixed, and nothing on the board reflects that. Reopened it to In Progress with the quote in a comment. This sharpens the standing "In Review is a stalled queue" note from 2026-08-04: the queue is not merely *slow*, some of it is **wrong**, and the evidence is sitting in the dev's own words in a channel nobody diffs against ticket status. **How to apply:** after every playtest, take each line of the team's findings and match it against tickets in In Review or Done, watching specifically for recurrence markers — "still", "again", "not fixed", "same as before". A recurrence reported by the ticket's own assignee is the strongest possible reopen signal and needs no further confirmation. Do apply a proportionality rule though: only reopen where the recurrence is explicit. A second item on the same list ("picked up banner as host, should change to bow for oscar client") described KAN-486 without saying "still", and the Gemini note showed the symptom was actually *wider* than that ticket's title, so the right move there was a comment asking the assignee to confirm same-defect-or-split, not a status change. Reopening on ambiguous evidence just churns the board. Source: K2C.

## 2026-08-05 — Gmail search returns THREADS but shows the FIRST message's metadata — the thread you need looks like an old mail from the wrong person (K2C)  [Tooling]
Robert asked me to reply to "Juliette's mail to Carolina". I ran three searches, concluded I could not find it, and asked him which mail he meant. **The thread was in the first search's results, and again in the third.** It renders as `From: Niclas Lagerlöf · Date: Wed, 24 Jun 2026 · Subject: Music/Content Creation Agreement templates`, because those fields describe the thread's **opening** message. The mail actually wanted — Juliette to Carolina, chasing an unsigned contract, 4 Aug — was the sixth message inside that same thread. I filtered on From and Date, judged it "old, wrong sender", and never opened it. The only field that told the truth was `messageCount: 6`. Compounding it: **Juliette sends from `juliette@combinedeffect.com`, not `@rawfury.com`** (RF's outsourced counsel at Combined Effect AB, signs as legal@rawfury.com), so a `from:@rawfury.com after:<date>` sweep returned nothing from her and I read that absence as confirmation she had not written. Two independent wrong signals pointing the same way, but the root error was having the thread and not opening it. **How to apply:** treat `messageCount` as the only load-bearing field in a Gmail search result row — From, Date and snippet all describe the thread's origin and actively mislead on long threads. If the count exceeds the messages you can account for, open it before concluding anything. And never conclude "nothing from X" off a `from:<domain>` filter when X may use a personal, agency or client-side address; search by thread subject or by the other party instead. This is the same discipline `/close` step 0 already mandates at report-writing time, applied where it actually pays, which is at search time. Cost here: I asked Robert a question he had already answered, and he had to point me back at a thread I had been shown twice. Source: K2C.

## 2026-08-05 — A pasted meeting transcript can be silently TRUNCATED — check the timestamps are continuous before you mine it, and before the sender assumes it landed (K2C)  [Client Coordination]
Niclas mailed over the RF/AP weekly transcript with "kunde inte ladda ner transcript då Ishani äger mötet, men här är en copy+paste på **allt** iaf". The docx runs 0:04 to **1:00**, then jumps straight to **35:42** and ends at 38:01. Thirty-five of thirty-eight minutes are gone, and the missing block is precisely the substance: the platform/cert brief, the publisher's revised marketing timeline, and the milestone-notes review. The cause is mundane and will recur — a Teams transcript pane virtualises its list, so a select-all copies only what has been scrolled into view, and you get a clean-looking document with a hole in the middle. **The tell is not length, it is timestamp continuity**: the file reads as a complete meeting because it has a start line, a stop line and a coherent wrap-up. **How to apply:** before quoting or actioning any pasted transcript, extract the timestamps and assert they advance without a jump; a gap larger than the meeting's natural pauses means you are holding a fragment. Say so immediately, because two things decay fast — the sender still has the tab open and can re-copy today, and the recipient has usually already replied "thanks" (Robert had, within six hours), which closes the loop and makes the fragment the permanent record. Note also who *owns* the recording (here Ishani, who is away, with Mia covering) since that determines whether a proper export is even reachable. And do still mine the fragment: the surviving three minutes carried a new publisher-side contact, the reactivation of a cultural-sensitivity review that had been logged as unanswered for a month, an undocumented build obligation, and the publisher naming its single most-wanted asset. A fragment is worth reading closely; it is just not worth trusting as complete. Source: K2C.

## 2026-08-05 — When three unrelated sources name the same asset in one day, that is the priority signal — go look at what the ticket for it actually says (K2C)  [Client Coordination]
Inside twenty-four hours the monarch surfaced in three places that do not talk to each other: the publisher call (Tim: a second island needs another monarch or "it will be the same one"; Pontus: "we should definitely up that"; **Niclas: it is "the most important one" for selling the Egyptian theme**), the playtest note (Imi actioned to design a new crown and make it selectable), and the backlog, where **KAN-248 Monarch rework sits at MS4 with all three children BACKLOG and UNASSIGNED**. Each source alone reads as ordinary: a design aside, an art to-do, a dormant epic. Together they say the publisher's headline asset has no owner three weeks from a 560 000 SEK gate. **How to apply:** when the same noun turns up in a client conversation, an internal work note and the backlog on the same day, treat the convergence itself as the finding and immediately pull that ticket's owner, status and sprint — the convergence is worth more than any one source's phrasing, and the gap it exposes is almost always an ownership gap rather than a scope gap. The inverse heuristic is just as useful: an item mentioned once by the client and never echoed internally is usually a passing remark, not a requirement. Corollary from the same pass: a publisher saying "most important" in a wrap-up aside carries the same weight as one saying it in a milestone mail, and it is far easier to miss. Source: K2C.

## 2026-08-04 — A no-fixVersion sweep is only mechanical where the PARENT is open; children of Done/Icebox parents must be flagged, not inherited (K2C)  [Tooling]
87 open KAN issues carried no fixVersion and looked like one bulk retag. Deriving each subtask's target from its parent split the set cleanly in two: **39 had an OPEN parent with a fixVersion** (Egyptian env art pass, the feature epics, the per-island mounts/items/blessings) and inherited safely; **48 did not, and every one of them was a real decision wearing a mechanical costume.** Three shapes to watch for. **(1) Live children under a Done parent** — KAN-406/441/442 are In Progress Ra art under KAN-94, which is Done at MS2; inheriting would have stamped work being done *this week* with a milestone delivered in June, i.e. hidden it from every release view AND falsified the MS2 record. **(2) Children under a Done parent that should CLOSE, not milestone** — Standard Horse 332/333 and Staff of Ra 318/319 sit under parents Robert closed as delivered; the right move is closing them, and a fixVersion would have made dead tickets look scheduled. **(3) An In Progress child under an ICEBOXED parent** — KAN-316 Greed Mask art, Imi, under KAN-218 which Robert iceboxed on Jul 31. That is the single most valuable thing the sweep surfaced: someone may be building parked scope, and it is invisible unless you compare child status against parent status. **How to apply:** never sweep an empty field by the field alone — join to the parent first and bucket by *parent* status. `node assistant/jira-set.js set <KEY...> fixVersion=MS4` takes **many keys in one call**, so the whole safe subset is two sanctioned calls rather than N (this also sidesteps the classifier's loop-over-mutations trip from 2026-07-26). Re-run the finding query afterwards and assert the count dropped by exactly the number you moved — 87 → 48 here, which is what proved no page was silently truncated. Source: K2C.

## 2026-08-04 — Diff standup ACTION ITEMS against tickets created that day, not just bot half-tickets — a day of zero board updates is the tell (K2C)  [Process]
The half-ticket sweep (`created >= last run`) returned **nothing**, which reads as a clean board. It was the opposite signal: **not one KAN issue was updated anywhere on Mon Aug 3**, while Discord #art carried a full day of real work — Eamonn posted wharf and beggar-camp art, Joanna posted two Anubis statue mockups, Tim issued a design ruling on the statue doorway. The Aug 3 Gemini note listed **6 action items and produced 0 tickets**. So the existing sweep only catches work the bot *tried* to ticket; it is structurally blind to work nobody ticketed at all. Two of those items (the wharf, the beggar camps) had **zero** dedup hits across the whole project and became KAN-483/484 — a week of art with no board presence, 24 days from a 560 000 SEK milestone. **How to apply:** add a second diff to step 1 of the daily routine — take the standup note's action items, dedup each against the tracker by keyword, and treat any with no hit as a candidate ticket, confirming against Discord before creating (the note states intent, Discord proves the work is live). And treat **"zero issues updated since yesterday"** as an alarm rather than a quiet day: on an active six-person sprint it means the board and the work have decoupled, which is exactly when a status report starts lying. Corollary worth carrying: the same pass found the note's owner attribution garbled again (it put Anubis warrior *spawn logic* on the porting lead while Discord shows the lead programmer raising it), so the note is a source for *what*, never for *who*. Source: K2C.

## 2026-08-02 — A blocked scrape can have an unblocked NOTIFICATION channel — check what the platform emails you before building a session (ND)  [Tooling]
db-233 had been parked since June on "CurseForge comments are JS-rendered behind sign-in, so WebFetch can't read them — needs a signed-in Playwright scrape or API access". True, and it framed the whole feedback loop as blocked on DevOps. But CurseForge **emails the comments**: `from:noreply@curseforge.com` "What's been happening at CurseForge" carries commenter handle, date, project and the first ~100 characters of the comment body, and it fans out to **six** AP accounts so it is heavily redundant. That was enough to triage the two most commercially serious reports on the project (a broken Tebex checkout and a cross-store entitlement failure) without any session at all. **How to apply:** when a source is gated, before scoping a scraper ask what that platform *sends outward* — notification mail, RSS, webhooks, digest emails — and whether the indexed mailbox already has months of it. The gated surface is the *canonical* copy, not the only copy. Two caveats to state when you use this route: the body is **truncated**, so it gives you the signal and the reporter but not the full text (cross-reference Discord, where the same users often paste the whole thing); and because it fans out per account you must **dedupe by date + commenter**, not by message. Corollary for the ticket: don't close the DevOps item, downgrade it — the mail route removed the urgency, it did not replace the scrape. Source: ND.

## 2026-08-02 — "Add <person's email> as a coworker" can be unexecutable for three separate reasons — check identity, access and mechanism before promising it (ND)  [Process]
Robert made "add Elias' private mail as coworker on the CurseForge forum" the top item. It looked like a two-minute click and was actually blocked three ways, each of which I only found by checking rather than assuming. **(1) Wrong identity primitive** — CurseForge adds project members **by username, not email**; you search the username, pick a role, and the invitee must then *accept*. An email address is not an input the flow takes. **(2) The person already existed** — `AP_Elias` is a live CurseForge account already receiving ND project notifications, tied to `elias.strandberg@aurorapunks.com`. So the real question was never "add him", it was "re-point his existing account to his private address, keeping his comment history, or add a second personal account". That is a question only Robert and Elias can answer, and it would have been invisible if I had gone straight to the UI. **(3) No credential** — there is no CurseForge session on the VPS and none in the secrets registry, so no agent can perform it at all; the `.atlassian-storageState.json` cookie-export pattern is the durable fix but needs Robert in a browser first. **How to apply:** for any "give X access to Y" instruction, resolve three things before reporting progress — what identity key the platform actually uses (username / email / account id), whether the person already has an account or membership, and whether we hold a credential that can perform the write. Reporting "blocked, and here are the three reasons with the exact fix for each" is worth far more than attempting it and failing on the first one. Related: the same pass found **six** AP CurseForge accounts on a live commercial product, several belonging to departed staff — an access-grant request is a good moment to audit the whole member list, not just add one row. Source: ND.

## 2026-08-02 — Creating a Jira PROJECT needs its own sanctioned helper, and the assignable-user check is the step everyone forgets (ND)  [Tooling]
Robert asked for the ND work to land in "a Jira project". `jira-set.js` operates on issues *inside* KAN and has no project-level verbs, so I wrote **`assistant/jira-project.js`** (`list|me|templates|show|issuetypes|create`) as its sibling — same auth (`~/.claude/.atlassian-credentials.json`), same file-based payload convention for `create` because the body is nested and a description will not survive shell quoting. Facts worth keeping: the aurorapunks instance had **exactly one project (KAN)** before this, so key collisions are not a concern there; `POST /rest/api/3/project` with `projectTemplateKey: com.pyxis.greenhopper.jira:gh-simplified-agility-kanban` + `projectTypeKey: software` yields a team-managed board matching KAN's shape (so jira-set.js's assumptions carry over); and a fresh team-managed project ships work types **Epic 10040 / Subtask 10041 / Task 10042 / Story 10043 / Feature 10044 / Bug 10045**. **The step that matters most:** immediately after creating the project, run `GET /rest/api/3/user/assignable/search?project=<KEY>` — the new ND board returned the existing 18-person K2C licence pool and **Elias, the only person who will actually work the board, was not in it** (no Atlassian licence). A project full of tickets nobody can be assigned to looks finished and is not. Same family as the 2026-07-14 learning that a board's assignee filter only lists people with issues on that board; the generalisation is that **Jira will happily let you build a board for someone who cannot be given a single ticket on it**, and it never warns you. Also inherited from team-managed: no Priority field out of the box, so a bug board needs the one-drag Priority add (2026-07-26 entry) before triage means anything. Source: ND.

## 2026-08-02 — Seed a new bug board from the RAW community channel, not from the scope doc that summarised it (ND)  [Client Coordination]
The ND scope plan (June 2026) already contained a tidy top-5 issue list, and seeding the new Jira project from it would have been one read and no tool calls. Reading the actual 400 days of `#ark-bugs` + `#ark-general` instead changed the priority order at the top. The scope doc's #1 was the PS5 crash; the raw channel showed that as of **Jul 23 and Jul 29 2026 two separate players could not complete a purchase at all** — the in-game BUY button never opens the Tebex checkout — which outranks it, because the engagement is *funded from Tebex revenue*, so a broken checkout defunds the fix for everything below it. The raw channel also surfaced things a summary structurally cannot: **elapsed time** (one player chased three times from Mar 18 to a first reply on Jun 2, another went from bug report to "complete waste of money" in two weeks), which showed the real top-line risk was **support silence** rather than any individual defect; and **self-resolving reports** (a player posting a problem and then "nvm, restarting fixed it") which are the highest-value tickets on the board — a restart-clears-it entitlement failure is a startup race, i.e. cheap to fix and highly visible. **How to apply:** a scope document is a *snapshot with a date*, and on a live product with paying customers the gap between the snapshot and today is exactly where the commercially urgent items live. Read the channel, then diff it against the doc, and say which way the priority moved and why. Practical detail: put reporter handle + date + channel in an info panel on every seeded ticket — on a board built from a year of chat, provenance is the only thing that stops the next person re-litigating whether a bug is real. Source: ND.

## 2026-08-02 — The Death Board API is on port 3777, and port 8080 lies to you about why it failed (K2C)  [Tooling]
Posting the session activity log, I tried `localhost:3000` (curl exit 7, connection refused), then 8080 because something was listening there — and got **`Unsupported method POST`**. That reply reads like a wrong *route* on the right server, so the natural next move is to go hunting for the correct endpoint path. It is actually a **different node service entirely**; the Death Board sets `PORT = 3777` in `assistant/server.js` and is the only thing bound on `*:3777` (everything else on the box binds 127.0.0.1). **How to apply:** read the port from `server.js` rather than assuming a conventional one, and confirm with `ss -lntp` before debugging a route. Generalises past this box: **a plausible-but-wrong HTTP error from the wrong service costs more time than a connection refusal from the right one**, because the refusal tells you the truth immediately and the 405 sends you looking in the wrong place. When an API rejects you in a way that doesn't match its documented shape, question *which server answered* before you question the path. Endpoint for the record: `POST http://127.0.0.1:3777/api/followups/<id>/activity` with `{text, link}` — it stamps `updated:` in the ticket frontmatter itself, so no separate edit is needed. **Refinement (2026-08-02, ND): `<id>` is the FULL FILENAME SLUG, not the short prefix.** `db-233` returns `{"error":"Follow-up not found"}`; the working id is `db-233-discord-read-access-ap-server-feedback`. The error is indistinguishable from a genuinely missing ticket, so don't conclude the ticket is gone — `GET /api/followups` and match on the prefix to recover the full slug (or just read the filename in `assistant/followups/`). Source: K2C, refined on ND.

## 2026-07-31 — "Where does this come from? I don't remember it" is answerable from created/creator/description — and one ticket turned out to be a bot TEST artefact (K2C)  [Tooling]
Robert hit three backlog tickets he didn't recognise and asked where they came from rather than just binning them. Pulling `created`, `creator`, `labels` and the raw description answered it in one query and changed two of the three answers. **KAN-182 War Room** and **KAN-184 Bulk Buy**: created by Robert himself on 2026-04-10 in the original backlog seed, already labelled `nice-to-have` at birth — so "feels out of scope" was correct and had been correct since April. **KAN-218 "Greed Mask upgrades"**: the description is the verbatim Discord message *"can you create atest ticlket to the Jira board and respond here the ticket ID"* — it is one of the **first Death Board bot tests from 2026-04-13**, wearing a real-sounding summary applied later. It had survived three months, been pulled into sprint S2, and was about to be triaged as if it were design scope. The important nuance: greed-mask work *was* real (Imi's 7 designs, the Set-inspired direction), so "this ticket is an artefact" is not the same as "this topic is fake" — say both, or you look like you are dismissing real work. **How to apply:** when anyone asks where a ticket came from, never answer from memory or from the summary. Pull creator + created + description + labels; the description on a bot-created ticket carries the originating message verbatim and a Discord permalink, which is a complete provenance trail. And treat a **summary/description mismatch as the tell for a repurposed or artefact ticket** — a real ticket's description elaborates its summary, an artefact's description is about something else entirely. Leave the provenance in a comment when you icebox one, so the next person doesn't re-litigate it. Source: K2C.

## <!-- ARCHIVE-INDEX -->Archived learnings index

72 older entries were rotated into `archive/pm/` to keep this file loadable in one pass.
Nothing was deleted. They are still indexed by RAG — `rag_search(query, source="agents")` finds them,
or open the archive file below (each has its own Contents block, so you can offset-read a single entry).

### 2026-Q3 — 53 entries → [`2026-Q3.md`](archive/pm/2026-Q3.md)

- 2026-07-31 — Before writing an epic's closing rationale, read its children — "cut" and "deli…
- 2026-07-31 — Milestone content items by the island that unlocks them, not by a blanket sweep…
- 2026-07-31 — Fortnox / invoice-status questions go to CorpBot, not to Robert (K2C)  [Process]
- 2026-07-31 — A verbally-agreed milestone change is a CONTRACT VARIATION — record it with a d…
- 2026-07-31 — A typo in the trigger phrase silently eats a bug report — reconcile Discord cre…
- 2026-07-31 — A note that looks confabulated may be a faithful record of a DERAILED meeting —…
- 2026-07-27 — `/rest/api/3/search/jql` caps a page at 100 no matter what `maxResults` says —…
- 2026-07-27 — When a bulk retag would reverse a decision Robert made explicitly, carve it out…
- 2026-07-27 — "The board contains no issues" = a sprint left in `future` past its start date,…
- 2026-07-27 — A sprint named for the next milestone can contain none of that milestone's work…
- 2026-07-26 — Team-managed field creation is a DRAG-AND-DROP palette, not a dialog — and the…
- 2026-07-26 — A shell `for` loop over jira-set.js writes is classifier-blocked; the same call…
- 2026-07-26 — "Make it a critical bug" on team-managed KAN: there is no Severity AND no Prior…
- 2026-07-26 — The Discord bot now DOES apply the @-mention assignee — the half-ticket defect…
- 2026-07-24 — The real trigger post was a BARE link with no keyword — a "safety" keyword gate…
- 2026-07-24 — Hand-built RFC822 replies mangle non-ASCII display names; send To/Cc as bare ad…
- 2026-07-24 — "Send the follow-up when X posts in Discord, no need to consult" = build a VPS…
- 2026-07-24 — A milestone delivery doc needs a "what shipped" section, not just "what's new"…
- 2026-07-24 — On delivery day the Gemini note gives the RULE, Discord gives the INSTANCES - r…
- 2026-07-24 — Discord bot half-tickets compound: sweep `created >= last run` EVERY run, and r…
- 2026-07-24 — Reuse a prior milestone Legend by pulling its STORAGE XHTML and mirroring its h…
- 2026-07-23 — Date the daily-run block from currentDate, not from the newest meeting note (K2…
- 2026-07-22 — Gemini garbles whole TOPICS, not just values - a note can invent a workstream t…
- 2026-07-22 — Discord-bot-created tickets are half-tickets - sweep them for triage gaps every…
- 2026-07-22 — Repeated e-signature mails to "the same" contract are usually ORDERED AUTO-ADVA…
- 2026-07-22 — Build a sanctioned node helper the moment a class of mutation keeps getting cla…
- 2026-07-22 — Jira descriptions support real tickable checkboxes via ADF taskList - use it fo…
- 2026-07-22 — For a checklist an external collaborator must extend, Confluence beats a GDoc w…
- 2026-07-22 — Atlassian page bodies are too big for an MCP call - file-based helpers are the…
- 2026-07-22 — Jira write calls via curl get auto-mode-classifier-denied even for routine-auth…
- 2026-07-20 — K2C Discord handle → real-name map, and why you MUST resolve it before assignin…
- 2026-07-20 — Resolve an assignment split from who REPORTS the work, not from the discipline…
- 2026-07-20 — Splitting a combined subtask: repurpose the original as one strand, create sibl…
- 2026-07-14 — "Resend expired signature link to X" — check LIVE OpenSign status first; X may…
- 2026-07-14 — K2C daily run: check for EXISTING backlog tickets before creating — active work…
- 2026-07-14 — Team-managed KAN: no second-assignee field, and the board Assignee filter only…
- 2026-07-13 — Client "what does role X do?" — verify the title against the structure WE autho…
- 2026-07-10 — Agile sprint move returns 204, but the immediate sprint=N JQL read is STALE — v…
- 2026-07-10 — "Graft into the MS schedule" = epic + discipline tasks at the right fixVersion,…
- 2026-07-10 — Transparency-flag client mails: surface the concern, defer the decision to thei…
- 2026-07-10 — Studio→publisher mails use collective "we", not first-person "I" (draft-vs-sent…
- 2026-07-10 — K2C RF recipient routing: iconography/naming/brand-sensitivity mails include Po…
- 2026-07-09 — A "fewer missions/levels" scope cut usually removes CONTENT, not SYSTEMS — don'…
- 2026-07-09 — Client shortlist objection "your team is the lightest / your timeline the short…
- 2026-07-09 — Client bringing a named domain expert to a pitch call = probe intel + a relatio…
- 2026-07-08 — Gemini notes garble specific dates/numbers/names — treat every hard value as su…
- 2026-07-08 — Closing In-Review milestone deliverables: gate on the client APPROVAL EMAIL, no…
- 2026-07-08 — KAN is team-managed: Bug type exists, Task->Bug is trivial, but custom-field cr…
- 2026-07-08 — K2C sprint ladder already implements "2-wk + hardening-before-each-milestone" t…
- 2026-07-08 — Drive folder IDs in project memory DRIFT — verify against reference_drive_folde…
- 2026-07-08 — K2C island→milestone map — DRIFTED, do not trust cached versions (corrected 202…
- 2026-07-08 — Atlassian bill "doubled" = extra PRODUCTS switched on (per-agent/creator), not…
- 2026-07-08 — The generic `atlassian-jira` MCP is bound to the K2C (KAN) site — for BADASS us…

### 2026-Q2 — 19 entries → [`2026-Q2.md`](archive/pm/2026-Q2.md)

- 2026-06-30 — "Full groom now" still means check-before-creating — pull existing tickets, don…
- 2026-06-30 — Vertical-slice milestone on a proven-base DLC: reframe "prove the direction" vs…
- 2026-06-26 — Before building a milestone delivery package, check whether a prior session alr…
- 2026-06-26 — Keep candid artist/working notes in client delivery docs — don't sanitize (K2C)…
- 2026-06-26 — Confluence rich delivery: inline video via embed macro + native image pages via…
- 2026-06-26 — Reading Discord pinned messages: use the raw REST pins endpoint, not the discor…
- 2026-06-26 — Editing a client email draft the user has already edited: read-fresh, recreate,…
- 2026-06-25 — For an alpha BUILD milestone, the real delivery state lives in Discord + the da…
- 2026-06-25 — Alpha delivery framing: lead with "the experience as a whole," pre-flag placeho…
- 2026-06-25 — "Go broad" art decision changes how per-island art tickets are read at mileston…
- 2026-06-24 — Steam Summer Sale discount entry requires pre-approval of specific percentages…
- 2026-06-22 — Cost-to-complete benchmarks for a mid-size European studio (2026, validated) (P…
- 2026-06-22 — Gemini standup notes assign owners reliably but DON'T reveal completion status…
- 2026-06-22 — K2C completion-status is unmaintained across ALL three trackers — true done-sta…
- 2026-06-22 — K2C team ownership-by-discipline map (K2C)  [Client Coordination]
- 2026-06-22 — "Sprint built" ≠ "sprint rolled" — a prior session can populate a future sprint…
- 2026-06-22 — After agile sprint-issue moves, verify membership with JQL `sprint = N`, NOT th…
- 2026-06-17 — A CUST spawn "only made one task" can be an under-built TEMPLATE, not a broken…
- 2026-06-17 — Backfilling an existing Location Epic: you can't re-fire the Flow — hand-clone…

## Jira: a ticket missing from a board has at least two distinct causes, check the type before the sprint
**Date:** 2026-09-03 · **Project:** K2C · **Category:** tooling / Jira

Two "why isn't this on the board" questions arrived a day apart with different answers, and the
second one is the trap because the first answer is fresh in mind.

1. **No sprint.** Issues created over REST get no sprint field. A sprint board renders only the
   active sprint, so they vanish. Fix: `POST /rest/agile/1.0/sprint/{id}/issue`.
2. **Wrong issue type.** In a **team-managed** (`next-gen`) project a board draws Task/Story/Bug
   only. **Subtasks never render as cards, whatever their sprint or status.** No configuration
   changes this; it is how the board works.

Diagnose type first, it is one field. `GET /rest/api/3/project/KAN` → `style: "next-gen"` tells you
which world you are in.

**The gotcha that will mislead you:** a subtask's Sprint field (`customfield_10020`) shows its
parent's sprint, so the ticket looks like a sprint member. It is not one. JQL `sprint = 9` returned
189 issues and zero subtasks on a board where 109 open subtasks existed. Both the board API and JQL
agree with each other and disagree with the issue's own field.

**Always quantify before recommending.** "KAN-673 is a subtask" is a shrug. "109 of 393 open issues,
28% of open work, including nearly all of the art list" is a decision. One JQL pass grouped by
parent turns a single-ticket question into the real finding.

**The second-order damage is worse than the invisibility.** Subtask status does not roll up. The
parent card KAN-142 sat in **To Do** while three children were In Progress. A board used for status
was reading the project as less advanced than it was, and nobody could see why.

**Fixing the view beats converting the data, and it was Robert's call.** Converting subtask→Task is
allowed (`editmeta` lists Task/Story/Bug as targets and `parent` is settable) but it flattens
Epic→Task→Subtask to Epic→Task and loses the per-island grouping card. A board built from a saved
filter shows everything with no data change. Recipe:
`POST /rest/api/3/filter` (share `{type:'project'}` or the board is invisible to the team) →
`POST /rest/agile/1.0/board {type:'kanban', filterId}`.

**Always re-map the columns after creating a board from a filter.** Auto-mapping is naive: it folded
BACKLOG *and* In Review into In Progress, and Icebox into Done. `PUT
/rest/greenhopper/1.0/rapidviewconfig/columns` with `{currentStatisticsField:{id:'none_'},
rapidViewId, mappedColumns:[{name, mappedStatuses:[{id}], isKanPlanColumn:false, min:'', max:''}]}`
works and is what the UI calls. Then verify no status is left unmapped, since an unmapped status
means cards that exist but never draw, which is the bug you were sent to fix.

**When answers to a multi-part question contradict each other, say so instead of executing both.**
Robert picked "convert nothing" and "close the parents as Done"; the second was only coherent if the
first had gone the other way. Closing KAN-142 with 14 open children would have hidden the work twice.
Flag and hold the conflicting half, deliver the rest.

## Closing a stale review column: the milestone label lies, the children do not
**Date:** 2026-09-03 · **Project:** K2C · **Category:** process / Jira hygiene

Robert asked to close the In Review tickets "from MS2 and earlier". The instinct was right (135
open in one column) but the instrument was wrong, and the gap between what he asked and what the
board contained was the whole job.

**Check whether the category the user named actually exists before you scope to it.** Zero In Review
tickets carried an MS0/MS1/MS2 fixVersion or an S1-S3 sprint. Only 5 both originated before MS3 and
had not moved since. The real bloat was 101 tickets from S8, the MS4 hardening sprint, that shipped
on 28 Aug and were never closed. Say that out loud and re-ask rather than closing 5 things and
calling it done.

**Sprint membership can be worthless as evidence.** I built a gate on "in S8 but not carried into
S9" and it returned 1 ticket. Testing the assumption killed it: all 20 *Done* S8 issues were in S9
too, so everything had been bulk-carried and S9 membership said nothing about whether work
continued. Always test a discriminator against a population where you know the answer (the Done
ones) before trusting it.

**AI notetakers write action items in the imperative, so keyword matching reads "to do" as "done".**
I matched ticket summaries against Gemini notes gated on /resolved|fixed|completed|implemented/ and
it surfaced "**Complete map UI** (Dubravko)" as evidence that the map UI ticket was complete. It is
an assignment. Every one of the 7 "corroborations" was a false positive. A summary of a standup
cannot verify ticket-level completion, and pretending it can silently closes live work. Past-tense
statements about a named person ("Fredrik resolved a bug causing banner duplication after saving and
loading") are real evidence; imperative bullets are not. Read those by hand, they are few.

**Never close a parent that still has open children.** KAN-354 was the single most tempting close
(In Review since June, untouched) and it had 4 open subtasks plus a comment saying the art iteration
continues into MS5. Make this a hard precondition, not a judgement call.

**Related tools:** the reusable duplicate scanner is `assistant/jira-dupes.js`; see
[[feedback_check_before_creating]] and the entry above on notetaker action lists.

## Duplicate detection on a Jira board: score the rare words, penalise the shared prefix
**Date:** 2026-09-03 · **Project:** K2C · **Category:** tooling

Built `assistant/jira-dupes.js` (registry-driven like the rest, so a new project is one JSON block).
Three things had to be right before the output was usable at all:

1. **Exclude structural pairs first.** A naive scan ranked "Camel: art" against its own parent
   "Camel" at 0.9. Subtasks sharing a parent, and any parent/child pair, must be skipped or real
   duplicates never surface. Before that filter, 33 hits were nearly all noise.
2. **IDF-weight the tokens against the board's own corpus.** "plinth" is worth far more than "asset".
   Flat token overlap buries the signal on a board where 80 summaries contain "map".
3. **Penalise a differing leading qualifier.** "Sobek - Level Art" vs "Sphinx - Level Art" scores
   high and is two different islands. A mismatched first token is evidence *against* duplication.

**The tool finds candidates; it must not decide.** Of 36 candidates, 2 were true duplicates, and 4
high scorers were deliberately distinct: hermit CHARACTER (Imi) vs hermit HOUSE (Eamonn) is the art
split, and Blood Moon composition (Carolina) vs engine loop support (Oskar) is the audio split.
Closing on score alone would have destroyed real work. Link the near-misses as "Relates" so the next
sweep does not re-raise them.

**A sync that creates from a list must check the existing epic tree, not just open summaries.** My
2026-09-01 art-schedule sync created KAN-693 "Demolisher Hermit" while KAN-269 "Demolisher hermit:
art assets" had existed under epic KAN-266 since April. It also made me report the demolisher
implementation as unticketed when KAN-270 was sitting right there. Fold the dupe scan into
`jira-sync.js plan` so creation is checked against the whole board including children.

## Finding someone's email: check calendar invites from other people at the same org
**Date:** 2026-09-03 · **Project:** K2C · **Category:** tooling / research
**Source:** Robert, directly.

Needed Pontus Rundqvist's address to share a deliverable. Gmail search, Drive, and the RAG wiki all
came back empty because he works with Robert on Slack, never over mail, and the Slack MCP servers
were down that session. I was about to ask Robert.

**The calendar has him.** `list_events` with `fullText: "Pontus"` returned
`{displayName: "Pontus Rundqvist", email: "pontus@rawfury.com"}` as an attendee on a recurring sync
organised by Ishani at Raw Fury. One call, exact answer, no guess.

**The general rule: a person who never mails you is still on the invite list of meetings organised
by their colleagues.** So when an address is missing, search the calendar for people at the SAME
ORG, not just the person. The attendee list of any invite from that company is a small internal
directory. This also gives you the org's address format, which turns a guess into a check.

Order to try: calendar attendee lists → Gmail → Drive permission lists on shared folders (existing
grants show real addresses) → the RAG wiki → ask Robert. Note `search_events` (semantic) returned
nothing here while `list_events` with `fullText` found it, so prefer `fullText` for a name.

Related: [[feedback_check_web_before_asking]], [[feedback_search_wiki_first]].

## 2026-09-03 (b) — Co-dev-bud: propageringskedjan finns nu som skill [sbz / Irons 2]

När ett bemanningsark ändras rör **en enda rad sju ställen** i offerten (total, FTE-månader och
blandad rate, betalplanens grupper, kurvans SVG-punkter, toppen på fyra ställen, milstolparnas
bemanning, rolltabellen). Checklistan, plus milstolpar som kassaflödesinstrument (mät längsta
obetalda sträckan) och listan över vad som aldrig får stå i en offert, ligger i
[[codev_bid_pitch]]. Läs den innan nästa co-dev-bud räknas om.
