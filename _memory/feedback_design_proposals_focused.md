---
name: Design proposals — keep super focused
description: Design/spec docs follow strict shape — short sentences, features and content, no repeating, why and how only. Counter the AI tendency to over-elaborate.
type: feedback
originSessionId: 9add9f39-e45a-4bf2-9a3d-84c764f3693c
---
When asked for a design proposal, design doc, spec, or technical proposal, the shape is fixed:

- **Short sentences.** Resist the AI tendency to nest clauses or compound thoughts. One idea per sentence.
- **Divide into features and content.** Structure mirrors the thing being designed (a list of components, features, fields, steps), not a narrative arc.
- **Avoid repeating.** If a fact appears in TL;DR it does not appear again in the body unless additive detail is required. Watch for the same point being made in "Problem", "Why", "Benefits", and "What you get" — that is four versions of the same thing.
- **Why and how only.** Why = the problem this fixes (one paragraph, not a sales pitch). How = the spec (tables, lists, steps). Drop "what you get", drop benefits-listing, drop risk-as-defense, drop comparison tables that aren't core to the design.

**Why:** AI writing tends to be over-ambitious — packs in extra context, restates for emphasis, adds reassurance and benefit-framing. Robert's design-doc audiences (game leadership, technical founders, finance counterparts) want the spec, not the case for the spec. Padding signals "AI-drafted" and gets the doc trimmed before it's read.

**How to apply:** Any time the brief is "design doc / spec / proposal / technical doc / structural plan", default to the focused shape. Length target: significantly under what the LLM instinct says is "thorough." Keep TL;DR, kill "what you get", kill "risks and mitigations" (unless a specific risk is decision-relevant), kill comparison tables that don't directly inform the design choice. If unsure whether a section earns its place, ask: "is this why or how, or is it selling?" Selling goes. The cover email/message can do persuasion if needed; the doc is the spec.

**Cross-reference:** [[feedback_no_em_dashes]] (zero tolerance), [[writing_voice_robert]] (global voice). Applies to all agents producing design output: PM (Jira/process design), DevOps (infra spec), UI (design briefs), GameDev (engine integration spec), ArtDirector (visual brief), Lawyer (memo structure where applicable).
