"""Self-test for the centering measurement.

Renders synthetic cards with known border widths, runs them through the real
measurement path, and checks the reported ratios. This is how we know the
number in the report means what it says without needing a graded card on hand.

    python3 -m pregrade.selftest
"""

import sys
import tempfile
from pathlib import Path

import cv2
import numpy as np

from . import centering, psa

BORDER_BGR = (70, 215, 245)  # Pokemon yellow
ART_BGR = (55, 45, 40)
BG_BGR = (95, 95, 95)


def render_card(left, right, top, bottom, rotate_deg=0.0, card_w=630, card_h=880):
    """Card with the given border widths, laid on a contrasting background."""
    card = np.full((card_h, card_w, 3), BORDER_BGR, dtype=np.uint8)
    # cv2.rectangle endpoints are inclusive, so subtract one to make the right
    # and bottom borders exactly `right` and `bottom` pixels wide.
    cv2.rectangle(
        card, (left, top), (card_w - right - 1, card_h - bottom - 1), ART_BGR, -1
    )
    # A bit of texture inside the art box so it is not a flat fill.
    cv2.circle(card, (card_w // 2, card_h // 2), 90, (120, 90, 70), -1)

    pad = 220
    canvas = np.full((card_h + 2 * pad, card_w + 2 * pad, 3), BG_BGR, dtype=np.uint8)
    canvas[pad : pad + card_h, pad : pad + card_w] = card

    if rotate_deg:
        h, w = canvas.shape[:2]
        m = cv2.getRotationMatrix2D((w / 2, h / 2), rotate_deg, 1.0)
        canvas = cv2.warpAffine(canvas, m, (w, h), borderValue=BG_BGR)
    return canvas


def check(name, left, right, top, bottom, rotate_deg=0.0, tol=1.2):
    expected_l = 100.0 * left / (left + right)
    expected_t = 100.0 * top / (top + bottom)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "front.png"
        cv2.imwrite(str(path), render_card(left, right, top, bottom, rotate_deg))
        m = centering.measure(path)

    if not m.get("ok"):
        print(f"FAIL {name}: measurement failed ({m.get('reason')})")
        return False

    got_l = m["horizontal"]["left_pct"]
    got_t = m["vertical"]["top_pct"]
    dl = abs(got_l - expected_l)
    dt = abs(got_t - expected_t)
    ok = dl <= tol and dt <= tol

    # Report the cap from the limiting axis, the same way the pipeline does it.
    axis, worse_pct, _ = psa.worse_axis(m)
    cap = psa.centering_cap(worse_pct, "front")
    print(
        f"{'PASS' if ok else 'FAIL'} {name}: "
        f"H {got_l:.1f}/{100 - got_l:.1f} (vantat {expected_l:.1f}, av {dl:.1f}), "
        f"V {got_t:.1f}/{100 - got_t:.1f} (vantat {expected_t:.1f}, av {dt:.1f}), "
        f"tak PSA {cap} ({axis}), matsakerhet {m['confidence']}"
    )
    return ok


def main():
    cases = [
        ("perfekt centrering", 45, 45, 45, 45, 0.0),
        ("55/45 gransfall for 10", 40, 49, 45, 45, 0.0),
        ("62/38 takas pa 9", 34, 55, 45, 45, 0.0),
        ("68/32 takas pa 8", 29, 61, 45, 45, 0.0),
        ("vertikalt skev 70/30", 45, 45, 27, 63, 0.0),
        ("roterad 7 grader", 40, 49, 45, 45, 7.0),
        ("roterad 12 grader, skev", 34, 55, 38, 52, 12.0),
    ]
    results = [check(*c) for c in cases]

    print()
    tolerance_cases = [(54.0, 10), (55.0, 10), (56.0, 9), (60.0, 9), (66.0, 7), (88.0, 4)]
    for pct, expected in tolerance_cases:
        got = psa.centering_cap(pct, "front")
        mark = "PASS" if got == expected else "FAIL"
        print(f"{mark} tolerans {pct:.0f}/{100 - pct:.0f} -> PSA {got} (vantat {expected})")
        results.append(got == expected)

    passed = sum(1 for r in results if r)
    print(f"\n{passed}/{len(results)} tester ok")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
