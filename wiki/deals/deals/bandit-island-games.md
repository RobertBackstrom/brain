---
type: deal
company: Bandit Island Games AB
slug: bandit-island-games
project: aurora_punks
status: Evaluating
priority: high
country: Sweden
size: small
last_activity: 2026-09-16
network_strength: warm
updated: 2026-09-16
---

# Bandit Island Games

## Snapshot
Stockholm studio, ~22 employees, founded 2022, office on Österlånggatan 43. Self-described as
"high-quality, IP-driven titles and original games for couch co-op, family fun, and next-gen
parties". Founded by ex-Bullfrog/King/Disney/Namco people. They build for **Amazon Luna
GameNight**, Amazon's phone-controlled party-game tier, where they have two quiz titles in
development including a **Jeopardy!** game. Target release February 2027; nothing is public yet. Robert has a personal-friend tier relationship with Stephen Jarrett.

**Live opportunity as of Sep 2026: console porting.** Inbound from Stephen 2026-09-10 asking
either for help estimating developer-months or for AP to take the porting job. This is now the
primary deal; the older Elias audio-middleware intro track is dormant underneath it.

## Key People
- [[../contacts/stephen-jarrett]] - Co-founder & CEO, stephen@bandit-island.com. Personal-friend tier. Made the inbound ask.
- [[../contacts/robert-woodburn]] - Co-founder ("Woody"), woody@bandit-island.com. Signed the NDA, owns the Amazon relationship, gates source access.
- Also on the mail thread: omar@, patrik@, patsy@, rebecca@bandit-island.com. Roles unconfirmed.

## Pipeline Status
Status: **Evaluating** - initial estimate delivered 2026-09-16, waiting on their Amazon approvals.

Track record on this deal: inbound Thu 10 Sep, office meeting Fri 11 Sep (Robert + Oskar Hansen),
mutual NDA signed the same day, estimate delivered Wed 16 Sep. Six days from first ask to a
costed proposal.

## What They Bring / What We Bring
**They bring:** two quiz titles in development for Amazon Luna, an Amazon relationship that
covers publishing support, and a February 2027 release target. A second title that runs on
the same codebase, so the expensive engineering is paid for once.

**We bring:** the porting capability they say is new to them, a porting lead who has taken Unity
titles through all three platform holders' certification, and a diagnosis of their actual problem
that they had not made themselves. The relationship is the way in; the technical read is what
makes us the vendor rather than a quote to compare.

## The Deal on the Table
Six SKUs (PS5, PS4, Xbox Series X/S, Xbox One, Switch, Switch 2). **3 684 000 SEK**, 30,7
FTE-months across five roles (Robert bills EP at 20 %), at the 120 000 SEK per FTE-month rate
he gave them in the office. Engine is Unity, confirmed at the meeting. Dec 2026 start, cert-ready Aug 2027, release-ready Nov 2027. Steam is theirs.

Pitch: https://pitch.aurorapunks.com/bandit-island/ (gated, creds in `assistant/pitch-auth.json`).
Full breakdown and the technical argument: [[../../../followups/bi-001-jeopardy-console-port-estimate]].
Project folder: [[../../../bandit_island/CLAUDE]].

**Why the number is not a normal porting number.** On Luna the game runs in Amazon's data
centre and the phone reaches it through the platform: QR scan, no app, no pairing, identical
across the GameNight library. Pairing and transport are Luna's, not the game's. On console none
of that exists, so the job is a port plus a feature build: room-code join, a companion web
client and a relay service, from nothing.

**Do not claim the speech recognition is Amazon's.** Corrected 2026-09-17 after Robert
challenged the provenance. We can evidence that voice arrives via the phone through the
platform; we cannot evidence who owns the recognition. It is now question 2 to the client and
an open item, not an assertion. Alternates were
priced openly in the pitch rather than hidden: second title 8 to 10 FTE-months, gamepad-only
~1,1 MSEK and explicitly not recommended.

## Activity Log
- 2026-09-16 - Estimate delivered as a gated web pitch; cover mail drafted on thread `1a0a9cb279aa62e5`. Woody replies 16:14 that Amazon talks are mid-flight, positive signals but nothing decided, and source access needs an approval tier cleared first. He expects news early w/c 21 Sep. Source: gmail thread `1a0a9cb279aa62e5`.
- 2026-09-11 - Office meeting, Österlånggatan 43, 15:00. Robert + Oskar Hansen saw the build. Mutual NDA signed the same day via Zigned (`RB_Bandit_Island_Games_NDAdocx.pdf`). Source: calendar invite from Stephen, Zigned confirmation.
- 2026-09-10 - Inbound from Stephen on LinkedIn: two quiz titles on Luna, considering PlayStation / Xbox / Switch / Steam ports, asking AP either to estimate developer-months or to take the job. Robert offers to come look at the project.
- 2026-05-06 - Personal-friend tier confirmed for the Elias audio-middleware intro; DM text in eli-007, Robert-handled. That track is dormant behind the porting deal. Source: [[../../umbrella/elias_bizdev/wave1_rolodex]].
- 2025-2026 - 39 LinkedIn DMs including dinner planning with Stephen + Vanessa. Source: [[../../agents/memory/bizdev_learnings]].

## Open Questions / Next Actions
- [ ] Source-code access, blocked on Amazon approval tiers. Everything downstream of it.
- [ ] How separable the Luna input layer is from game logic. Engine itself is confirmed Unity.
- [ ] Jeopardy! rights for console distribution, possibly scoped to Luna only. Not our work, on our critical path.
- [ ] Who publishes on console, Amazon or Bandit Island, and who holds the platform accounts.
- [ ] Confirm Amazon really covers QA and release management.
- [ ] Old-gen in or out. PS4 + Xbox One is the one line that removes cleanly.
- [ ] Light nudge to Woody at the end of w/c 21 Sep if nothing lands. A chase would be wrong here, the delay is genuinely Amazon's.

## Cross-links
- Project: [[../projects/aurora_punks]]
- Dormant track: [[../projects/elias]]
- Contacts: [[../contacts/stephen-jarrett]], [[../contacts/robert-woodburn]]
