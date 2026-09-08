# Tuut cloud / telco distribution: portfolio + IP sourcing brief

**Date:** 2026-09-08
**Owner:** Robert
**Counterparty:** Robert Schmiedl, Managing Director, Tuut (robert@tuut.sk, +421 902 682 716, Discord roberttuut)
**Trigger:** Call held today, 2026-09-08 14:00, "Aurora Punks x TuuT, Cloud Gaming for telcos"
**Deliverable built:** https://pitch.aurorapunks.com/portfolio (gated, user `aurorapunks`, pass `dlXmpV4dJaLn`)

---

## 1. What Tuut is actually asking for

From Schmiedl's 1 Sep mail, in his own words: three of Tuut's existing partners have started
providing cloud gaming for telcos and TV set-top boxes, and "usually the integration is simple,
they just need a steam key and they can add the game to their cloud and offer it."

Two things follow from that sentence.

1. Tuut is an **aggregator, not the platform**. They sit between us and three unnamed operators.
   Worth establishing early who those three are, because we may already have a direct relationship
   with one of them (see section 2).
2. "They just need a Steam key" understates the integration. Every streaming licence Aurora Punks
   has actually signed asks for considerably more than a key, and that gap is where the work sits.
   The portfolio page now front-loads the real answer, which should save a round trip.

**History with Schmiedl.** Met at the SpielFabrique workshop, Africa Games Week, Cape Town, late
Nov 2024. The TuuTap track ran Dec 2024 through Jan 2025 and stalled: he wanted vertical 9:16
gaming, and Hooja, Block'Em! and Iron Evil are all landscape. His own note then was that Block'Em!
"could be re-iterated to a TOP DOWN or BOTTOM UP direction and it would be great, probably the best
fit", and that Hooja "could be a good game for our standard distribution as is". Robert also
introduced him to Behold (Lina, Binni, KM) in Jan 2025.

**Read:** this cloud-gaming approach is the *landscape-friendly* version of the same relationship.
The genre objection that killed TuuTap does not apply here. That is why it reopened.

---

## 2. We have done this before, and it matters commercially

Three prior agreements set the reference points. All are in Drive and indexed.

| Counterparty | What it was | Terms we accepted | Status |
|---|---|---|---|
| **KT Game Box** (Korea Telecom) | Telco cloud streaming, Korea | Contract signed Nov 2021 for **1993 Space Machine, TaniNani, Hoplegs** | Signed and returned by KT. Exactly the deal shape Tuut is describing |
| **Blacknut** | SVOG cloud subscription, worldwide | **70% of Net Revenue x time-spent share**, worldwide **non-exclusive**, 2-year term auto-renewing | Licensor on the paper is **White Lines Black Spaces AB**, now bankrupt. Term ran from May 2023. Treat as lapsed, but verify |
| **Plug In Digital** | PC digital distribution | Ludovic Reimonenq. Robert proposed **Distant Bloom, Go Fight Fantastic, KreatureKind, Sir Whoopass, Ooglians** in Nov 2024 | Stalled on re-papering to the correct legal entity |

**Three consequences for the Tuut conversation:**

1. **We have a price anchor.** Blacknut got 70% of net revenue to the licensor, allocated by time
   spent. That is the number to hold Tuut against, and note it was for a *worldwide, non-exclusive*
   grant. Anything materially below 70% net, or any request for exclusivity, should be pushed back.
2. **Non-exclusive is our default and our precedent.** Nothing in the Blacknut paper blocks a
   parallel telco deal. Confirm before signing that Tuut's operators accept non-exclusive, which
   they normally do.
3. **Ask which three operators.** If one of them is Blacknut or KT, we have a direct relationship
   already and do not need Tuut's margin in the middle.

**Action:** confirm whether the Blacknut agreement lapsed. It named WLBS as licensor and WLBS is
bankrupt, so the counterparty position is unclear and the two-year term from May 2023 has run.
Auto-renewal is one year at a time unless terminated with 6 to 3 months notice, which nobody is
likely to have served.

---

## 3. What a streaming platform actually screens on

Taken from Blacknut Annex 2, which is a real signed deliverable spec rather than a guess. This
now drives the "cloud fit" score on every page of the portfolio.

**Technical**
- Native **Linux build is the preferred execution target**. Windows accepted (Windows Server 2012,
  DirectX 11 / OpenGL / SDL2), but Linux is cheaper to run at scale.
