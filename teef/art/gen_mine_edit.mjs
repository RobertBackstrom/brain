// Re-render the "avenue" hero (port_77240 framing): real London gate, ONE right lamp, no phone box. Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const PROMPT = `Tall vertical portrait. Looking down a long straight Soho Chinatown street in London at night from a slightly elevated camera, the wet cobbled street receding into fog toward the far end. At the end of the street stands a large, ornate, real London Chinatown paifang gate modelled on the Wardour Street gate: three tiered green and gold glazed pagoda roofs with upswept eaves and dragon finials, a central gold signboard with red Chinese characters, richly painted red, gold, blue and green carved beams and dougong brackets. Realistic brick Soho townhouses line both sides with neon Chinese shop signs, a few small realistic hooded figures walking on the street. A single red paper lantern glows on the right side of the street near a shopfront, and there are no other lanterns anywhere else. Desaturated teal-green night gloom with warm amber and red accents, heavy volumetric atmospheric fog, wet reflective cobblestones, dramatic low-key cinematic lighting, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game, high detail, no text, no UI, no watermark`;

const SEEDS=[77240, 21044, 58931];
async function gen(seed){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt:PROMPT,image_size:'portrait_16_9',num_images:1,seed,num_inference_steps:34,guidance_scale:3.6})});
  if(!res.ok){console.error(`[mine:${seed}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`mine_${seed}.jpg`); fs.writeFileSync(file,img);
  console.log(`[mine:${seed}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
const out=(await Promise.all(SEEDS.map(gen))).filter(Boolean);
console.log(`DONE ${out.length}/3`);
