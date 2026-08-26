#!/usr/bin/env python3
"""Build a 2x2 contact sheet of the SD3.5-large run."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SEEDS = [1337, 4242, 9001, 7777]
TILE_W, TILE_H = 768, 512  # halved from 1536x1024
LABEL_H = 36
PAD = 8

cols, rows = 2, 2
sheet_w = cols * TILE_W + (cols + 1) * PAD
sheet_h = rows * (TILE_H + LABEL_H) + (rows + 1) * PAD
sheet = Image.new("RGB", (sheet_w, sheet_h), (20, 20, 20))
draw = ImageDraw.Draw(sheet)

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except OSError:
    font = ImageFont.load_default()

for idx, seed in enumerate(SEEDS):
    r, c = divmod(idx, cols)
    img = Image.open(ROOT / f"merged_seed{seed}.png").convert("RGB")
    img.thumbnail((TILE_W, TILE_H), Image.LANCZOS)
    x = PAD + c * (TILE_W + PAD)
    y = PAD + r * (TILE_H + LABEL_H + PAD)
    sheet.paste(img, (x + (TILE_W - img.width) // 2, y + (TILE_H - img.height) // 2))
    draw.text((x + 8, y + TILE_H + 6), f"seed {seed}", fill=(230, 230, 230), font=font)

out = ROOT / "contact_sheet.png"
sheet.save(out, optimize=True)
print(f"wrote {out}")
