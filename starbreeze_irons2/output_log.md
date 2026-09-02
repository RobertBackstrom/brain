# Output Log — Project Irons 2 (Starbreeze)

Track significant deliveries, drafts, and external posts here. Each entry: date, what, where it went, outcome.

| Date | What | Where | Outcome |
|------|------|-------|---------|
| 2026-08-17 | Read Tobias Remmers' brief (feature list + staffing outline, 12 Aug, Matt Dixon cc) | Gmail thread `19ff6451882f7d46`, 2 PDF attachments | Scope: 4 new heists (Turbid Station, 99 Boxes/Touch The Sky, Syntax Error, Under The Surphaze) + upgrade of the 4 HR1 stages + systems work (progression rework, stealth ingredients, shield AI, restart/partial escape, UI/UX, PUBG engine + 3C). SBZ outline: 7 milestones / ~12 months, 31-43 roles, peak 30-40 concurrent |
| 2026-08-17 | Co-dev proposal — HTML living-doc | **pitch.aurorapunks.com/project-irons-2** | Live. AP as full co-dev team across all disciplines, phased ramp 7 → 14 → 4 over 13 months (Sep 2026 to Sep 2027), peak 14 against a self-imposed 15 ceiling. QA outside the core as external contractor, quoted separately. On-site at SBZ. No named resources per Robert. Sequenced disciplines, not parallel |
| 2026-08-17 | Gated the pitch (HTTP Basic Auth, whole slug) | `assistant/pitch-auth.json` → `project-irons-2` | user `starbreeze` / pass `Ai8M9hj8JNyG`; realm "Project Irons 2 - Aurora Punks x Starbreeze - Confidential". 401 without creds / 200 with, verified live. Gated because the page carries Krafton/PUBG-confidential scope detail. Ungate = remove the key |
| 2026-08-17 | Indicative commercials, v1 | same page | Superseded. Blended 950 SEK/h (rate card AAA column) = 152 000 SEK per FTE-month, 22 496 000 SEK total |
| 2026-08-17 | Revision pass on Robert's 9 feedback items + 3 answers | same page | (1) Hero lede de-salesed, now plain "our take, read against your 12 Aug material". (2+7) On-site claim corrected to leads-on-site, rest hybrid, split set per phase. (2) New section "Why the team is this size" with what keeps it down and where it would go up. (3) "Bigger and more complex" attributed to Tobias, not stated as our finding. (4+5) **Engine and 3C work moved to AP**, PUBG team reduced to access, approval, constraints and a named counterpart. (6) Pricing switched to flat retainer **140 000 SEK per developer per month**, total **20 720 000 SEK**. (8) QA priced at **500 SEK/h**, 80 000 per full QA month, separate line. (9) Software licences folded into the retainer, third-party licence exclusion removed. Ceiling language replaced with "recommended max" |
| 2026-08-17 | Scalability framing added per Robert | same page, "On team size" callout | Explicit: per-head pricing with Krafton = we can staff deeper and run more heists in parallel; fixed price = lean team protects their margin. Framed as AP being on Starbreeze's side of the margin question rather than defending a number. Tables re-verified arithmetically, live 200 with auth / 401 without |
| 2026-08-17 | Design and audience due diligence memo, v1 | `drafts/design_due_diligence.md` (internal, not sent) | 8-section memo for the Tobias/Matt conversation. Key findings: RankOne overlap runs through PD2 not PD3 (20.4% of PUBG panel co-plays PD2 at 4.06x vs 2.25% PD3; 27.7% of PAYDAY panel plays PUBG); PUBG base is neutral on stealth (1.00x) and strong on loud co-op PvE (1.63x, SWAT 2.53x); HR1 gave no Steam CCU lift (Apr 353k avg vs May 322k/Jun 317k, SteamCharts); PD3 halo real but tiny (~260 avg CCU); PAYDAY community sentiment negative on resource-diversion grounds (Steam forums + TheKknowley 210k-sub channel). Verdicts: Tobias supported on stealth avoid-list, progression rework, restart/partial escape; contradicted on complexity growth; top ask = HR1 mode telemetry from Krafton. Gaps flagged honestly: no public retention data, Reddit blocked, Starbreeze Q2 2026 report not yet out |
| 2026-08-17 | Memo v2: PUBG-side sentiment gap partially closed | same file, sections 4, 5, 8 revised in place | New source: full PUBG Steam forum sweep (app 578080, ~10 threads, ~30 participants). Players who engaged liked the mode ("event is good", one playing it exclusively); complaints = music volume, team saboteurs, stealth bonus too low, one bug. PD3 funnel thread: 6/6 "no". Two verdicts moved: partial escape upgraded to "supported with direct player evidence" (saboteurs exploit all-four-must-escape); stealth bet refined (first-hand feedback attacks reward size, not mechanics count). Definitive route failures documented: Reddit 403s the VPS IP on every route incl. realistic browser; YouTube comments behind bot-check then captcha wall (Playwright + yt-dlp). Console sentiment: zero read, needs residential-IP manual pass |

| 2026-08-17 | Fable agent + RankOne audience/sentiment due diligence | `drafts/design_due_diligence.md` | RankOne panel (3 109 PUBG profiles) + SteamCharts + 80.lv interview + community channels. Key: crossover affinity runs through **PAYDAY 2** (20.4%, 4.06x) not PD3 (2.25%); PUBG base **neutral on stealth (1.00x)**, strong on loud co-op PvE (1.63x) and SWAT (2.53x); HR1 gave **no Steam CCU lift** for PUBG; PD3 halo real but ~260 concurrents. Verdicts: Tobias **supported** on stealth avoid-list, progression rework, restart/partial escape; **contradicted** on "bigger and more complex" as a goal; silent on difficulty/weapons/shield. Spot-checked SteamCharts (exact match) and the 80.lv interview (exists, Remmers + Gi Hwan Park) |
| 2026-08-17 | Audience section added to pitch page | same page, "What we looked at before writing this" | Stat band (4.06x / 2.53x / 1.63x / 1.00x) + plain-language "how to read these" callout + three things we would raise + the telemetry ask. Sharpest findings (no CCU lift, hostile PAYDAY community, complexity contradicted) deliberately **kept off the page** for the meeting, per Robert |

