#!/usr/bin/env python3
"""Composite a Teef-style HUD over the chosen isometric Chinatown render."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

BASE = '/home/assistant/projects/teef/art/concepts/flux/iso_250688.jpg'
OUT  = '/home/assistant/projects/teef/art/concepts/iso_250688_ui.png'

img = Image.open(BASE).convert('RGBA')
W = 1600; H = round(img.height * W / img.width)
img = img.resize((W, H), Image.LANCZOS)

# fonts
FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
f_big   = ImageFont.truetype(FB, 30)
f_med   = ImageFont.truetype(FB, 26)
f_small = ImageFont.truetype(FB, 20)
f_tiny  = ImageFont.truetype(FB, 16)

# palette (Teef brutalist: red accent + paper + ink)
RED   = (210, 42, 42, 255)
GOLD  = (232, 161, 75, 255)
PAPER = (244, 241, 234, 240)
INK   = (13, 13, 15, 255)
WHITE = (245, 245, 245, 255)

ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov)

# top darkening for HUD legibility
top = Image.new('RGBA', (W, 130), (0, 0, 0, 0))
ImageDraw.Draw(top).rectangle([0, 0, W, 130], fill=(8, 10, 12, 130))
top = top.filter(ImageFilter.GaussianBlur(0))
ov.alpha_composite(top, (0, 0))

def chip(x, y, w, h, bg, radius=18, outline=(255,255,255,40), ow=2):
    d.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=bg, outline=outline, width=ow)

def ctext(cx, cy, s, font, fill):
    bb = d.textbbox((0,0), s, font=font); tw=bb[2]-bb[0]; th=bb[3]-bb[1]
    d.text((cx-tw/2, cy-th/2-bb[1]/1), s, font=font, fill=fill)

PADY = 26; BH = 60

# --- top-left: currency ---
cx0 = 34
chip(cx0, PADY, 210, BH, (13,13,15,205))
d.text((cx0+22, PADY+14), '£', font=f_big, fill=GOLD)
d.text((cx0+58, PADY+16), '2,480', font=f_med, fill=WHITE)

# --- top-center: TARGET. TEEF. search pill (signature element) ---
sw = 560; sx = (W - sw)//2
chip(sx, PADY, sw, BH, PAPER, radius=BH//2, outline=(13,13,15,60), ow=2)
# magnifier glyph
gx, gy = sx+34, PADY+BH//2
d.ellipse([gx-12, gy-12, gx+8, gy+8], outline=INK, width=4)
d.line([gx+7, gy+7, gx+18, gy+18], fill=INK, width=4)
d.text((sx+72, PADY+15), 'TARGET. TEEF.', font=f_med, fill=(20,20,22,255))

# --- top-right: phone chip ---
pw = 70; px = W-34-pw
chip(px, PADY, pw, BH, (13,13,15,205))
# phone glyph
phx, phy = px+pw//2, PADY+BH//2
d.rounded_rectangle([phx-13, phy-19, phx+13, phy+19], radius=5, outline=WHITE, width=3)
d.line([phx-5, phy+13, phx+5, phy+13], fill=WHITE, width=3)
d.ellipse([phx-1, phy-15, phx+1, phy-13], fill=WHITE)

# --- target marker near the ring (approx center-low) ---
mx, my = int(W*0.50), int(H*0.66)
# pin
d.polygon([(mx, my+22), (mx-13, my-4), (mx+13, my-4)], fill=RED)
d.ellipse([mx-16, my-30, mx+16, my+2], fill=RED, outline=WHITE, width=3)
ctext(mx, my-14, '£', f_small, WHITE)
# label chip above pin
lbl = 'MUG · THE DIP'
bb = d.textbbox((0,0), lbl, font=f_tiny); lw = bb[2]-bb[0]
chip(mx-lw//2-14, my-66, lw+28, 30, (13,13,15,215), radius=8, outline=(210,42,42,180), ow=2)
ctext(mx, my-51, lbl, f_tiny, WHITE)

# --- bottom-right: primary action button ---
bw, bh = 240, 64; bx, by = W-34-bw, H-34-bh
chip(bx, by, bw, bh, (210,42,42,235), radius=14, outline=(255,255,255,60), ow=2)
ctext(bx+bw//2, by+bh//2, 'SWIPE IT', f_med, WHITE)

# --- bottom-left: small objective ticker ---
ob = 'OBJECTIVE  ·  Lift the mark by the gate'
chip(34, H-34-46, 470, 46, (13,13,15,190), radius=10, outline=(255,255,255,30), ow=1)
d.text((52, H-34-37), 'OBJECTIVE', font=f_tiny, fill=GOLD)
d.text((158, H-34-37), '·  Lift the mark by the gate', font=f_tiny, fill=WHITE)

out = Image.alpha_composite(img, ov).convert('RGB')
out.save(OUT, quality=92)
print('saved', OUT, out.size)
