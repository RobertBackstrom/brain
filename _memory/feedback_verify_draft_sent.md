---
name: verify-mail-status-against-live-gmail-never-from-memory
description: "Live Gmail is the single source of truth for draft/sent status — when reporting AND in every written record (output_log, trackers, wiki). Never from session memory; correct stale entries on sight. All projects, all agents."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0510e4d6-9262-4120-b007-7aad4de9fe5e
  modified: 2026-08-16T18:18:58.942Z
---

Before reporting the status of ANY email — draft pending, sent, awaiting reply — verify it against live Gmail. Never report mail status from your own session memory of "I created a draft earlier."

**Why:** Robert reviews and sends drafts manually, and acts on mail outside Claude's sessions. On 2026-05-20 Claude reported the Bibbi brand-pack email as "sits in Drafts, needs CC before sending" — based on memory of having created the draft — when Robert had already sent it hours earlier. The draft state in memory was stale; live Gmail was the truth. Robert's instruction: "check mail inbox status, not only memory."

**How to apply:**
- After creating a Gmail draft, before calling outreach complete: search `in:sent to:<recipient>` (or by subject) to confirm whether it actually went out.
- Before reporting a prospect as "awaiting reply" or "draft ready": re-pull the thread. A reply may have landed; the draft may have been sent and edited. `messageCount > 1` on a thread is a tell that the state moved.
- When recapping session status that includes mail, verify the live state of each mail item first — don't trust the recap you wrote earlier in the same session.
- **Before ASKING Robert to send a draft, or asking "where do things stand" — check `in:sent` FIRST.** Robert routinely sends drafts himself within minutes. Prompting him to send (or reconciling status) without checking Sent is the exact friction he wants gone. (2026-06 Formula Drone: Claude drafted the James headshot/bio mail AND the Bill+James pitch mail, then told Robert they were "ready to send" and asked where things stood at close — both were already sent, days earlier. Robert's instruction: "always check sent prior to asking me for drafts.")
- Update trackers/the deal wiki with the confirmed live status, not the assumed one.
- **Tooling trap (2026-07-03, Teef/Tom Storr):** `gmail_thread` / `gmail_read` render an *unsent draft* inline in the thread as if it were a real message, with a normal-looking messageId and date. Reading the thread alone will make you report a draft as "sent/replied." ALWAYS cross-check with `gmail_list_drafts` (filter by `threadId` or `to:`) before asserting an outbound message went out. If a message's id shows up in `gmail_list_drafts`, it is a draft, full stop — Robert has NOT sent it, and any promise it contains ("numbers by Thursday") was never made to the counterparty.

## The written record must track reality too (Robert, 2026-07-16)

**"Always use the actual status of draft and sent as source of truth. For all projects and agents everywhere."**

The rule isn't only about what you *say* in chat — it governs every durable artifact: `output_log.md`, deal wiki, trackers, followups, project memory, status reports.

- **A log entry is a claim about the world, not a diary of your intent.** Writing "Gmail-utkast (ej skickat)" is only true at the instant you write it. Robert routinely sends within minutes, so that line is often false by the next morning. Log the *outcome*, and if the outcome isn't known yet, say so in a way that invites correction ("utkast skapat, sändstatus ej verifierad") rather than asserting "ej skickat" as settled fact.
- **Correct stale entries on sight — including other agents' and other sessions'.** If you notice an old line saying "ej skickad" and `in:sent` shows it went out, fix it. Don't leave it because it isn't yours or isn't today's task. A wrong log is worse than no log: the next agent grounds on it and repeats the error. (Found 2026-07-16: the 2026-07-15 AP entry still called two Amer-mails "ej skickade" that Robert had sent at 19:10/19:11 the same evening.)
- **Re-verify before you write, not just before you speak.** Check `in:sent` / `gmail_list_drafts` at the moment of logging.
- Same principle for anything else with a real-world state behind it — signature status (query OpenSign live), payment status, publication status. The system of record wins over your memory of what you did.

## "Sent" is not the only thing to verify — check the recipient line too (2026-08-16)

When the *point* of a mail was to change **who is on the thread**, confirming that it sent proves
nothing. Verify the `To`/`Cc` of the sent message against the decision.

**Why:** On 2026-08-11, Robert decided to put Deema Almutairi (Merak Capital) and Andreea Chifu
back on the Exel accelerator thread after an earlier reply had dropped them. The mail went out on
time and carried its content correctly, so a plain `in:sent` check passed — but it went `To: Kelly
Zmak` only, and the re-add never happened. The consequence surfaced a day later: Kelly opened his
answer with "HI Robert and Andreea" and addressed it to Robert alone. He believed he had briefed
Andreea on a 23-team cohort roster she never received, and nobody knew.

**How to apply:** whenever a decision concerns distribution — loop someone in, drop someone, move
a person from Cc to To, take a thread private — read the sent message's recipient headers, not just
its presence in Sent. Same for forwards and intros. If the recipients do not match the decision,
say so immediately; a silently-missing recipient degrades quietly and is usually only discovered
through a downstream confusion like the one above.

Applies to all projects and all agents. Related: [[feedback_gmail_draft_dedup]], [[feedback_compare_draft_vs_sent]], [[feedback_inbox_convention]], [[output_log]].
