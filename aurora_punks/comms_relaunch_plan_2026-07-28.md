# Aurora Punks - public relaunch plan, run-up to Pharaoh Lands (Oct 8)

**Date:** 2026-07-28
**Owner:** Robert | **Prepared by:** BizDev | **Ticket:** apb-040
**Status:** DRAFT for Robert. Nothing published, no accounts touched.
**Window:** 10 weeks. 2026-07-28 to 2026-10-08.

---

## 1. The situation

AP has been publicly silent since APDS went into konkurs in December 2025. On **8 October** Raw Fury announces **Kingdom Two Crowns: Pharaoh Lands**, and AP is credited (planning against that as a guarantee per Robert 2026-07-28).

That gives a fixed, external, third-party-validated date to aim at. The job in the next ten weeks is to make sure that when the announce lands, someone who searches "Aurora Punks" finds a company that is visibly working, not a company whose most recent public trace is a bankruptcy.

**Two audiences, two tracks, almost no shared content:**

| Track | Channel | Audience | Purpose |
|---|---|---|---|
| **A - B2B** | LinkedIn (Robert personal + AP company page) | Publishers, studios seeking co-dev, platform holders, talent, investors | Credibility and inbound BD |
| **B - Players/UGC** | AP Discord as landing page, fed by TikTok / IG Reels / YT Shorts | ARK: Survival Ascended mod players, old-IP players | A live community that is worth landing on |

Run them on one publishing rhythm but with separate calendars. Do not cross-post B2B craft posts to TikTok or mod clips to LinkedIn.

---

## 2. The three calls worth making up front

**1. Do not post a "we are back" statement.** It makes the bankruptcy the story and invites the question in the comments. Start shipping proof instead and let the Raw Fury credit do the talking. If asked directly, the plain line is: Aurora Punks AB is the live company, the development services subsidiary was wound down in December 2025, the team and the work continued. Never lead with it, never dodge it.

**2. Lead the B2B track from Robert's personal profile, amplify on the company page.** Robert's profile is warm, the company page is cold, and in this industry people follow people. Company page reshares and carries the assets.

**3. Oct 8 belongs to Raw Fury.** AP amplifies and adds the layer RF will not publish, which is how it was built. Do not compete with the reveal or pre-empt it.

---

## 3. Phase 0 - plumbing (Jul 28 to Aug 10, no posting)

Nothing public goes out in these two weeks. This is the part that is easy to skip and expensive to skip.

1. **Access audit.** Confirm who holds admin on the AP LinkedIn company page (`linkedin.com/company/aurora-punks/`), who owns the Discord guild (`616345869490454593`), and whether AP-controlled TikTok / Instagram / YouTube accounts exist at all. The last known CM was Elin Faskhoody in 2021, so assume nothing. **YouTube resolved (db-055, 2026-08-20):** channel exists — `@aurorapunks` / `UCN5MWCq05Yj47EELO6Pvo7w`, confirmed via YouTube Data API v3 (read-only, not scraped). 184 subs, 60 uploads spanning KreatureKind/Vessels of Decay/Sir Whoopass. Last upload 2025-06-27 — dormant, predates the konkurs. Existence is confirmed; **admin/posting access is still unverified** and remains part of this audit. TikTok/Instagram still open.
2. **Ask Raw Fury for the pack.** Pontus / Niclas: confirm the credit wording, the embargo (what AP may say and from exactly when), which assets AP may use, and whether AP gets a "developed by" line on the Steam page. This is the single biggest dependency in the plan.
3. **Make the Discord worth landing on before driving any traffic to it.** Driving short-form traffic into a dead server is worse than not driving it. Minimum viable: an ARK changelog channel fed by Elias' Phase 1 bug fixes, a public Magic Expansion roadmap, rooms for the back catalogue, clean roles and onboarding. CM agent owns this.
4. **Fix the LinkedIn MCP session** (DevOps, db-112 class). Currently down, which blocks page verification and scheduling.
5. **Add an Aurora Punks section to `skills/client_channels.md`.** AP has no entry today, which is why this plan starts with an audit instead of a calendar.

---

## 4. Track A - LinkedIn (B2B)

**Content pillars**, in the order they carry weight:

