---
project: db
status: open
priority: low
updated: 2026-09-03
created: 2026-09-03
type: task
owner: DevOps
---

## nd-discord-read.js returns a silent, convincing "0 messages" when given a bad argument

`assistant/nd-discord-read.js` takes **positional** args (`[perChannelLimit] [sinceDays]`), but nothing
validates them. Called with a flag style instead — `node assistant/nd-discord-read.js --days 400` — it
does this:

- `PER = parseInt('--days')` → `NaN`
- the fetch loop guard is `while (all.length < PER)` → `0 < NaN` → `false`, so it **never fetches**
- `SINCE_DAYS` still picks up `400` from the second arg, so the header prints a plausible
  `#### #ark-bugs  (0 msgs in last 400d)`
- exit code **0**

Output is indistinguishable from "the channels are genuinely empty". During the 2026-09-03 ND pass this
produced a confident wrong reading — all four ARK channels reported zero over 400 days, which looked
like the Death Board bot had lost guild access, and was very nearly filed as a bot-token regression.
Re-run as `node assistant/nd-discord-read.js 100 45` and it returns 27 messages across the channels,
including the reports that were then attached to ND-11.

The bot and its channel access are **fine**. This is purely an input-handling footgun, and it is the
worst kind: a read tool that fails closed and quiet, on a project where "the community has gone silent"
is a believable answer.

**Fix (small):**
1. Reject / warn on `NaN` after `parseInt`, or fall back to the documented defaults (100 / 90).
2. Accept `--limit` / `--days` flags as well as positionals, since that is what a caller reaches for.
3. Make an empty result distinguishable from a failed one — print the fetch count attempted, or exit
   non-zero when zero messages were fetched across *every* channel.

Worth a sweep for the same pattern in the sibling read scripts (`nd-seed-backlog.js`, the cm-* readers)
— any `parseInt(process.argv[n])` feeding a loop bound has the same failure shape.

Source: ND PS5-testing pass, 2026-09-03.
