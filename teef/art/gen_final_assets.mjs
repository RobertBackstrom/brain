// Hero sans phone box (seed 90233) + standalone phone-box asset on green screen. Flux.dev.
import fs from 'node:fs'; import path from 'node:path';
const ENV = fs.readFileSync('/home/assistant/projects/assistant/.env','utf8');
const FAL_KEY = (ENV.match(/^FAL_KEY=(.*)$/m)||[])[1]?.trim();
const OUT='/home/assistant/projects/teef/art/concepts/flux';

const SCENE = `Tall vertical portrait. High aerial drone camera looking steeply down at about 55 degrees over a dense Soho Chinatown district in London at night. The clear focal landmark is a large, highly ornate and colourful real London Chinatown paifang gate modelled on the Wardour Street gate: three tiered green and gold glazed pagoda roofs with sharply upswept eaves and dragon finials, richly painted red, gold, blue and green carved beams and dougong brackets, a central gold signboard with red Chinese characters, red lanterns hanging beneath, spanning the main street. Around it rooftops and a grid of narrow streets between brick townhouse blocks fill the frame, thin foggy haze at the top. Dense gritty Urban Cyber detail: tangled overhead electric and telecom cables, rusty fire escapes, rooftop water tanks, AC units, satellite dishes and antennas, tall neon vertical Chinese and Japanese signs glowing magenta red and cyan, street signs and traffic lights, graffiti on shutters, market stalls and clutter on wet cobbles. Small realistic hooded figures along the street below, a couple inside a glowing orange target ring (#ff7a1a). Heavy volumetric fog, depth falloff, desaturated teal-green night gloom with warm amber and neon accents, dramatic low-key cinematic light, wet reflections, realistic physically based rendering, Unreal Engine 5 cinematic, photoreal moody mobile game, high detail, no text, no UI, no watermark`;

const BOX = `A single classic red British telephone box, K6 design, full body, three-quarter front view, standing upright and complete, isolated and centered on a solid flat uniform chroma key green screen background, even soft studio lighting with a subtle cool night tone, realistic high detail, sharp, no text, no people, no extra objects`;

async function gen(prompt, seed, label, size){
  const res=await fetch('https://fal.run/fal-ai/flux/dev',{method:'POST',
    headers:{'Authorization':`Key ${FAL_KEY}`,'Content-Type':'application/json'},
    body:JSON.stringify({prompt,image_size:size,num_images:1,seed,num_inference_steps:36,guidance_scale:3.7})});
  if(!res.ok){console.error(`[${label}] HTTP ${res.status}`);return null;}
  const j=await res.json(); const url=j.images?.[0]?.url; if(!url)return null;
  const img=Buffer.from(await (await fetch(url)).arrayBuffer());
  const file=path.join(OUT,`${label}.jpg`); fs.writeFileSync(file,img);
  console.log(`[${label}] ${(img.length/1024).toFixed(0)}KB -> ${path.basename(file)}`); return file;
}
await Promise.all([
  gen(SCENE, 90233, 'hero_nobox', 'portrait_16_9'),
  gen(BOX, 5521, 'phonebox_green', 'portrait_4_3'),
]);
console.log('DONE');
