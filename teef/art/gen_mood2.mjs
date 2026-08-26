// Teef mood pieces v2 — STYLIZED to match the art-style guide characters (designer-toy / Bad Guys / Pixar)
// + the Casual map palette. Drops all photoreal terms. Flux.dev REST.
import fs from 'node:fs';
import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
const OUT = '/home/assistant/projects/teef/art/concepts/mood';
fs.mkdirSync(OUT, { recursive: true });

const TAIL = `stylized 3D animated mobile game render in the style of The Bad Guys movie and designer-toy figures, clean semi-low-poly stylized characters with large simplified heads, smooth rounded forms, simple faces with subtle glowing eyes, hooded streetwear with oversized tech bags and chunky trainers, vibrant saturated colour, purple and magenta neon glow, graffiti tags on brick walls, wet London street at night with warm window light, soft cinematic lighting, smooth matte shading, playful premium 3D render, no text, no UI, no watermark, no realism, not photoreal`;

const SCENES = [
  { key: 'lift2',    prompt: `An elegantly dressed civilian "mug" target character with a smaller head, clean high-end streetwear, an oversized luxury crossbody bag and headphones, standing on a stylized London street absorbed in a large smartphone; a hooded thief character with a big hood, complex silhouette and glowing eyes sneaks in close behind, reaching for the bag. A red British phone box and a red double-decker bus, stylized brick London townhouses, three-quarter camera. ${TAIL}` },
  { key: 'recruit2', prompt: `Two hooded stylized thief characters in a graffiti-covered London back-alley beside a glowing neon cafe sign, a larger older crew member facing a smaller wiry younger recruit and sizing him up, a black London cab parked at the alley mouth, steam from a vent, three-quarter camera. ${TAIL}` },
  { key: 'fence2',   prompt: `A stylized older fence character in a flat cap behind a cluttered workbench in a graffiti-covered railway-arch lock-up, glowing gold chains, jewellery and neat stacks of cash laid out with a neon loot-glow, peering at a gold chain through a jeweller's loupe, crates and bric-a-brac in shadow, warm lamp pool. ${TAIL}` },
];
const SEEDS = [250688, 71044];

async function gen(scene, seed){
  const res = await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:scene.prompt,image_size:'landscape_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.5})});
  if(!res.ok){console.error(`[${scene.key}:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url){console.error(`[${scene.key}:${seed}] no url`);return null;}
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`${scene.key}_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[${scene.key}:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const jobs=[]; for(const s of SCENES) for(const seed of SEEDS) jobs.push(gen(s,seed));
const out=(await Promise.all(jobs)).filter(Boolean);
console.log(`\nDONE ${out.length}/${jobs.length}`);
