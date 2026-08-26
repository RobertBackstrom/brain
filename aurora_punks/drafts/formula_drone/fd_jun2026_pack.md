# Formula Drone — work pack (2026-06-22)

Prepared for the **Thu Jun 25, 11:00–11:30 CEST** FD <> Aurora call.
Agenda on James's invite: *Badass link / Drone platform possibilities with Robin / Finance + timing.*
Context grounded in: deal page `wiki/deals/deals/formula-drone.md`, Jon Sturgess's Flightball financial model, AP history dossier (`aurora_punks/ap_history_dossier.md`).

> **Jun 18 call (confirmed by Robert 2026-06-22):** nothing concrete agreed beyond *"we need to be prepped for due diligence from investors on IP rights for the tech and AP as a team."* That's the brief driving §2 (team) and the public pitch below.

> **"Robin" — confirmed: Robin Hoffa** (Eternal Minds dev, on the BADASS roster). Ties the "drone platform possibilities" agenda item to the BADASS link.

> **Investor pitch — LIVE (canonical /fd):** https://pitch.aurorapunks.com/fd/ — the "AP as a team + tech/IP ownership" story for FD's investors. **Now password-gated** (Basic Auth, user `fd` / pass in `assistant/pitch-auth.json`), shared with James + Bill the same way as the Teef proposal. Carries **no** rev-share %, budget figures or contract terms (those stay in §3 below). Living doc: edit `pitches/fd/index.html`, URL updates instantly. (Old `/formuladrone-ap` now 301-redirects here.)

---

## 1. BADASS intro (cross-project bridge)

Long-standing open action on the deal page: introduce FD (Bill/James) to BADASS (XR/drone synergy). It's now live as the "Badass link" agenda item.

**Suggested play:** raise it on the Jun 25 call first (confirm Bill wants the intro and what he wants out of it), then fire the email below. Double-opt-in — give Rosemary a heads-up before sending so the BADASS side is warmed too.

### Draft intro email (Robert's voice) — DO NOT SEND, draft only

**To:** Bill Rudgard, Rosemary Lokhorst · **Cc:** James Waite, Alex Sangwin-Skillen
**Subject:** Formula Drone <> BADASS Studios

> Hi both,
>
> Wanted to connect you two. There's an overlap here worth a proper conversation.
>
> Bill (cc James) runs Formula Drone in the UK. They're building Flightball, a live 5v5 drone sport, played with bumper-drones and a floating ball, with a produced showcase event and an angel round in motion. Aurora Punks is building the multiplayer game side.
>
> Rosemary (cc Alex) runs BADASS Studios. They've built BadassXR, a UE5 platform for live sport: AR/VR broadcast, digital-twin venues, fan apps and a companion game. It currently powers the E1 electric powerboat championship.
>
> Drone sport and XR broadcast belong in the same room. The live-event production, the broadcast layer, the fan app and the game around the sport itself, that's the stack BADASS has built and roughly what Flightball needs around the live event.
>
> I'll let you take it from here. Happy to sit in if it's useful.
>
> Best
> Robert

*Notes: kept light on both descriptions so neither side has to decode the other. No commercial framing — that's for them to find. Logged as an Open Action; once sent, I'll log it on the FD deal page and the BADASS-side memory per the BD↔PM bridge rule.*

---

## 2. Investor-DD "team + numbers" pack (AP as the Flightball dev partner)

What Bill needs for funder DD on the Flightball "team": proof Aurora Punks is a real, capable studio and that the build plan + cost are credible. Below is the **content draft** — final form should be a one-pager GDoc or a slide appended to the FD deck (not an .md to Bill). Everything here is from AP's own public deck material; verify the entity note before it goes out.

### Aurora Punks — Flightball development partner

**Who we are.** Stockholm-based co-development studio, founded 2019. "Developers for developers." ~20 FTE in Stockholm plus partner studios in Belgrade, Copenhagen and London. We take teams from prototype to release across PC, console and live platforms.

