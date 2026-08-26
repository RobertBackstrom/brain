---
title: Legal Knowledge Base
owner: Lawyer agent
status: scaffolded
last_reviewed: 2026-05-03
---

# Legal Knowledge Base

Maintained by the **Lawyer** agent ([agents/lawyer.md](../../agents/lawyer.md)). Reference, not legal advice — every substantive question still ends with "real lawyer should review."

## Topic files

- [Swedish Corporate Law](sv_corp_law.md) — ABL, board duties, firmateckning, bolagsstämma, aktieägaravtal
- [Swedish Tax](sv_tax.md) — Skatteverket, 3:12, F-skatt, moms (VAT), cross-border consulting, förmånsbeskattning
- [Swedish Employment](sv_employment.md) — LAS, MBL, anställningsformer, konkurrensklausuler, contractor vs employee
- [Swedish & EU IP](sv_ip.md) — upphovsrätt, varumärke, patent, mönsterskydd, trade secrets, game-specific licensing
- [GDPR](gdpr.md) — platform-side data flows, controller/processor, subject rights, IMY

## Reference catalogues

- [Contract templates](templates/_index.md) — exhaustive catalogue of AP / CZP / Runatyr master templates + counterparty references on file. Companion to the [[reference_contract_templates]] skill (curated "start here" subset).

## Conventions

Every claim in a topic file should carry:
- **Citation** — lagrum (e.g. `ABL 8 kap. 4 §`), Skatteverket ställningstagande/rättslig vägledning ID + date, case ref, or external authority
- **`last_verified`** — date the citation was last checked against the source. Re-verify anything older than 6 months before relying on it.
- **`robert_position`** — when Robert has a specific stance (templates, deal positions, escalation thresholds), tag it explicitly so future agents don't override it from generic guidance.

## How the Lawyer agent uses this

1. Lookup → answer drawn from wiki entries with citations attached.
2. Gap → research → write back to the relevant topic file before moving on.
3. Stale entry → re-verify, update `last_verified`, fix if changed.
4. Robert correction → tag `robert_position` and pin near the top of the topic file's relevant section.

## Pending population

The skeleton files below have section headings but minimal content. They get filled task-by-task as real questions land. First fill: **IP rights** (assignment kicking off 2026-05).
