// Teef Chinatown — ELEVATED aerial 3/4 + WIDE + REALISTIC (K&G mood). Flux.dev.
import fs from 'node:fs';
import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
const OUT = '/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `High-angle aerial cinematic establishing shot, camera looking down at roughly 45 degrees over a whole Soho Chinatown city block in London at night, wide zoomed-out view revealing the street grid from above, the ornate Chinatown paifang gate (grand traditional Chinese archway, upturned tiled roofs, carved beams) as the centerpiece below, surrounded by realistic Soho brick townhouses and narrow connecting streets, a red British phone box, a red double-decker bus, cobbled streets, red paper lanterns strung overhead, neon Chinese shop signage. A few small realistic 3D human characters in hooded streetwear walking the streets far below, gritty realistic human proportions, grounded believable figures. Subtle orange glowing gameplay target rings (#ff7a1a) on the wet cobblestone. Heavy volumetric atmospheric fog with strong depth falloff, desaturated teal-green night gloom (#1e2e2b #2a3f3a) over night-blue shadow (#14202e), punctuated by warm amber (#e8a14b) and lantern red (#d22a2a) practical lights, dramatic low-key cinematic lighting, wet reflective cobblestone, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody game environment, high detail, atmospheric depth, no text, no UI, no watermark`;

const SEEDS = [250688, 73419, 44120, 80517];
async function gen(seed){
  const res = await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'landscape_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.5})});
  if(!res.ok){console.error(`[w2:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url){console.error(`[w2:${seed}] no url`);return null;}
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`wide2_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[w2:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`\nDONE ${out.length}/${SEEDS.length}`);