- **DRM free**, delivered as a self-contained flat archive (tar / zip / rar).
- **Save data must be extractable**, ideally an XML file or an identifiable path, because the
  platform pulls user data out after each session and reinjects it before the next one.
- Full controller support, since the device is a TV, a set-top box or a handset with a pad.

**Editorial**
- 3+ screenshots at 1920x1080 landscape, logo, cover, a 160-character brief and a 2000-character
  long description, EFIGS where available.

**The commercial sting in the tail:** Blacknut's licence fee is net revenue **multiplied by the
time-spent share**, and "Technical Costs" (CPU, bandwidth, cloud storage) are deducted *before*
that split. So a cheap-to-render game with long sessions earns disproportionately more than an
expensive-to-render game with short ones. Card games and cozy management titles are structurally
advantaged. That is a real argument for leading with **KreatureKind** and **Distant Bloom**, not
just for leading with our biggest title.

---

## 4. Catalogue readiness, honestly assessed

11 titles are on the portfolio page. The headline problems:

- **Only 1993 Space Machine has a Linux build.** Everything else is Windows-only against a spec
  that prefers Linux. Not a blocker, but it is a cost argument the operator will make.
- **Block'Em! ships multiplayer-only.** It has our broadest localisation (13 languages) and the
  best living-room profile on paper, but a solo subscriber cannot play it. Schmiedl flagged this
  exact issue himself in Jan 2025. A single-player mode against AI bots would unlock it.
- **Tears of Adria declares no controller support.** Best review score in the catalogue (Very
  Positive) and a macOS build, but no pad support is a hard blocker for TV and set-top. Worth
  confirming with Ark Island whether the store page is simply out of date.
- **Ooglians is English-only and still in Early Access.**
- **IRON EVIL and Robot Lord Rising are unreleased.** Both partial controller support.

**Strongest to lead with:** Sir Whoopass (1,919 reviews, Very Positive, 9 languages, full pad),
Distant Bloom (single-player, full pad, DualSense profiles, calm pace), KreatureKind (10 languages,
low bitrate cost), Go Fight Fantastic, Chenso Club, 1993 Space Machine (the Linux build).

### Rights, and who signs

- **Owned, we sign alone:** 1993, Chenso Club, Block'Em!, Ooglians, IRON EVIL. Note the signing
  entity is **Creation Zero Point Holding AB (Steamworks partner 418393)**, not Aurora Punks AB.
  The 18 appids moved from APDS to CZP effective 1 July 2026.
- **Publishing rights, developer countersigns:** Distant Bloom, Go Fight Fantastic (Kinda Brave /
  Windup), KreatureKind (Valiant). We hold the publishing mandate and a revenue interest, not the
  IP, so the streaming grant needs the developer on the paper.
- **Brokered only:** Tears of Adria and Knives & Gutters (Ark Island), Sir Whoopass (Atomic Elbow).
  We have the relationship and full Steamworks access. They sign.
- **Not offered:** Robot Lord Rising. Legally Runatyr's per the 2023-06-29 Samarbetsavtal. It is on
  the page at your instruction, labelled as unresolved rather than as ours. Flagging once more that
  offering it for licence before the Runatyr position is settled carries real risk.

**Not on the page:** Massive Attax, JETZNAB, Aurora and Innsmouth are inside the 18 transferred
appids but have no public store presence, so there is no data or media to build a page from.
Vessels of Decay is excluded because ownership is still flagged UNCLEAR pending the 2022 CZP /
Blackdrop överlåtelseavtal.

---

## 5. Partner and dormant IP leads

You asked who else is sitting on games that could fit. Tiered by how actionable each is.

### Tier 1: live relationships, self-published, no external publisher

| Who | What they have | Why it fits |
|---|---|---|
| **Upstream Arcade** (AP holds 15%) | Own IP, actively shopping for publishers as of the Oct 2024 investor update. 505 Games and Devolver both circled and neither closed | They need distribution and we are already a shareholder. Cleanest ask on this list |
| **Red Marmoset Studios** (AP holds 15%) | UK team, seasoned, past early-stage funding | Same logic |
| **Eddaheim** (AP equity) | Neon Knights: Humanity Erased, Epic MegaGrant | Copenhagen, AP already a holder |
| **Northify** (AP ~7%) | Portfolio to confirm | Low friction to ask |
| **Ark Island** | Tears of Adria, Knives & Gutters | Already in the portfolio. Robert holds 5% and full Steamworks access |
| **Atomic Elbow** | Sir Whoopass, biggest audience we can point at | Already in the portfolio, brokered |
| **Pixadome, Cat Shawl, Ember Trail, Dinomite, Valiant** | Their own back catalogues beyond the titles we publish | Pixadome's Hayfever is the obvious one, historically bundled with Chenso Club |

