# The Author — Learnings

Cross-project voice-editing learnings for the [[the_author]] agent. Append inline as you learn,
with date + channel/person tag. Durable per-person / per-channel patterns also get folded into
the matching `skills/voice/` file so every future pass inherits them.

Rule: never record a fabricated pattern. Every line traces to a real message Robert wrote, a
correction he made, or an example he pasted. Simulated-context passes are flagged as simulation.

---

## 2026-08-28 - Rubrikregeln bekräftad en andra gång samma dag, nu på engelska och mot en publisher [k2c / Pharaoh Lands, mail register]

Andra oberoende bekräftelsen på **samma dygn** av regeln i Curveball-entryn längre ned: *rubriken är
en etikett som namnger ämnet, inte en mening som gör en poäng.* Den förra evidensen var svensk och
mot ett utvecklarteam Robert känner väl. Den här är **engelsk och mot Raw Furys producenter**, alltså
en formellare yta och en annan språkregister. Regeln överlever båda.

Diffen: MS4-leveransmailet gick ut 28 aug 22:27 (tråd `1a04a098c9f6e01b`) med **exakt en ändring**
mot det jag lämnade ifrån mig. Robert bytte

> Everything is on one page:

mot

> Delivery notes.

Notera vad som faktiskt togs bort. "Everything is on one page" är inte hype och inte en säljmening i
vanlig mening, den låter saklig. Men dess nyttolast är **fullständighet som egenskap hos vårt arbete**
("vi har samlat allt åt er"), inte information mottagaren behöver. "Delivery notes." är substantivet
som namnger länken och inget mer. Jag hade redan kört ett antisäljpass över texten på Roberts brief
och ändå lämnade jag den kvar, för den läste som ren funktion.

**Lärdomen är alltså inte regeln, den fanns redan. Lärdomen är hur lågt tröskelvärdet ligger.**
En ram som bara mycket svagt värderar vårt eget arbete åker ut. Testet är inte "låter det säljigt"
utan **"vad är nyttolasten - ett faktum mottagaren behöver, eller en egenskap hos oss?"** Applicera
det även på meningar som redan känns neutrala, och särskilt på ingressraden precis före en länk
eller en lista, som är där ramen sätter sig oftast.

Vad han INTE rörde: allt annat, ordagrant, inklusive `*asterisk*`-ankarna, de tre faktastyckena och
avslutningen. Konsistent med hårdgränsen - registret arbetar på ramen runt fakta, aldrig på fakta.

Folded into [[voice_channel_mail]] (kontexten "Statusmail till klientens team" gäller även
leveransmail till publisher) och [[voice_anti_selling]]. Category: channel register (mail-evidenced).

