"""PSA grade tolerances and band synthesis.

Centering is the only PSA criterion with published numeric tolerances, so it is
the only one we compute deterministically. Everything else (corners, edges,
surface) comes from the vision pass and is treated as a soft signal.
"""

# Highest grade allowed at a given centering ratio, expressed as the larger of
# the two side percentages (55/45 -> 55). Source: PSA published grading standards.
FRONT_TOLERANCE = [(10, 55), (9, 60), (8, 65), (7, 70), (6, 80), (5, 85)]
BACK_TOLERANCE = [(10, 75), (9, 90), (8, 90), (7, 90), (6, 90), (5, 90)]

GRADE_LABELS = {
    10: "Gem Mint",
    9: "Mint",
    8: "NM-MT",
    7: "NM",
    6: "EX-MT",
    5: "EX",
    4: "VG-EX or lower",
}


def centering_cap(worse_pct, side="front"):
    """Highest grade the measured centering still permits.

    worse_pct is the larger side percentage of the worse axis, e.g. 62.0 for a
    62/38 card. Returns 4 as a floor meaning "capped below EX".
    """
    table = FRONT_TOLERANCE if side == "front" else BACK_TOLERANCE
    for grade, tol in table:
        if worse_pct <= tol + 1e-9:
            return grade
    return 4


def worse_axis(measurement):
    """Pick the limiting axis from a centering measurement.

    Returns (axis_name, worse_pct, ratio_string).
    """
    h = measurement["horizontal"]
    v = measurement["vertical"]
    h_worse = max(h["left_pct"], h["right_pct"])
    v_worse = max(v["top_pct"], v["bottom_pct"])
    if h_worse >= v_worse:
        return "horizontal", h_worse, f"{h['left_pct']:.0f}/{h['right_pct']:.0f} L/R"
    return "vertical", v_worse, f"{v['top_pct']:.0f}/{v['bottom_pct']:.0f} T/B"


def synthesize(centering_front, centering_back, vision):
    """Combine the deterministic centering cap with the vision assessment.

    Returns a dict with the grade band, the limiting factor, and a submit call.
    """
    caps = []
    limiters = []

    if centering_front and centering_front.get("ok"):
        axis, pct, ratio = worse_axis(centering_front)
        cap = centering_cap(pct, "front")
        caps.append(cap)
        limiters.append(f"front centering {ratio} ({axis}) caps at {cap}")

    if centering_back and centering_back.get("ok"):
        axis, pct, ratio = worse_axis(centering_back)
        cap = centering_cap(pct, "back")
        caps.append(cap)
        limiters.append(f"back centering {ratio} ({axis}) caps at {cap}")

    v_low = vision.get("estimated_grade_low") if vision else None
    v_high = vision.get("estimated_grade_high") if vision else None

    hard_cap = min(caps) if caps else None

    if hard_cap is not None and v_high is not None:
        high = min(hard_cap, v_high)
    elif hard_cap is not None:
        high = hard_cap
    else:
        high = v_high

    low = v_low if v_low is not None else (high - 1 if high else None)
    if low is not None and high is not None:
        low = min(low, high)

    # The limiting factor is whichever constraint actually binds the top of the band.
    if hard_cap is not None and (v_high is None or hard_cap <= v_high):
        limiting = limiters[caps.index(hard_cap)]
    elif vision:
        limiting = vision.get("limiting_factor") or "condition (see vision notes)"
    else:
        limiting = "unknown (no vision pass, no usable centering measurement)"

    return {
        "grade_low": low,
        "grade_high": high,
        "centering_cap": hard_cap,
        "vision_low": v_low,
        "vision_high": v_high,
        "limiting_factor": limiting,
        "all_caps": limiters,
    }


def submit_call(band, vision):
    """Blunt submit / skip recommendation, independent of card value.

    Value-aware EV lives in value.py and overrides this when comps exist.
    """
    high = band.get("grade_high")
    if high is None:
        return "OKLART", "Otillracklig data for att bedoma. Fota om enligt protokollet."
    if high >= 10:
        return "SKICKA IN", "10 ar mojlig. Vardet av en 10 motiverar nastan alltid gradingavgiften."
    if high == 9:
        return "KANSKE", "Takas pa 9. Lonar sig bara om PSA 9-comp klart overstiger raw + avgift."
    if high == 8:
        return "SKIPPA", "Takas pa 8. Sall en 8 som raw eller i bulk, gradingavgiften ater marginalen."
    return "SKIPPA", f"Takas pa {high}. Inte vart en inskickning."


def photo_quality_warnings(vision, centering_front, centering_back):
    """Collect the reasons this assessment should not be trusted too far."""
    warnings = []
    if centering_front and not centering_front.get("ok"):
        warnings.append(
            "Framsidans centrering gick inte att mata: " + str(centering_front.get("reason"))
        )
    if centering_back and not centering_back.get("ok"):
        warnings.append(
            "Baksidans centrering gick inte att mata: " + str(centering_back.get("reason"))
        )
    if centering_front and centering_front.get("ok") and centering_front.get("confidence") == "low":
        warnings.append("Lag matsakerhet pa framsidans centrering, spretiga kantavlasningar.")
    if not vision:
        return warnings
    pq = vision.get("photo_quality") or {}
    if not pq.get("raking_light_present"):
        warnings.append(
            "Inget snedljusfoto. Ytrepor i folien ar i praktiken osynliga, "
            "sa skillnaden mellan 9 och 10 gar inte att avgora."
        )
    if not pq.get("corner_macros_present"):
        warnings.append("Inga hornnarbilder. Hornbedomningen ar en gissning.")
    if not pq.get("front_straight_on"):
        warnings.append("Framsidan ar inte tagen rakt ovanifran. Centreringsmatningen blir skev.")
    if not pq.get("sharp"):
        warnings.append("Oskarp bild. Ytan och kanterna gar inte att bedoma.")
    for issue in pq.get("issues") or []:
        warnings.append(issue)
    return warnings
