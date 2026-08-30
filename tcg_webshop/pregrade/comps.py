"""Validation and storage for the comp prices behind the EV box.

The engine reads comps from a `card.json` next to a card's photos. Nothing in
the pipeline invents a price, so an absent or malformed card.json is the single
reason the report says "comps saknas" instead of a number.

This module exists because the failure was silent. `run.load_comps` handed
whatever JSON it found straight to `value.expected_value`, which reads exactly
the keys `raw_sek` and `psa<N>_sek`. Write `psa10_price`, or a price as the
string "9000", and every lookup misses: no exception, no warning, just the same
"comps saknas" you get from having written nothing at all. Validating at the
boundary turns that into a message that names the key.

Schema (every field optional except that you need at least one price):

    {
      "card":   "Charizard VMAX 020/189",   free text, for the operator
      "set":    "Darkness Ablaze",          free text
      "raw_sek":   1200,                    what it sells for ungraded
      "psa10_sek": 9000,                    what it sells for at PSA 10
      "psa9_sek":  2600,                    ... and so on, psa1 through psa10
      "source": "eBay sold, 90d, n=12",     where the numbers came from
      "checked": "2026-08-30"               when they were last true
    }

`source` and `checked` are not used in the maths. They are here because a comp
price is a perishable fact, and a number with no provenance is not one you can
audit six months later when the submit call turns out to have been wrong.
"""

import json
import re
from datetime import date

GRADE_KEY = re.compile(r"^psa(\d{1,2})_sek$")

TEXT_FIELDS = ("card", "set", "source")
MAX_TEXT = 200

# A card priced above this is not something this tool should be quietly doing
# arithmetic on. The cap is a typo-catcher, not a market judgement: it is there
# to turn a fat-fingered 90000000 into an error instead of a submit call.
MAX_PRICE_SEK = 5_000_000

# Keys people reach for that the engine does not read. Mapping them to the real
# key by hand beats a fuzzy match, because a wrong guess here silently changes a
# price.
ALIASES = {
    "raw": "raw_sek",
    "raw_price": "raw_sek",
    "raw_sek_price": "raw_sek",
    "ungraded_sek": "raw_sek",
}


class CompsError(ValueError):
    """Raised for comps that cannot be stored. Message is operator-facing."""


def _price(value, key):
    if isinstance(value, bool):  # bool is an int in Python; never a price
        raise CompsError(f"{key}: {value!r} är inte ett pris")
    if not isinstance(value, (int, float)):
        raise CompsError(
            f"{key}: priser måste vara tal, inte {type(value).__name__} "
            f"({value!r}) — skriv 9000, inte \"9000\""
        )
    if value != value or value in (float("inf"), float("-inf")):
        raise CompsError(f"{key}: {value!r} är inte ett ändligt tal")
    if value <= 0:
        raise CompsError(f"{key}: priset måste vara större än noll, fick {value}")
    if value > MAX_PRICE_SEK:
        raise CompsError(
            f"{key}: {value:,.0f} kr är över taket {MAX_PRICE_SEK:,.0f} kr, "
            "troligen en felskrivning"
        )
    return float(value)


def validate(raw):
    """Normalise a comps dict. Returns (comps, warnings).

    Raises CompsError on anything that would otherwise store a price the engine
    cannot read, or read a price that is not one.
    """
    if not isinstance(raw, dict):
        raise CompsError(f"comps måste vara ett JSON-objekt, fick {type(raw).__name__}")

    out = {}
    warnings = []

    for key, value in raw.items():
        if not isinstance(key, str):
            raise CompsError(f"ogiltig nyckel: {key!r}")

        canonical = ALIASES.get(key, key)
        if canonical != key:
            warnings.append(f"{key} tolkades som {canonical}")

        if canonical == "raw_sek":
            out["raw_sek"] = _price(value, key)
            continue

        m = GRADE_KEY.match(canonical)
        if m:
            grade = int(m.group(1))
            if not 1 <= grade <= 10:
                raise CompsError(f"{key}: PSA-betyg går från 1 till 10, inte {grade}")
            out[f"psa{grade}_sek"] = _price(value, key)
            continue

        if canonical in TEXT_FIELDS:
            text = str(value).strip()[:MAX_TEXT]
            if text:
                out[canonical] = text
            continue

        if canonical == "checked":
            text = str(value).strip()[:MAX_TEXT]
            if text:
                out["checked"] = text
            continue

        # Unknown key. This is the case the whole module is for: refuse it
        # loudly rather than store a price nothing will ever read.
        raise CompsError(
            f"okänd nyckel {key!r}. Priser heter raw_sek och psa1_sek..psa10_sek; "
            f"övriga fält är {', '.join(TEXT_FIELDS)}, checked"
        )

    prices = [k for k in out if k.endswith("_sek")]
    if not prices:
        raise CompsError(
            "inga priser. Minst ett av raw_sek eller psa1_sek..psa10_sek krävs"
        )

    graded = sorted(
        (int(GRADE_KEY.match(k).group(1)), out[k]) for k in prices if GRADE_KEY.match(k)
    )

    if not graded:
        warnings.append(
            "bara raw_sek — utan minst ett psa<N>_sek går det inte att jämföra "
            "gradering mot att sälja rått"
        )
    if "raw_sek" not in out:
        warnings.append(
            "raw_sek saknas — rapporten visar nettot för en graderad försäljning "
            "men ingen skillnad och ingen rekommendation"
        )

    # A lower grade fetching more than a higher one is not impossible, but it is
    # almost always two prices swapped. Warn, do not refuse: the operator may
    # genuinely have a thin market where it is true.
    for (g_low, p_low), (g_high, p_high) in zip(graded, graded[1:]):
        if p_low > p_high:
            warnings.append(
                f"psa{g_low}_sek ({p_low:,.0f}) är högre än psa{g_high}_sek "
                f"({p_high:,.0f}) — priserna kan vara omkastade"
            )

    if "raw_sek" in out and graded and out["raw_sek"] > graded[-1][1]:
        warnings.append(
            f"raw_sek ({out['raw_sek']:,.0f}) är högre än det bästa graderade "
            "priset — då säger räkningen alltid sälj rått"
        )

    if "checked" not in out:
        warnings.append("checked saknas — comps åldras, datera dem")

    return out, warnings


def load(card_dir):
    """Read and validate card.json. Returns (comps, warnings, problem)."""
    path = card_dir / "card.json"
    if not path.exists():
        return None, [], None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [], f"card.json är inte giltig JSON: {exc}"
    try:
        comps, warnings = validate(raw)
    except CompsError as exc:
        return None, [], f"card.json: {exc}"
    return comps, warnings, None


def store(card_dir, raw):
    """Validate and write card.json. Returns (comps, warnings)."""
    comps, warnings = validate(raw)
    comps.setdefault("checked", date.today().isoformat())
    card_dir.mkdir(parents=True, exist_ok=True)
    (card_dir / "card.json").write_text(
        json.dumps(comps, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return comps, [w for w in warnings if not w.startswith("checked saknas")]