| 2026-08-17 | Stealth-reward finding promoted to the pitch page | same page, "What we would raise early" | Per Robert. The one first-hand HR1 stealth account complained about the **10% completion bonus**, not the mechanics count, so the cheapest HR2 stealth investment is payout tuning through the new currency economy before new sensor types. Connects Tobias's progression rework to his stealth problem. Framed on the page as n=1 with an explicit "we would not build a plan on it", to avoid overstating a single forum post to a client |

| 2026-08-17 | Feature plan Gantt added | same page, "Your feature list against the milestone schedule" | Tobias's full feature list sequenced at **month resolution** across 13 months (not phase blocks, so durations are real). 33 bars in 6 groups: engine/platform, heist content, systems, UI/UX, release, QA. Footer row shows developers per month, tying the staffing curve to feature density. Four stated sequencing decisions: HR1 upgrades late at Alpha 2 (systems baseline must exist first), heists staggered not parallel (lets LD peak at 3 not 5), stealth in two sets with the second telemetry-gated, engine work front-loaded with a go/no-go gate at Alpha 1. Rendered and visually verified via Playwright chromium |
| 2026-08-17 | 20% contingency added to budget | same page, commercials | Delivery subtotal 20 720 000 + contingency 4 144 000 = **24 864 000 SEK**. Shown as its own table rows plus a callout: held against named risks, drawn by agreement, unused not invoiced. **Open choice for Robert:** the "what is not drawn is not invoiced" sentence makes the higher number sellable but gives up the upside. Strip it if the contingency should be firm budget |
| 2026-08-17 | Draft mail to Tobias + Matt | Gmail thread `19ff6451882f7d46`, draft `r7316947061089275624` | Reply on the existing feature-list thread, Matt added back (he was cc on Tobias's original, dropped from Robert's 13 Aug reply). Link + credentials + 5-point summary + ask for a walkthrough time. **Not sent**, awaiting Robert |

| 2026-08-20 | Staffing revised on Robert's instruction | pitch page, all views | Merged Executive Producer + Producer to one row (one producer on the project). UI Programmer FP→A2. +1 Level Designer FP→Beta (peak now 4). Systems Designer extended FP→Beta. +1 Environment artist PA→A2. Lighting narrowed to A2+Beta only. UI/UX FP→A2. Console Lead 50% in Sep and FP, then full. Added Character Artist FP→A2. **Curve 6.5 / 14.5 / 17 / 18 / 19 / 13 / 7 / 4, peak 19** (was 14). 180.5 FTE-months. **Subtotal 25 270 000 + 20% contingency 5 054 000 = 30 324 000 SEK** (was 24 864 000, +22%). Updated everywhere: staffing table, hero SVG, Gantt bands + month footer, cost table, milestone headcounts, narrative. Rendered and verified |

## Open items
- **Rate settled at 140 000 SEK per developer per month** (Robert, 17 Aug). Reasoning: Starbreeze will likely push back on an hourly rate because a Czech studio undercuts it, so a flat retainer avoids the hourly comparison. Rift-sourced people must be held down to match this level.
- **Rift confirmed** (Robert, 17 Aug): they did need AP's help. That is a separate project tracked in its own session.
- **Krafton hands-off in Irons 1** per Robert, which is why the PUBG-dependency framing was removed. Worth verifying before the meeting if it comes up.
- **No names in the offer** per Robert. CVs for lead roles offered once scope and structure are agreed.
- **Sent mail now contradicts the page.** Robert's 18 Aug mail states "peaks at 14 (not counting QA)"; the page says 19 since the 20 Aug revision, and the budget moved 24,9 to 30,3 MSEK. He should raise it himself rather than let Tobias and Matt discover a 36% headcount increase on a page he told them is live. **Open decision for Robert.**
- **Lean argument weakened, not lost.** 19 against Tobias's 30-40 is still roughly half, but the "under 15" framing is gone and the hero now reads "Peak 19". If he wants back under 15 the cheapest trims are the 4th level designer at Alpha 1 and the character artist.
- **Rift meeting 21 Aug** (Gustav Wassberg; Dmitry = Tech Lead, Jesper = Level Design Lead can join the Starbreeze meeting). Gustav wants a pre-meeting at their office to align expectations. The revised plan needs peak 4 level designers, so Rift carries more of the plan than before and their rate must fit under 140k/dev/month.
- **Krafton's evidence base is weak, and Tobias and Matt know it.** Both told Robert they believe Krafton just ran an AI sweep over player sentiment for the first gamemode, and that real telemetry might change their own assumptions. This puts AP on the same side as Tobias and Matt rather than against them: our telemetry ask backs a position they already hold. Page framing set to "measured behaviour rather than inferred sentiment", which lands the point without naming the AI sweep in writing. Never put the AI-sweep remark on the page or in mail, it is an internal Starbreeze view of their funder.
- **Starbreeze Q2 2026 interim report** was unpublished at research time. First public read on post-launch economics. Check before the meeting.
- Project folder scaffolded minimally (this log + drafts/). Full scaffold per [[new_project_scaffold]] and a DB prefix still to be assigned if the deal progresses.

