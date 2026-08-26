# RankOne - Data-Rights Scoping Memo: Licensing User-Preference Data to AI Entities

**Prepared by:** Lawyer agent (masterbrain) for Robert / RankOne biz-dev
**Date:** 2026-06-17
**Status:** Internal scoping memo - proportional (verdict + gating issues), NOT a full formal opinion. Not legal advice; a licensed advokat / dataskyddsjurist must sign off before any binding buyer commitment.
**Subject:** Can RankOne Global AB (org 559168-5325) lawfully license its curated user-preference data to third-party "AI entities" (AI labs, recommendation-engine companies, data buyers)?
**Asset in scope:** ~101k users (largely Twitch/streamer-acquired, EU + global), 2.6M+ manually curated game relations (Played / Playing / Want-To-Play), 413k written reviews, plus profile data. Human-curated, longitudinal, multi-platform, tied to identifiable user accounts.

---

## TL;DR

- **Verdict: VIABLE WITH CONDITIONS.** Not hard-blocked, but the current data asset cannot be licensed for AI use in its present (user-tied, identifiable) form on the current paperwork. The viable product is an **anonymised / aggregated preference dataset**, not raw per-user records.
- **The pivot lives or dies on which of two paths RankOne picks:** (A) a true **anonymised-aggregate** product that exits GDPR scope entirely (cleanest, no consent re-paper needed, but caps how granular/per-user the buyer's data is), or (B) **identifiable / pseudonymous** data licensing, which requires fresh **opt-in consent re-papering** under a new purpose and is fragile (withdrawable, transfer-exposed, AI-Act-touched).
- **Four gating red flags** (detail in §4): (1) purpose-limitation breach (Art. 5(1)(b)) - data was collected to build gaming profiles, not to feed AI buyers; (2) no current lawful basis to license to third parties; (3) the anonymisation bar is high and per-EDPB case-by-case - "aggregated" is not automatically "anonymous"; (4) non-EU buyers (US AI labs) trigger Chapter V transfer machinery.
- **Single most important next step:** pull and read RankOne's **current ToS + privacy policy** to establish what purposes and disclosures users actually agreed to. Everything downstream depends on that text. Until it is read, treat the pivot as legally unscoped.

---

## 1. Lawful basis under GDPR

RankOne is a **controller** (Art. 4(7)) - it determines the purposes and means of processing its users' preference data. Licensing that data to a third party for the third party's AI use is a **new processing purpose** and a **disclosure to a recipient** (Art. 4(9)), both of which need their own lawful basis under Art. 6(1).

### 1.1 The two candidate bases

**Consent (Art. 6(1)(a)).** The clean basis for licensing identifiable preference data to named third parties for AI use. Must be freely given, specific, informed, unambiguous, and as easy to withdraw as to give (Art. 7; Recital 32). Bundled / pre-ticked / "by using the app you agree" consent is invalid. Practical consequences: it is **withdrawable at any time** (Art. 7(3)), and a buyer who has ingested withdrawn-consent data into a trained model has a problem RankOne cannot fully fix downstream. Consent is the **only** honest basis for the identifiable-data path.

**Legitimate interest (Art. 6(1)(f)).** Tempting because it avoids a consent campaign, but **weak-to-unusable here**. It requires a three-part balancing test (legitimate interest + necessity + the interest not overridden by data-subject rights/expectations). Selling/licensing user-tied taste data to external AI buyers fails the **reasonable-expectations** limb: a user who curated a gaming backlog did not reasonably expect their profile to be packaged and licensed to an AI lab. The **EDPB Opinion 28/2024** (17 Dec 2024) confirms LI *can* in principle cover AI-related processing but only after a genuine, documented balancing test and only where the processing is within data-subject expectations - which third-party AI licensing of identifiable preference data is not. **Do not build the pivot on LI for identifiable data.** LI is only defensible for RankOne's *own internal* analytics, not external licensing.

### 1.2 The escape hatch: move the data outside personal-data scope

If the licensed dataset is **not personal data**, GDPR does not apply to it at all (Art. 2(1)), and the consent / LI question disappears. Two routes, with very different legal weight:

- **Pseudonymisation (Art. 4(5)).** Replacing direct identifiers with a key. **Does NOT exit GDPR scope** - pseudonymised data is still personal data (Recital 26, explicit). Useful as a security/minimisation measure and to strengthen a transfer or LI posture, but it does not make the data licensable consent-free.
- **Anonymisation (Recital 26, Art. 4(1)).** Genuinely anonymous data is outside GDPR. **This is the only route that exits scope.** The bar is the **"means reasonably likely to be used"** test (Recital 26): data is anonymous only if no one - not RankOne, not the buyer, not a third party - can re-identify an individual using means reasonably likely to be used, accounting for cost, time, and available technology.

**The bar for "anonymous" is high, and aggregation alone does not clear it.** Per **EDPB Opinion 28/2024**, anonymity must be assessed **case-by-case** and a dataset is not anonymous merely because it has been bundled or had names stripped. Two specific traps for RankOne's data:

1. **Uniqueness / singling-out.** A longitudinal, multi-platform list of 2.6M game relations across ~101k users is extremely high-dimensional. A user's specific combination of played/wanted titles + review timestamps is very likely **unique** - a classic singling-out / mosaic re-identification risk even with the account ID removed. This is the same failure mode as the Netflix Prize and AOL search-log re-identifications.
2. **Free-text reviews.** The 413k written reviews are the worst offender. Free text routinely contains self-identifying content ("as I said on my stream", names, locations, handles). Reviews cannot be treated as anonymous by stripping the author ID - the text body itself carries identifiers.

**Bottom line on §1:** A genuinely **anonymised aggregate** (e.g. "X% of users who played A also want B", genre-cohort preference vectors, k-anonymity / differential-privacy-protected aggregates) can be licensed **without consent and without GDPR constraint** - this is the clean product. Raw or lightly-pseudonymised per-user records (especially review text) **cannot** be treated as anonymous and require fresh opt-in consent to license.

---

## 2. ToS / privacy-policy coverage

**This section is provisional - the current ToS and privacy policy have not yet been read (see next steps). The following is what such consumer-app terms almost certainly do NOT cover.**

### 2.1 What the current terms almost certainly do not cover
A "Your Life in Games" gaming-profile app's privacy policy was, on overwhelming probability, written to cover: providing the service, building the user's own profile, improving the product, internal analytics, and *aggregate* developer insights (the existing B2B Insights product). It was **not** written to cover **licensing user-tied data to external third-party AI entities for those third parties' own purposes**. That is a materially different recipient and purpose.

### 2.2 The purpose-limitation problem (Art. 5(1)(b)) - the central legal trap
Data must be collected for "specified, explicit and legitimate purposes" and not further processed in a manner **incompatible** with those purposes. Data collected to build a personal gaming profile, then repurposed to be licensed to AI buyers, is a **textbook purpose-limitation conflict**. The compatibility assessment (Art. 6(4)) weighs the link between old and new purpose, the context, the nature of the data, consequences for users, and safeguards. External AI licensing is a **stretch too far** from "build your gaming profile" to be compatible. Two lawful exits:
- **Fresh consent** for the new purpose (consent is treated as breaking the compatibility chain - the user re-authorises the new purpose directly), or
- **True anonymisation** before licensing (no personal data = no purpose-limitation constraint).

There is no third "we updated the privacy policy" exit. Unilaterally amending the privacy policy to add "we may license your data to AI partners" does **not** retroactively legitimise data already collected under the old purpose, and for the identifiable path does not substitute for consent.

### 2.3 What new disclosures / consent mechanics would be required (identifiable path)
- **Opt-in, not opt-out.** For licensing identifiable preference data to third-party AI buyers, **opt-in is required** - this is not a legitimate-interest "object" scenario. Opt-out would be invalid consent.
- **Granularity (Recital 43, Art. 7).** Consent must be **unbundled** from the core ToS - a user must be able to use RankOne without consenting to AI licensing. Ideally granular per purpose (e.g. separate toggles for "aggregate insights" vs "licensing to AI partners").
- **Named or categorised recipients + purpose specificity.** "AI partners" is borderline too vague; the more specific the recipient category and AI use, the safer.
- **Withdrawal mechanism** as easy as opt-in (Art. 7(3)).
- **Transparency (Arts. 13-14)** updated to describe the new recipients, purpose, transfer destinations, and retention.

---

## 3. Special angles

### 3.1 Profiling / automated decision-making (Arts. 21-22)
RankOne's own products (Profile Similarity, WTP-Drafter, Personalized Feed) are **profiling** (Art. 4(4)). That is manageable within the service relationship. The exposure rises if licensed data feeds a buyer's system that makes **decisions with legal or similarly significant effect** about individuals (Art. 22) - less likely for game-recommendation use, but flag it for any buyer whose use touches eligibility, pricing, or content gating directed at identifiable users. **Right to object to profiling (Art. 21)** must be honoured for the identifiable path.

### 3.2 International transfer - US AI labs (Chapter V)
If buyers are non-EU (US AI labs are the obvious case), licensing personal data to them is a **restricted transfer** under **Chapter V (Arts. 44-49)**. Lawful transfer requires one of:
- **Adequacy decision** - for the US, the **EU-US Data Privacy Framework** covers DPF-certified recipients only. Verify the specific buyer is certified; if not, no adequacy.
- **Standard Contractual Clauses (Art. 46(2)(c))** plus a **transfer impact assessment** (post-*Schrems II*), with supplementary measures as needed.
- Note the DPF has faced ongoing legal-stability questions; SCCs remain the durable fallback.

**This entire section disappears if the licensed dataset is genuinely anonymous** - anonymous data is not personal data and Chapter V does not apply. This is a strong second reason to favour the anonymised-aggregate product.

### 3.3 EU AI Act touchpoints (if data feeds training)
The **AI Act (Reg. (EU) 2024/1689)** is in force; it becomes **fully applicable 2 August 2026**, and **GPAI-model obligations (incl. training-data transparency) have applied since 2 August 2025**, with Commission enforcement powers from 2 August 2026. RankOne as a **data supplier** is not itself a "provider" of an AI model, so the direct AI-Act obligations sit with the buyer. But two practical touchpoints:
- **Training-data transparency / copyright (Art. 53 GPAI duties):** buyers must publish a summary of training data and respect copyright opt-outs. Expect buyers to demand **provenance and rights warranties** from RankOne in the licence - RankOne must be able to give them honestly (ties back to §3.4).
- **Commercial reality:** the AI Act makes *provenance and rights-cleared data* more valuable (the whole thesis of the pivot), but also means buyers will diligence RankOne's rights chain harder. Clean consent / clean anonymisation is a **sales asset**, not just a compliance cost.

### 3.4 Who owns the 413k reviews (IP / copyright)
Under Swedish copyright law (**URL 1960:729**), a written review of sufficient originality is a **literary work** and copyright vests in the **author (the user)** - Sweden has **no work-for-hire doctrine**; the platform owns the review text only to the extent the **ToS contains an explicit licence or assignment**. Two consequences:
- **Check the ToS licence grant.** Most UGC platforms take a broad licence ("perpetual, worldwide, sublicensable licence to use, reproduce, and distribute"). If RankOne's ToS has a broad **sublicensable** licence, RankOne can likely sublicense the review text to buyers as a **copyright** matter. If the licence is narrow ("to operate the service") or non-sublicensable, RankOne **cannot** license the reviews onward without re-papering.
- **Copyright licence ≠ GDPR basis.** Even a perfect copyright sublicence does **not** solve the GDPR problem - the review text is *also* personal data (§1.2 trap 2). Both gates must be cleared for the reviews.
- **Moral rights (URL 3 §, ideell rätt)** cannot be assigned wholesale, only waived for use limited in nature and extent - relevant if reviews are reproduced without attribution at scale.

---

## 4. Verdict + gating red flags

**Verdict: VIABLE WITH CONDITIONS.** The pivot is legally legitimate as a direction. It is **not** licensable on the current asset + current paperwork without one of two deliberate moves: (A) build a genuinely anonymised-aggregate product, or (B) re-paper consent for an identifiable-data product. Path A is cleaner, faster to lawful, and transfer-proof, but yields a less granular product. Path B yields the richer per-user product the buyer ideally wants, but is consent-fragile, withdrawal-exposed, and transfer-encumbered.

**The four things that gate it:**

1. **Purpose limitation (Art. 5(1)(b)) - the master gate.** Data was collected to build gaming profiles, not to license to AI. Cured only by fresh consent (Path B) or true anonymisation (Path A). No privacy-policy edit cures it retroactively.
2. **No current lawful basis to license identifiable data to third parties.** Consent is the only honest basis (LI fails the expectations test per EDPB Opinion 28/2024). Today RankOne almost certainly does not hold it.
3. **The anonymisation bar (Recital 26 + EDPB Opinion 28/2024).** "Aggregated" is not automatically "anonymous." High-dimensional preference vectors enable singling-out; free-text reviews carry embedded identifiers. Clearing the bar needs real technique (k-anonymity / differential privacy / aggregation + a documented re-identification-risk assessment), assessed case-by-case.
4. **International transfer (Chapter V) for non-EU buyers.** US AI labs need DPF certification or SCCs + TIA - unless the data is genuinely anonymous, in which case this gate vanishes.

**Real-lawyer escalation:** before any binding licence or LOI, a licensed Swedish **dataskyddsjurist / advokat** must (a) sign off on the anonymisation methodology if Path A, or the consent mechanics if Path B, and (b) draft/review the buyer licence (rights warranties, transfer clauses, AI-Act provenance reps). This memo is a scoping read, not that sign-off.

---

## 5. Concrete next steps for Robert / RankOne

1. **Pull and read the current ToS + privacy policy (highest priority).** Everything above is provisional until the actual text is read. Specifically check: (a) the stated **purposes** of processing; (b) whether any **third-party / data-licensing / "partners"** disclosure already exists; (c) the **UGC licence grant** for reviews - is it broad and **sublicensable** or narrow; (d) existing **consent mechanics** (what users actively tick vs passively accept). Source likely at rankone.global / in-app; ask Johan/Peter Spegel for the live text if not public. *Until this is read, treat the pivot as legally unscoped.*
2. **Decide Path A vs Path B early - it is a product decision with legal consequences, not the reverse.** Path A (anonymised aggregate) is the recommended default: it exits GDPR scope, needs no consent campaign, sidesteps Chapter V, and still sells the thesis (provenance + rights-clean). Path B only if a buyer genuinely needs per-user granularity and will pay enough to justify the consent re-paper + transfer machinery + fragility.
3. **For Path A: commission a re-identification-risk assessment** of a sample aggregated dataset before pitching it as "anonymous." Handle review text separately - it likely cannot be included in an anonymous product without aggressive redaction/aggregation. Document the methodology (this *is* the anonymisation evidence the EDPB expects).
4. **For Path B (if chosen): design the consent re-paper now.** Unbundled, opt-in, granular toggle ("license my data to AI partners"), easy withdrawal, updated Arts. 13-14 transparency, named recipient categories. Expect meaningful opt-in attrition - model the corpus at, say, 20-40% opt-in, not 100%, when sizing the product for buyers.
5. **Gate buyer conversations on rights posture.** Do not let a buyer LOI get concrete until either the anonymisation methodology (A) or the consent basis (B) exists. A buyer will diligence the rights chain hard (AI-Act provenance pressure, §3.3); arriving with clean rights is a sales advantage, arriving without is a deal-killer.
6. **Engage a Swedish dataskyddsjurist before any binding commitment** - for sign-off on the chosen path's methodology and to draft the buyer licence (warranties, SCCs/DPF, AI-Act reps). Budget this as a real line item, not an afterthought.
7. **Watch the user-trust collision** (flagged in the pivot reconciliation note): even a fully lawful "we license your taste data to AI" can spook the engaged 20% who are the corpus engine. The anonymised-aggregate framing ("we never share your individual profile, only anonymous trends") is both the legally cleaner and the trust-cleaner story - another reason to favour Path A.

---

## "Real lawyer should look at"

A licensed Swedish **dataskyddsjurist / advokat** (data-protection specialist) must review before any binding buyer commitment: the anonymisation methodology (Path A) or consent mechanics + privacy-policy/ToS amendments (Path B), the UGC/copyright sublicence chain for the reviews, and the buyer licence agreement including Chapter V transfer mechanism and AI-Act provenance warranties. This memo is a proportional scoping read to steer biz-dev, not a formal legal opinion and not legal sign-off.

---

*Sources / authorities cited: GDPR (EU) 2016/679 - Arts. 4, 5(1)(b), 6, 7, 13-14, 21-22, 28, 44-49; Recitals 26, 32, 43. EDPB Opinion 28/2024 on AI models (17 Dec 2024) - anonymisation case-by-case + LI balancing. EU AI Act Reg. (EU) 2024/1689 - GPAI obligations live 2 Aug 2025, full applicability + enforcement 2 Aug 2026. Swedish copyright: URL (1960:729) 3 §; dataskyddslagen (2018:218). Internal: rankone_ai_data_pivot_reconciliation.md; wiki/company/rankone.md; RankOne CLAUDE.md. EU AI Act timeline verified via European Commission digital-strategy + artificialintelligenceact.eu (2026-06-17); EDPB Opinion 28/2024 verified via edpb.europa.eu (2026-06-17).*