1. **Proof of delivery.** Pharaoh Lands is embargoed until Oct 8, so before that: Water Me & You (114K wishlists, EA Feb 2027), Tears of Adria, the publishing slate.
2. **Method.** How AP actually runs co-dev: the network model, a vetted senior bench stood up per project rather than a fixed headcount. This is the real differentiator and it is genuinely postable without naming clients.
3. **People.** Name the senior bench. Named people beat abstract seats, and it answers the "who would actually do this work" question before it is asked.
4. **Partner amplification.** Reshare Raw Fury, Shosha, Ark Island, Kinda Brave. Cheap, warm, and it puts AP back in adjacent feeds.

**Beats:**

| When | Beat |
|---|---|
| Aug 11 | First post. Not a comeback post. The co-dev network model, or the bench. |
| Aug 18 | Gamescom pre-post: AP is going, here is what we are looking for. Direct BD lead-gen. |
| Aug 25-29 | **Gamescom, Cologne.** Raw Fury party Aug 26 (k2c-028). Best single BD moment before October. Post live, meet people, follow up the week after. |
| Sep 1-28 | 1 to 2 posts a week. Method and people pillars. WMY wishlist milestone if one lands. |
| Oct 1-7 | Hold. Nothing that pre-empts the reveal. |
| **Oct 8** | Amplify RF's announce, then the AP post RF will not write: what the team built and how. |
| Oct 9-31 | Sustain 2 a week. Convert attention into BD conversations while the credit is fresh. |

Cadence: 1 a week from Aug 11, 2 a week from mid-September.

---

## 5. Track B - Discord and the short-form funnel

**The honest read:** the ARK: Survival Ascended mod community is the only live player audience AP has. Necrotic Dominion is around 10K downloads and ND: Armory around 16K on CurseForge, plus ARK: Sorcery Evolved. The old IPs (BlockEm!, Chenso Club, Ooglians, 1993) are dormant catalogue. So build the funnel on ARK and give the back catalogue rooms in the Discord rather than a content pillar of its own.

**Why this works right now:** Elias Strandberg started 2026-07-17 on the mod. Phase 1 is the bug backlog, and the top community pain is the console/PS5 and dedicated-server launch failure that has paying customers blocked. **Fixing that publicly is the content.** Phase 2 is the Magic Expansion, which is a roadmap the community can follow.

**Funnel:** short-form (TikTok, IG Reels, YT Shorts) to Discord as the landing page.

- **Production:** the reel pipeline already exists (`build_reel.py`, JSON config driven, built for ToA but reusable by swapping the config and game context). Content Editor agent owns production.
- **Source footage:** Elias plus the creator community.
- **Cadence:** 3 a week per platform once running, starting September.
- **Hooks that work for mod content:** before and after on a fixed bug, "this mod adds X to ARK", build showcases, creator reposts.
- **Creator program:** ARK creators get early access to the Magic Expansion. That is the supply side of the funnel and it costs nothing but coordination.

**Open decision for Robert:** post the ARK short-form under a **Necrotic Dominion** brand identity rather than Aurora Punks. Mod audiences follow the mod, not the studio, and it keeps AP's own channels B2B-clean. AP appears as publisher in the bio, and the shared AP Discord stays the single landing point for both. Recommended, but it is a brand call and it is yours.

---

## 6. Dependencies and risks

1. **Raw Fury embargo and credit wording.** Unconfirmed. Everything in October hangs on it. Ask this week.
2. **Account access.** Unknown for TikTok / IG / YT, assumed stale for LinkedIn. Phase 0 resolves it.
3. **LinkedIn MCP down.** Could not verify the AP page's actual last-post date for this plan. DevOps fix needed.
4. **Capacity.** Robert is the approval bottleneck. Production runs on Content Editor plus the reel pipeline, Discord on CM. Robert approves, does not produce.
5. **Entity hygiene.** Necrotic Dominion is contracted under CZP Holding AB dba Aurora Punks. Public posts use the Aurora Punks brand with no entity detail, and must never imply the bankrupt APDS.
6. **Erik / Behold timing.** A visible relaunch in September and October sits on top of a live control conversation. Momentum helps a valuation. It also raises AP's profile while ownership is unsettled. Robert's call whether that shapes the timing.

---

## 7. First five actions

1. Mail Pontus and Niclas at Raw Fury for the announce pack, embargo and credit wording.
2. Run the access audit on LinkedIn, Discord, TikTok, Instagram, YouTube.
3. Decide the Necrotic Dominion versus Aurora Punks brand question for the short-form funnel.
4. Stand up the Discord: ARK changelog, Magic Expansion roadmap, back-catalogue rooms, roles.
5. Draft the Aug 11 LinkedIn post and the Aug 18 Gamescom post.
