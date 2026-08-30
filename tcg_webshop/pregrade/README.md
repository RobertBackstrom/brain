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
| `comps.py` | card.json schema, validation, storage |
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

## Comp prices (`card.json`)

The EV box stays empty until a card has prices. They live in a `card.json` next
to the photos, and `comps.py` is the only thing that reads or writes it.

```json
{
  "card": "Charizard VMAX 020/189",
  "set": "Darkness Ablaze",
  "raw_sek": 1200,
  "psa10_sek": 9000,
  "psa9_sek": 2600,
  "psa8_sek": 1500,
  "source": "eBay sold, 90d, n=12",
  "checked": "2026-08-30"
}
```

Prices are `raw_sek` and `psa1_sek` through `psa10_sek`, in kronor, as numbers.
Everything is optional except that at least one price has to be there.

Two behaviours worth knowing:

- **Unknown keys are an error, not a shrug.** `value.py` reads exactly these key
  names. Writing `psa10_price`, or `"9000"` as a string, used to miss every
  lookup silently and produce the same "comps saknas" as an unpriced card. The
  validator names the offending key instead.
- **`raw_sek` is what produces a recommendation.** With graded prices only, the
  report gives the net for a graded sale and stops. It does not compare against
  a raw sale it has no price for, and it does not print a zero in place of one.

`source` and `checked` are not used in the maths. A comp price is perishable,
and a number with no provenance is not one you can audit later when the submit
call turns out to have been wrong. `checked` is stamped with today's date when
comps arrive through the API.

Over HTTP, `PUT /api/cards/<batch>/<card>/comps` replaces the document and
reprices the card from the stored grade band, without touching the photos or
paying for another vision pass. See `api/README` notes in `api/server.py`.

## Tests

```bash
python3 -m pregrade.selftest   # centering measurement, needs OpenCV
python3 api/test_api.py        # HTTP API, comps and EV; stubs OpenCV
```

`selftest` renders synthetic cards with known border widths, pushes them through
the real measurement path, and checks the reported ratios and the tolerance
table.

`test_api` runs the real server on a loopback port. It stubs `cv2` and `numpy`,
so it runs on a box with no OpenCV: nothing it covers reaches the measurement or
the vision pass.

## Known limits

- Centering is accurate to roughly 1 percentage point. A card sitting exactly on
  a tolerance boundary (55/45 for a 10, 60/40 for a 9) can flip either way, so
  treat boundary cases as unresolved rather than decided.
- The border scan assumes a card with a distinct printed frame. Full-art and
  borderless cards have no clean transition to find; the measurement will either
  fail loudly or report low confidence. Do not trust a low-confidence number.
- No comp fetching. Prices are entered by hand, through the app or a `PUT` to
  the comps endpoint, and land in `card.json`. An automated source would be the
  Lister comp engine, which is itself deferred (`mkt-007`). Nothing here invents
  a price.
- Grading cost assumptions in `value.py` are placeholders until the PSA Europe
  dealer path is actually priced.