**Why we fit Flightball.**
- Multiplayer and live-service is our core: co-dev on large competitive multiplayer titles, plus our own live-service mobile work.
- We already have a working **sim engine** — the single biggest de-risking factor for the Flightball build (FD's own financial model credits this).
- Console and cross-platform shipping experience, including certification and porting.

**Track record (selected co-dev).** Ready or Not (UE4→UE5, console port + cert), The Finals (UE5, UI + cross-platform), Helldivers 2, Darktide, Ghost Signal: A Stellaris Game (VR full-service), Mad Skills BMX 2 (live-service). Originals incl. BlockEm! and the Robot Lord Rising IP.

**Key people on the Flightball side.**
- Robert Bäckström — Founder / Executive Producer. Fatshark core member, ex-Raw Fury.
- Marcus Thorell — Game Director, 20y design.
- Peter Nilsson — Tech Director (Fatshark / Bitsquid-Stingray engine lineage).
- Tim Browne — Creative Design Director.
- Plus a full engineering / art / QA bench drawn from the AP roster + partner studios.

**Delivery plan and numbers (staged to the raise, per Jon's model).**
- Seed tranche **£60k** → crude-but-playable prototype (v0.1 + functional v1) for the showcase window.
- Fit-out **£200k** → multi-platform v1 release, ~18 months.
- Growth **£530k** → v2 features, console cert, eSport infrastructure (Y2–3).
- Total dev budget across rounds: **£790k**. AP commercial terms: £30k upfront licence + rev-share (see §3 — under negotiation).

> **Verify before sending:** (1) contracting entity is **Aurora Punks AB (559256-9718)**, not the bankrupt APDS — older decks blur this. (2) Use ~20 FTE + partner studios as the headcount. (3) Do **not** put AP's own seed-raise / corporate revenue projections into FD's DD pack — they're aspirational and irrelevant to Flightball; the only numbers Bill's investors need are the Flightball build plan above.

---

## 3. Negotiation position (AP terms, before contracting)

Their opening (Jon's model, all marked "negotiable"): **£30k upfront licence + 20% rev-share**, no equity to AP, all Flightball IP assigned to FD "regardless of sim engine." Their internal `Strategic_Notes` tells FD that 20% is AP's *ceiling* and to push AP to 15% (every 5pp cut ≈ £30–50k Y4 EBITDA for them). So expect a haircut attempt. Recommended counter:

1. **Rev-share: hold 20% as the floor, not the ceiling.** Their own model credits AP's existing sim engine as a key seed-investor de-risking factor — that's the leverage. AP carries multi-year delivery risk and the rev-share is heavily back-loaded (almost nothing until Y3–Y4). If they push to 15%, don't give it free — trade it for a higher upfront or milestone guarantees.
2. **Upfront: push above £30k, or add per-round milestone payments.** £30k is thin when AP's upside is back-loaded. Tie payments to each round closing so AP isn't financing FD's fundraising risk.
3. **IP / engine line — the important one.** Fine for FD to own Flightball-the-sport IP (rules, arena designs, branding). But AP **retains ownership of its sim engine and any reusable tech and licenses it to the project** — do not assign it. That engine is the de-risking asset; assigning it away gives up AP's leverage and a reusable platform. → **Lawyer to review the IP/assignment clause once drafted.**
4. **Equity: agree to none.** Matches their "keep the cap table clean" preference and keeps AP's own cap table clean. But that makes the rev-share AP's only upside, so point 1 (hold 20%) becomes non-negotiable.
5. **Gating: stage AP's resourcing to each round close.** No committed dev spend before the matching tranche is funded.
6. **Platform: agree Epic-first** (12% vs Steam's 30%). Aligns both sides' margin and lifts AP's rev-share base.

---

## Next actions
- [ ] Confirm who "Robin" is + any Jun 18 outcomes (then I refine this pack)
- [ ] Jun 25 call: raise BADASS link, get Bill's nod on the intro
- [ ] After call: send intro email (double-opt-in Rosemary first); log on FD deal page + BADASS memory
- [ ] Package the §2 team+numbers content as a GDoc / deck slide for Bill
- [ ] Lawyer review of the IP/engine clause once terms are drafted
