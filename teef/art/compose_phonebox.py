#!/usr/bin/env python3
from PIL import Image, ImageFilter, ImageDraw, ImageMath, ImageChops

HERO='/home/assistant/projects/teef/art/concepts/flux/hero_nobox.jpg'
BOX ='/home/assistant/projects/teef/art/concepts/flux/phonebox_green.jpg'
OUT ='/home/assistant/projects/teef/art/concepts/hero_with_box.png'

hero=Image.open(HERO).convert('RGBA')
W=720; H=round(hero.height*W/hero.width); hero=hero.resize((W,H),Image.LANCZOS)

# --- key green ---
box=Image.open(BOX).convert('RGB')
r,g,bch=box.split()
greenmask=ImageMath.eval("255*((g>80)&(g>(r+25))&(g>(b+25)))",r=r,g=g,b=bch).convert('L')
alpha=ImageChops.invert(greenmask).filter(ImageFilter.GaussianBlur(1.2))
box=box.convert('RGBA'); box.putalpha(alpha)
box=box.crop(box.getbbox())

target_h=165
box=box.resize((max(1,round(box.width*target_h/box.height)),target_h),Image.LANCZOS)

bx=int(W*0.135); by=int(H*0.82)
cx=bx+box.width//2; ground=by+box.height

ov=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(ov)
d.ellipse([cx-box.width*0.55, ground-10, cx+box.width*0.55, ground+12], fill=(0,0,0,120))
ov=ov.filter(ImageFilter.GaussianBlur(5))

refl=box.transpose(Image.FLIP_TOP_BOTTOM)
ra=refl.split()[3].point(lambda p:int(p*0.22)); refl.putalpha(ra)
refl=refl.filter(ImageFilter.GaussianBlur(2))

out=Image.alpha_composite(hero,ov)
out.alpha_composite(refl,(bx,ground-4))
out.alpha_composite(box,(bx,by))

glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
gd.ellipse([cx-70,ground-30,cx+70,ground+30],fill=(210,40,40,60))
glow=glow.filter(ImageFilter.GaussianBlur(12))
out=Image.alpha_composite(out,glow)

out.convert('RGB').save(OUT,quality=92)
print('saved',OUT,out.size,'box',box.size,'at',(bx,by))
