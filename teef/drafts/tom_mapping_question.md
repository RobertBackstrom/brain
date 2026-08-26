# Draft message to Tom — mapping recommendation + fidelity/scope question

*Standalone, sent ahead of Friday's full proposal. Softened Mapbox stance ("we'd propose"), TL;DR up top, question reframed to cover London fidelity + mission-polish allocation around the CPI/D3 test goal. For Robert's review before send.*

---

**TL;DR:** For Teef we would not lean on the runtime map SDKs (Mapbox, Cesium). We would build London from open geo data and bake it into the game, which keeps it offline, cheap and on-style. One thing we need from you: how recognisable London needs to be, and how evenly polished across the six missions, given the test is really about the first few days.

Hi Tom,

Two quick things on the build before the full proposal lands Friday.

**On the map:** rather than a runtime map SDK, we would propose building London from open geo data (OpenStreetMap / Ordnance Survey) and baking it into the game. Mapbox and the like are excellent for live, online maps, but for Teef they pull against three things that matter here:

1. **Offline.** Teef has to run offline. Those SDKs are built to stream map tiles online.
2. **Cost.** They bill per map load. A baked map has no runtime map cost at all, which is the right call for a soft-launch test where you don't want a metered dependency in the build.
3. **Look.** Their building layers are generic extrusions. We want a stylised London that reads as London at a glance, and we get far more control over that by building and baking it ourselves.

So our recommendation is the geo-data-plus-bake route: pull Soho and East Mayfair footprints, roads and heights, build the base once, and hand-craft a few hero landmarks (Big Ben, black cabs) so it reads as London instantly. Fully offline, clean licensing. Mapbox stays in our back pocket as a reference if we ever want its 3D layer.

**The question.** The brief asks for all six missions completable, which we are planning for. Given the test is really measuring CPI and early (D3) retention, the thing we want to get right with you is where the fidelity sits:

- **How recognisable** the real London needs to be: layout plus a few hero landmarks so it clearly reads as London (our recommendation for the test), or street-accurate Soho and Mayfair (materially more art work).
- **How evenly polished** the six missions need to be: we would weight the art and polish toward the opening missions that carry your D3 numbers, and keep the later missions solid but lighter, unless you want even depth across all six.

A steer on both and we will lock the plan around it in Friday's proposal.

Cheers,
Robert
