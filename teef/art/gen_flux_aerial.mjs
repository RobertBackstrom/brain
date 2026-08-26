// Teef Chinatown — PORTRAIT, high aerial tilted-down city-spread (prototype-match). Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait composition. High aerial drone camera looking steeply down at about 55 degrees over a Soho Chinatown district in London at night, you look down across the rooftops and a grid of narrow streets crisscrossing between blocks of realistic brick townhouses, NOT a single straight street, the whole city district spread out and filling the frame with only a thin band of foggy haze at the very top. The ornate Chinatown paifang gate sits among the blocks as one recognisable landmark, rows of red paper lanterns strung over the streets, a red double-decker bus and red phone box small below, neon Chinese signage, wet cobbled streets seen from above. Small realistic hooded human characters dotted along the streets far below, a couple standing inside glowing orange gameplay target rings (#ff7a1a) on the cobbles, small green pickup markers scattered. Heavy volumetric atmospheric fog with depth falloff, desaturated teal-green night gloom (#1e2e2b #2a3f3a) over night-blue shadow (#14202e), warm amber (#e8a14b) and lantern red (#d22a2a) practical lights, dramatic low-key cinematic lighting, wet reflective surfaces, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game environment, high detail, no text, no UI, no watermark`;

const SEEDS=[77240,44120,29155,83014];
async function gen(seed){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.6})});
  if(!res.ok){console.error(`[aer:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`aer_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[aer:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`DONE ${out.length}/4`);
