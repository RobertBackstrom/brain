---
title: Formula Drone NDA — Light Review
counterparty: Formula Drone Ltd (UK)
ap_entity: Aurora Punks AB (559256-9718)
doc_date: 2026-04-30
reviewer: Lawyer agent
review_date: 2026-05-06
review_depth: LIGHT (proportional — commodity NDA, low-risk inbound mutual)
linked_ticket: db-091
linked_deal: wiki/deals/deals/formula-drone.md
---

# Formula Drone NDA — Light Review (2026-05-06)

## Verdict
**Sign with minor pushback.** Mostly fine, but two real issues (signing entity + one-sided indemnity) and one term-length nudge that's worth raising in a single short reply to James.

## Real red flags

1. **Signing entity is wrong on the AP side (Clause: parties block).**
   The doc names "Robert Bäckström of Aurora Punks at Timmermansgatan 43, 118 55 Stockholm". This binds **Robert personally**, not the company. Confidential information from FD will flow into AP AB's commercial work; the AP AB entity must be the signatory.
   *Fix:* "Aurora Punks AB (org. nr. 559256-9718), Timmermansgatan 43, 118 55 Stockholm, Sweden, represented by Robert Bäckström." Robert signs as authorised signatory, not as principal.

2. **One-sided indemnity (Clause 17).**
   "The Recipient undertakes to indemnify and keep **Party 1** at all times fully indemnified..." — only Party 1 (Formula Drone) gets the indemnity. In a *mutual* NDA both sides must benefit. This is the single biggest tell that the doc was originally drafted as a one-way NDA and re-skinned.
   *Fix:* replace "Party 1" with "the Discloser" so it runs both ways, or strike the clause entirely (most mutual NDAs don't carry an indemnity at all — breach + general damages is enough).

3. **Term length 5 years post-termination is on the long side (Clause 14).**
   For a fundraising-stage NDA covering finance numbers + investor deck, 2-3 years is the market norm. 5 is not abusive but it's the kind of thing AP can ask to shorten without friction. Trade-secret-grade information rightly survives indefinitely under Sweden's FHL anyway, so no harm in shortening the contractual term.
   *Fix:* "three (3) years" — or accept 5 if FD pushes back; not a hill to die on.

## Specifically checked — pass

- **Mutuality:** Yes, genuinely bilateral in the body (Clauses 1, 2, 3-12 all use "Recipient/Discloser" generically). Indemnity (#17 above) is the only carve-out that breaks the symmetry.
- **Governing law / jurisdiction (Clause 20):** English law, exclusive jurisdiction of the courts of England and Wales. Standard for a UK counterparty. **Acceptable** — flag only because exclusive jurisdiction means AP can't sue FD in Sweden if needed, but for an NDA-only matter that's tolerable. If this were the underlying dev contract, push for non-exclusive.
- **Definition of Confidential Information:** Reasonably scoped. Captures the usual categories. **No "residuals" trap** (no clause saying the receiving party gets to keep "general knowledge retained in unaided memory"). Good.
- **Carve-outs (in the definition):** All four standard carve-outs present — public domain, prior knowledge, independent development, and (in Clause 11) compelled disclosure with notice obligation. Clean.
- **Return/destruction (Clause 9):** Standard — return or delete + furnish certificate on request. Fine.
- **IP (Clause 1):** Explicit "no licence granted, no IP rights transferred either direction." This is exactly the right shape — it does NOT leak any AP IP. Good clause.
- **No non-solicit, no non-compete, no exclusivity.** Clean — none of those clauses snuck in. (Worth noting because they sometimes do in re-skinned NDAs.)
- **No "no hire" / non-poach.** Absent. Good.
- **Survival post-termination of obligations (Clause 14):** Clauses 3-9 expressly survive expiry. Standard.

## Suggested reply to James (single short email)

Three small tweaks before signing:
1. AP-side party should be "Aurora Punks AB (org. nr. 559256-9718)" with Robert as authorised signatory — not Robert personally.
2. Clause 17 (indemnity) currently runs only to Party 1; please make it run to "the Discloser" so it's mutual, or drop the clause.
3. Clause 14: would prefer 3 years post-termination rather than 5; happy to compromise if you have a specific reason for 5.

Otherwise good to go.

## "Real lawyer" recommendation
None needed for an NDA at this level. If FD pushes back on (1) — the signing entity fix — that's not a legal question, that's a "we'd be signing the wrong contract" question, and they have to accept it. (2) and (3) are negotiable.

## Process notes
- Source PDF: `assistant/uploads/FD-AP-NDA-2026-04-30.pdf`
- Length: 4 pages, 20 numbered clauses
- House style: appears to be a UK SME/founder-grade NDA, not a magic-circle template