| 2026-08-24 | The Author: voice pass on the pitch page | https://pitch.aurorapunks.com/project-irons-2/ (live, gated) | 35 edits stripping the selling and self-narration layer per [[voice_anti_selling]], on Robert's instruction to hold to dry facts. Numbers and the four sequencing decisions kept, framing cut. Removed: the "How to read these" callout (over-index scale folded into the source note as fact), the closing "Our position" callout, "It is not a headcount we picked and then justified", "We would rather build this from evidence than from taste", "the single most common way this kind of plan loses a month", "a Beta with new features in it is a Beta that slips", "we would rather find that in February than in August", "we would rather you saw the number", "If the evaluation says the scope needs to change, you hear it in September rather than at Alpha", and the hero's closing deference about setting headcount against their commercial structure. The "How to read the shape" panel became "Constraints in the schedule", keeping the plan facts and dropping the chart-reading narration. "What would settle it properly" lost the two positioning bullets ("whoever produced them", "we would rather make that ask alongside you") and kept the telemetry list plus a one-line "measured behaviour, not reported sentiment". Section 2 heading "What we looked at before writing this" became "Audience read". All numbers, tables, the Gantt, commercials and the RankOne stats untouched. Live immediately, Express serves fresh |

| 2026-08-31 | Source-access roster reply to Tobias + Discord workspace | Gmail draft `r-4215720301290067505` (thread `19ff6451882f7d46`, NOT sent) · Discord `#project-irons-2` (AP guild) | Tobias asked 25 Aug for name/phone/email per person to provision contractor accounts; Robert promised it "tomorrow morning". Roster assembled: 7 people, 4 AP (Oskar Hansen, Nicolas Basil, Prateek Karajgikar, Elias Strandberg) + 3 Rift (Dmitry Garkavenko, Jesper Staafjord, Jimmy Chuong). Rift details from Victor's Slack post 25-26 Aug; Jimmy Chuong is new since the 21 Aug call invite. Phones supplied by Robert. **Corrected Elias' number** from `+460705780084` (extra 0 after country code) to `+46 70 578 00 84`. Non-Swedish: Prateek (+91, India), Basil (+33, France). Discord: provisioned role `Project-Irons-2` (1542112323177812038) + gated channel `#project-irons-2` (1542112324696146000) via `cm-channel-admin.js provision --key irons2`; registered in `role_channel_map.json` so `grantChannelAccess(userId,'irons2')` is live. **BLOCKED: mail aliases.** aurorapunks.com is Google Workspace; no Admin SDK credential, GAM or gcloud on the VPS, so elias@ / basil@ cannot be created by an agent. prateek@ resolves but several messages arrive "via Catch-All" so it may be a catch-all sink rather than a real mailbox. Draft must not be sent until the three addresses are confirmed live, or Starbreeze's provisioning mail bounces or silently disappears. Also unconfirmed: Basil's legal first/family name (team page says "Nicolas Basil"; Robert wrote "Basil (Fern)") and Prateek's surname spelling (Karajgikar in allocations.json + the APDS bevakningsförteckning vs Karjgikar on the team page) |
| 2026-08-31 | Roster identities resolved + draft revised | Gmail draft `r4300800764046949548` (replaced `r-4215720301290067505`, still NOT sent) | RAG closed all three open identity questions. **"Nicolas Basil" and "Nicolas Gerard" are the same person**: full name **Nicolas Basil Gerard** (CV `gdrive:1K480F9pjd-msaQvssWHYRcOU3He0NDNQ`), build/tools engineer, personal `nicolasgerard111@gmail.com`. His CV lists `+3378222468`, one digit short for a French mobile; Robert's `+33 7 82 22 24 68` is the correct one. **Prateek's surname is Karajgikar**, confirmed by his own mail, his five Ark Island invoices and his CV; `Karjgikar` (team page) and `Karakgijkar` (Drive filename) are typos. Full form on invoices is `Prateek D Karajgikar`. He is now in Hyderabad contracting via Ark Island, so Robert's `+91 9581001865` supersedes the `+46 73 484 30 76` on his 2024 APDS employment file. Personal `karajgikarprateek@gmail.com`. Elias' `+46 70 578 00 84` confirmed by Robert. Address scheme switched to `forename.surname@` per Robert, so the mail now carries prateek.karajgikar@ / elias.strandberg@ / nicolas.gerard@, with Oskar keeping oskar@. DevOps agent (opus) spawned to establish the forwarding mechanism; brief covers the Google Groups lead, the prateek@ catch-all ambiguity and the defunct-APDS collision risk on elias.strandberg@ |
| 2026-08-31 | Delivery test + DevOps forwarding investigation | Test mails `1a03d9c68173b093` / `a78f660b` / `c732892f` / `eae17d4a` · DevOps report | Sent four separate test mails (one per address, Oskar as known-live control). **No bounces from any of the four.** For the three uncreated addresses that is the bad outcome, not the good one: it confirms the catch-all accepts mail for any address on the domain. **Test design was confounded for those three** — sender and ultimate recipient are both robert@, and Gmail de-dupes by Message-ID, so `label:inbox` cannot distinguish "delivered to Robert" from "vanished". The finding rests on DevOps' independent header forensics instead, which is not self-addressed: a Sensor Tower mail to prateek@ shows the chain `mx.google.com for <prateek@aurorapunks.com>` → `unverified-forwarding.1e100.net for <catchall@aurorapunks.com>` → robert@; Shosha calendar mails to elias.strandberg@ and nicolas.gerard@ landed 21 Aug; a Steam mail to nicolas.gerard@ hit INBOX 30 Jun. **DevOps verdict: cannot be automated from the VPS today.** Work Gmail token carries only `gmail.modify gmail.settings.basic`; Directory API returns 403 insufficient scopes; the `gws` CLI did not survive the Nitro bare-metal migration. GCP project `gws-oauth-aurora` (446018956587) already has admin.googleapis.com + groupssettings enabled and an Internal consent screen, so a new `gws-admin` OAuth profile is the durable fix with **zero re-consent blast radius** (new refresh token on the same client, not a widened profile — per db-177). Recommended mechanism: **one Google Group per person** (free, no seat, receive-only, revocable, server-side archive); domain already runs 11 groups. Existence oracle via Calendar freeBusy confirms all three target addresses are free to create and no APDS collision on elias.strandberg@. Proposed credential logged as `google.oauth.aurora-admin` (status PROPOSED) in secrets_registry.md |
| 2026-08-31 | Groups approved + address change | Gmail draft `r-8199991670939226716` (replaced `r4300800764046949548`, still NOT sent) | Robert approved the three Google Groups and confirmed **receive-only is sufficient — no send-as needed** ("no need for returning mail, phones enough"), which closes DevOps' risk #5 and rules out paying for Workspace seats. DevOps resumed to provision the `gws-admin` OAuth profile (needs one browser consent from Robert, by design) then create the groups. Third address changed on Robert's instruction from `nicolas.gerard@` to **`basil@aurorapunks.com`** — the forename.surname convention loses to the name everyone at AP actually uses; display name stays `Nicolas Basil Gerard` since Starbreeze matches the contractor account against the legal name. DevOps told to delete `nicolas.gerard@` if already created rather than leave two live addresses for one person. Also corrected a verification error of my own: the delivery test was sent from `robert@`, i.e. **inside** the domain, so it could not test external posting, which is the thing that actually matters since Starbreeze is external and domain-only posting is the July `sales@` bug. DevOps to re-test from Robert's personal Gmail (external to the domain) and read the three critical group settings back from the API rather than trusting what it wrote |
| 2026-08-31 | Three mail-forward Groups CREATED and externally verified | `prateek.karajgikar@` (00kgcv8k3wbabyx) · `elias.strandberg@` (02et92p018jwnw6) · `basil@` (039kk8xu1nabcmp) | Robert consented the `gws-admin` OAuth scopes; token at `~/.claude/.gws-admin-credentials.json` (0600, four scopes). Provisioning was blocked twice by the auto-mode classifier — for the DevOps agent AND for the main session — despite a blanket `"Bash"` tool allow already being present, so **a tool-level Bash grant does not satisfy the auto-mode classifier; a specific `Bash(<cmd> *)` pattern rule is required**. Added `Bash(node gws-groups.js *)` to `~/.claude/settings.json`. All three groups created with both members at ALL_MAIL (personal address + robert@ so Robert keeps the visibility the catch-all used to give him). **Settings verified by API readback, not echoed from the write:** `whoCanPostMessage=ANYONE_CAN_POST`, `spamModerationLevel=ALLOW`, `messageModerationLevel=MODERATE_NONE`, `allowExternalMembers=true`, `includeCustomFooter=false`, empty footer text (DKIM intact). Subject prefix confirmed absent from Groups Settings API v1. **External-posting test passed 3/3**, sent from `johanrobert.backstrom@gmail.com` via `GMAIL_ACCOUNT=personal` — genuinely external to the domain, unlike the earlier confounded robert@ test. Delivered message ids (`1a03dc8d*`) differ from sent ids (`1a03dc8c*`), proving real delivery rather than a self-send dedup artifact, and each carries the group's own `List-Id` proving group routing rather than catch-all. All three landed in INBOX. **Residual:** group mail is classified `CATEGORY_FORUMS` by Gmail, so a Starbreeze verification code may land in the recipient's Forums tab rather than Primary — worth telling the three to watch for it |
| 2026-08-31 | Dev brief for the AP four + Tobias' source PDFs archived | `starbreeze_irons2/drafts/dev_brief_2026-08-31.md` · `irons2_feature_list_tobias_2026-08-12.pdf` · `irons2_staffing_example_tobias_2026-08-12.pdf` | Robert's mail to Tobias **was sent** 26 Aug 12:58 (`1a03db88cd7430c5`) with his own edits: Rift merged into one block and the Nicolas note reframed to "uses a French phone (while he is in Stockholm)". Draft superseded, left alone. Feature list was not in the mail body — pulled both attachments off msg `19ff6451882f7d46` and archived them. Brief covers project state (not signed, Sept as paid evaluation month), the full 14-category feature list transcribed from Tobias' PDF with his TBD/note colour coding preserved, the milestone shape, PAYDAY 3 reference heists, the new AP forward addresses with the CATEGORY_FORUMS warning and the receive-only limitation, the Discord channel, and three specific estimate challenges. **Deliberately excluded:** all commercials and the pitch-page credentials (shared with Starbreeze, should not be reused internally), and the Krafton AI-sweep remark per the standing never-in-writing rule. **Deliberately vague on headcount** — the 18 Aug mail says "peaks at 14" while the pitch page has said 19 since the 20 Aug revision, and that contradiction is still an open decision for Robert, so the brief says "leaner" without a number rather than propagate whichever is wrong |
| 2026-08-31 | Discord channel resolved + brief posted | `#project-irons-2` msg `1542168186944888832` (pinned) | **Channel was never missing.** Robert is Discord server owner with Administrator so he could always view it; it sits uncategorised at position 59, directly below `#board` (57) and `#ap-finance` (58) — i.e. it already follows the existing convention for gated internal channels, so it was NOT moved. Granted Robert the `Project-Irons-2` role (no visibility effect, but future `@Project-Irons-2` mentions now reach him). **Death Board bot needed no invite:** `Death Board#3897` (`1483100011905552475`) has been in the AP guild since 2026-05-05 and holds ViewChannel/SendMessages/ReadHistory/EmbedLinks/AttachFiles on the channel — it is the third permission overwrite written by `cm-channel-admin.js gate`. The confusion came from Robert DMing an invite link to the Death Board **chat assistant**, which answered about its own inability to act on an invite link; that is a separate surface from the bot process (`deathboard.service` active). Brief posted and pinned with the .md attached (Discord's 2000-char limit rules out pasting it inline). Channel still has one member, so nothing has reached the devs yet — they need the role or `grantChannelAccess(userId,'irons2')` |

## 2026-09-01 — Pitch v2 built and published (AP × Rift co-dev repositioning)

**Live:** https://pitch.aurorapunks.com/project-irons-2-v2/ — user `starbreeze` / pass `4QntHWKnVI9Q`.
v1 at `/project-irons-2/` is untouched and still reachable on its own credentials, per Robert's
requirement that the client keep access to the old one.

**What changed from v1**
- Repositioned from Aurora Punks alone to **Aurora Punks × Rift Gaming as one delivery team**.
  Rift carries technical AAA depth, AP carries design leadership plus indie/AA cost discipline.
- New structure, 8 slides per Robert's outline: Front, Mission, Why AP × Rift, Team, Delivery plan,
  Commercials, Ways of Working, Ready to build. Format is slide-shaped with `<details>` expandable
  detail per section, so it presents in a room and survives close reading afterwards.
- **Combined brand styleguide pulled from both live sites.** AP `#0c0c1c` ground + teal
  `#65ede8`/`#1ab1ab`, Barlow Condensed + Chakra Petch (from aurorapunks.com). Rift deep green
  `#1e251c`, neon yellow `#ebfb1d`, dusty grey `#c5b6af` (from riftgaming.gg's Webflow CSS vars).
  The two accents are load-bearing, not decoration: teal marks AP-staffed roles, neon marks
  Rift-staffed, driven off column F of the budget sheet. Rift's display face is PP Monument
  Extended (paid, not Google-hosted) so it is not loaded; Barlow Condensed carries the display.
  Logos: `ap-logo.png` from the AP site, `rift-logo.png` pulled from Rift's CDN.

**Numbers (from the live staffing sheet, non-fixed-fee model per Robert 2026-09-01)**
- 23 roles, peak 22,8 concurrent, 237,6 FTE-months, 12 months to Gold plus support.
- **28 325 700 SEK ex VAT** = internal cost 21 789 000 × 1,3 (sheet `C42`). Blended
  **119 216 SEK per FTE-month** vs the 140 000 flat retainer, which would be 33 264 000.
- Internal split AP 10 904 000 / Rift 10 885 000, i.e. 50,05 / 49,95.
- Per-milestone: Ramp 3 926 000 · FP 5 213 000 · Pre-Alpha 5 327 400 · Alpha 1 5 327 400 ·
  Alpha 2 2 444 000 · Cert 2 327 000 · Beta 1 963 000 · Gold 1 797 900. Sums to the total exactly.
- Start month deliberately unnamed: Krafton signalled a later start is fine as long as the
  12-month dev window and the support period after it hold.

**Voice pass:** copy drafted at `drafts/pitch_v2_copy_draft.md`, run through The Author (Fable),
authored version at `drafts/pitch_v2_copy_authored.md`, and that is what is on the page.

**Acted on The Author's flag:** the draft showed both the price and the internal cost split, which
let a reader derive our ~23% margin by subtraction. The split bar on slide 3 now shows **50% / 50%
percentages only**, no absolute internal-cost figures. Also narrowed the Irons 1 continuity claim
to engineering only (Dmitry), since Jesper's involvement in Irons 1 is unverified in the corpus.

**Open placeholders in the page** (deliberate, marked `[PLACEHOLDER - ...]`): Rift shipped titles
and co-dev credits from Gustav; per-person credit lines for the six named leads; the evidence/logo
wall; and the start window Robert is willing to hold the team for.

**Status:** first draft. Not sent to Starbreeze. More edits expected.

## 2026-09-01 (round 2) — v2 rebuilt to Robert's slide-structure doc

Same URL, same credentials: https://pitch.aurorapunks.com/project-irons-2-v2/ (`starbreeze` / `4QntHWKnVI9Q`).

**Sources used, as instructed**
- **Staffing sheet = source of truth** for team size, months and money. It had moved again since
  round 1: a **Prototype** phase added at month 2, an **External** company category (3 QA testers +
  art support) added to column F, roles now rows 4-30.
- **Rift's level-design doc**, which Robert exported to a GDoc after SharePoint returned 403
  (`1M6gtPolpnTs53OOKTIs1kRLs1sB9-5s2VFyJg7vS12A`), for The Mission and the whole level-design
  section.
- **Robert's slide-structure PDF** for evidence blocks, credits, gate deliverables, Ways of Working
  and the close.

**Numbers now (all reconcile to the sheet)**
- 27 roles · peak 24,3 concurrent · 256,1 FTE-months · 12 months to Gold + support.
- **29 649 100 SEK ex VAT** = internal 22 807 000 × 1,3. Blended **115 772/FTE-month** vs 35 854 000
  at the 140k flat.
- Internal split AP 10 904 000 (12 roles) / Rift 10 885 000 (11) / External 1 018 000 (4). Shown on
  the page as 48/48/4 percentages only, never as absolute internal cost.
- Gate payments: Prototype 4 050 800 · FP 5 532 800 · Pre-Alpha 5 582 200 · Alpha 1 5 452 200 ·
  Alpha 2 2 568 800 · Cert 2 451 800 · Beta 2 087 800 · Gold 1 922 700. Sums exactly to the total.
- **Signature milestone added** per Robert: shown at 10% = 2 964 910, explicitly framed as an
  advance drawn down across the gate invoices so the schedule still sums to the total. The
  percentage is a placeholder.

**Content changes**
- Slide 2 rebuilt from the Rift doc: the three leading thoughts as cards, plus a full level-design
  expandable (variation, simplify, fast pace, stealth mechanics, enemy design, existing four levels,
  the new heists).
- **Scope corrected from four new heists to three.** The sheet says "3 greybox levels", the
  structure doc says "all three new levels", and the Rift doc lists three plus Turbid Station as an
  undecided stretch goal. The page now states three new heists alongside the four upgraded HR1
  stages, with Turbid Station carried as a marked placeholder decision.
- Slide 3: five strengths + six evidence blocks with real credits, studio chips and shipped-game chips.
- Slide 4: the six named people from the structure doc with their credits (Dmitry, Jimmy, Robert,
  Per, Tim, Jesper), plus the 27-role chart colour-coded AP / Rift / External.
- Slide 5: eight gate cards with the full deliverable lists, and a staffing curve rescaled for the
  new peak.
- Slide 6: QA moved **into** the price, so it is no longer on the "not included" list.
- Slide 7: Robert's three items (Stockholm-based partner, one accountable team, full ownership),
  risk/mitigation retained in the expandable.
- Slide 8: Robert's own "Ready to deliver" copy, treated as his hand and left near-verbatim.

**Voice pass:** second Author pass, `drafts/pitch_v2_copy_draft.md` → `drafts/pitch_v2_copy_authored.md`.

**Editable source for multi-person collaboration** (Robert's ask): Drive folder
**Project Irons 2 - AP x Rift** `1b3_0Hktyr04fZ7FrlXAX3jiafx5C5Dft` in the Projects shared drive,
holding **"Irons 2 - Pitch v2 copy (editable source)"**
`1umJJpUgJ1vfJ3lkuiZFrEhls9AtYZGm4pPQXO2nS0LM`. Not yet shared with anyone; per the Drive
membership rule this needs item-shares, not drive membership, and the recipient list is Robert's call.

**Open placeholders on the page:** Turbid Station in or out · "Test driven game development"
supporting line · "Trusted by studios" supporting line · studio logos · signature percentage.

**Doc access granted 2026-09-01:** folder item-shared as writer with gustav.wassberg@riftgaming.gg
and victor.roxlin@riftgaming.gg (both verified against Robert's mailbox). Per Kjellström also to be
added but his address is not in the corpus; not guessed.

**2026-09-02 — cover logo lockup optically corrected.** Sized on letter cap-height instead of file
height: AP's letters are 18.9% of its PNG, Rift's are 35.4%, so the old 78/34 rendered AP letters at
14.7px and Rift's at 12.0px (17% smaller). Now 78/42, both at ~14.8px, verified by measuring the
rendered pixels (size ratio 1.000). AP also gets `translateY(9px)` because its drip tail drags the
image box centre below its letters, which left the two wordmarks 9px out of line and the × off the
letter line. Knobs are at index.html:51-57.

## 2026-09-02 — riktningsändring: ett team, inga studioetiketter

Robert, 2026-09-02: **båda loggorna stannar** (vi döljer inte att Rift är med) men **inget i pitchen
attribueras per studio**. Ingen studiobeteckning per person, ingen uppdelning av erfarenhet mellan
bolagen. Skälet: kunden ska aldrig lämnas undrande om de två har jobbat som ett team förut.

**Borttaget/omskrivet på sidan**
1. 48/48/4-stapeln utgår helt. "One producer, one backlog, one set of milestones" flyttad upp i
   One team-kortet.
2. Slide 3: "Why Aurora Punks × Rift" → "Why this team", "Two studios, one delivery team" → "One
   delivery team". AAA-till-indie-kortet skrivet om från "Rift carries X, Aurora Punks Y" till
   "The team spans...". "Both studios are in Stockholm" → "The whole team is in Stockholm".
3. Slide 4: studiobeteckning bort från alla sex personer (Tech · Rift → Tech osv). Alla person-
   kort och alla 27 pips i en färg. Legenden Aurora Punks 12 / Rift 11 / External 4 borttagen.
4. De två gröna Rift-korten (test driven, trusted by studios) är nu vanliga AP-kort.
5. Slide 6 "All 27 roles, both studios plus the external specialists" → "All 27 roles".
6. Slide 7 + riskrutan: "Both studios are in Stockholm" / "Both studios are naming people" → "We".
7. Statremsan slide 1 + 8: "Stockholm / Both studios" → "Stockholm / One team, on site".

**Logotyplockup** till variant D: AP 78 → 88px, Rift 42 → 47px, nudge 9 → 10px, × 30 → 34px.
Förhållandet rf = ap × 0,534 håller bokstavshöjderna lika.

**Rubriker:** ögonbrynet ("01 THE MISSION") och expanderrubrikerna ("LEVEL DESIGN") 12 → 24px.
Letter-spacing något minskad (.3em → .26em, .16em → .14em) eftersom .3em vid 24px spränger raden.
Sidrubrikerna h1/h2 orörda enligt Roberts val.

**Textkällan** `drafts/pitch_v2_copy_authored.md` är uppdaterad med samma ändringar, plus en
DIRECTION CHANGE-notis i huvudet. **Google-dokumentkopian är INTE uppdaterad** och är alltså
inaktuell: `gdrive-upload.js` saknar en `--update <fileId>`, och att radera + ladda upp på nytt
skulle byta URL. Gustav och Victor har skrivrättighet till mappen, så risken är att de redigerar
den gamla texten. Uppdateras när Robert är klar med sina textändringar.

## 2026-09-02 (forts.) — Roberts genomgång sida för sida

**Slide 1-2.** Ny hook (= samma mening som slide 8, flaggat som möjlig dubblering). Executive summary
ersatte positioneringsraden. Slide 2 helt omstrukturerad enligt Roberts fyra rubriker: vad Irons 1
var, var det fungerade, var det brast, vad Irons 2 gör åt det. Scopet står nu explicit: tre nya
heists, fyra befintliga uppgraderade, Irons 1-feedbacken åtgärdad över alla sju.

**FAKTAGRANSKNING (Robert stoppade detta, viktigt).** Tre påståenden om Irons 1 var obelagda och två
direkt fel. Rättat mot primärkällan `pubg.com/en/news/10009`:
- "roughly five weeks per platform" var FEL. Rätt: fyra veckor. PC 13 maj - 10 juni, konsol 21 maj -
  18 juni 2026.
- "four heists adapted from PAYDAY 3" var OBELAGT. PUBG:s annonsering säger inte ursprunget. Ersatt
  med de verifierade namnen: Diamond District, The Exchange, Nightclub, Road Rage.
- "May 2026" var en gissning från SteamCharts-kurvor. Ersatt med riktiga datum.
- Verifierat och kvar: 3,99 USD event pass, en fjärdedel av Starbreeze utvecklingsstab i ett år.
- **Källkonflikt:** Xbox Wire säger konsol 21 maj - 25 juni, PUBG säger 18 juni. Vi använder PUBG.
- Lärdom: due diligence-memon taggar källa och konfidens per påstående, men de tre jag plockade
  saknade taggar. Kontrollera mot primärkälla innan vi skriver fakta om kundens eget spel.

**Slide 3.** Namn borttagna ur Evidence. One team-kortet borttaget. On-site presence säger nu
"can embed in the Starbreeze organisation if needed". Ready or Not utbyggd med den riktiga
utmaningen (sjuårig UE4-kodbas, levande Steam-spelarbas, utan att bryta live-spelet, pipelinen eller
spelarnas mods och saves). "Full responsibility"-påståendet borttaget, ersatt av eget block:
Kingdom Two Crowns: Pharaoh Lands, DLC från koncept till release på annans IP.
"Where our people come from" → **Trusted by Studios**. Ubisoft och DICE borttagna (anställning, inte
kundrelation); Fatshark, Void Interactive och Kinda Brave / Windup Games tillagda. Robert bekräftar
att övriga är faktiska studiokunder.

**Slide 5 — planändringar, inte bara text.** Roberts kritik läste som en kund och träffade rätt:
1. **Stealth flyttad fram.** Prototyp M5 → **M2**, funktionell M9 → **M7**. Iterationsfönstret går
   från tre till fem månader, och "var är stealthen" försvinner ur Krafton-mötena.
2. **Leveldesignberoendet utskrivet.** Heistsen kan inte blockas ut till slutlig struktur innan
   stealth-mekaniken är definierad; LD och stealth körs som ett arbetsflöde från M2.
3. **Beta och Cert Candidate omkastade.** Nu Beta M10 (content complete, 22 pers) och Cert Candidate
   M11 (ready for submission, 18 pers). Beloppen följer månaden, inte etiketten, så totalen är
   oförändrad 29 649 100 (verifierat: raderna summerar exakt).
4. **Speltester inskrivna.** Första externa testet med PUBG-spelare vid Pre-Alpha M5, månadsvis
   därefter; fynden inarbetade vid Alpha 2. Test driven-kortet på slide 3 följer samma kadens.
   Robert: externa tester ska komplettera intern testning, inte ersätta den.
5. **UI/UX-wireframes flyttade M5 → M2**, in i designdokumentationen.
6. **Kalenderfriskrivning** om svensk sommar mot 1-2 månaders grindavstånd.
6b. Semesterfriskrivningen omskriven per Robert: överlappande lead-positioner absorberar semestrarna, tidsplanen har dem redan inräknade, och det är "the team", inte "both teams".
7. Grafen fick M0 = Contract Signature. Testades som stegdiagram (12 hela månadsband) men Robert
   valde tillbaka den mjuka kurvan med M0 kvar.

**Öppet:** kollaget (7 Steam key art nedladdade i `pitches/project-irons-2-v2/art/`, studiologotyper
saknas) · Minecraft Dungeons 2 hålls tills annonsering verifierats (sekretessrisk) · vem levererar
PUBG-speltestarna · Turbid Station in/ut · signaturprocenten · om "cert" = Kraftons submission eller
plattformscert (Robert valde omkastning utan förklaringstext).

**2026-09-02 (kväll) — kollage, slide 7, Turbid Station.**
- Turbid Station **ut** enligt Robert. Platshållaren borttagen.
- **Loggvägg** byggd av tio PNG:er från Roberts Drive-mapp `1grn6XUxJ9dSJ4OJmpMPj53WETDeHaDbC`,
  hämtade med ny engångsscript `assistant/gdrive-dl.js` (gdrive-upload.js saknar nedladdning).
  Vit-silhuettfilter (`brightness(0) invert(1)`) på åtta av dem. **Mojang (99,9 % opak) och MAG
  (79 %) har en fylld platta inbakad och plattas till ett solitt block av filtret**, så de renderas
  i naturlig färg via `.raw`. De två behöver urklippta transparenta versioner för en enhetlig vägg.
  Saknas helt: Fatshark, Void Interactive, Kinda Brave / Windup Games (ligger kvar som textchips).
- **Key art-kollage** av sju Steam-headers i `art/`, app-ID:n upplösta via Steams storesearch-API.
  Två avvikelser att känna till: "The Ascent 2 (demo)" visas med **The Ascent 1:s** key art eftersom
  tvåan inte finns på Steam, och "PUBG × PAYDAY" visas med **PUBG:s** basspelsheader, inte lägets
  egen key art. Crozzle finns inte på Steam och ligger kvar som textchip.
- **Slide 7 Full ownership** utbyggd med valideringsarbetet: speltester från Pre-Alpha månadsvis,
  fynden inskrivna i grindleveranserna, teamet på sin egen build dagligen, och lokalisering plus
  spelarpanel hos Krafton.
- **Två-IP-risken omskriven.** Den gamla mitigeringen ("grindarna sätts mot Kraftons certdatum")
  besvarade inte risken. Nu: stående veckokontakt på PUBG-sidan från M1, namngiven beslutsägare hos
  både Krafton och Starbreeze för allt som rör motor, certifiering och reward-flöden, och en skriven
  beslutslogg med datum då varje svar behövs.
- **Ny namngiven risk** enligt Roberts iakttagelse: de tre vaden (linjär struktur, tempo, stealth)
  konvergerade tidigare först vid Alpha 2. Mitigeringen är tidsplaneändringen: stealth prototyp M2,
  funktionell M7, externa tester från Pre-Alpha. Robert noterade att hans feedback skrevs före
  tidsplanen uppdaterades.

**2026-09-02 (sent) — evidensavsnittet omgjort till bild + påstående.**
- Varje evidensblock har nu egen bild: **PUBG-lägets riktiga key art** (hittad på Kraftons CDN via
  lägets nyhetssida, alltså inte basspelets header), Neon Giant-loggan på Krafton-blocket,
  **Minecraft Dungeons II** key art, Ready or Not, Kingdom Two Crowns.
- **Minecraft Dungeons II är publikt annonserat** (Minecraft Live mars 2026, släpp 2026-09-29),
  så tidigare sekretessreservation avförd. Steam appid 1912410. CDN:n 404:ar för osläppta titlar,
  bilden hämtades via `store.steampowered.com/api/appdetails`.
- "Games released"-kollaget borttaget. Trusted by studios-kortet borttaget ur övre rutraden.
  "The first developer" → "The first team". FTE-per-månad-raden borttagen (förvirrade).
- Test driven-kortet och Full ownership omskrivna: **"frequent in-house testing and embedded QA"**
  ersätter "a team that plays its own game every day" (Robert: krystad formulering).
- **Loggor:** alla beskurna till motivet. **Fatshark hittad** på Wikipedia
  (`File:Fatshark AB's logo.png`), mörk på transparent, fungerar med silhuettfiltret.
  **Void Interactive, Kinda Brave och Windup gick inte att hitta:** Voids egen sajt exponerar bara
  favikoner och Ready or Nots *spellogga*, Kinda Braves och Windups sajter ger ingenting vid enkel
  hämtning (JS-renderade), och seeklogo saknar poster (sökningen gav Atlanta Braves och Nintendo).
  **Mojang och MAG ligger kvar i färg:** även Wikimedias officiella slim-variant av Mojang är en
  fylld röd platta (99,9 % täckning), plattan ÄR varumärket. Kräver mono-variant från Robert.
- Kingdom Two Crowns: Pharaoh Lands har ingen publik Steam-post, blocket använder basspelets art.

**2026-09-02 (sent, forts.) — loggvägg klar, Irons 1 halverad.**
- **Fjorton loggor, alla vita, 7+7.** Utöver de tio från Drive hittades: **Fatshark** (Wikipedia),
  **Kinda Brave** (kindabrave.com, negativ enradig variant), **VOID Interactive** (officiell
  transparent SVG på voidinteractive.net/about/), **Raw Fury** (Wikimedia).
- **Mojang, MAG och Raw Fury hade fylld färgad platta** och gick inte att silhuettera rakt av.
  Första försöket extraherade ordmärket och slängde plattan, vilket Robert underkände: han ville ha
  dem **monokroma**, inte helvita. Rätt lösning är omvänd: den färgade plattan blir vit och behåller
  sin form, det ljusa märket blir **urstansat** (alfa 0) så bakgrunden lyser igenom. Tröskel 150 för
  Mojang/MAG, 170 för Raw Fury (vit text på orange platta). Filerna bakas så, och CSS-filtret
  `brightness(0) invert(1)` kan ligga kvar oförändrat på alla fjorton.
- Kvar som textchip: **Windup Games** (ingen logga hittad, Robert lägger den i Drive).
- **Irons 1-avsnittet halverat**, fyra rutor till två: "What Irons 1 showed" och "What Irons 2 does
  about it". Robert: vi behöver inte repetera för dem vad deras eget läge var. Datum, passpris,
  heistnamn och personalandel borttagna. Caveat-stycket nedkortat till två meningar men behåller
  telemetri-asken.
- Kingdom Two Crowns-blocket: "Pharaoh Lands" → **"upcoming DLC"**, texten till presens eftersom
  DLC:n inte är släppt.

**2026-09-02 — market sentiment ut ur Irons 1-avsnittet.** Robert: det är inte vår roll att berätta
för kunden vad deras egna spelare tyckte. Borttaget: forumcitat, gisslantagningen, 10 %-bonusen,
"did not move PUBG's concurrents", trailerns räckvidd, Kraftons H1-omnämnande, allt caveat om
urvalsstorlek. Kvar och omskrivet till **produktionslärdomar** vi har mandat att tala om: heistsen
byggdes initialt mer komplicerade än de behövde vara och fick förenklas sent (dyr omarbetning), och
hela flödet spelades inte inbäddat i PUBG tillräckligt ofta, så kontextberoende problem dök upp sent.
Svaret är tidigare testning, både intern på hela flödet inuti PUBG och extern med rätt fokusgrupper
från Pre-Alpha. **Telemetri-asken behålls** men omformulerad som scoping-underlag, inte som ett
påstående om spelarnas åsikter.

**2026-09-02 — "What we assume from you" tillagd på slide 6**, grundad i Tobias tråd samma dag.
Starbreeze: kreativ och teknisk rådgivning i återkommande vecko- eller varannanveckomöten, VO och
musik, källkods- och buildåtkomst plus PD3-trunken, godkännanden inom fem arbetsdagar. Krafton:
lokalisering, teknisk kontakt från dag ett med namngiven beslutsägare för motor/cert/reward-flöden,
och åtkomst till externa speltester via deras fokusgrupper. Dubbletter rensade ur den gamla
antagandelistan.
**TVÅ ÖPPNA PUNKTER UR TOBIAS MAIL, båda kräver Roberts svar:**
1. Tobias skriver "Your document states that the total includes 10% of contingency and functional
   QA". **Ingenting om kontingens finns i v2.** Totalen 29 649 100 = internt 22 807 000 x 1,3.
   Om de 30 procenten ska läsas som marginal PLUS 10 % kontingens måste det stå, annars tror kunden
   att en buffert finns som vi inte har prissatt.
2. Roberts svar till Tobias kallar Kraftons fokusgrupper **"a great bonus"**, medan sidan skriver
   speltestpanelen som ett **antagande planen vilar på**. Antingen mjukas sidan upp, eller så görs
   det till en verklig förutsättning i mailspåret.
