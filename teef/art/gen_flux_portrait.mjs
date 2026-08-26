// Teef Chinatown — PORTRAIT (9:16) + more zoomed out, realistic K&G mood. Flux.dev.
import fs from 'node:fs';
import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
const OUT = '/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait composition, very high aerial drone view looking steeply down at a 50 degree angle over a large area of Soho Chinatown in London at night, zoomed far out to reveal many city blocks and the street grid receding into fog, the ornate Chinatown paifang gate (traditional Chinese archway, upturned tiled roofs) as a small recognisable landmark down among realistic Soho brick townhouses and narrow streets, red British phone boxes, a red double-decker bus, cobbled streets, rows of red paper lanterns strung between buildings, neon Chinese shop signage. Several small realistic 3D human characters in hooded streetwear scattered on the streets far below, gritty realistic proportions. Subtle orange glowing gameplay target rings (#ff7a1a) on the wet cobblestone. Heavy volumetric atmospheric fog with strong depth falloff, desaturated teal-green night gloom (#1e2e2b #2a3f3a) over night-blue shadow (#14202e), warm amber (#e8a14b) and lantern red (#d22a2a) practical lights, dramatic low-key cinematic lighting, wet reflective cobblestone, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game environment, high detail, atmospheric depth, no text, no UI, no watermark`;

const SEEDS = [44120, 250688, 31507, 77240];
async function gen(seed){
  const res = await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.5})});
  if(!res.ok){console.error(`[port:${seed}] HTTP ${res.status} ${(await res.text()).slice(0,160)}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url){console.error(`[port:${seed}] no url`);return null;}
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`port_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[port:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`\nDONE ${out.length}/${SEEDS.length}`);
