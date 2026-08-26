---
name: Legal knowledge base
description: Pointer to wiki/legal/ — owned by Lawyer agent. Use for Swedish corp/tax/employment/IP/GDPR lookups before asking Robert or external counsel.
type: reference
originSessionId: 5e97309f-7bcc-4783-8d95-842876a3a790
---
# Legal Knowledge Base — `wiki/legal/`

Owned and maintained by the **Lawyer** agent ([agents/lawyer.md](/home/assistant/projects/agents/lawyer.md)).

## Topic files

- [wiki/legal/_index.md](/home/assistant/projects/wiki/legal/_index.md) — landing page + conventions
- [wiki/legal/sv_corp_law.md](/home/assistant/projects/wiki/legal/sv_corp_law.md) — ABL, board duties, firmateckning, bolagsstämma, aktieägaravtal
- [wiki/legal/sv_tax.md](/home/assistant/projects/wiki/legal/sv_tax.md) — Skatteverket, 3:12, F-skatt, moms (VAT), cross-border, förmån
- [wiki/legal/sv_employment.md](/home/assistant/projects/wiki/legal/sv_employment.md) — LAS, MBL, anställningsformer, konkurrensklausuler, contractor vs employee
- [wiki/legal/sv_ip.md](/home/assistant/projects/wiki/legal/sv_ip.md) — upphovsrätt, varumärke, patent, mönster, FHL, game-specific licensing
- [wiki/legal/gdpr.md](/home/assistant/projects/wiki/legal/gdpr.md) — controller/processor, subject rights, IMY, breach notification

## How to use (for non-Lawyer agents)

- Need a quick lagrum check or Skatteverket position? Read the relevant topic file.
- Cite the same way the topic file does — lagrum + date or Skatteverket guidance ID.
- **Verify dates.** Re-check anything where `last_verified` is older than 6 months before relying on it. If uncertain, route the question to Lawyer via `/lawyer <task>`.
- **Robert positions are pinned.** When a topic file has a `robert_position` block, that overrides generic guidance. Don't second-guess from external sources.

## When to escalate to Lawyer (or beyond)

- Contract review / redlining → `/lawyer`
- Litigation, regulatory disputes, employment terminations, IP enforcement, material exposure → Lawyer flags "real lawyer" — Robert has go-to advokater outside this system.

## When to update

If you discover a new lagrum, Skatteverket position, or partner-specific stance worth keeping, add it to the relevant topic file with citation + `last_verified` date. Lawyer agent owns curation but any agent can append.