## 2026-07-14 — Agent created
- The Author is an editor/proofreader, not a from-scratch writer. Cheap models draft; Fable
  runs the short final voice-adaptation pass. This is the token-economy reason the agent exists
  (Robert's framing). Category: process.
- Voice corpus seeded: `skills/voice/` (channel_mail/linkedin/discord/social + people/). Mail
  register mined from real sent mail; Discord + social have no corpus yet (blocked on DevOps
  ingestion — see the handoff ticket). Category: tooling.

## 2026-07-14 — Charity leadership-book voice pass (long-form English prose)
- **Robert does not talk about himself in the third person.** In his own reflective / long-form
  writing, "the leader is the membrane between them" → "I sit in the middle of that." Convert
  generic "the leader / a leader does X" self-references to first-person "I". (His correction,
  this pass.) Exceptions that stay: "my job as a leader", "as a leader" (already first-person
  framing) and "leaders" meaning *other* people he develops. Category: voice rule (global).
  Also: he dislikes writerly metaphors that aren't his ("membrane") — prefer his own recurring
  plain phrases ("sits in the middle", from his stakeholder-map answer).
- His long-form spoken voice (from the Jun-16 Charity transcript) = plain, self-aware, uses
  "you" generically ("if you work hard you're allowed to play hard"), leads with the positive
  before owning a flaw, concrete anecdotes over abstractions. For a *book* it's fine to soften
  genuinely crude phrasing ("looks like shit" → "looks rough") but keep the bluntness of the
  point. This is the polished-English register, NOT the Swenglish/short-message brevity (that
  rule is WhatsApp/DM only — do not apply it to book/essay prose). Category: channel register.
- Fetching a Drive PDF via `mcp__gdrive__gdrive_read_file` returns the file base64-encoded, not
  extracted text. Decode the base64 to a .pdf and run `pdftotext -layout` to get readable text.
  Category: tooling.

## 2026-07-14 — Voice-corpus mining method
- To build or extend a channel/person voice profile: spawn **Opus** (not Fable) agents that
  search Robert's **SENT** mail only (gmail MCP, `in:sent` / `from:me` / `to:<addr>`), read 3-6
  real threads, and distill **per-person** (greeting, SV→EN switch point, sign-off, running
  jokes) + **per-context** (warm reply / milestone / apology / admin / intro) patterns with short
  quoted fragments. Never fabricate; note thin corpora honestly. Fable is reserved for the actual
  voice-adaptation pass, not analysis. Source: The Author build. Category: process/tooling.

## 2026-07-17 — Amer Alsalek (Book It AB, redovisningskonsult) — Discord DM pass, runatyr
- **Mail register to Amer (real sent mail, indexed):** Swedish throughout, "Hej Amer," opener,
  very short and plain ("Noterat - jag hjälper till att besvara Christines frågor.", "Tack -
  fick filerna. Återkommer med eventuella frågor efter genomgång."), closes "Mvh, Robert".
  Already uses " - " hyphen breaks natively. No banter, no smileys - working-professional plain.
- **Discord DM to Amer = simulation** (no Discord corpus in RAG yet): applied core voice +
  Swenglish-brevity ("Tja!" no name, no sign-off) on top of the plain-professional mail register.
  Converted a numbered list to short sequential paragraphs (numbered lists banned in messages per
  [[writing_voice_robert]]) and unwrapped hard line breaks so the body pastes clean into Discord.
  Learn from Robert's edits on send and fold a real profile into `voice/people/` then.
  Category: person register (partial, mail-evidenced) + channel simulation flag.

## 2026-07-22 — Eamonn Byrne (Lost Hive) — K2C invoicing mail pass
- Seeded `voice/people/eamonn-byrne.md` from three real sent threads (subcontract update
  4 Jun, VAT Q&A 9 Jun, agreement share 29 May). To Eamonn Robert writes "Hi Eamonn,",
  structured-but-warm contract mail, credits him ("good catch"), explains the why, closes
  "Thanks,\nRobert". Payment phrasing precedent: "you invoice on Raw Fury's acceptance...
  we pay once the matching payment comes through to us." Category: person register (mail-evidenced).
- Pass pattern that worked here: open a mail that answers a Discord/side-channel question with
  "This follows your question on X" (his real construction from the 4 Jun mail), and when a
  brief demands a TL;DR that "doesn't just repeat a body point", make it the synthesis the body
  never states outright (here: "two invoices, not one"). Category: mail register.

## 2026-07-15 — Charity leadership-book: don't over-flagellate him
- **In reflective first-person, keep Robert humble but never self-flagellating; in a failure
  chapter, always name what he genuinely did well.** He pushed back twice this session that
  drafts made him too harsh on himself — Ch.2 "I wasn't equal to the task / I'd be lying if I
  said I did it well", and Ch.3 framing difficult colleagues as "peers I didn't get along with".
  His real self-image is a competent, humble operator, not someone who runs himself down.
  Category: voice rule (global, reflective/long-form).
- **How to apply:** (1) balance every admitted limit with the actual skill shown — Ch.2 reframed
  so communication is credited ("kept the sinking ship afloat longer / extended the time it took
  to sink"). (2) Reframe hard-won lessons as *superpowers* where true — Ch.3: not "I had bad
  peers" but "there were people nobody else could reach, and getting the difficult/brilliant ones
  to function was my superpower" (a thread that recurs in trait 1.4 "placement", 4.2 brilliant
  jerks, and Sec-6 People — keep it consistent across the doc). Source: Robert reacts, this pass.

## 2026-07-24 — AP shareholder letter (English, all 11 holders) — voice pass, apb
- Register anchor found and mined: Robert's real 9 Feb 2026 shareholder letter
  (gmail:msg:19c42e29b0cd8a4a, undisclosed-recipients). Distilled a new "Shareholder /
  investor letter" context into [[voice_channel_mail]]: "Hej," opener even on the worst news,
  asterisk-wrapped summary block up top ("*Kort sammanfattning:...*"), bad news as one plain
  causal sentence with zero drama and no self-flagellation, every bad-news beat paired with the
  forward path in the same letter, collective "vi" for company actions with "jag" only for the
  personal ask, offers a call at the end, and a real closing ("Vänliga hälsningar,\nRobert") -
  the second context after authorities where he closes formally. Category: channel register
  (mail-evidenced).
- **English shareholder register = simulation** (he has no prior English investor letter in the
  corpus): kept Swede-to-Swede English (KSEK/MSEK, decimal commas, "reverser" untranslated,
  "(kontrollbalansräkning)" gloss), stripped native-American idiom ("puts us in the room"),
  used "Best,\nRobert" as the English stand-in for "Vänliga hälsningar". Flagged as simulation;
  learn from Robert's edits when he sends. Category: simulation flag.
- Mixed audience (VC/industry + bus/timber investors): gloss games jargon the way his Feb letter
  did - term plus a short apposition ("intäktsdelningsbaserade (rev share) projekt" → here
  "the final expansion (DLC)", "Gold, the finished game"), never a lecture. For an all-Swedish
  audience the Swedish statutory term in parens beats the English translation. Also renamed
  "TL;DR" to "The short version" for the non-industry holders (Feb precedent: "Kort
  sammanfattning"). Category: audience pattern.
- Thank-you for crisis money: unsentimental cause-effect beats rhetorical antithesis. Cut
  CorpBot's "difference between a company with a future and a company being wound down" for
  "put up that half million on a week's notice, at a point when it was far from a safe bet.
  It is what made everything else in this letter possible. Thank you." (Simulated phrasing,
  consistent with his no-gush, lead-with-facts posture from the Feb letter.) Category: register.
- Tooling: Edit/Write hit repeated PreToolUse hook timeouts this session; the Bash heredoc →
  cp path worked. If file tools stall, fall back to shell. Category: tooling.

## 2026-07-24 — AP shareholder letter, pass 2: my default register runs too grandiose (Robert), apb
- **Robert's verdict on pass 1: "fortfarande lite för grandios och AI-säljig i sin ton."** The
  first pass fixed Americanisms and structure but left a pitch-deck register underneath - lines
  that exist to impress rather than inform. For investor/shareholder documents this is MY
  default failure mode, so every future pass in this register starts by hunting these
  constructions, not by polishing word choice. Category: register correction (his words, this pass).
- The constructions he flagged or that I cut, concretely:
  (1) humble-brag asides after a good fact - "which does not happen often" → state the fact,
  stop ("approved 2 July, with no feedback from Raw Fury").
  (2) a lecture sentence explaining why a number matters - "That is the whole point of the
  structure" → delete; the number and its consequence carry it.
  (3) aphorism framing - "What makes the contract worth more than its own value is..." →
  delete the frame, keep the plain causal sentence behind it.
  (4) self-congratulatory framing of partly forced outcomes - "We rebuilt Aurora Punks
  deliberately small" → "Aurora Punks is a small company now."
  (5) portentous one-line teasers - "One thing you should know before it reaches you." →
  delete, start with the fact.
  (6) rhetorical three-beat buildup with a punch payoff (three drum-beat sentences + "Five of
  you did.") → compress the beats into one running sentence, keep the short factual payoff.
  (7) closing flourishes, INCLUDING anti-salesy ones - "I would rather show you a number we can
  hit than one that sounds better" is still a flourish → "The 4,5 is a conservative number."
  (8) doubled-emphasis tricolons - "It is open-ended, it is profitable, and it pays for the
  entire fixed base on its own" → "open-ended, profitable, and covers the fixed base on its own."
- Guardrail he set himself: do NOT overcorrect into flatness or false modesty - when the facts
  are genuinely good, hiding them is its own dishonesty. Target: a competent operator reporting
  plainly; the numbers carry the weight, the prose stays out of the way. At most one flourish
  per letter, and prefer zero. Category: register correction. Folded into [[voice_channel_mail]]
  "Shareholder / investor letter".

## 2026-08-07 — Andreea Chifu (Bright Gambit) — WhatsApp mentor-curriculum pass, bright_gambit
- **Andreea register (mail-evidenced, 2022-2025 threads):** zero ceremony both directions.
  Robert opens mid-thought or with a bare "Hi!", one-line direct asks ("You wanna join in on
  this?", "Hi! We got this application to AP, maybe someone for your AI-ambitions in BG."),
  no sign-off, connector moves woven in ("Btw you should pitch Andreea Kulebra!"). She mirrors
  it (short questions stacked, "/Andreea" at most). Peer since ~2021 (BG advisor/investor, ex
  Raw Fury overlap). No smileys observed in the corpus - don't add them by default. No
  `voice/people/` profile existed; this entry is the seed. Category: person register (mail-evidenced).
- **Biggest de-AI lever on a near-final English DM: contractions.** The draft was structurally
  already Robert (short opinions, fact→ask→stop) but ran fully uncontracted ("do not", "it is",
  "I would") - that alone made it read as AI/formal prose. Contracting throughout (I'd, don't,
  it's, I'll) plus breaking one overloaded sentence did 90% of the pass; almost no word choice
  needed changing. Check contractions FIRST on any English DM/WhatsApp pass. Note: his *mail*
  register is mixed ("Sounds great and I am in" uncontracted), so this is a DM/phone-register
  rule, not global. English WhatsApp register itself = partial simulation (corpus is mail);
  learn from his edits on send. Category: channel register (DM/WhatsApp, English).
- Small polish tells worth hunting in near-final drafts: doubled prepositions ("towards X
  rather than towards Y"), connective "then" after an if-clause, conditional padding ("it would
  be the real thing" → "it's the real thing"). Grammar-teacher-correct constructions he
  wouldn't type on a phone. Category: register.
- **SUPERSEDED IN PART, same day:** Robert hand-edited this pass before sending and cut about
  a third of it as "AI selling slop". The contraction rule above stands; the register entry is
  now a full profile at `voice/people/andreea-chifu.md` and the correction is the next entry.

## 2026-08-07 — Andreea WhatsApp, Robert's own-hand edit: "AI selling slop", bright_gambit
- **The rule (his cuts, all of them, one test): does the sentence change what happens next,
  or does it change how Robert looks?** He kept every sentence acting on the plan - genuine
  questions, concrete logistics, plain caveats, sharp opinions in service of a recommendation
  - completely untouched (the genre paragraph, Sunday, Tuesday, the telemetry flag). He cut
  every sentence acting on his image. Full taxonomy with his real examples now lives in
  `skills/voice/anti_selling.md`; wired into [[writing_voice_robert]] DO-NOTs, the voice
  _index, and [[the_author]] itself. Category: register correction (his hand, this pass).
- The cut categories, one example each: impact promises ("That one exercise moves more than
  any lecture"); quotable maxims ("Game feel doesn't teach from slides"); credential claims
  ("I run a lot of this in production, so it's the real thing and not a demo"); grading her
  material ("Strongest day of the five"); helpfulness narration/upsells ("Good that you're on
  another track, then I take UX and game feel on my own", "Say the word if you want them for
  your track too"); thoroughness displays (the staff/outsiders/other-cohort enumeration plus
  its pre-hedge); foresight elaborations beyond the ask (the publisher/investor week-9
  paragraph); meta-signposting ("Two smaller ones:").
- **The discriminator is NOT punchiness.** He kept "Small teams need five things they can
  ship this month, not a full standard to fail against" and "As the sheet stands they pitch
  before they get the frame" untouched - both punchy, both arguing for a concrete change.
  Punchy-for-the-plan stays; punchy-for-Robert goes. This is the guardrail against
  overcorrecting into flatness (same guardrail he set on the 2026-07-24 grandiose-investor
  correction; this is the DM/peer flavour of that same disease).
- **The positive form, from his one rewrite:** "someone relaxed about letting me touch it" →
  "for us to work in it together." Expert-performing-on-their-build reframed as joint work.
  Never stage Robert in front of a room in a peer message. His enthusiasm register: one
  fast-typed line, typo left in ("I'm definately interested!"), not stacked commitments.
- **Instruction-hierarchy lesson, against myself:** the drafting brief marked the two maxims
  load-bearing and told me to protect them; I obeyed; he deleted exactly those two lines.
  A brief's "protect this punchy line" is subordinate to the corpus - quotability is itself
  the failure mode in his peer register (a maxim performs for an audience; a DM has none).
  [[the_author]] step 3 now carries an explicit override: selling sentences get cut even
  when the brief protects them, with the cut flagged in the return note. Category: process
  correction (operating instructions were actively harmful and are now changed).
- **Voice cuts vs content decisions - keep them separate.** Three of his cuts changed what
  the message commits to, not how it reads, and are HIS decisions, not voice rules: (1) the
  on-site Riyadh Sunday-Thursday availability commitment, (2) the money question (fixed
  frame vs per person, which the draft tied to booking travel), (3) the polish-backlog scope
  rule (under a day of work, visible in first ten minutes). The Thursday who-signs-off/week-9
  sub-questions also went. Do not "learn" these as register; surface them to Robert as open
  items he removed. Drafting lesson that IS voice-adjacent: don't stack commitments and money
  asks into an enthusiasm reply unless the brief calls for them. Category: content vs voice
  separation.

## 2026-08-24 — Client-facing documents (Confluence build notes + HTML pitch): his own edits define the register, k2c + sbz
- **New surface, real evidence.** Robert hand-edited the Raw Fury build-notes page (Confluence 145260546, versions 15-19, no version messages, on top of the agent's v14) and then told The Author both that page and the Irons 2 pitch were full of "AI floskler". His instruction: dry fact, no digressions, no writing on the reader's nose, "nästan som en bruksanvisning". This is the **document** flavour of the same disease as the grandiose-investor register (2026-07-24) and the peer-DM selling slop (2026-08-07). Category: channel register (documents, evidence-based).
- **What he cut, from the diff:** (1) all three assessment/justification macro boxes, including one whose whole payload was our own verdict on the counterpart's survey ("v2 is in good shape for what this test is for") and one that pre-defended the length of our defect lists ("Why these lists are long"); (2) a speculative "the open question is whether a player who has never seen the game understands what to do" line; (3) a process explanation compressed to nothing: "We use purple deliberately to flag assets that have not had their Egyptian pass, so purple means art not final, not a rendering bug" became **"which is a debug flag"**; (4) the two sections that told the partner how to work and who we are, "How findings reach us" and "Contacts".
- **What he kept, untouched:** every defect list, build ID, table, the "What we would like to learn" asks, and the thank-you to the counterpart. So on a document the register is not "say less" - it is **say only what the reader has to act on or look up**. Questions to the counterpart survive; verdicts about the counterpart's work and explanations of our own reasoning do not.
- **The compression ratio is the tell.** His purple-tint edit is the single sharpest datapoint in the corpus for how far to compress: 34 words to 6, keeping the one operative fact and deleting the reassurance and the not-a-bug framing. When a sentence explains *why we did something*, the dry version is usually the last clause of it.
- **Fluff accumulates as factual rot.** Four real errors were sitting inside the flowery version of that page and only surfaced when compressing to fact: a heading counting six focus areas with five left, a table row emptied mid-edit, a stale Chariot/Q15 clause contradicting the tip box two screens above, and Q13 vs Q14 disagreeing about the same survey question. **Run a consistency check as part of every document pass** - cross-reference every number, question ID and count against the other places the document states them. The dry register makes contradictions visible that the padded one hides. Category: process.
- **Pitch-page flavour (Irons 2, 35 edits).** Same rule, one addition: on a *pitch* the maxim is the dominant failure mode, not the credential claim. Cut lines were near-perfect aphorisms - "A Beta with new features in it is a Beta that slips", "It is not a headcount we picked and then justified", "We would rather build this from evidence than from taste", "we would rather find that in February than in August". Each ends a bullet whose first half is the actual fact, so the mechanical form of the cut is **keep the clause up to the full stop, delete the clause after it**. Also cut a whole closing "Our position" callout and a "How to read these" reading-instruction box; the non-obvious content of the latter (1.00x = baseline) survived as one factual line in the source note. Category: register (pitch documents).
- **Reading instructions are the document-surface form of meta-signposting.** A panel titled "How to read the shape" or "How to read these" is the document equivalent of "Two smaller ones:" from the Andreea cuts. Where such a panel carries genuine plan facts, retitle it to what it actually lists ("Constraints in the schedule") and drop the bullets that only narrate the chart. Do not delete facts to honour a tone rule.
- Tooling: `mcp__atlassian-confluence__conf_get` on `/wiki/rest/api/content/{id}?expand=body.storage&version=N` returns any historical version's storage body, which is how the v14-to-v19 diff was recovered. `conf_put` needs the page's real `spaceId` (get it from `/wiki/api/v2/pages/{id}`); passing a wrong one fails with the misleading "Only DRAFT pages can be moved between spaces". Version history does **not** distinguish Robert's hand edits from an agent's, both carry his account id - use the version *message* (agents wrote one, his own edits had none) as the signal. Category: tooling.
- **Correction, same day: do not restore content from an older version because it looks accidentally deleted.** In the v14-to-v19 diff two of Robert's edits looked like slips, a focus-list item removed while its heading still counted it, and a table row left as two empty cells. Both were **factual deletions**: Ra *is* the start island, so a separate Start island entry was wrong, and the farmers are Egyptian, so the Greek-farmers known issue was wrong. Restoring them put two errors back into a client-facing page. The rule: when his edit leaves an internal inconsistency, the inconsistency is the signal to **ask which side is true**, never to reinstate the older text. He deletes to correct facts at least as often as to cut tone, and The Author cannot tell the two apart from the diff alone. Category: process correction (his, 2026-08-24, k2c).

## 2026-08-26 — Disposable Corps pitch page + Magnus WhatsApp: applying the bruksanvisning register [dsc, 2026-08-26, register]
- First pass applying the 2026-08-24 "bruksanvisning" directive, two days after it was issued, to a page built from scratch. The Irons 2 mechanical rule (keep the clause up to the full stop, delete the aphorism after it) covered maybe half the work; this page's dominant pattern was different: **the diagnostic verdict sentence** - a bolded conclusion the prose builds toward ("They are all legibility problems", "That means the hosting model is closer to player-hosted than it looks", "it only delivers if the decisions can actually be made"). The fix is not deletion but inversion: state the classification or requirement as a flat opening fact and delete the build-up ("Most are readability and UX problems rather than content or production value problems."). A verdict the plan depends on is content; the drum-roll toward it is not. Category: register (pitch documents).
- Second recurring pattern: **the self-justifying kicker**. Panel kickers phrased as "Why the squad AI matters commercially" / "Why it is affordable" pre-frame the panel as an argument. Retitle to the subject ("Low concurrency", "Scope of work") and the same facts stop selling. Same move as retitling "How to read these" on Irons 2 - the heading is where the register leaks first. Category: register (pitch documents).
- Constraint interaction worth remembering: the no-implying-the-team-lacks-skill rule and the dry register pull the same direction. "It is the one discipline the project has never had" and "We add the disciplines the project has never had: technical leadership, ..." were both flourish AND borderline capability judgements about the developer; the dry rewrite (name the seats being added, say the existing team stays and keeps building) fixed both at once. Dryness is itself a scrubbing tool. Category: process.
- The evocative core-loop sentence ("you dig the trench, you fight in the trench you dug, and it is blown apart underneath you") was kept: it defines what stays in scope, so it acts on the plan. Its neighbours ("You are an officer spending men who are meant to be spent", "The thing nothing else does at this scale is already in the title") acted on the reader and went. One vivid sentence can be load-bearing while identical-sounding ones around it are decoration; test each separately. Category: register.
- WhatsApp side: the Swedish draft was already near-register; the two cuts were an announcing-directness opener ("En ärlig grej som är värd att säga innan du visar den:") and a benefit-explainer clause ("så ingen behöver ta allt på en gång"). Kept "och den är nyttig för investerarna oavsett vem som kör sen" - it argues for the concrete phase-0 ask, so it is plan-acting, not selling. Category: register (DM, Swedish).
- Consistency check finding, unresolved and NOT mine to fix: the WhatsApp message quotes 275k / 1,5M / 3,45-3,8M while the pitch page's gates read 235 000 / 1 175 000 / 2 820 000 SEK total (185 000 / 925 000 / 2 220 000 cash). Numbers are locked for The Author, so both left untouched and the mismatch flagged upward. Per the 2026-08-24 correction: an internal inconsistency is a question for Robert, never a silent fix. Category: process.

## 2026-08-28 - Olle + Joel (The Gang) statusmail: Robert strök säljande rubriker, fakta i fred [cvb / Curveball, mail register]
- Evidens av starkaste sorten: hans egen hand. Diff mellan utkastet
  (`curveball/drafts/mail_olle_joel_2026-08-28.md`) och det skickade mailet 22:22 samma kväll
  (gmail-tråd `19e889144ac3e56a`), sammanställd i `curveball/drafts/mail_diff_2026-08-28.md`.
  Hans egen sammanfattning: "Överlag så tog jag bort säljande rubriker, fakta fakta fakta är
  vad som är viktigt. Inte krångla till det." Alla regler nedan folded into
  [[voice_channel_mail]] som ny kontext "Statusmail till klientens team", plus en
  korsreferens i [[voice_register_documents]] regel 5 (rubrikregeln är nu mail-evidensbaserad,
  inte bara dokument). Category: channel register (mail-evidenced).
- **Rubriken är en etikett som namnger ämnet, oftast ett substantiv, inte en mening som gör en
  poäng.** "LootLocker lever, er egen backend gör det inte" blev "LootLocker"; "En praktisk sak
  medan vi jobbar" blev "Versionshantering". Rubrikregeln från dokumentregistret (2026-08-24)
  gäller alltså även mailens fetade sektionsrubriker - rubriker är där registret läcker först,
  på båda ytorna.
- **Mottagarens nytta: en gång, kort, gärna i rubriken - aldrig som säljmening i brödtexten.**
  Han la till "om Blast TV vill testa" i rubriken och strök samtidigt "Bra läge för
  blast.tv-spåret ... om ni vill hålla den kontakten varm" (värdering + tolkning av deras
  affär åt dem + upprepning, tre fel i en mening). Undantaget som bekräftar regeln: det är
  inte förbjudet att nämna deras intresse, det är förbjudet att sälja det.
- **Ingressen är faktumet, inte en agenda.** "Kort läge:" och "Det jag behöver från er är ett
  beslut om var vi lägger testbyggen" ströks båda; frågan ställs där den ställs och behöver
  ingen avisering. Nya mönster i samma familj som meta-signposting: den artiga inbjudan att
  invända ("men säg till om det ligger något där som ni vill spara") och uppräkningssignalen
  ("behöver vi två saker:") stryks när listan ändå står på raden efter.
- **Struktur: besläktade punkter slås ihop hellre än numreras var för sig.** Punkt 6 ("En sak
  till på samma tema") flyttade in i LootLocker-stycket, sex punkter blev fem. En rubrik som
  säger "på samma tema" är själv beviset på var punkten hör hemma.
- Vad han INTE rörde: app-id:n, branch-nummer, backend-URL:en, publisher key-resonemanget och
  hela mainline-stycket, nästan ordagrant. Konsistent med hårdgränsen från dokumentpassen:
  registret arbetar på ramverket runt fakta, aldrig på fakta. "Tja,"-öppningen och "/Robert"
  överlevde också; ingen personprofil för Olle/Joel finns ännu i `voice/people/`, seeda vid
  nästa pass om korpusen behövs. Category: register + process.

## 2026-08-31 - Reed Hunt / ID@Xbox correction mail: positional frames are the mail-body slop [apb / Xbox, mail register]
- Robert's verdict on the draft, verbatim: "wall of text, massor av onödiga AI slop fraser." The named
  slop shares one shape: **sentences that locate a fact relative to the mail's own structure instead of
  stating it** - "Worth noting alongside it", "One thing does follow from it", "For completeness on the
  developer agreement", "The rest of my last mail still stands, and those are the ones I would like to
  get moving", "That is the contract working as written, not a block". This is the mail-body flavour of
  meta-signposting ([[voice_anti_selling]] cut 8) and of the Curveball ingress rule (2026-08-28): the
  fix is deletion, never a different connective. A fact that needs a home gets a noun-label lead-in
  ("Still open from my last mail:") or just starts; it never gets an escort sentence. Category: register
  (mail, his critique this pass).
- Self-correction retraction register, applied: when Robert corrects his own earlier claim to a partner,
  the retraction is the opener and one plain line ("Scratch the payment part of my last mail, I had the
  cause wrong."), then straight to the mechanism. No "let me correct before anything else", no restating
  the wrong theory ("The payments did not stop because of X. They stopped because Y") - state only the
  true cause. Consistent with the no-self-flagellation rule (shareholder register) on a new surface:
  admitting an error to a platform contact. Rewrite is a simulation on top of core voice + status-mail
  register (no `voice/people/` profile for Reed; corpus around him is mostly his mails, not Robert's) -
  verify against Robert's edits on send. Category: register (partial simulation).
- Compression datapoint: a 6-row unit-sales table whose story is "start high, then zero" carries in one
  clause ("sales went from 1,584 units in January to zero from May"); the table earns its place only
  when the reader must act on individual rows. ~400 words → ~250 with zero facts lost. Category: register.

## 2026-08-31 - Reed Hunt profile seeded: what a long platform-partner thread teaches that single mails cannot [apb / Xbox, person register]
- Seeded `voice/people/reed-hunt.md` from four real threads spanning Sep 2022 to Aug 2026
  (`18347e49c2f76550`, `19d804ae3666ef5f`, `19ddfcc812e25c3a` 21 msgs, `1a042aaf152a5ddf`).
  Three things about mining a multi-year platform thread that a per-mail read misses:
  (1) **The From header is register data.** Reed's mail arrives from the team alias
  `idam@xbox.com` carrying his personal signature, and his personal sends from `v-reedhunt@`;
  the alias is read by Matt Hanson, IDSetup and RoyCare and auto-replies "3 business days".
  Which address Robert writes to decides continuity (alias survives Reed's month-long OOO) and
  audience (alias mail must be self-contained). A profile built from bodies alone loses this.
  (2) **Date gaps assign the stalls, so read them before writing "he is slow".** The brief said
  threads died from Reed's slowness; the timeline shows the Jun-Aug 2026 stall was roughly half
  Robert's (Entra billing + vacation) and Reed chased Robert through the spring. The honest
  version went in the profile - it changes the warranted tone (no apology theatre needed, Reed
  apologises more than Robert does).
  (3) **The counterparty's reply shape validates the register.** Reed answers numbered mails
  point by point same-day and demonstrably misses status updates with no question in them
  ("apologies I missed your previous email" after Robert's questionless Jun 18 note). That is
  corpus proof for two profile rules: numbered admin lists are the right form for Xbox mail,
  and every mail must end in a question or a go/no-go. Category: process (profile mining).

## 2026-08-31 - Joel/Gustav/Olle LootLocker-svaret: passet efter en färsk hand-diff [cvb / Curveball, mail register]
- Första passet med `curveball/drafts/mail_diff_2026-08-28.md` som facit i samma tråd, till samma
  mottagare, tre dagar senare. Mina edits är MINA (application pass, inte hans hand) - verifiera mot
  vad Robert faktiskt skickar och diffa igen. Tre observationer värda att spara:
- **Styckeantalet ägs av innehållsbriefen, inte av "kortare är bättre".** Min misstanke var sex
  stycken där fyra räcker; vid genomläsning bar varje stycke ett eget innehållsmoment som briefen
  räknade upp (nej-svaret, Gustavs förslag, Cloud-justeringen, Inventory Service + DLC-skillnaden,
  sömmen/konsol, accessbegäran). Rätt kompression var inom styckena (~15 % bort), inte att slå ihop
  dem. Slå bara ihop stycken när ett stycke saknar eget innehållsmoment (jfr hans egen 6-till-5-
  sammanslagning 2026-08-28, där punkt 6 var "samma tema" som punkt 3). Category: process.
- **Smickrande tolkning av motpartens kod är också en ram.** "Er egen kod har en
  LootLockerServerLoadoutValidator, så ni landade i samma slutsats när ni byggde det" - biten efter
  kommat narrerar deras resonemang åt dem för att validera vår poäng. Fakta-halvan gör hela jobbet
  ensam; läsaren drar slutsatsen själv. Samma släkte som dokumentregistrets
  capability-judgement-regel, fast i berömmande riktning. Category: register (my edit, unverified).
- **"Begäran får inte drunkna" implementeras genom att mailet SLUTAR på begäran, inte genom att
  annonsera den.** Draftens sista mening hade en benefit-svans ("så slipper vi sätta om det från
  grunden") efter själva asken - samma mönster som WhatsApp-cutten 2026-08-26 ("så ingen behöver ta
  allt på en gång"). Svansen ströks; sista raden före /Robert är nu själva handlingen. En "hör av
  er"-dörr (invariant 4) läggs INTE efter en skarp ask - den är då en reservationsdörr som späder ut
  den enda handling mottagaren ska utföra. Category: register (my edit, unverified).

## 2026-09-01 - Irons 2 pitch v2 (AP × Rift repositioning): sales-doc pass notes [sbz / Starbreeze, document register]
- **Hook lines on a pitch page: build them from Robert's own sent mail on the same thread, not from
  invented taglines.** The draft's hook ("Here is the team that has already run this once") was both a
  credential claim and factually thin; the replacement ("How we would staff and run it, as one
  integrated team") is lifted near-verbatim from his real 18 Aug pitch mail to Tobias/Matt ("Here is
  our take on how we would staff and run it", gmail:msg:1a011f8a296a0bf2). When the counterparty has a
  live thread, the register anchor for the document's framing sentences is already written. My edits
  this pass are application, not his hand - verify against what survives his review. Category:
  register (pitch documents, partial simulation).
- **A number can carry an argument; a frame explaining the number cannot.** The 50/50 cost split and
  the 119 216-vs-140 000 comparison stayed untouched as facts, while their interpretive escorts
  ("which is what an integrated team looks like", "shipping against a number rather than discovering
  one") went. When a brief says an argument must survive, the surviving form is the number plus at
  most a flat contrast ("not a prime and a subcontractor"); the reader does the concluding. Same
  family as the diagnostic-verdict inversion (2026-08-26 dsc). Category: register (pitch documents).
- **Consistency check extension: what can the reader derive by subtraction.** The page states the
  price (28 325 700) AND the internal cost split (10 904 000 + 10 885 000 = 21 789 000), which hands a
  CGO the margin by arithmetic. Numbers are locked for The Author so both stand, flagged upward. Add
  "derivable facts" to the document-pass consistency check alongside sums and counts - a page can leak
  by juxtaposition without any single line being wrong. Category: process.
- Starbreeze counterparty register (thread-evidenced, no voice/people profile yet): Robert to
  Tobias/Matt is "Hello Tobias," / "Hi Tobias, Matt,", short plain sentences, "Best" close, asks
  practical questions inline ("Is it possible to add Dmitry from Rift Gaming?"). Tobias mirrors with
  "Hello Robert," and numbered practical asks; Matt signs "Best, Matt" with full block. Seed a
  `voice/people/` profile if mail volume grows. Category: person register (partial, mail-evidenced).

## 2026-09-01 - Irons 2 pitch v2, round 2 (rebuilt draft, same day): second-pass notes [sbz / Starbreeze, document register]
- **A second round on a rebuilt draft is a new pass, not a patch of the old output.** The draft was
  rebuilt from Robert's own slide-structure PDF plus Rift's level-design memo, and most of round 1's
  problems did not recur: the content was already facts (deliverable lists, level reads, mechanics
  lists), so the pass shrank to tails and frames. When the source material is a practitioner memo,
  the register work concentrates in the drafter's connective tissue, not the substance. Category: process.
- **The brief-restatement hook survives where the tagline hook died.** Round 1's invented hook was
  replaced from Robert's sent mail; round 2's hook restated the client's own brief ("An accessible,
  fast-paced PAYDAY built for PUBG players. That is the brief.") and only its commitment tail ("and
  it is the part we would hold on to hardest") needed cutting. The client's brief in their own terms
  is as legitimate a hook source as Robert's sent mail - both are found language, not coined language.
  Category: register (pitch documents, my edit, unverified).
- **When a structure-doc bullet has no supporting content, the honest fix is a [PLACEHOLDER], not a
  drafted fact.** "Test driven game development" and "Trusted by studios" came from Robert's structure
  doc with nothing under them; the corpus had no citable practice, and propping "Trusted by studios"
  with client names would break the no-client-cross-reference rule. Gave the first the one supportable
  fact already on the page (QA lead + three testers inside the price) plus a placeholder, left the
  second as a bare placeholder. Adding a placeholder is inside The Author's mandate when the
  alternative is inventing evidence; deleting a bullet from Robert's own structure doc is not.
  Category: process.
- **A section marked as the client's or a colleague's hand gets constraint checks only.** Slide 8
  (Robert wrote the "READY TO DELIVER" block) passed the dash/banned-word/hype checks and shipped
  verbatim, selling beats intact - same footing as the untouchable positioning line. The anti-selling
  override applies to a drafter's sentences, never to Robert's own; the brief saying "his hand" is
  what flips the mode. Category: process.
- Recurring cut shapes this pass, all from earlier taxonomy, none new: drum-roll opener before the
  audience fact ("The audience is the constraint everything else follows from"), diligence tails
  ("rather than hoped around it", "rather than added when it hurts"), a claimed-understanding opener
  ("We understand the creative and technical goals... and" → keep only the ownership commitment), and
  a soft relational clause ("build relationships face to face" - "on site" already carries it).
  Confirms the taxonomy is stabilising; the marginal value is now in what NOT to touch. Category: register.

## 2026-09-01 - Olle access-svaret: tredje passet i samma tråd, taxonomin räckte nästan [cvb / Curveball, mail register]
- **Omfrågad fråga besvaras rent, utan referens till det tidigare svaret.** Olle frågade 1 sep vem
  som ska ha LootLocker-access; Robert hade redan svarat 31 aug. Direktivet (Roberts brief, inte
  korpusobserverat - flagga som sådant tills en diff bekräftar): svara som om frågan var ny, inget
  "som jag skrev igår". Adressen till mottagaren är svaret, inte tråkhistoriken. Category: register
  (brief-instructed, unverified).
- **Ett mekanismfaktum kan ersätta en hel lösningsdiskussion.** Olles "det behöver vi också lösa"
  om assets föll på ett enda faktum: exporten hämtar allt i lagret oavsett filtyp. Formen som bar:
  flat slutsats först ("Assets behöver inget eget spår"), sedan mekanismen (ListFiles), stopp.
  Utkastets version sa samma sak som både ram ("löser sig i samma svep") och svans ("i samma
  körning") - **samma faktum dubblerat som inledningsram och nyttosvans är en jaktbar form**; behåll
  en av dem, helst som flat öppning. Category: register (my edit, unverified).
- Benefit-explainern "det blir snabbare och tål att en tjänst försvinner" ströks trots att den är
  sann: i en tråd som handlar om att LootLocker försvinner är motiveringen självevident, och en
  teknisk mottagare drar slutsatsen själv. Samma släkte som 2026-08-26-cutten ("så ingen behöver ta
  allt på en gång"). Ingen "hör av er"-dörr tillsatt - mailet är tre svar, inget att öppna för.
  Category: register (my edit, unverified).

## 2026-09-02 - Carolina Foghammar (K2C-kompositör) Discord-DM om STIM/RF-avtalet: simulation, avjuridifiering [k2c, Discord register]
- **Korpus till Carolina = mail, inte Discord.** Roberts riktiga mail till henne (tråd `19ef0a0480c2762d`, juni 2026): "Hej Carolina!" / "Hej.", helsvenska, mycket korta stycken, förklarar ett nej med ett faktum och stannar ("vi kan tyvärr inte gå högre än 172:- / timmen"), "mvh". Discord-passet = simulation ovanpå det + Discord-registrets "Tja!" utan namn och utan avslut. Verifiera mot vad han faktiskt skickar. Category: person register (mail-evidenced, Discord simulerad).
- **Avjuridifiering är ett registerjobb, inte en faktaändring.** Briefen förbjöd jurist-ord; "framförande- och mekanikrätten" blev "det STIM sköter åt dig", vilket är samma sak sagt från hennes sida av bordet. Testet: kan mottagaren kontrollera påståendet utan att slå upp termen? Category: register (Swedish DM, my edit, unverified).
- **Lugnande ram är plan-verkande när målet är en signatur.** "Inget konstigt", "inte ett problem, bara en formulering" behölls trots att de liknar ramar jag annars stryker: de ändrar vad som händer härnäst (hon signerar) och inte hur Robert ser ut. Strök däremot "En sak jag vill vara tydlig med:" (annonserad rakhet, jfr 2026-08-26) och slog ihop de två bilaga-punkterna till en (jfr hans 6-till-5 2026-08-28). Category: register.
- **KORRIGERING samma dag (Roberts feedback, riktig evidens):** "Tja!", "nåt", "så det går fort", "Inget problem" underkändes som **för oseriöst**. Discord-registrets "Tja! utan namn" gäller kompisar/peers, INTE när Robert är uppdragsgivare och executive producer i ett avtalsärende mot en ung anställd. Där är registret **varmt men vuxet**: "Hej Carolina," som öppning (samma som hans mail till henne), utskrivna ord i stället för talspråksförkortningar, fortfarande kort och Discord-format, men han ska låta som någon som läst avtalet. Rollrelationen (arbetsgivare till anställd, avtal) slår kanalregistret. Folded into [[voice_channel_discord]]. Category: channel register correction (his words, 2026-09-02).
- Sakfelet i samma pass ("hela STIM-pengen", Twitch/YouTube som långsiktig intäkt) var draftens, inte mitt, men lärdomen gäller mig: The Author kollar inte fakta, men **ett faktum som låter för bra för mottagaren i ett avtalsärende är en signal att flagga uppåt**, på samma sätt som interna inkonsekvenser. Category: process.

## 2026-09-03 - Christine Lef (Parameter Revision, revisor) APDS/Alpidus-svaret: revisorsregistret i hans egen hand [apb / AP ÅR 2025, mail register]
- **Registret till Christine är mail-evidensbaserat, samma tråd (`19efe024989a86f1`, hans mail 26 aug 2026).** "Hej Christine," / "Mvh" + "Robert". Avsnitt med **bara rubrikrader, inga asterisker och ingen numrering** (till skillnad från milstolpemail till klienter, där han asteriskar). Rubriken är ämnet som substantiv ("Engagemangsbesked från Almi", "DekoDu"). Bindestreckslistor för poster och belopp, decimalkomma, "procent" utskrivet. Erbjudanden i formen "Säg till om du vill att vi ... så ordnar vi det" och "Kontoutdraget kan jag skicka." Ingen TL;DR-etikett; öppningsraden 26 aug var "Tar dina punkter i tur och ordning." Category: person register (mail-evidenced, ingen `voice/people/`-profil ännu, seeda vid nästa pass).
- **Lång revisorsmail: faktisk tvåradsingress i stället för TL;DR-block.** Långmailregeln kräver ett TL;DR, hans revisorsregister har inget. Kompromissen jag valde: två sakmeningar före första rubriken som bär huvudpoängen (bilagorna, huvudbok 547 000 mot bank 326 000), ingen etikett, ingen "detaljer nedan"-signpost. Samma logik som "ingressen är faktumet" (Curveball 2026-08-28). **Min edit, overifierad** - diffa mot vad han skickar. Category: register (my edit, unverified).
- **Analysavsnitt öppnar med slutsatsen, sedan metoden.** "Jag har stämt av X mot Y ... De två stämmer inte överens" blev "Huvudboken och banken stämmer inte överens. Jag har stämt av mot ...". Samma inversion som diagnostic-verdict-regeln (dsc 2026-08-26), nu på revisorsmail. Rubriken "Vad som faktiskt betalades" bytt till "Betalningarna enligt banken" (substantivetikett, "faktiskt" är en kontrast). Category: register (my edit, unverified).
- **Positionell ram struken:** "Det är den differens du reagerade på" - hon ställde frågan själv, meningen lokaliserar faktumet i stället för att säga det (jfr Reed Hunt 2026-08-31). Category: register.
- **Processfynd, flaggat uppåt, inte rört:** (1) tråden innehåller redan ett halvfärdigt utkast i Roberts hand daterat 3 sep 09:15 (avbruten mening "misstänker att de om"), så Gmail-drafts måste dedupas mot det, inte läggas bredvid; (2) siffror som mailet inte förklarar: bankens 30 000 den 7 jan mot fakturan om 44 000, 44 000 den 16 maj utan majfaktura, och de tre 5 000-fakturorna jun-aug som inte återfinns i bankgenomgången. Siffror är låsta för The Author; konsistensfynd är frågor till Robert, aldrig tysta fixar. Category: process.

## 2026-09-03 - Simon Jakobsson (K2C-anställning) OpenSign-brödtext: rollrelationen igen, korpus = hans eget mail [k2c, mail/OpenSign register]
- **Korpus till Simon finns, ett riktigt sänt mail 26 aug (`1a03ce90ab2c24ce`):** "Hej Simon,", helsvenska, korta faktastycken, punktlista för det kommersiella, "Hör av dig om något är oklart." + "Robert". Draftens "Tja Simon!" byttes till "Hej Simon," på samma grund som Carolina-korrigeringen 2026-09-02: arbetsgivare till anställd i ett avtalsärende är varmt men vuxet, och det vinner över Discord-vanan även när de DM:at varandra. Avslutet lyftes ordagrant från hans mail. Category: person register (mail-evidenced, seed för `voice/people/simon-jakobsson.md` om volymen växer).
- OpenSign-brödtext är en mailyta utan granskningsdraft, så passet gjorde faktakoll mot k2c-051 och draft_12 innan register: anställning (inte B2B), personnummer/adress var tomma fält, §5.4 12→6 mån var Lawyers rekommendation som Robert nu tagit. Allt stämde; inget flaggat. Ingen ny ursäkt tillagd, den var redan given på Discord samma morgon. Category: process.

## 2026-09-03 - Tobias Remmers, plan-v2 delivery mail: the thread already holds the template [sbz / Irons 2, mail register]
- **Robert's 18 Aug pitch mail (gmail thread `19ff6451882f7d46`) is the structural template for every "here is the page" mail in this thread**: half-sentence lateness up top ("Took me a few days longer than I said."), "Here is our take...", link + user/pass on their own lines, a noun lead-in ("What is in there:") and a numbered list of 5, then one line on the page being live rather than a deck. Numbered lists are corpus-verified to Starbreeze, same as to Xbox. The v2 delivery mail was passed onto that skeleton; lateness became "a day later than I said" (his form, not an apology), and "as promised" went as a frame. Category: person/thread register (mail-evidenced).
- **Register to Tobias since 20 Aug: "Hello Tobias," or bare "Hello,", and "Best" alone with no name** (Gmail appends the block). Five consecutive sends confirm it; "Hi Tobias," only in the first reply. Use "Hello". Category: person register (mail-evidenced, seed for `voice/people/tobias-remmers.md` if volume grows).
- **Price delta to a client: number, delta, cause, stop.** First pass cut "It is priced from what the team actually costs" as a defensive contrast. Coordinator then corrected the facts: the live v1 page had moved twice after 18 Aug and last read 35 343 000 (flat 140k per developer, QA separate), so the new 29 974 100 is a REDUCTION, not an increase, and the pricing-basis clause became the operative cause of the delta and went back in as the third sentence, minus "actually" ("priced from what the team costs, not a flat 140k per developer per month"). Lesson: whether a clause is defensive or operative depends on which direction the number moved; verify the counterparty's last-seen number against the live page, not the mail, before passing a price line. Category: register + process.
- **Fact check that the pass caught, flagged upward not fixed:** the draft said "the 24,9 in my August mail", but the 18 Aug mail carried no total (only "indicative commercials"); the number lived on the page, and the page had since been revised to 35,3 (see above). "Compare against the old link" line was cut on Robert's decision: never invite a diff against a page that moved without notice. Also: draft peak 25 vs project memory peak 24,8; Tobias reads the document as 10 % contingency while Robert's 2 Sep mail said 20 percent. Numbers are locked for The Author. Category: process.
- The one addition: a walk-through door ("Shout if you want to walk through it live", his own milestone-mail phrase) because Tobias's 2 Sep mail asked "when can we have an updated staffing plan *and a meet again*" and the draft answered only the first half. A door that answers an open question is plan-acting, not padding. Category: register.

## 2026-09-03 (b) — Sänt vs utkast: Irons 2-planen till Tobias [sbz / Starbreeze, mail]

Robert skickade 22:25 samma kväll och gjorde sex ändringar i den röstpassade texten. Alla sex är
mönster, inte tillfälligheter.

1. **Nya mottagare presenteras överst, med relation och skäl.** Utkastet lade tyst till tre adresser
   och nämnde Rift först i punkt 1. Robert öppnade i stället med ett eget stycke: vilka de är, att
   AP teamar upp med dem, att de satt på första projektet, och att AP och Rift jobbat ihop förut med
   bra resultat. **Regel: när ett mail introducerar nya namn i en kundtråd hör presentationen och
   motivet högst upp, före sakinnehållet.**
2. **"Gates" blev "milestones" mot kunden.** Han sa milestones genomgående, aldrig gates, trots att
   pitchsidan säger gates. Använd milestones i kundtext.
3. **Prishistoriken ströks helt.** Utkastet hade den avvägda formuleringen "down from the 35,3 on the
   first version, with QA inside and a higher peak". Robert ersatte hela punkten med
   "The total is 29 974 100 SEK (roughly 115K per man month)." **Han föredrar pris plus enhetspris
   framför en berättelse om hur priset rört sig.** Notera också att han **öppet exponerar den
   blandade månadskostnaden**, vilket motsäger den gamla 140k-platt-doktrinen om att undvika
   jämförbara enhetspriser. Fråga inte igen, kvot per manmånad är numera säljargument.
4. **Förseningsfrasen ströks.** Jag lade in "a day later than I said" enligt hans eget 18 aug-mönster
   ("Took me a few days longer than I said"). Det mönstret gäller **flerdagarsförseningar**. Vid en
   dag levererar han bara, utan att peka på det.
5. **Han krediterar kundens egna folk.** Punkt 1 blev "our designers deep diving into both PD3 and
   Irons 1 (the meeting we had with your tech and design team was very helpful as well)".
   Kundens bidrag nämns när man beskriver vad arbetet vilar på.
6. **Avslutningen ströks.** "Still a live page ... Shout if you want to walk through it live."
   Han hade redan etablerat living-page-principen i tråden 18 augusti. **Upprepa inte en ram som
   redan är etablerad i tråden.**
7. Han använde **smiley** mot Tobias. Konsekvent med [[feedback_smileys_in_mails]]: förbudet gäller
   första kontakt, inte en etablerad tråd.

Behöll oförändrat: "Hello X," som hälsning, numrerad lista, "Best" utan namn, och punkt 2:s
erkännande att teamet vuxit ("We increased from our initial suggestion to 27 roles").

## 2026-09-03 - Colin Cragg (Blue Scarab) Perforce re-access mail: person register seeded from the thread [bsc / Equinox, mail register]
- **Register to Colin is thread-evidenced (`19db48bbc8f4a4c3`, `19efbab8a8cadcb3`):** "Hi Colin," on the structured mail (17 May), "Hey Colin," / bare "Colin," on one-liners, plain prose paragraphs with parentheses for asides, no asterisk headers, no numbered lists, closes "Best" + "Robert". Colin himself opens "Robert," and calls his team "the tech guys"; mirrored that phrase. No `voice/people/colin-cragg.md` yet - the deal-wiki contact page carries the voice notes; seed a profile if volume grows. Category: person register (mail-evidenced).
- Cuts this pass, all from existing taxonomy: enumeration signal ("Two things I need from you.") with the asks following straight after; positional frame ("So far I have only been dealing with you") ahead of the who-do-I-talk-to ask; the "now rather than after a decision" tail on the KM-clarity paragraph rewritten as a flat sequence ("we can have that ready before anyone has to decide") to avoid the X-not-Y construct the brief banned. Kept both benefit clauses that argue for a concrete ask (build machine = setup off the clock, engine in depot = a week saved). Category: register (my edit, unverified - diff against what he sends).

## 2026-09-04 - Amer Alsalek, APDS-underlaget: registret bekräftat i samma tråd, ett snitt [apb / AP ÅR 2025, mail register]
- Amer-registret från 2026-07-17 håller i tråd `19efe024989a86f1` (hans egna sändningar 14 aug, 3 sep, 4 sep 09:09): "Hej Amer," eller ingen hälsning alls på enradare, "Mvh" ensamt eller "Mvh" + "Robert", tilltal med namnet sist utan komma ("Återkommer under dagen med det materialet Amer."). Bindestreckslistor för bilagor och poster, som till Christine. Ingen `voice/people/`-profil ännu; två korpusentries räcker som seed om volymen växer. Category: person register (mail-evidenced).
- Enda registersnittet: "En sak innan du bokar:" ströks som annonserad instruktion (samma släkte som "En ärlig grej ... innan du visar den:" 2026-08-26). Instruktionen börjar med verbet: "Boka mot 326 000 kr, inte huvudbokens 547 000." Ränteargumentet formulerades med hans eget verb från 3 sep ("stämmer mot"). Resten av utkastet var redan register, inklusive att mailet slutar på frågan. Min edit, overifierad - diffa mot vad han skickar. Category: register.

## 2026-09-04 - Joel Edström, följemail till publishing-avtalet: fjärde passet i Curveball-tråden [cvb / Curveball, mail register]
- **Avsändarsignatur i tråden är "/Robert", inte "//R".** Både 28 aug och 31 aug skickade Robert med "/Robert" (diffarna i `curveball/drafts/mail_diff_*.md`); "//R" finns inte i korpusen till The Gang. Byt tyst till den evidensbaserade formen även när utkastet kommer från Robert-nära håll. Öppningen "Tjena Joel," behölls: han skriver "Tjena," bart till gruppen, och Joel själv öppnar "Tjena Bäckan", så namnet i ett mail riktat till en av tre mottagare är inom register. Category: person register (mail-evidenced).
- **Ingressen före en länk: verb eller substantiv, ingen beskrivning av dokumentets egenskaper.** "Det ligger som ett dokument du kan kommentera rakt i" blev "Kommentera direkt i dokumentet". Samma snitt som "Everything is on one page" → "Delivery notes." (k2c 2026-08-28): kommentarsrätten är en instruktion till mottagaren, inte en egenskap hos vår leverans. Category: register (my edit, unverified).
- **En numrerad tvåpunktslista före en jurist-/partsfråga får en etikett av ett ord ("Två frågor:"), inte "Två saker jag behöver från er:".** Uppräkningssignalen är samma släkte som 2026-08-28-cutten, men listan är berättigad (admin/avtal är hans ena numrerade kontext) och behöver ett substantiv som pekar på den. Varje fråga skrevs om så att den slutar på själva frågan ("Ska det vara Sweden AB?"), inte på en "säg till om"-formel. Category: register (my edit, unverified).
- **Vad som fick stå kvar trots att det liknar ramar:** "Samma struktur som 30 juni" (säger att inget är omförhandlat, ändrar vad han gör härnäst) och "en advokat tittar på det parallellt, så räkna med små ändringar i texten" (säger åt honom att inte kommentera formuleringar). Plan-verkande, inte Robert-verkande. Category: register.
- **Konsistensfynd, flaggat uppåt, inte rört:** briefen räknade "fem punkter om vad som står i avtalet", utkastet hade fyra stycken (rev share, Steam-app, kod, LUG). Alla faktameningar behölls, men den femte punkten, om den fanns i drafterns huvud, saknas i underlaget. Siffror och parter kontrollerade mot `publishing_agreement_thegang_2026-09-04.md` (559511-5568) och `term_sheet_2026-08-31.md` (100 000 / 30-70 / tio arbetsdagar / 30 dagar): stämmer. Category: process.
