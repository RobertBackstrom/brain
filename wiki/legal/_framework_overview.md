---
name: Legal Framework Overview
description: Ties together the group's legal framework — entities + signing authority, contract templates, standard positions (IP, pass-through, no-AI, arbitration, related-party), the Swedish-law KB, doc workflow, and active matters. Entry point for any legal work.
type: reference
---

# Legal Framework Overview

Entry point for legal work across the group. Detailed Swedish-law notes live in the sibling KB files; this overview maps the framework and points into them.

## Entities & signing authority
See [[company_structure_ownership]] for the full map. Signing authority:
- **Aurora Punks AB** — firmateckning **två i förening** (typically Mattias Wiking + Robert). Board: Mattias (chair), Alexander Bergendahl, Andreea Chifu, KM Troedsson, Robert.
- **CZP Holding AB** — Robert (Director), sole owner.
- **Related-party rule (ABL 8 kap. 23 §):** when contracting with a counterparty the group part-owns (Red Marmoset, Bright Gambit, 5 Fortress, Dark Riviera, Malformation, RankOne), the AP side must be signed by **independent** board members and the related-party relationship disclosed in the board minute. Anyone conflicted (e.g. Andreea Chifu re Bright Gambit; Robert re Red Marmoset/CZP) abstains from that side. See [[company_structure_ownership]] related-party section.

## Contract templates & where they live
- AP AB master **MNDA**: GDrive `1DOlOQIP4B5VwZmFc34q3D74qoLYEqizTxrzgo8J_KOw` (use when AP drafts; for inbound counterparty MNDAs run the three-tell scan — see [[lawyer]] learnings).
- CZP subcontractor / outsourcing master + MNDA templates: `czp_legal/templates/{MNDA,Subcontracts}/` (AP AB master, not the WLBS legacy). See [[reference_contract_templates]].
- Paying-Agent Agreement template: `umbrella/k2c_sands_of_duat/Legal/` (promote to `czp_legal/templates/PayingAgent/` once instance count ≥ 3).

## Standard positions (apply by default)
- **IP — Sweden has no work-for-hire:** authorship vests in the natural-person creator; must be **explicitly assigned/licensed**. "No licence granted" clauses are protective, not restrictive. Moral rights (ideell rätt, URL 3 §) cannot be waived in the blanket — only specific-scope. See [[sv_ip]].
- **Back-to-back flow-down** (publisher → AP → subs): match cure period (≤ master), customer-only convenience termination, no-AI rep, post-release support duration/trigger. See [[lawyer]] K2C learnings.
- **Payment:** pass-through (sub paid only after AP receives the upstream payment) — current K2C wording is "within 5 business days after AP receives the corresponding RF payment". Where a group entity is the paying agent (CZP for K2C), its own fee is settled by **set-off against the intercompany balance**, not self-invoice.
- **No AI-generated content** rep where the upstream master requires it (RF 7.2.3); mirror as a rep, no carve-out the master lacks.
- **Dispute resolution:** Swedish District Court (Stockholm) for Swedish counterparties; **SCC arbitration, seat Stockholm, English** for foreign counterparties (enforceable via the New York Convention) + a confidentiality undertaking.
- **Cross-border VAT** clauses do NOT belong in B2B service contracts (reverse charge is statutory). See [[lawyer]] learnings.

## Swedish-law knowledge base (this folder)
- [[sv_corp_law]] — ABL: board duties, firmateckning, jäv/ABL 8:23, värdeöverföring (17:1), bolagsstämma.
- [[sv_tax]] — 3:12 / fåmansföretag, F-skatt, moms/reverse charge, borgen/regress (IL 48:24, RÅ 2001:57), intercompany paying-agent tax-cleanliness.
- [[sv_employment]] — LAS/MBL, anställningsformer, konkurrensklausuler, contractor-vs-employee.
- [[sv_ip]] — upphovsrätt/URL, ideell rätt, varumärke, mönster, FHL trade secrets.
- [[gdpr]] — platform-side data flows, controller/processor, IMY.
- Re-verify any citation older than ~6 months before relying on it.

## Document workflow
- Folder model: `_legals` (signed) / `_legals/_working` (drafts/review) / `_legals/_archive` (superseded) per project — [[czp_project_folder_structure]], [[drive_versioning]].
- "Share with signatories" = GDrive comment-share + a review/redline cover letter, then **Google Sign** for signature — [[share_for_signature]], [[google_drive_esignature]].
- Lawyer agent reviews/advises; CorpBot ships/files. Always end advisory output with a "real lawyer should review" line.

## Active legal matters
- **RobotLord IP dispute (RLR)** — epic `rlr`; Scen & Film / ideell rätt; Dark Riviera (CZP 6%, Robert chair) + Runatyr-obestånd latent. See [[project_rlr_ip_dispute]].
- **APDS konkurs** — Robert's personal borgen recourse; AP wholly-owned APDS bankrupt; konkursförvaltare Nils Åberg (Carler). Capital-loss/regress treatment per [[sv_tax]].
- **WLBS AB konkurs** — AP wholly-owned, bankrupt.

Cross-refs: [[company_structure_ownership]], [[projects_catalogue]], [[reference_legal_kb]], [[reference_contract_templates]].
