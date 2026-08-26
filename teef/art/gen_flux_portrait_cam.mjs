// Teef Chinatown — PORTRAIT, camera matched to the prototype's tilted follow-cam. Flux.dev.
import fs from 'node:fs';
import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env', 'utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m) || [])[1]?.trim();
const OUT = '/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait composition. Third-person follow-camera over a Soho Chinatown district in London at night, camera angled at about 50 degrees looking forward and down across the city so multiple streets, rooftops and blocks spread across the frame and recede toward a thin band of hazy fog at the very top, the city fills almost the whole frame with only a sliver of foggy sky at the top. The ornate Chinatown paifang gate sits in the mid-distance as one recognisable landmark among realistic Soho brick townhouses and narrow streets, red paper lanterns strung between buildings, a red British phone box, a red double-decker bus, neon Chinese shop signage, cobbled streets. A few small realistic 3D human characters in hooded streetwear scattered through the streets, gritty realistic proportions. Subtle orange glowing gameplay target rings (#ff7a1a) on the wet cobblestone. Heavy volumetric atmospheric fog with depth falloff, desaturated teal-green night gloom (#1e2e2b #2a3f3a) over night-blue shadow (#14202e), warm amber (#e8a14b) and lantern red (#d22a2a) practical lights, dramatic low-key cinematic lighting, wet reflective cobblestone, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game environment, high detail, no text, no UI, no watermark`;

const SEEDS = [77240, 44120, 60931, 18402];
async function gen(seed){
  const res = await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.6})});
  if(!res.ok){console.error(`[cam:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url){console.error(`[cam:${seed}] no url`);return null;}
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`cam_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[cam:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`\nDONE ${out.length}/${SEEDS.length}`);
