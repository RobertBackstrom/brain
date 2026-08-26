# pregrade

Photo folder in, PSA pre-grade report out. Phase 1 of the TCG grading-concierge
track (tcg-001): the filter that decides which cards are worth a submission fee.

Robert-facing shooting instructions live in `../PHOTO_PROTOCOL.md`.

## Design

The pipeline deliberately splits what can be **measured** from what can only be
**estimated**, and never lets a model do the first job.

| Criterion | How | Why |
|---|---|---|
| Centering | OpenCV: card quad detection, perspective warp, colour-transition scan from each edge | The only PSA criterion with published numeric tolerances, so it should be measured, not guessed. Accurate to about 1 percentage point on synthetic tests. |
| Corners, edges, surface, print, authenticity | Vision model over the photos | No numeric standard exists. The model is told the measured centering as fact and forbidden from re-estimating it. |
| Grade band | `psa.synthesize()` takes the minimum of the centering cap and the vision ceiling | The band top is whatever binds first. |
| Submit / skip | `psa.submit_call()`, overridden by `value.expected_value()` when comps exist | Condition alone answers "can it grade well"; comps answer "is it worth it". |

The vision prompt hard-codes two honesty rules: without a raking-light shot,
surface is marked unassessable and capped at 9; without corner macros, corners
are capped at 9. So the tool cannot report "10 likely" off a single flat phone
photo, which is the failure mode that would make it useless.

## Files

| File | Role |
|---|---|
| `centering.py` | Card detection, perspective warp, border measurement |
| `psa.py` | PSA tolerance tables, grade-band synthesis, submit call |
| `vision.py` | Condition assessment, two backends (see below) |
| `value.py` | Grade distribution and EV against comps |
| `report.py` | Per-card markdown, per-batch CSV |
| `run.py` | Batch CLI |
| `selftest.py` | Synthetic cards with known centering, validates the measurement |

## Backends

`vision.py` defaults to the **CLI backend**: it shells out to `claude -p` exactly
the way `assistant/server.js` does, so it runs on Robert's Max subscription with
no console API key. That matches the VPS reality since db-036 (2026-04-16), when
`ANTHROPIC_API_KEY` was commented out of `assistant/.env` in favour of the
subscription.

If `ANTHROPIC_API_KEY` is ever set again, the SDK backend takes over
automatically and uses structured outputs (`output_config.format`) for a
schema-guaranteed response. Force either with `--backend cli|api` or
`PREGRADE_BACKEND`.

Note: spawning the CLI from **inside** an interactive Claude Code session is
blocked by the permission classifier. Run batches from a plain shell, cron, or a
systemd unit. `--no-vision` works anywhere.

## Model

Resolved from `assistant/config.json` `agent_governance.model_tiers.opus`, never
hardcoded, per the project model-routing rules. `PREGRADE_MODEL` overrides for a
one-off run.

## Tests

```bash
python3 -m pregrade.selftest
```

Renders synthetic cards with known border widths, pushes them through the real
measurement path, and checks the reported ratios and the tolerance table.

## Known limits

- Centering is accurate to roughly 1 percentage point. A card sitting exactly on
  a tolerance boundary (55/45 for a 10, 60/40 for a 9) can flip either way, so
  treat boundary cases as unresolved rather than decided.
- The border scan assumes a card with a distinct printed frame. Full-art and
  borderless cards have no clean transition to find; the measurement will either
  fail loudly or report low confidence. Do not trust a low-confidence number.
- No comp fetching. Prices come from `card.json` or, later, the Lister comp
  engine. Nothing here invents a price.
- Grading cost assumptions in `value.py` are placeholders until the PSA Europe
  dealer path is actually priced.
