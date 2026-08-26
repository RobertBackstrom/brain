#!/usr/bin/env python3
"""Composite the real Teef prototype PORTRAIT HUD over the chosen portrait render."""
from PIL import Image, ImageDraw, ImageFont
import sys

BASE = sys.argv[1] if len(sys.argv) > 1 else '/home/assistant/projects/teef/art/concepts/flux/port_77240.jpg'
OUT  = sys.argv[2] if len(sys.argv) > 2 else '/home/assistant/projects/teef/art/concepts/teef_chinatown_hud_portrait.png'

img = Image.open(BASE).convert('RGBA')
W = 720; H = round(img.height * W / img.width)
img = img.resize((W, H), Image.LANCZOS)

M = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
f_hud = ImageFont.truetype(M, 24)
f_ban = ImageFont.truetype(M, 20)
f_d   = ImageFont.truetype(M, 17)

RED=(228,24,24,255); GREY=(185,185,189,255); WHITE=(242,242,242,255)
ov = Image.new('RGBA',(W,H),(0,0,0,0)); d = ImageDraw.Draw(ov)
def tw(s,f): bb=d.textbbox((0,0),s,font=f); return bb[2]-bb[0]

# top bar
d.line([0,72,W,72], fill=(255,255,255,26), width=1)
d.text((34,30),'£',font=f_hud,fill=GREY); d.text((68,30),'0',font=f_hud,fill=WHITE)
ph='PHONES'; n='0'; nw=tw(n,f_hud); pw=tw(ph,f_hud)
d.text((W-34-nw-16-pw,30),ph,font=f_hud,fill=RED); d.text((W-34-nw,30),n,font=f_hud,fill=WHITE)

# objective banner (just below bar)
ban='FIND MARK // TEEF IT'; bw=tw(ban,f_ban); bx=(W-bw)//2
d.rounded_rectangle([bx-18,86,bx+bw+18,122],radius=6,fill=(8,8,10,205),outline=(255,255,255,38),width=1)
d.text((bx,93),ban,font=f_ban,fill=WHITE)

# bottom-left movement pad (joystick)
jx,jy,jr=120,H-130,78
d.ellipse([jx-jr,jy-jr,jx+jr,jy+jr],outline=(220,220,224,70),width=2,fill=(255,255,255,12))
d.ellipse([jx-24,jy-24,jx+24,jy+24],fill=(230,230,234,55),outline=(240,240,244,120),width=2)

# bottom-right DASH
cx,cy,r=W-110,H-130,58
d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(20,20,22,180),outline=(212,212,216,150),width=2)
dw=tw('DASH',f_d); d.text((cx-dw//2,cy-9),'DASH',font=f_d,fill=WHITE)

out = Image.alpha_composite(img,ov).convert('RGB')
out.save(OUT,quality=92)
print('saved',OUT,out.size)
