// Teef Chinatown — isometric diorama + brutalist low-poly characters. Flux.dev (REST).
import fs from 'node:fs';
import path from 'node:path';

const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
if (!FAL_KEY) throw new Error('FAL_KEY not found');

const OUT = '/home/assistant/projects/teef/art/concepts/flux';
fs.mkdirSync(OUT, { recursive: true });

const PROMPT = `Isometric 2.5D video game diorama level, top-down three-quarter isometric camera looking down at the scene, the ornate Soho Chinatown paifang gate as the centerpiece of an isometric city block - a grand traditional Chinese archway with upturned tiled roofs and carved beams - surrounded by narrow London brick townhouses, a red British phone box, cobbled street, red paper lanterns strung overhead. Several small stylized low-poly hooded characters scattered on the street: dark charcoal-grey monochrome low-poly figures with hoods, chunky simple geometric vinyl-toy forms, no faces, standing and walking. Glowing orange circular gameplay target rings (#ff7a1a) on the wet cobblestone beneath two characters. Atmospheric fog at the edges and into depth, dark moody night with desaturated teal-green gloom (#1e2e2b #2a3f3a) over night-blue shadow (#14202e), punctuated by warm amber (#e8a14b) and lantern red (#d22a2a) practical lights, dramatic low-key lighting, wet cobble reflections, faint white graffiti tags on shutters, clean readable isometric level, cinematic, high detail, soft ambient occlusion, painterly stylized textures, no UI, no text, no watermark`;

const SEEDS = [73419, 250688, 88123, 41577];

async function gen(seed) {
  const res = await fetch('https://fal.run/fal-ai/flux/dev', {
    method: 'POST',
    headers: { 'Authorization': `Key ${FAL_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt: PROMPT, image_size: 'landscape_16_9', num_images: 1, seed, num_inference_steps: 32, guidance_scale: 3.8 }),
  });
  if (!res.ok) { console.error(`[iso:${seed}] HTTP ${res.status} ${(await res.text()).slice(0,200)}`); return null; }
  const j = await res.json();
  const url = j.images?.[0]?.url;
  if (!url) { console.error(`[iso:${seed}] no url`); return null; }
  const img = Buffer.from(await (await fetch(url)).arrayBuffer());
  const file = path.join(OUT, `iso_${seed}.jpg`);
  fs.writeFileSync(file, img);
  console.log(`[iso:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`);
  return file;
}

const out = (await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`\nDONE: ${out.length}/${SEEDS.length}`);
