"""Deterministic centering measurement from a straight-on card photo.

The pipeline is: find the card quad in the photo, warp it to a normalized
rectangle, then walk inward from each edge until the border colour changes.
That transition is the printed frame, and the four distances to it are what
PSA's centering tolerances are expressed in.

This is the only part of the pre-grade that is measured rather than estimated,
so it is kept separate from the vision pass and never asks a model for a number.
"""

import cv2
import numpy as np

# Standard TCG card is 63 x 88 mm. Warping to a fixed size normalizes the
# measurement regardless of how far away the photo was taken.
CARD_W = 716
CARD_H = 1000

# Colour distance (CIELab) that counts as leaving the border.
DELTA_THRESHOLD = 16.0
# How many consecutive pixels must exceed it, to ignore dust and JPEG noise.
RUN_LENGTH = 4
# Fraction of each dimension to search inward before giving up on that scan line.
MAX_SEARCH = 0.30
# Skip this fraction at both ends of each edge so corners and rounded radii
# do not pollute the border colour sample.
EDGE_MARGIN = 0.18
SCAN_LINES = 41


def load_image(path, max_side=2400):
    img = cv2.imread(str(path))
    if img is None:
        raise ValueError(f"could not read image: {path}")
    h, w = img.shape[:2]
    scale = max_side / float(max(h, w))
    if scale < 1.0:
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
    return img


def _order_points(pts):
    """Return the quad as top-left, top-right, bottom-right, bottom-left."""
    pts = pts.reshape(4, 2).astype("float32")
    ordered = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    ordered[0] = pts[np.argmin(s)]
    ordered[2] = pts[np.argmax(s)]
    d = np.diff(pts, axis=1)
    ordered[1] = pts[np.argmin(d)]
    ordered[3] = pts[np.argmax(d)]
    return ordered


def find_card_quad(img):
    """Locate the card outline. Returns (quad, method) or (None, reason)."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 40, 130)
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8), iterations=2)
    edges = cv2.erode(edges, np.ones((3, 3), np.uint8), iterations=1)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None, "no contours found (is the card on a contrasting background?)"

    img_area = float(img.shape[0] * img.shape[1])
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:6]

    for c in contours:
        area = cv2.contourArea(c)
        if area < 0.12 * img_area:
            continue
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            return _order_points(approx), "quad"

    # Fall back to the minimum-area rectangle of the largest plausible contour.
    for c in contours:
        if cv2.contourArea(c) < 0.12 * img_area:
            continue
        box = cv2.boxPoints(cv2.minAreaRect(c))
        return _order_points(np.array(box)), "minAreaRect"

    return None, "card outline too small in frame (fill at least 35% of the shot)"


def warp_card(img, quad):
    dst = np.array([[0, 0], [CARD_W - 1, 0], [CARD_W - 1, CARD_H - 1], [0, CARD_H - 1]], "float32")
    m = cv2.getPerspectiveTransform(quad, dst)
    return cv2.warpPerspective(img, m, (CARD_W, CARD_H))


def _delta_e(lab_a, lab_b):
    return float(np.linalg.norm(lab_a.astype(np.float32) - lab_b.astype(np.float32)))


def _scan_side(lab, side):
    """Distances from one edge to the printed frame, one per scan line."""
    h, w = lab.shape[:2]
    if side in ("left", "right"):
        span, depth = h, w
    else:
        span, depth = w, h

    lo = int(span * EDGE_MARGIN)
    hi = int(span * (1 - EDGE_MARGIN))
    positions = np.linspace(lo, hi, SCAN_LINES).astype(int)
    max_depth = int(depth * MAX_SEARCH)

    def pixel(pos, d):
        if side == "left":
            return lab[pos, d]
        if side == "right":
            return lab[pos, depth - 1 - d]
        if side == "top":
            return lab[d, pos]
        return lab[depth - 1 - d, pos]

    # Sample the border colour from a band just inside the physical edge so the
    # cut line and any shadow at the very edge are excluded.
    sample = np.array([pixel(p, d) for p in positions for d in range(3, 9)], dtype=np.float32)
    border = np.median(sample, axis=0)

    hits = []
    for p in positions:
        run = 0
        found = None
        for d in range(3, max_depth):
            if _delta_e(pixel(p, d), border) > DELTA_THRESHOLD:
                run += 1
                if run >= RUN_LENGTH:
                    found = d - RUN_LENGTH + 1
                    break
            else:
                run = 0
        if found is not None:
            hits.append(found)
    return hits


def measure(path):
    """Measure centering for one card image.

    Returns a dict with ok=True and per-axis percentages, or ok=False + reason.
    """
    img = load_image(path)
    quad, method = find_card_quad(img)
    if quad is None:
        return {"ok": False, "reason": method, "source": str(path)}

    card = warp_card(img, quad)
    lab = cv2.cvtColor(card, cv2.COLOR_BGR2LAB)

    sides = {}
    spreads = {}
    for side in ("left", "right", "top", "bottom"):
        hits = _scan_side(lab, side)
        if len(hits) < SCAN_LINES // 3:
            return {
                "ok": False,
                "reason": f"could not find the printed frame on the {side} edge",
                "source": str(path),
            }
        sides[side] = float(np.median(hits))
        q75, q25 = np.percentile(hits, [75, 25])
        spreads[side] = float(q75 - q25)

    lr = sides["left"] + sides["right"]
    tb = sides["top"] + sides["bottom"]
    if lr <= 0 or tb <= 0:
        return {"ok": False, "reason": "degenerate border measurement", "source": str(path)}

    # Wide interquartile spread means the scan lines disagreed, usually from a
    # tilted shot or a busy border. Report it rather than hiding it.
    worst_spread = max(spreads.values())
    confidence = "high" if worst_spread <= 4 else ("medium" if worst_spread <= 10 else "low")

    return {
        "ok": True,
        "source": str(path),
        "detection": method,
        "confidence": confidence,
        "border_px": sides,
        "spread_px": spreads,
        "horizontal": {
            "left_pct": 100.0 * sides["left"] / lr,
            "right_pct": 100.0 * sides["right"] / lr,
        },
        "vertical": {
            "top_pct": 100.0 * sides["top"] / tb,
            "bottom_pct": 100.0 * sides["bottom"] / tb,
        },
    }


def format_measurement(m):
    if not m or not m.get("ok"):
        return "ej matbar"
    h = m["horizontal"]
    v = m["vertical"]
    return (
        f"{h['left_pct']:.0f}/{h['right_pct']:.0f} vanster/hoger, "
        f"{v['top_pct']:.0f}/{v['bottom_pct']:.0f} topp/botten "
        f"(matsakerhet: {m['confidence']})"
    )
