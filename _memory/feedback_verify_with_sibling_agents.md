---
name: feedback_verify_with_sibling_agents
description: "Check another named agent's domain before flagging its status as an open question for Robert"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 00523b80-f175-4b90-a692-f0929309fc20
  modified: 2026-08-02T12:03:51.991Z
---

Before escalating a question that sits in another named agent's domain, query that domain instead of asking Robert. Robert, 2026-07-31, after I flagged "send the MS3 invoice" as outstanding when he had already sent it: *"you can verify questions like this from the admin agent who handles Fortnox in the future."*

**Why:** the agent registry exists so each domain has an owner with live access. CorpBot owns invoicing/accounting and has Fortnox access on the VPS, so invoice-sent and payment-landed are *checkable facts*, not questions. Asking Robert spends his attention on something the system already knows. This is [[feedback_search_wiki_first]] pointed at a sibling agent rather than at the RAG index.

**How to apply:** when a report is about to list an item as outstanding, ask which agent owns that domain — money and invoicing to CorpBot, infra and tooling to DevOps, deal history to BizDev, assets to Index — and verify there first. Report the verified state. Routing the *action* to the owning agent stays correct; what changes is that the *status* gets verified rather than asked. See [[project_agent_registry]].

Sibling rule, one level down: [[feedback_check_activity_before_blocking]] covers the same instinct inside a single ticket — read the activity log, the parent epic and related tickets before calling something blocked. This memory is the cross-agent version of that.
