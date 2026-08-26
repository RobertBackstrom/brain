#!/usr/bin/env python3
"""Composite the REAL Teef prototype HUD (monospace, minimal) over the chosen wide realistic render."""
from PIL import Image, ImageDraw, ImageFont
import sys, os

BASE = sys.argv[1] if len(sys.argv) > 1 else '/home/assistant/projects/teef/art/concepts/flux/wide2_44120.jpg'
OUT  = sys.argv[2] if len(sys.argv) > 2 else '/home/assistant/projects/teef/art/concepts/teef_chinatown_hud.png'

img = Image.open(BASE).convert('RGBA')
W = 1600; H = round(img.height * W / img.width)
img = img.resize((W, H), Image.LANCZOS)

M = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
f_hud  = ImageFont.truetype(M, 26)
f_ban  = ImageFont.truetype(M, 24)
f_dash = ImageFont.truetype(M, 20)

RED   = (228, 24, 24, 255)
GREY  = (180, 180, 184, 255)
WHITE = (240, 240, 240, 255)

ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov)

def text_w(s, f):
    bb = d.textbbox((0,0), s, font=f); return bb[2]-bb[0]

# faint top divider line (prototype has a thin rule under the top bar)
d.line([0, 78, W, 78], fill=(255, 255, 255, 28), width=1)

# top-left: currency
d.text((40, 34), '£', font=f_hud, fill=GREY)
d.text((78, 34), '2,480', font=f_hud, fill=WHITE)

# top-right: PHONES n
ph = 'PHONES'; n = '3'
nw = text_w(n, f_hud); pw = text_w(ph, f_hud)
d.text((W-40-nw-18-pw, 34), ph, font=f_hud, fill=RED)
d.text((W-40-nw, 34), n, font=f_hud, fill=WHITE)

# top-center banner: dark pill + white monospace objective (prototype voice)
ban = 'FIND A PUNTER. TEEF IT.'
bw = text_w(ban, f_ban); bx = (W - bw)//2
d.rounded_rectangle([bx-22, 30, bx+bw+22, 70], radius=6, fill=(8, 8, 10, 205), outline=(255,255,255,40), width=1)
d.text((bx, 38), ban, font=f_ban, fill=WHITE)

# bottom-right: DASH circular button
cx, cy, r = W-92, H-92, 50
d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(20,20,22,180), outline=(210,210,214,150), width=2)
dw = text_w('DASH', f_dash)
d.text((cx-dw//2, cy-10), 'DASH', font=f_dash, fill=WHITE)

out = Image.alpha_composite(img, ov).convert('RGB')
out.save(OUT, quality=92)
print('saved', OUT, out.size)
