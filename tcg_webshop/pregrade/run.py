"""Batch runner: photo folder in, pre-grade report out.

    python3 -m pregrade.run --batch 2026-08-03

Layout it expects:

    intake/<batch>/<card-id>/front.jpg
                            /back.jpg
                            /corner-tl.jpg      (optional)
                            /raking.jpg         (optional)
                            /card.json          (optional comps)

Writes reports/<batch>/<card-id>.md and reports/<batch>/summary.csv.
Processed folders are moved to intake/_processed/<batch>/ unless --keep is set.
"""

import argparse
import json
import shutil
import sys
import traceback
from pathlib import Path

from . import centering, psa, report, value, vision

ROOT = Path(__file__).resolve().parent.parent
INTAKE = ROOT / "intake"
REPORTS = ROOT / "reports"

IMAGE_EXT = {".jpg", ".jpeg", ".png", ".heic", ".webp", ".tif", ".tiff"}


def classify_shots(card_dir):
    """Map photos to roles by filename. Unmatched images become extra shots."""
    shots = {}
    extras = []
    for path in sorted(card_dir.iterdir()):
        if path.suffix.lower() not in IMAGE_EXT:
            continue
        stem = path.stem.lower()
        if stem.startswith("front") or stem.startswith("fram"):
            shots["front"] = path
        elif stem.startswith("back") or stem.startswith("bak"):
            shots["back"] = path
        elif stem.startswith(("corner", "horn")):
            shots[f"corner:{stem}"] = path
        elif stem.startswith(("raking", "angle", "snedljus")):
            shots["raking light"] = path
        else:
            extras.append(path)
    for path in extras:
        shots[f"extra:{path.stem}"] = path
    return shots


def load_comps(card_dir):
    meta = card_dir / "card.json"
    if not meta.exists():
        return None
    try:
        return json.loads(meta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"  ! card.json is not valid JSON, ignoring: {exc}", file=sys.stderr)
        return None


def process_card(card_dir, use_vision=True, backend=None):
    shots = classify_shots(card_dir)
    if not shots:
        raise ValueError("no images in folder")
    if "front" not in shots:
        raise ValueError("no front photo (name it front.jpg)")

    cf = centering.measure(shots["front"])
    cb = centering.measure(shots["back"]) if "back" in shots else None

    result = None
    if use_vision:
        result = vision.assess(shots, cf, cb, backend=backend)

    band = psa.synthesize(cf, cb, result or {})
    call, reason = psa.submit_call(band, result)
    warnings = psa.photo_quality_warnings(result, cf, cb)
    ev = value.expected_value(band, result, load_comps(card_dir))

    return {
        "shots": shots,
        "centering_front": cf,
        "centering_back": cb,
        "vision": result,
        "band": band,
        "call": call,
        "reason": reason,
        "warnings": warnings,
        "ev": ev,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Pre-grade a batch of card photos.")
    parser.add_argument("--batch", required=True, help="folder name under intake/")
    parser.add_argument("--intake", default=str(INTAKE))
    parser.add_argument("--out", default=str(REPORTS))
    parser.add_argument(
        "--no-vision",
        action="store_true",
        help="centering only, no API call (fast, free, no condition assessment)",
    )
    parser.add_argument("--keep", action="store_true", help="do not move folders to _processed")
    parser.add_argument(
        "--backend",
        choices=["cli", "api"],
        help="cli = claude CLI on the Max subscription (default), api = console API key",
    )
    args = parser.parse_args(argv)

    batch_dir = Path(args.intake) / args.batch
    if not batch_dir.is_dir():
        parser.error(f"no such batch: {batch_dir}")

    out_dir = Path(args.out) / args.batch
    out_dir.mkdir(parents=True, exist_ok=True)

    card_dirs = sorted(d for d in batch_dir.iterdir() if d.is_dir() and not d.name.startswith("_"))
    if not card_dirs:
        parser.error(f"no card folders in {batch_dir}")

    if not args.no_vision:
        print(f"vision: {vision.resolve_model()} via {args.backend or 'auto'} backend")

    rows = []
    failures = []
    for card_dir in card_dirs:
        card_id = card_dir.name
        print(f"[{card_id}] processing...")
        try:
            res = process_card(card_dir, use_vision=not args.no_vision, backend=args.backend)
        except Exception as exc:  # keep the batch going, report at the end
            print(f"  ! failed: {exc}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            failures.append((card_id, str(exc)))
            continue

        md = report.card_markdown(
            card_id,
            res["shots"],
            res["centering_front"],
            res["centering_back"],
            res["vision"],
            res["band"],
            res["call"],
            res["reason"],
            res["warnings"],
            res["ev"],
        )
        (out_dir / f"{card_id}.md").write_text(md, encoding="utf-8")
        rows.append(
            report.csv_row(
                card_id,
                res["centering_front"],
                res["centering_back"],
                res["vision"],
                res["band"],
                res["call"],
                res["ev"],
                res["warnings"],
            )
        )
        band = res["band"]
        print(
            f"  -> PSA {band.get('grade_low')}-{band.get('grade_high')}, "
            f"{res['call']} ({band.get('limiting_factor')})"
        )

        if not args.keep:
            dest = Path(args.intake) / "_processed" / args.batch / card_id
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                shutil.rmtree(dest)
            shutil.move(str(card_dir), str(dest))

    if rows:
        report.write_summary(out_dir / "summary.csv", rows)
        print(f"\n{len(rows)} kort klara. Rapporter: {out_dir}")
    if failures:
        print(f"\n{len(failures)} misslyckades:")
        for card_id, err in failures:
            print(f"  - {card_id}: {err}")
    return 1 if failures and not rows else 0


if __name__ == "__main__":
    sys.exit(main())
