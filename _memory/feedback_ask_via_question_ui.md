---
name: feedback-ask-via-question-ui
description: "Every request for Robert's input goes through the multi-option question UI (AskUserQuestion), never as inline bullets or a numbered list in prose. Applies to the Assistant and every spawned agent."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ddd890a8-5a9b-4c76-8937-6ebde663d8ff
  modified: 2026-08-07T16:15:31.317Z
---

**All requests for input from Robert must use the multiple-choice question UI** — the
`AskUserQuestion` tool, which renders selectable options with an "Other" box at the bottom for
free text. Never ask by writing questions inline as bullet points or a numbered list in prose.

This applies to the main Assistant **and every spawned or named agent**, on every surface where
that UI is available.

**Why:** Robert stated it directly on 2026-08-07. Inline question lists put the work on him: he
has to parse prose, decide what is actually being asked, and then type a free-form answer that
addresses each item in order. The option UI turns that into a click, keeps the answer structured
enough that the next turn cannot misread it, and still leaves the "Other" box for the cases where
none of the options fit. It is the same interrupt-load argument as [[feedback_search_wiki_first]]
— minimise what Robert has to produce by hand.

**How to apply:**
- Any time the next step depends on a decision only Robert can make, reach for the question UI.
  That includes the Plan-Confirm-Execute clarifying questions ([[feedback_plan_confirm_execute]]),
  approval gates, scope choices, and the `/close` ritual's own prompts.
- Put your recommendation first and mark it "(Recommended)".
- Do not also restate the questions as prose above the UI call. Context and findings go in the
  prose; the questions themselves live only in the UI.
- Multi-select when the choices are not mutually exclusive.
- **This does not change report formatting.** [[feedback_numbered_lists_in_reports]] still holds
  for *output* — findings, summaries, status reports stay numbered. The rule here governs
  *input requests* only. Reporting in numbered lists, asking through the UI.
- Spawned agents that cannot reach the UI (background/server-spawned runs with no interactive
  channel) fall back to the IPC protocol in [[agent_ipc]], not to prose questions.
