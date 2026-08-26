"""Expected-value math for a submission decision.

This is deliberately simple and its assumptions are all visible at the top of
the file. It answers one question: given a grade band and comp prices, is this
card worth the grading fee, or is it better sold raw?

Comps are not fetched here. They come from a card.json next to the photos, or
later from the Lister comp engine. Nothing invents a price.
"""

# Assumption block. Replace with real numbers once the PSA Europe dealer path is
# priced out (see web-scan.md, addendum on Frankfurt batch economics).
GRADING_COST_SEK = 450  # per card, landed: grading fee + share of shipping + insurance
SALES_FEE_PCT = 0.10  # marketplace cut on the eventual sale
MIN_EV_MARGIN_SEK = 250  # below this the hassle is not worth it


def grade_distribution(band, vision):
    """Probability per grade across the band.

    Weighted toward the bottom of the band when the criteria that actually
    separate a 9 from a 10 (surface, corners) could not be seen in the photos.
    """
    low = band.get("grade_low")
    high = band.get("grade_high")
    if low is None or high is None:
        return {}
    grades = list(range(int(low), int(high) + 1))
    if not grades:
        return {}
    if len(grades) == 1:
        return {grades[0]: 1.0}

    blind = 0
    if vision:
        if not (vision.get("surface") or {}).get("assessable", False):
            blind += 1
        if not (vision.get("corners") or {}).get("assessable", False):
            blind += 1

    # decay 1.0 means flat across the band, lower means pessimistic.
    decay = {0: 1.0, 1: 0.6, 2: 0.4}[blind]
    weights = [decay ** (high - g) for g in grades]
    total = sum(weights)
    return {g: w / total for g, w in zip(grades, weights)}


def expected_value(band, vision, comps):
    """Compare grading against selling raw.

    comps is a dict with any of raw_sek, psa10_sek, psa9_sek, psa8_sek, psa7_sek.
    Returns None when there is nothing to compute from.
    """
    if not comps:
        return None
    raw = comps.get("raw_sek")
    dist = grade_distribution(band, vision)
    if not dist:
        return None

    graded_gross = 0.0
    covered = 0.0
    for grade, p in dist.items():
        price = comps.get(f"psa{grade}_sek")
        if price is None:
            continue
        graded_gross += p * price
        covered += p

    if covered < 0.5:
        return {
            "computable": False,
            "reason": "comps saknas for storre delen av gradebandet",
            "distribution": dist,
        }

    # Renormalize over the grades we actually have comps for.
    graded_gross = graded_gross / covered
    graded_net = graded_gross * (1 - SALES_FEE_PCT) - GRADING_COST_SEK
    raw_net = raw * (1 - SALES_FEE_PCT) if raw is not None else None
    delta = graded_net - raw_net if raw_net is not None else None

    verdict = None
    if delta is not None:
        if delta >= MIN_EV_MARGIN_SEK:
            verdict = "GRADA"
        elif delta <= 0:
            verdict = "SALJ RAW"
        else:
            verdict = "MARGINELLT"

    return {
        "computable": True,
        "distribution": dist,
        "graded_gross_sek": graded_gross,
        "graded_net_sek": graded_net,
        "raw_net_sek": raw_net,
        "delta_sek": delta,
        "coverage": covered,
        "verdict": verdict,
        "assumptions": {
            "grading_cost_sek": GRADING_COST_SEK,
            "sales_fee_pct": SALES_FEE_PCT,
            "min_ev_margin_sek": MIN_EV_MARGIN_SEK,
        },
    }
