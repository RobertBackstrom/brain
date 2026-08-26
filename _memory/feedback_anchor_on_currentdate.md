---
name: anchor-on-currentdate
description: "Take \"today\" from the session currentDate context, never infer it from dates inside files"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d4e634eb-8bb2-459a-8528-e934a60c5e77
  modified: 2026-08-16T18:18:42.189Z
---

Anchor "today's date" on the session's `currentDate` system context. Never infer it from dates inside files - a document's "Prepared:" line, the newest activity-log entry, or a prior memory's date.

**Why:** On 2026-05-22 a PM session read the CUST migration dry-run's "Prepared: 2026-05-21" line plus the activity-log rhythm and operated as if today were 2026-05-21 - a full day off. That mis-stamped the activity log and agent learnings, and pushed a time-sensitive client migration and its team heads-up onto the wrong days. Conversations span days and context-summarisation boundaries; a file's date records when it was written, not today.

**How to apply:** At session start, read `currentDate` from context and treat it as ground truth. Re-derive every relative date - today, tomorrow, yesterday, "this weekend", T-1 - from it, not from a file. When a user says "tomorrow", compute it from `currentDate`. If a conversation has spanned days and a relative date is ambiguous, ask rather than guess. Applies to all agents, and especially PM and BizDev, which date-stamp logs, tickets, trackers, and outreach.

**Also never trust the shell `date` command for "today."** On 2026-07-03 a `date` call in the sandboxed Bash returned 2026-07-01 (two days off — sandbox clock skew) and that wrong value got stamped into the output log, agent learnings, and a ticket during `/close` before the real date was caught. The lesson from the original 2026-05-22 miss (reading a file's date) generalises: **the only trustworthy source of "today" is the session `currentDate` context** — not files, not activity-log rhythm, not `$(date)`. When you catch a stamped date that disagrees with `currentDate`, fix every place it landed.

**BUT `currentDate` itself goes stale in long-running sessions — corroborate before trusting it
blindly.** On 2026-08-16 a session that had spanned 10-16 August was still being injected with
`currentDate: 2026-08-12`. Following the rule above literally, the Assistant described a meeting
that had happened three days earlier as "tomorrow", and briefed Robert to prepare for a call that
was already past. Two independent sources contradicted the injected value: fresh Gmail timestamps
running to 16 August in **both** mailboxes, and the system clock.

**The refined rule:** `currentDate` is the default anchor and still beats any single file date or
a bare `$(date)` call. But it is a snapshot taken when the session started, not a live clock. When
**two or more independent, freshly-observed sources agree on a later date** — incoming mail
timestamps, calendar events, the system clock — they win, and `currentDate` is stale. The tell is
a session that has obviously run for days: multiple "Session ended" auto-entries on different
dates, or mail arriving that postdates `currentDate`. In that situation, check before you stamp
anything or compute any relative date, and say plainly which date you are using and why. A
mis-stamped log is recoverable; telling Robert to prepare for a meeting he already missed is not.

**Where this bites most: agent-learning entries and output logs.** Every `[YYYY-MM-DD]` you append to `agents/memory/*_learnings.md`, an `output_log.md`, or a ticket must equal `currentDate`. This is the step agents most often skip while heads-down in the work. The memory-write ritual now names it explicitly — see [[feedback_memory_write_protocol]] "Date-stamp check."

**The failure mode that got past all of the above (k2c, 2026-08-24).** The rule was still read as
"do not trust a stale `currentDate`". The actual miss was the mirror image: `currentDate` said
Monday 24 Aug, and a rolling log ticket's newest entry said the 20th, so the 20th became "today"
and a whole PM run processed the wrong four days of meetings. **A rolling log stops updating when
nobody runs it, so its last entry dates the last run, never the present.** Same for a file's
`updated:` frontmatter and its filesystem mtime, which agreed with each other and were both wrong.

**Read `currentDate` before opening any log, and resolve what "yesterday", "since Friday" and
"today" mean in absolute dates before touching the material.** If the newest entry in a rolling
source predates `currentDate`, that gap is the thing to investigate, not a definition of now. The
two-independent-sources override above still applies, but it takes *incoming* evidence such as mail
timestamps or calendar events, and a stale internal log is never that.

**Återfall 2026-08-26, och lärdomen är *när* kontrollen ska ske.** `currentDate` sa 24
augusti, verkligheten var den 26:e. Sessionen hann stämpla fjorton filer plus en
**klientfacing sida som skulle vidare till en partners finansiärer** med fel datum, och
felet fångades först av mailkontrollen i `/close`. Overriden i stycket ovan fungerade
exakt som beskriven, sent-mailens tidsstämplar och systemklockan pekade båda på den 26:e,
men den kördes två timmar för sent.

**Regeln som saknades:** kör korroboreringen **innan den första daterade artefakten
skrivs**, inte vid stängning. Triggern är enkel: så fort en session ska producera något
daterat som lämnar huset (en pitchsida, ett avtal, ett mail, en offert med kurs- eller
referensdatum), verifiera datumet mot en färsk extern källa först. Det kostar ett
verktygsanrop. Att rätta i efterhand kostade här fjorton filer, en ompublicering och en
omhämtad växelkurs, och hade sidan gått ut under tiden hade den burit fel datum hos en
finansiär.

