#!/usr/bin/env python3
"""Round-3 contact sheets: one 2x2 per branch + a 3x4 master (rows = branches)."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
TILE_W, TILE_H = 768, 512
LABEL_H = 36
PAD = 8

try:
    FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except OSError:
    FONT = ImageFont.load_default()

run = json.loads((ROOT / "_run_log.json").read_text())
branches = [(b["dir"], b["seeds"]) for b in run["branches"]]


def build(tiles, cols, out_path):
    rows = (len(tiles) + cols - 1) // cols
    w = cols * TILE_W + (cols + 1) * PAD
    h = rows * (TILE_H + LABEL_H + PAD) + PAD
    sheet = Image.new("RGB", (w, h), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)
    for idx, (label, p) in enumerate(tiles):
        r, c = divmod(idx, cols)
        x = PAD + c * (TILE_W + PAD)
        y = PAD + r * (TILE_H + LABEL_H + PAD)
        if p.exists():
            img = Image.open(p).convert("RGB")
            img.thumbnail((TILE_W, TILE_H), Image.LANCZOS)
            sheet.paste(img, (x + (TILE_W - img.width) // 2, y + (TILE_H - img.height) // 2))
        else:
            draw.text((x + 8, y + TILE_H // 2), "MISSING", fill=(200, 60, 60), font=FONT)
        draw.text((x + 8, y + TILE_H + 6), label, fill=(230, 230, 230), font=FONT)
    sheet.save(out_path, optimize=True)
    print(f"wrote {out_path}")


all_tiles = []
for name, seeds in branches:
    tiles = [(f"{name} / seed {s}", ROOT / name / f"seed{s}.png") for s in seeds]
    build(tiles, 2, ROOT / f"contact_{name}.png")
    all_tiles += tiles
build(all_tiles, 4, ROOT / "contact_master.png")