### Tier 2: dormant or closed studios where IP was or is buyable

| Who | Status | Detail |
|---|---|---|
| **Studio Camelia** (Emma Delage) | Liquidated | Emma told Robert directly, 20 Sep 2025: **"Regarding the IP: it can still be bought out from the liquidator."** That is Alzara. On Radiant Echoes she recommended starting the code from scratch. She is now at Sandfall. **Warmest lead on this list, and it is a direct quote, not an inference** |
| **Ace Maddox AB** | Bankrupt, Nov 2024 | Formal asset tender circulated by trustee Mehrnaz Pakgohar at DLA Piper (Jenny Räf cc). Robert forwarded it to himself and to Bibbi but no bid is recorded. Two years cold, so assets are likely gone, but the trustee can confirm in one mail |
| **Legendo Entertainment AB** (556553-0606) | Bankrupt 2 Oct 2024, Gothenburg | Trustee Patric Lundin, Sara Stridsman at Wåhlin. They approached Robert. Long catalogue of older PC and console titles, which is exactly the shape of content telco streaming services buy cheaply |
| **Windswept Interactive** | Bankrupted | **AP already holds the source code plus the Ghost Signal revenue share.** This is an asset we own and are not exploiting |
| **WhyKev** | Dormant | TaniNani and Hoplegs. Both already went to KT Game Box in the 2021 deal, so they are proven in exactly this channel. Rights position needs checking, likely reverted |

### Tier 3: worth a call, larger or more complex

- **Amber Studio** (Catalin Butnariu): owns original IP and holds the Elric rights. Note our own
  Elric option is recorded as dead, so this is theirs, not a conflict.
- **Hex Foundry Entertainment AB** (559501-1650): bought Agents of Concordia from us Dec 2025.
- **Neon Artery**: Vessels of Decay, subject to the buyout clause.
- **Grey Tower**: studio with self-owned IP across RPG, platform, strategy.
- **Global Top Round** (Jan Halwe): a portfolio of early-stage teams and an explicit stated move
  away from full acquisition toward partnership. One introduction could surface several titles.

**Recommended first three calls:** Emma Delage on Alzara, because the IP is confirmed available
and the relationship is warm. Upstream Arcade, because they want distribution and we are a
shareholder. Legendo's trustee, because a bankrupt back catalogue of older console titles is
cheap and is precisely what these services stock.

---

## 6. Open items

1. **Confirm the Blacknut agreement's status.** WLBS is the named licensor and is bankrupt.
2. **Ask Tuut which three operators.** If we already deal with one, cut out the middle.
3. **Get the revenue split in writing early**, and anchor on Blacknut's 70% of net to licensor.
4. **Sales units are not on the portfolio yet.** Pulling real lifetime units needs a Steamworks
   session, and the account holding most of these titles uses mobile 2FA on Robert's personal
   Steam login, so it cannot be automated headless. The pages currently say units are available
   under NDA, which is a reasonable pre-MNDA position. Say the word and this can be pulled
   manually per title.
5. **Tears of Adria controller support**: confirm with Ark Island whether the store page is stale.
6. **Block'Em! single-player mode**: scope the cost. It unlocks our most localised title.
7. **Robot Lord Rising** is listed as unresolved. Revisit if the Runatyr position moves.

---

## 7. Sources

- `aurora_punks/ap_ip_ownership_canonical.md` (authoritative rights map, 2026-07-07)
- Blacknut Licence agreement (Drive, `1XovMUTrwExpMdDc-IfNyISYbGkyAhJLB`), Annexes 1 and 2
- KT Game Box thread, Oct to Nov 2021, Minji Seo
- Tuut threads: "Cloud Gaming cooperation" (Sep 2026), "TuuTap" (Dec 2024), "Call and feedback" (Jan 2025)
- Plug In Digital thread, Ludovic Reimonenq, Nov 2024 to Jan 2025
- Studio Camelia thread, Emma Delage, May 2025 to Mar 2026
- Ace Maddox tender, DLA Piper, Nov 2024. Legendo bankruptcy notice, Wåhlin, Oct 2024
- Steam public storefront API, retrieved 2026-09-08
