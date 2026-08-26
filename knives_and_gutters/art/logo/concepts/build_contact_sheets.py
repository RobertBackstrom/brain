#!/usr/bin/env python3
"""
Build per-angle contact sheets for K&G logo concepts.

Layout per angle: 2 rows × 4 cols
  Row 1: Lane A (Flux.dev) seeds 101, 202, 303, 404
  Row 2: Lane B (fast-SDXL) seeds 101, 202, 303, 404

Outputs:
  contact_angle1_composition.png
  contact_angle2_detail.png
  contact_angle3_crudeness.png
  contact_master.png  (all three angles stacked)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FLUX_DIR = ROOT / "fal-flux"
SDXL_DIR = ROOT / "fal-sdxl"

ANGLES = [
    ("angle1_composition", "Angle 1 — Composition-led (Knivar och Rännstenar layout, Gary Chalk crudeness)"),
    ("angle2_detail", "Angle 2 — Detail-led / TOP PRIO (roc_logo02 detail + John Blanche surrealism)"),
    ("angle3_crudeness", "Angle 3 — Crudeness-led (pure Gary Chalk Mordheim cover)"),
]
SEEDS = [101, 202, 303, 404]
LANES = [
    ("Lane A — Flux.dev", FLUX_DIR),
    ("Lane B — fast-SDXL", SDXL_DIR),
]

TILE = 512
PAD = 12
HEADER_H = 56
LABEL_H = 28


def load_font(size: int):
    for path in (
        "/home/assistant/projects/skills/fonts/Montserrat-VariableFont.ttf",
        "/home/assistant/projects/skills/fonts/OpenSans-ExtraBold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            continue
    return ImageFont.load_default()


def build_angle(angle_slug: str, header: str) -> Image.Image:
    cols = len(SEEDS)
    rows = len(LANES)
    sheet_w = PAD + cols * (TILE + PAD)
    sheet_h = HEADER_H + rows * (LABEL_H + TILE + PAD) + PAD
    sheet = Image.new("RGB", (sheet_w, sheet_h), (16, 16, 16))
    draw = ImageDraw.Draw(sheet)

    title_font = load_font(22)
    label_font = load_font(15)
    seed_font = load_font(13)

    draw.text((PAD, 16), header, fill=(230, 220, 200), font=title_font)

    y = HEADER_H
    for lane_label, lane_dir in LANES:
        draw.text((PAD, y + 6), lane_label, fill=(180, 180, 200), font=label_font)
        y += LABEL_H
        x = PAD
        for seed in SEEDS:
            tile_path = lane_dir / f"{angle_slug}_seed{seed}.png"
            if tile_path.exists():
                tile = Image.open(tile_path).convert("RGB")
                tile = tile.resize((TILE, TILE), Image.LANCZOS)
                sheet.paste(tile, (x, y))
            else:
                draw.rectangle([x, y, x + TILE, y + TILE], fill=(40, 40, 40), outline=(80, 80, 80))
                draw.text((x + 8, y + 8), f"missing\n{tile_path.name}", fill=(160, 80, 80), font=seed_font)
            draw.text((x + 6, y + TILE - 22), f"seed {seed}", fill=(255, 230, 160), font=seed_font, stroke_width=2, stroke_fill=(0, 0, 0))
            x += TILE + PAD
        y += TILE + PAD
    return sheet


def main():
    sheets = []
    for slug, header in ANGLES:
        sheet = build_angle(slug, header)
        out = ROOT / f"contact_{slug}.png"
        sheet.save(out, optimize=True)
        print(f"wrote {out}")
        sheets.append(sheet)

    # Master = stack the three vertically
    if all(sheets):
        gap = 18
        w = max(s.width for s in sheets)
        h = sum(s.height for s in sheets) + gap * (len(sheets) - 1)
        master = Image.new("RGB", (w, h), (8, 8, 8))
        y = 0
        for s in sheets:
            master.paste(s, (0, y))
            y += s.height + gap
        out = ROOT / "contact_master.png"
        master.save(out, optimize=True)
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
