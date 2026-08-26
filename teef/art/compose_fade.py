#!/usr/bin/env python3
"""Annotated transparency / distance-fade feature treatment on the hero frame."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE='/home/assistant/projects/teef/art/concepts/hero_with_box.png'
OUT ='/home/assistant/projects/teef/art/concepts/teef_transparency.png'

img=Image.open(BASE).convert('RGBA')
W,H=img.size
CY=(95,235,238)
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
f_lab=ImageFont.truetype(MONO,18); f_sub=ImageFont.truetype(MONO,13); f_top=ImageFont.truetype(MONO,17)

# --- ghost an occluding foreground building (lower-right block) ---
poly=[(545,690),(720,720),(720,1195),(505,1150)]
mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).polygon(poly,fill=255)
faded=Image.blend(img, Image.new('RGBA',(W,H),(24,44,46,255)), 0.6)
img=Image.composite(faded,img,mask)

ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
# cyan wireframe inside the ghosted block (clipped by mask)
wf=Image.new('RGBA',(W,H),(0,0,0,0)); wd=ImageDraw.Draw(wf)
for gx in range(505,721,26):
    wd.line([(gx,690),(gx,1195)],fill=(*CY,190),width=2)
for gy in range(700,1196,34):
    wd.line([(505,gy),(720,gy)],fill=(*CY,190),width=2)
wd.polygon(poly,outline=(*CY,255))
wf=Image.composite(wf,Image.new('RGBA',(W,H),(0,0,0,0)),mask)
ov.alpha_composite(wf)

# revealed player + target ring 'through' the ghost
d.ellipse([600,1030,690,1072],outline=(255,140,30,255),width=4)
d.ellipse([618,1020,672,1050],outline=(255,180,80,200),width=2)
d.rounded_rectangle([632,968,658,1028],radius=10,fill=(235,235,238,255))  # player capsule
d.ellipse([636,958,654,980],fill=(235,235,238,255))

# --- distance fade emphasis at top ---
grad=Image.new('L',(1,H),0)
for y in range(H):
    grad.putpixel((0,y), max(0, int(120*(1-(y/ (H*0.32)))) ) if y< H*0.32 else 0)
grad=grad.resize((W,H))
fog=Image.new('RGBA',(W,H),(150,180,180,255)); fog.putalpha(grad)
ov.alpha_composite(fog)

def panel(x,y,lines,fonts,maxw):
    h=8
    for t,f in zip(lines,fonts): h+=f.size+6
    d.rounded_rectangle([x,y,x+maxw,y+h],radius=6,fill=(8,10,12,212),outline=(*CY,170),width=2)
    yy=y+8
    for t,f in zip(lines,fonts):
        d.text((x+12,yy),t,font=f,fill=(235,245,245,255)); yy+=f.size+6

# label 1: transparency (left of ghost), leader line to building
panel(60,792,['// CAMERA-RELATIVE TRANSPARENCY','occluding buildings fade to a','wireframe so the mark stays visible'],[f_lab,f_sub,f_sub],330)
d.line([(390,838),(560,900)],fill=(*CY,220),width=2); d.ellipse([556,896,566,906],fill=(*CY,255))

# label 2: distance fade (top)
panel(int(W/2-185),150,['// BORDERING AREAS FADE WITH DISTANCE'],[f_top],372)
d.line([(W//2,196),(W//2,250)],fill=(*CY,200),width=2)

out=Image.alpha_composite(img,ov).convert('RGB')
out.save(OUT,quality=92)
print('saved',OUT,out.size)
