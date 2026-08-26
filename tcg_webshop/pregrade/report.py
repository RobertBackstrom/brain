"""Per-card markdown report and per-batch CSV summary."""

import csv

from . import centering as centering_mod
from . import psa

CSV_FIELDS = [
    "card_id",
    "name",
    "set",
    "number",
    "finish",
    "grade_low",
    "grade_high",
    "centering_cap",
    "front_centering",
    "back_centering",
    "limiting_factor",
    "call",
    "ev_verdict",
    "ev_delta_sek",
    "warnings",
]


def _ratio(m):
    if not m or not m.get("ok"):
        return ""
    h = m["horizontal"]
    v = m["vertical"]
    return f"{h['left_pct']:.0f}/{h['right_pct']:.0f} LR, {v['top_pct']:.0f}/{v['bottom_pct']:.0f} TB"


def card_markdown(card_id, shots, cf, cb, vision, band, call, reason, warnings, ev):
    card = (vision or {}).get("card") or {}
    lines = []
    lines.append(f"# Pre-grade: {card.get('name') or card_id}")
    lines.append("")
    ident = ", ".join(
        x for x in [card.get("set_or_series"), card.get("number"), card.get("finish")] if x
    )
    if ident:
        lines.append(f"**Kort:** {ident}")
    lines.append(f"**Mapp:** `{card_id}`")
    lines.append("")

    lines.append("## Utfall")
    lines.append("")
    if band.get("grade_low") is not None and band.get("grade_high") is not None:
        lo, hi = band["grade_low"], band["grade_high"]
        span = f"PSA {lo}" if lo == hi else f"PSA {lo} till {hi}"
        lines.append(f"**Trolig grade:** {span} ({psa.GRADE_LABELS.get(hi, '')})")
    else:
        lines.append("**Trolig grade:** gar inte att bedoma pa dessa bilder")
    lines.append(f"**Begransande faktor:** {band.get('limiting_factor')}")
    lines.append(f"**Rekommendation:** {call}. {reason}")
    lines.append("")

    lines.append("## Centrering (uppmatt optiskt)")
    lines.append("")
    lines.append(f"- Framsida: {centering_mod.format_measurement(cf)}")
    lines.append(f"- Baksida: {centering_mod.format_measurement(cb)}")
    if band.get("all_caps"):
        for cap in band["all_caps"]:
            lines.append(f"- {cap}")
    lines.append("")
    lines.append(
        "PSA-toleranser framsida: 10 kraver 55/45 eller battre, 9 tillater 60/40, "
        "8 tillater 65/35, 7 tillater 70/30."
    )
    lines.append("")

    if vision:
        lines.append("## Skick")
        lines.append("")
        for key, label in [("corners", "Horn"), ("edges", "Kanter"), ("surface", "Yta")]:
            block = vision.get(key) or {}
            flag = "" if block.get("assessable") else " (EJ BEDOMBAR pa dessa bilder)"
            lines.append(f"**{label}{flag}** - tak {block.get('grade_ceiling')}")
            lines.append("")
            lines.append(block.get("observations", ""))
            lines.append("")
        if vision.get("print_defects"):
            lines.append("**Tryckfel:** " + "; ".join(vision["print_defects"]))
            lines.append("")
        if vision.get("authenticity_flags"):
            lines.append("**Aktahets-flaggor:** " + "; ".join(vision["authenticity_flags"]))
            lines.append("")
        if vision.get("notes"):
            lines.append(vision["notes"])
            lines.append("")

    if ev and ev.get("computable"):
        lines.append("## Ekonomi")
        lines.append("")
        lines.append(f"- Forvantat brutto graderat: {ev['graded_gross_sek']:.0f} kr")
        lines.append(f"- Netto efter avgifter och grading: {ev['graded_net_sek']:.0f} kr")
        if ev.get("raw_net_sek") is not None:
            lines.append(f"- Netto om saljs raw: {ev['raw_net_sek']:.0f} kr")
            lines.append(f"- Skillnad: {ev['delta_sek']:+.0f} kr")
        lines.append(f"- **Slutsats: {ev['verdict']}**")
        lines.append("")
        dist = ", ".join(f"PSA {g}: {p*100:.0f}%" for g, p in sorted(ev["distribution"].items()))
        lines.append(f"Antagen gradefordelning: {dist}")
        a = ev["assumptions"]
        lines.append(
            f"Antaganden: {a['grading_cost_sek']} kr per kort i gradingkostnad, "
            f"{a['sales_fee_pct']*100:.0f}% saljavgift."
        )
        lines.append("")
    elif ev:
        lines.append("## Ekonomi")
        lines.append("")
        lines.append(f"Ej berakningsbar: {ev.get('reason')}")
        lines.append("")
    else:
        lines.append("## Ekonomi")
        lines.append("")
        lines.append(
            "Inga comps angivna. Lagg en `card.json` bredvid bilderna med "
            "`raw_sek`, `psa9_sek`, `psa10_sek` sa raknas EV ut."
        )
        lines.append("")

    if warnings:
        lines.append("## Sa har langt racker bilderna inte")
        lines.append("")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")

    lines.append("## Underlag")
    lines.append("")
    for label, path in shots.items():
        lines.append(f"- {label}: `{path.name}`")
    lines.append("")
    return "\n".join(lines)


def csv_row(card_id, cf, cb, vision, band, call, ev, warnings):
    card = (vision or {}).get("card") or {}
    return {
        "card_id": card_id,
        "name": card.get("name", ""),
        "set": card.get("set_or_series", ""),
        "number": card.get("number", ""),
        "finish": card.get("finish", ""),
        "grade_low": band.get("grade_low", ""),
        "grade_high": band.get("grade_high", ""),
        "centering_cap": band.get("centering_cap", ""),
        "front_centering": _ratio(cf),
        "back_centering": _ratio(cb),
        "limiting_factor": band.get("limiting_factor", ""),
        "call": call,
        "ev_verdict": (ev or {}).get("verdict", ""),
        "ev_delta_sek": f"{ev['delta_sek']:.0f}" if ev and ev.get("delta_sek") is not None else "",
        "warnings": " | ".join(warnings),
    }


def write_summary(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
