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

## 2026-09-07 - Ellen Berglund (Carler, APDS-förvaltarteamet) + Sylvain Runberg (Dark Riviera): två korta passregister seedade [apds / dr, mail register]
- **Ellen-registret är mail-evidensbaserat (tråd `19d0bcf056f93280`, hans sändningar mar 2026):** "Hej Ellen," eller bara "Hej"/"Hej, ...", helsvenska, korta hela meningar, sak och stopp, "Mvh" (eller inget avslut alls på enradare). **Han speglar INTE hennes trivselfraser** - hon skriver "Hoppas allt är bra!", "Trevlig helg!", "glad påsk 😊"; hans svar har noll pleasantries, värmen ligger i substansen ("Bra fråga", "Vad bra med access"). Detta är biträdande-juristen i det EGNA teamet, inte motpartens jurist - varmare än Nils Åberg-registret men samma helsvenska saklighet. Struk därför en draftad "Trevlig vecka!" i förlikningsavtalspasset. Category: person register (mail-evidenced).
- **Sylvain/Dark Riviera-tråden (`1a05e003bb84fb6f`):** Roberts eget 1 sep-mail är mallen: "Hi - sorry for the slow reply here.", korta rader, "Best" ENSAMT utan namn (sigblocket bär namnet - samma mönster som Tobias 2026-09-03). Sylvain öppnar "Dear all" och använder ":)", etablerad tråd sedan 2023. Schemasvaret passades mot korpusfragmentet "Tuesday sounds good!" (warm reply-registret) i stället för draftens "let's lock Tuesday"; tid som "15:00 CET" (europeisk 24h, franska mottagare), inte "3pm". Category: person/thread register (mail-evidenced).

## 2026-09-04 - Joel Edström, följemail till publishing-avtalet: fjärde passet i Curveball-tråden [cvb / Curveball, mail register]
- **Avsändarsignatur i tråden är "/Robert", inte "//R".** Både 28 aug och 31 aug skickade Robert med "/Robert" (diffarna i `curveball/drafts/mail_diff_*.md`); "//R" finns inte i korpusen till The Gang. Byt tyst till den evidensbaserade formen även när utkastet kommer från Robert-nära håll. Öppningen "Tjena Joel," behölls: han skriver "Tjena," bart till gruppen, och Joel själv öppnar "Tjena Bäckan", så namnet i ett mail riktat till en av tre mottagare är inom register. Category: person register (mail-evidenced).
- **Ingressen före en länk: verb eller substantiv, ingen beskrivning av dokumentets egenskaper.** "Det ligger som ett dokument du kan kommentera rakt i" blev "Kommentera direkt i dokumentet". Samma snitt som "Everything is on one page" → "Delivery notes." (k2c 2026-08-28): kommentarsrätten är en instruktion till mottagaren, inte en egenskap hos vår leverans. Category: register (my edit, unverified).
- **En numrerad tvåpunktslista före en jurist-/partsfråga får en etikett av ett ord ("Två frågor:"), inte "Två saker jag behöver från er:".** Uppräkningssignalen är samma släkte som 2026-08-28-cutten, men listan är berättigad (admin/avtal är hans ena numrerade kontext) och behöver ett substantiv som pekar på den. Varje fråga skrevs om så att den slutar på själva frågan ("Ska det vara Sweden AB?"), inte på en "säg till om"-formel. Category: register (my edit, unverified).
- **Vad som fick stå kvar trots att det liknar ramar:** "Samma struktur som 30 juni" (säger att inget är omförhandlat, ändrar vad han gör härnäst) och "en advokat tittar på det parallellt, så räkna med små ändringar i texten" (säger åt honom att inte kommentera formuleringar). Plan-verkande, inte Robert-verkande. Category: register.
- **Konsistensfynd, flaggat uppåt, inte rört:** briefen räknade "fem punkter om vad som står i avtalet", utkastet hade fyra stycken (rev share, Steam-app, kod, LUG). Alla faktameningar behölls, men den femte punkten, om den fanns i drafterns huvud, saknas i underlaget. Siffror och parter kontrollerade mot `publishing_agreement_thegang_2026-09-04.md` (559511-5568) och `term_sheet_2026-08-31.md` (100 000 / 30-70 / tio arbetsdagar / 30 dagar): stämmer. Category: process.

## 2026-09-07 - Elias Strandberg (Necrotic Dominion, timanställd) PS5-överlämningsmail: tunn korpus, arbetsgivarregistret igen [nd, mail register]
- **Korpus till Elias = en OpenSign-brödtext (15 jul 2026, `19f65bc958fe6571`): "Läs igenom och signera. Hör av er vid frågor."** plus Discord-fragment i projektloggen (helsvenska, "Absolut"). Ingen `voice/people/`-profil. Passet är alltså simulation ovanpå Carolina/Simon-regeln (2026-09-02/03): arbetsgivare till ung anställd = "Hej Elias,", utskrivna ord, kort, "/Robert" från warm-reply-registret. Inget smiley, ingen observerad i korpusen. Verifiera mot vad han skickar. Category: person register (simulation, seed).
- Snitt, alla från befintlig taxonomi: annonserad instruktion "Det viktiga innan du börjar svara:" struken, faktumet öppnar stycket (jfr Amer 2026-09-04); ingressen före länken "Allt ligger här, med direktlänk till varje meddelande:" blev "Listan ligger här:" (egenskap hos leveransen, jfr "Delivery notes." 2026-08-28; dessutom sakfel, CurseForge saknar per-kommentar-länkar); dubbel "som ... som"-relativsats om Linkdu47 bruten till tre raka meningar. Behöll "Snyggt jobbat med PS5-fixen." som egen rad (erkännande utan gush är plan-verkande: han ska svara 16 personer i eget namn) och "Två jag skulle ta först:" som substantivetikett före listan. Ämnesrad som etikett med hans bindestreck: "PS5-fixen - vilka som väntar på svar". Category: register (my edits, unverified).
- Faktauppdatering samma dag (andra passet): bara fördelningsraden byttes och 16 blev 17. Allt annat ordagrant. Fördelningen skrevs som namn plus antal i löpande text, ingen lista. Category: process.
- **RÄTTELSE (samma dag, tredje passet): konsistenskollen 5+3+9=17 gick igenom men var FEL.** Två av de fem Robert svarat på (JimmyJobi, MasterJay) frågade om uppdateringens *tidplan*, inte om kraschen, och ingick alltså aldrig i de 17. Rätt fördelning var 5 svarade + 1 kvar hos Robert (Linkdu47) + **11** till Elias. Summan gick ihop bara för att definitionen av "de 17" tyst flyttade sig mellan passen. **Lärdom: en aritmetisk konsistenskoll validerar bara att talen går ihop, aldrig att kategorierna är desamma som förra gången.** När ett tal ändras mellan två pass (16→17), räkna om varje delmängd från grunddatat i stället för att subtrahera från den gamla summan. Category: process (correction).
- **VERIFIERAT REGISTER: Robert bytte "Hej Elias," mot "Tja" innan han skickade** (skickat 2026-09-07 15:28, tråd `1a07c02e221f2fea`). Simuleringen ovanpå Carolina/Simon-regeln ("arbetsgivare till ung anställd = Hej <namn>,") gällde alltså INTE här. Mot Elias är öppningen **"Tja"**, utan namn och utan komma, vilket ligger närmare Discord-registret (helsvenskt, kort) än mailregistret. Detta är nu observerat, inte simulerat. Gäller sannolikt fler unga svenska interna mottagare där det finns en levande Discord-kanal parallellt med mailen: **låt den varmaste observerade kanalen sätta öppningen, inte mailkonventionen.** Category: person register (VERIFIED).

## 2026-09-07 (b) - Ellen Berglund, godkännande av förlikningsavtalet: registret bekräftat i samma tråd, korrigering av relationsetiketten [apds / K 4429-25, mail register]
- **Korrigering av entryn ovan (2026-09-07 a):** Ellen är INTE "det egna teamet". Carler är konkursförvaltarens byrå, alltså konkursboets sida och motpart i förlikningen. Registret i sig stämde (helsvenska, kort, inga speglade trivselfraser), bara etiketten var fel. Rätt beskrivning: motpartsjurist med korrekt men inte kylig relation, ett snäpp varmare än Nils Åberg-registret. Category: person register (rättelse).
- **Tråden `1a06ceef69d2c958` bär hans eget färska svar (6 sep): "Hej Ellen," / en mening / "Mvh" / "Robert" på egna rader.** Det är mallen för allt i tråden; draften låg redan där. Enda ingreppen: "så ... så att"-dubbelkonstruktionen bruten med hans eget "då"-led ("då kan jag fakturera det sista också", 28 mar) och ordparet signering/signerar avdubblat ("skriver under"). Category: register (my edit, unverified).
- **Deadline-svansen behölls som plan-verkande.** "då hinner återkallelsen in i tid" är inte juridisk motivering utan det som styr när hon laddar upp; punkt 2.2 och lagrum nämns inte, hon kan avtalet. Samma gräns som Nils Åberg-korrigeringen 2026-08-27: konsekvensen får stå, resonemanget bakom får inte. Category: register.

## 2026-09-07 - Disposable Corps, the Rift-facing page: the split is the subject, the partnership is not [dsc / Rift Gaming, document register]
- **When the reader is the partner, seat-by-seat attribution is content and stays; what still goes is the partnership sold as a concept.** The 2026-09-02 Irons 2 direction (no "Rift does X, AP does Y") was for a client-facing page. On a page whose purpose is to put two Rift seats in a budget, "Jesper on UX", "Dima on the network question", the Side column and the 28/58 split are the plan. Cut instead: "delivered by Aurora Punks and Rift Gaming as one team" (meta), "We would rather have you as a partner, but not on a story either of us would have to walk back", "the kind of finding we would want your people arguing with us about in the review month rather than agreeing with us about in month nine". Discriminator: who-does-what stays, why-us-together goes. Category: register (pitch documents, my edits, unverified).
- **New tic family on this drafter: announced honesty.** "What it is *honestly* expected to sell", "Two *honest* caveats", the eyebrow "*Honest* risk", "chosen as *honest* matches", "What we are not going to pretend about the upside", "we would rather say this now than in month four", "We ran this properly rather than writing a number we liked". The brief asked for bluntness and the drafter labelled it instead of doing it. The fix is deletion of the label; the blunt fact underneath ("The 15 percent revenue share is worth nothing in the low and base cases", "The return is the fee") was already there and stays word for word. Robert's own plain register never grades its own candour (shareholder letter: "The 4,5 is a conservative number", not "to be honest, 4,5"). Same species as the announcing-directness openers in DMs (2026-08-26, 2026-09-04), now on a document. Category: register (pitch documents).
- **Dead cross-references are a consistency finding the dry register exposes.** "Section six is written for him" and "The item this page is really about. Section six." on a page with no numbered sections. Replaced with "the UX section further down" and flagged. Add to the document-pass consistency check: every internal reference (section, table, figure) must resolve on the page as published. Category: process.
- **Vague fractions next to a table must use the table's denominator.** "Rift carrying a quarter of this project" (500k of the 2,16M total) sat beside "just under six tenths of it" (1,04M of the 1,8M delivery scope): two bases in one sentence. The page's own cards say 28 % and 58 % of the delivery scope, so the sentence now uses those. Not a number change, a base correction with figures already on the page; flagged upward anyway. Category: process.
- **A credential tail on a named counterpart can also be a fact error.** "by someone who has done live service in the engine" credentialed Dima AND asserted a known engine on a page that says "engine and version are not confirmed" three sections later. Cut for register, and the cut removed the contradiction. Category: register + process.
- **"Never change markup" and the all-flourish paragraph.** Under a no-markup constraint a `<p>` whose whole payload is a flourish cannot be deleted; replace its content with the nearest plan fact ("It is one of the decisions the review month has to settle."). One casualty this pass: an inline `<em>` around one word of a sentence that was cut in full; block structure, tables, lists and CSS untouched. Category: tooling.
- **Substance flags, not mine to fix:** (1) the page states "in the same first position" / "with both of us in first position" as a term, but the split doc says the first-position clause is not written into the LUG plan and the analysis puts the pro-rata crossing at ~50 000 units instead of 14 400; (2) "Steam page live since May 2025" vs the LUG page's "18 mo since store page went live" on 26 Aug 2026; (3) "strong in China and thinner in the West" about the publisher was replaced with LUG's own "China first, then global" because the page must survive being forwarded to LUG; Robert may want the sharper version back. Category: process.

## 2026-09-07 (b) - Jesper Staafjord + Victor Roxlin (Rift Gaming), Disposable Corps-mailet: Rift-registret seedat, samma tic på svenska [dsc / Rift, mail register]
- **Registret till Victor är mail-evidensbaserat (tråd `19ff11ffdddaf217`, tre sändningar 11-12 aug 2026):** bart "Hej," eller "Hej!" utan namn, helsvenska med Swenglish-inslag ("introt", "IRL", "Tech Lead"), en till tre meningar, "mvh" ensamt. Till Victor + Gustav samtidigt (2 sep, tråd `1a062c5db34f74e5`) vidarebefordrar han med en enda osignerad rad ("Känns ju positivt när de börjar rekommendera folk."). Victor svarar "Hej Robert," / "Vänligen,", Gustav casual med emoji. **Jesper: ingen direkt mail från Robert i korpusen** (bara cc på Irons 2-tråden och Gustavs möteskallelse 20 aug), så Jesper-sidan är simulation ovanpå Victor-registret. Peer-relation, träffade IRL 13 aug. Ingen `voice/people/`-profil ännu; seeda `victor-roxlin.md` om volymen växer. Category: person register (mail-evidenced + simulation).
- **Announced honesty-ticen från sidpasset samma dag återkom ordagrant på svenska:** "Det jag inte tänker låtsas om:", "En sak till som du ska veta innan du räknar, Victor.", "Bättre att du vet det nu än att du läser det i ett utkast.", "en *ärlig* invändning", "en *riktig* försäljningsanalys". Alla strukna; de fetade faktameningarna under dem ("revenue sharen är värd noll i låg- och basfallet", "förstapositionen i vattenfallet är inte säkrad än") står kvar ordagrant och är blunta nog utan förvarning. Samma drafter, samma dag, två ytor, samma familj. Category: register (mail, my edits, unverified).
- **Avslutet: reservationsraden ersattes av schemafrågan.** Utkastet slutade på "Man börjar med en enda genomlysningsmånad, inte med tolv." efter samtalsasken: en X-inte-Y-lugnare som späder ut den enda handlingen. Faktumet flyttade in i Kommersiellt-blocket som planinformation ("Det enda någon åtar sig från start är genomlysningsmånaden.") och mailet slutar nu på "Vilken dag passar er?" (Reed Hunt-regeln: mailet slutar i en fråga eller ett go/no-go, inte i en "hör av er"-dörr). Category: register.
- **Länkblocket upp direkt efter ingressen**, URL och creds på egna rader utan backticks (Gmail plain text renderar dem inte; hans eget 24 aug-mail: "user: starbreeze pass: ..."). Samma skelett som Tobias 18 aug. "Sidan nedan" och "punkt fyra här" blev "sidan" och "under Kommersiellt här nedan" när numret 4 försvann från rubriken. Category: register.
- **Enhetspris tillagt, flaggat:** "Platserna: UX 40 000 i månaden på halvtid, dev 45 000 på halvtid, Dimas genomlysning 30 000 i månad ett." Siffrorna finns på sidan; tillägget följer 3 sep-evidensen (han exponerade själv 115K per manmånad). Split-dokumentet pekar ut 40 000 för en halvtidssenior som det Victor kommer trycka på, så raden är ett innehållsval Robert ska godkänna, inte en röstregel. Category: content vs voice separation.
- **Konsistensfynd i mailet, fixat i prosa:** "det ligger överst på fellistan" stod tre stycken efter en lista där UI/UX kom sist; "en fjärdedel av projektet eller knappt sex tiondelar" var samma blandade nämnare som på sidan (23 % av totalen mot 58 % av leveransscopet) och blev 28/58 procent av leveransscopet med mailets egna siffror. "Tolvmånadersuppdrag" blev "tolvmånadersplan" eftersom inget är signerat; flaggat. Category: process.

## 2026-09-07 (c) - Ellen Berglund, utökat svar med utdelningsfrågan: en öppen fråga utan siffra [apds / K 4429-25, mail register]
- Tillägget till det redan godkända svaret var en fråga om utdelning för CZP:s bokföring. Draftens "En sak till, för vår bokföring: kan du ge en indikation på ..." byttes till hans egen admin-konstruktion "skulle jag vilja veta" (korpus: "då skulle jag vilja veta priset för hela den tjänsten"), med "för vår bokföring" som inledande skäl och inget mer. "En sak till" är samma uppräkningssignal som ströks 2026-08-28. Frågan hålls öppen ("vilken utdelning ... kan vänta sig"), ingen procentsats, inga lagrum, ingen moms: nämner man en siffra får man den siffran tillbaka i stället för det troliga "ingen utdelning". Mailet slutar på frågan. Min edit, overifierad. Category: register (mail till motpartens jurist).

## 2026-09-07 (c) - Disposable Corps deck v2 + mail v2 (Rift): a rebuilt draft is a new pass, and the count that survives a rebuild is the dangerous one [dsc / Rift, document + mail register]
- **A rebuild on a reshaped deal carries the old deal's prose frames into the new tables.** The v2 deck's cover still said "Two seats in it for Rift, and a third left open" (v1 shape: Jesper + Dima + open dev) above a v2 table with one Rift seat and one open seat; the v2 mail's opener said "de två platser jag vill fylla från er sida" while its own point 2 left the developer seat open between Rift and AP. Both fixed to match the tables and flagged. Add to the document-pass consistency check: **after a deal reshape, read every prose count (seats, sides, people) against the table on the same page**, the drafter updates numbers and forgets the counts written as words. Category: process.
- **Direction-of-billing error in the Swedish:** "Ni faktureras kontant" (you are invoiced) for "Ni får betalt kontant" (you are paid). A one-word slip that inverts who pays whom in a commercial mail; The Author does not check facts, but a verb pointing at the wrong party is register-adjacent enough to fix and flag. Category: process.
- **Announced honesty, third surface, same day:** "What we are not going to pretend about", "Said here because you would find it out in a draft anyway", "we ran it properly rather than writing a number we liked", "men du ska veta det", "En sak till, Victor:". All cut, the bold facts under them untouched. Three passes in one day on the same drafter confirm the family is stable; the fix is always deletion of the label. Category: register.
- **Slide-deck register vs long-form document register.** On the Irons 2 v2 frame the cuts shrank to headings (verdict h2 "A good idea that never became readable" -> "Live since May 2025, silent since January 2026"), deep-panel summaries that argued ("Why the differentiator is real" -> "The differentiator against the comparable set") and tails. Component text (faults, priorities, tables, cards) was already dry. The deck's direct address to one reader ("Jesper, this is the job", "twenty minutes in it will tell you more than this deck can") was kept as plan-acting: it tells the reader what to do first. Category: register (pitch decks, my edits, unverified).
- **Mail whose job is a demo link: the second link gets subordinated, not removed.** "Hela upplägget:" became "Upplägget, när ni har spelat:", so the pitch link reads as step two rather than a competing call to action. Subject kept demo-first as a label ("demon först, sen upplägget"). Category: register (mail, my edit, unverified).
- **Robert's own direction language is the flat form of a benefit-explainer.** "We would rather carry the risk than split it, and it keeps your side simple" became "Cash on one side, upside on the other, neither split", which is his split-doc instruction ("they want cash, we want upside, so stop splitting both") minus the presumption about what Rift wants. When a selling sentence paraphrases a direction Robert gave, the direction is the replacement. Category: register.

## 2026-09-07 (d) - Umeå tingsrätt (återkallelse av bevakning) + Ellen-påhäng om utdelning: myndighetsregistret är hans egna två mail till registrator [apds / K 4429-25, mail register]
- **Tingsrättsregistret är mail-evidensbaserat, två sändningar till samma registrator (13 jul `19f5bd4fa37f912f`, 27 aug `1a044cec40466df9`):** "Hej," även till domstol, "Härmed inkommer ...", målet skrivs "mål K 4429-25" (aldrig "ärende"), bolaget som "Aurora Punks Development Services AB, 559320-7466, i konkurs", belopp som "512 500 kr inklusive moms", och sedan hans fasta rad *"Jag är tacksam för en bekräftelse på att [X] har kommit in i målet."* Avslut "Med vänlig hälsning" + fullt block (namn, roll, bolag + org.nr, mail, telefon). Ingen "härmed anhålles", inga lagrum, ingen slutsats åt domstolen. Category: register (myndighet, mail-evidenced).
- Passet på återkallelseskrivelsen: "Ärende" bytt till "Mål" enligt korpus, "bevakande nr 5" flyttad till partsbeteckningen (hans egen ämnesrad 27 aug), och draftens "Tvisten om bevakningen kräver därmed ingen ytterligare prövning" struken - det är domstolens slutsats, inte avsändarens (samma gräns som Nils Åberg-regeln: konsekvensen kan stå, resonemanget inte, och här var det bara resonemang). Lade till bekräftelseraden ovan eftersom den finns i båda hans tidigare mail och styr när han vet att fristen är klarad; flaggad som tillägg. Behöll briefens skrivelseform (rubrikrad, dateline, sigblock utan "Med vänlig hälsning") - om den går som mailbrödtext i stället för bilaga är hans precedens "Hej," + "Med vänlig hälsning". Category: register (my edit, unverified).
- Ellen-påhänget: "En sak jag glömde fråga:" är samma annonserande signal som "En sak till" (2026-08-28, 2026-09-07 c) och ströks; frågan ställs direkt med "för vår bokföring" som ledande skäl och "skulle jag vilja veta" (korpus). "Hej igen," som öppning är tredje mailet samma dag; overifierat mot korpus, lär av hans sändning. Category: register (my edit, unverified).

## 2026-09-07 (d) - Disposable Corps, fjärde passet (delad revenue share): en regel överlever som mekanism, inte som slogan [dsc / Rift, document + mail register]
- **En kommersiell regel som drafter vill göra "minnesvärd" ska skrivas som mekanismen, inte som maxim.** Utkastets "the revenue share follows the money at risk, one to one. Equal share, equal deferral." / "revenue sharen följer pengarna som ligger i risk, en till en. Lika uppskjutet, lika andel" är en kiasm byggd för att citeras; korpusen (Robert strök själv "Game feel doesn't teach from slides" och den grandiosa investerartonen) säger att citerbarhet är felmodusen. Kvar blev "The revenue share follows the deferral: same amount deferred, same share of net" / "Revenue sharen följer uppskjutningen: samma belopp uppskjutet, samma andel av netto." Samma sak, noll slogan. Ramarna runt den ("The rule is one line", "so neither side has to argue about it again", "så slipper vi förhandla om den igen") var självberöm av regelns elegans och åkte. Category: register (my edits, unverified).
- **En patch på en kommersiell sektion tappar termer som resten av sidan hänvisar till.** "In first position" / "i första position" försvann ur mekanismmeningen när korten skrevs om, medan notisen "The first position is not secured yet" och Victor-stycket i mailet fortfarande hänvisade till den. Bild 05:s ingress sa fortfarande att bara AP skjuter upp. Konsistenskontrollen efter en delvis omskrivning: **läs varje mening utanför sektionen som refererar till den** (ingresser, notiser, nästa steg) och varje term som notiserna förutsätter. Category: process.
- **"Er kontant ändras inte av det" är plan-verkande och ska stå först i stycket, inte som ett eget efterstycke.** Som separat stycke efter mekanismen läste det som en patch; som första bisats i uppskjutningsstycket är det svaret på Victors första fråga. Den förklarande svansen "inte kontanter som görs om till risk" blev "inte i stället för den", vilket är samma faktum utan övertalningen. Sammanslagningen är samma grepp som hans egen 6-till-5 (2026-08-28). Category: register.
- **Tredje gången samma dag: "worth saying plainly" är själv en announced-honesty-fras.** "now that we carry it equally, it is worth saying plainly rather than once the deferral is already sitting on your books" och "så du ska ha det innan du räknar" strukna; det nya faktumet ("on both sides", "påverkar det er lika mycket som oss") bär hela poängen. Category: register.

## 2026-09-07 (e) - Disposable Corps, femte passet (verklig kostnad mot betalt): rättviseargumentet är förhandshedge, och en ombyggd kommers lämnar gamla tal kvar på omslaget [dsc / Rift, document + mail register]
- **"Nobody recovers anyone else's, and neither of us is paid twice for the same hour" / "ingen får betalt två gånger för samma timme" är antisäljkategori 6 (förhandshedge) i avtalsform.** Den besvarar en invändning motparten inte rest, och mekanismen ("each side recovers its own carried cost", "var sida hämtar hem sitt eget") säger redan samma sak. Struken på båda ytorna; termen "pro rata mellan oss om nettot inte räcker" lades till i mailet så att mail och deck anger samma regel. Category: register (my edits, unverified).
- **En eftergift skrivs som en rad i tabellen, inte som en mening om eftergiften.** Roberts egen plats till underpris ("costs 35 000 and the project pays 20 000", "Vi bär 180 000 på min egen plats") stod redan som faktum i utkastet och lämnades orörd. Det är rätt form: siffran bär eftergiften, ingen prosa om den. Category: register.
- **När kommersen byggs om från "uppskjutet arvode" till "verklig kostnad mot betalt" överlever gamla nyckeltal utanför sektionen.** Omslagets stat "180 000 SEK per month, whole project" finns inte längre i någon tabell (nu 187 500 verklig kostnad / 155 000 betalt), och delningsstapeln (51/49) stämmer inte med sin egen bildtext på verklig-kostnadsbasis (54/46; scenario B:s 78 stämmer). Siffror är låsta för The Author, båda flaggade. Regeln från (c) och (d) gäller en gång till: efter en ombyggnad, läs varje tal utanför sektionen mot den nya tabellen, inklusive omslaget. Category: process.
- **Plain-text-tabell med fyra talkolumner i Gmail är bräcklig.** Radetiketter av olika längd i proportionellt typsnitt driver kolumnerna; en rad per plats i prosa ("Produktägare och UX, Jesper, 60 procent: kostar 72 000, projektet betalar 55 000, Rift bär 17 000.") överlever alla klienter. Flaggat till koordinatorn i stället för att slåss med blanktecken. Category: tooling/register (mail).

## 2026-09-07 (f) - Disposable Corps deck: Robert's own specimen of the register he rejects, and what it caught that four passes missed [dsc / Rift, document register, HIS EVIDENCE]
- **The specimen, his call, verbatim from the live deck:** "The demo is free and live. Jesper, twenty minutes in it will tell you more than this deck can, and the first two of those minutes are the whole argument for the UX seat." He called it AI slop. It had passed my third-pass read in full; I had kept it as "plan-acting" because it tells Jesper what to do first. The coordinator's replacement, which stands: "Jesper, start with the tutorial. That is where the UX problems are." Category: register correction (his words, 2026-09-07).
- **Why it survived: the anti-selling test asked whose value the sentence carries, and it carried the reader's action, so it passed. The specimen adds a second test the first one does not cover: HOW the sentence is built.** Four shapes, all present in that one line: (1) a quantity used for cadence, not measurement ("twenty minutes", "the first two of those minutes"); (2) the escalating pair, a claim then a sharper claim built on it; (3) the document grading itself ("more than this deck can"); (4) a conclusion asserted on the reader's behalf ("are the whole argument for"). A sentence can act on the plan and still be slop by construction. Run both tests. Category: register rule (global for documents).
- **What the second test caught on a full re-read that the first had cleared, eight in all:** the CTA sub "twenty minutes is enough" (same rhetorical quantity); "Play it before you read the rest" (deck referring to its own rest); "a dug trench is only interesting if somebody has to storm it" (aphorism built on the claim before it); "The one part of the game whose job is to explain the rest cannot be read or heard" (a sharper restatement of the fact in the previous sentence, from the UX brief, so practitioner origin is no protection); "Programmer hours alone do not close it" and "One sector at a time is what makes this tractable" (conclusions drawn for the reader); "the on ramp to the whole differentiator" and "the single input the whole commercial rests on" (the specimen's own intensifiers, "whole" and "single"). All in slides 01 to 05, none in the commercial or the risk rows: the drift concentrates where the drafter is persuading the designer, not where numbers carry the page. Category: register (my edits on his pattern, unverified individually).
- **Process failure, mine as much as the brief's:** passes four and five were scoped to the commercial and nothing re-read the rest, so the line lived through two more rounds. When a document is rebuilt or the register target sharpens, the pass is the whole document; a scoped brief is a floor, not a ceiling. Category: process.
- **Kept on purpose, so the next pass does not relitigate:** "Every round builds to one moment: the whistle, the climb over the top, the barrage." (the loop's design target, three concrete beats, not a rhetorical quantity) and "The seat is scoped as product owner as well as designer ... next to the interface is better than in a document" (Robert's own direction language). If he cuts either, that is new evidence and goes here. Category: register.

## 2026-09-07 (g) - Disposable Corps, jämförelseblocket: "user manual mindset" i Roberts egna ord, tillämpat på en Alike/Different-lista [dsc / Rift, document register, HANS INSTRUKTION]
- **Roberts instruktion, ordagrant via koordinatorn:** jämförelsegrupper är "highly subjective", håll det "super safe", punktlista med **likhet och skillnad** per titel, inget säljspråk, "user manual mindset". Det är samma direktiv som 2026-08-24 ("nästan som en bruksanvisning") uttalat en gång till, nu på en komponent där frestelsen att argumentera är som störst. Category: register (his words, 2026-09-07).
- **Formen som håller: en Different-rad listar vad titeln saknar, den drar inte slutsatsen.** Strukna svansar: "which is an outcome nobody can plan for" (BattleBit), "It is a positioning reference, not a competitor" (BF1), "Worth knowing that the audience for this loop is already served free by mods" (Minecraft), "It survives on mod support" (kausalpåstående, kvar: "Mod support, which this game does not have"), "the reference most players will have in mind" (påstående om spelarnas huvuden). Kvalitetsomdömen blir sakskillnader: "no shooter feel" → "Minecraft combat rather than shooter gunplay". Category: register (my edits, unverified).
- **Sammanfattningsstycket efter en likhets/skillnadslista är alltid det gamla argumentet i nya kläder.** "Two facts sit across the set. Nothing in it combines... And the titles that still hold players are the ones playable without other people" var precis den slutsats listan skulle låta läsaren dra själv; Different-raderna listar redan vad varje titel saknar och Alike-raderna för Ravenfield och OHD bär bot-poängen. Struket i sin helhet på koordinatorns förhandsgodkännande. Regel: **en referenstabell får ingen slutsatsparagraf**; om slutsatsen behövs står den på en annan bild, som fakta. Category: register.
- **Ingressen till en referenstabell är en etikett, inte en läsanvisning.** "Comparable sets are a matter of opinion, so this one ... leaves the reading to you" var både förhandshedge (antisälj 6) och läsinstruktion (dokumentregistret regel 3). Blev "Alike and different, per title. Steam figures pulled 7 September 2026." Category: register.
- **Konsistensfynd:** bild 05:s bildtext sa att de fyra exkluderade titlarna "sold between one and ten million copies each"; Operation: Harsh Doorstop är gratis och blockets egen Different-rad säger att ägarantalet är nedladdningar, inte försäljning. Ändrat till "have between one and ten million owners each", siffrorna orörda, flaggat. En bildtext som sammanfattar en tabell på en annan bild måste läsas mot den tabellens egna rader. Category: process.
- **Uteslutningskontroll som del av passet:** "Dig In" (Cold Pixel, AP-närstående) fick inte finnas i gruppen; grep träffade bara loopfasen "Dig in" på bild 03. När en brief namnger en titel som INTE får förekomma, grep:a på den innan och efter, och skilj träffar på namnet från träffar på ordet. Category: process.
- **Tillägg samma pass, Roberts andra fynd på bild 02, hans ord: AI slop.** "Every line on that list is design and readability, not missing content, technology or production value." Det var MIN omskrivning från tredje passet (kortad från "That is why more programmer hours alone would not fix it"); jag behöll slutsatsen och strök bara svansen. Han underkände slutsatsen själv. Struket i sin helhet på koordinatorns beslut, som jag delar: den tvåkolumniga fellistan ovanför visar sex designsvar i rad, och stycket var en dom lagd ovanpå en tabell som redan gjort poängen. **Regeln som saknades: efter en tabell som talar för sig själv följer inget stycke alls, inte ett kortare.** "Trimma svansen" är inte ett pass när huvudsatsen är själva slutsatsen. Negationstriaden ("not X, Y or Z") är kadens, inte information. Category: register correction (his evidence, 2026-09-07, mot min egen edit).

## 2026-09-07 (h) - Disposable Corps bild 04: "Stop acting like a hollywood market guy. Just describe our expectations." Fjärde korrigeringen samma dag, samma sjuka [dsc / Rift, document register, HANS ORD]
- **Roberts ord, ordagrant:** "Seriously. Jesper - this is the job. Stop acting like a hollywood market guy. Just describe our expectations." Det underkända: en dramatiserad spelarresa ("A new player launches the tutorial and meets... They then enter a match where... Then the enemy AI kills them before they have worked any of it out") med direkt tilltal som presentatörsgest överst. Jag hade behållit "Jesper, this is the job" i tre pass som plan-verkande. Koordinatorns omskrivning, som står: en ingress som säger vad platsen är och vad vi förväntar oss att den äger, en punktlista "What we have seen in the public build" med observationerna som fristående punkter i valfri ordning, en källrad. Category: register correction (his words, 2026-09-07).
- **Regeln han lägger till: en observationslista har ingen berättarordning.** "A new player launches... then... then" är en handling med punchline; samma sex fakta som punkter utan "and then" är en rapport. Praktikerursprung (UX-briefen skrev resan) skyddar inte; formen är det som dömer. Direkt tilltal ("Jesper, this is the job") är scenen, inte adressen; "Jesper, start with the tutorial" överlevde hans läsning eftersom det är en instruktion, inte en presentation. Category: register rule (documents).
- **Svepet efter samma form på bild 01 till 05, åtta snitt, alla på "performing rather than reporting":** "It is the differentiator ... not because it is missing" (verdikt + negationskadens ovanpå "This exists already"), "so a match is always playable" (slutsats på en likhetsrad), **"Every round builds to one moment: the whistle, the climb over the top, the barrage" (min avsiktliga behållning från (f), nu struken: samma dramatiserade triad som han just underkänt, bara kortare)**, "completely", "decisions rather than discovery" (antites byggd för att landa), "read through whichever HUD exists that day" (min egen litterära formulering), rubriken "The number the publisher has to move" (verdiktrubrik, hans egen rubrikregel 2026-08-28), och den fetade "Everything at this budget that is still alive plays offline" ovanpå tabellen som visar det (samma form som bild 02-strykningen i (g)). Category: register (my edits on his pattern).
- **Sammanfattning av dagens fyra korrigeringar, för nästa dokumentpass:** (1) retorisk kvantitet + eskalerande par + dokumentet om sig självt + slutsats åt läsaren; (2) verdiktstycke ovanpå en tabell som redan visar det; (3) [samma som 2, andra bilden]; (4) berättarordning och presentatörstilltal. Gemensam nämnare i hans egna ord: **"hollywood market guy"**, dvs. draftern uppträder. Testet som fångar alla fyra: *skulle den här meningen stå i en bruksanvisning?* Om den bara står där för att landa, stryk. Antisäljtestet (vems värde) och formtestet (hur byggd) räcker inte ensamma; det tredje testet är genren. Category: register rule (global, documents).
- **Tunn punkt är bättre än dramatiserad punkt, men en punkt utan observation ska ut eller få ett faktum.** "Enemy AI kills the player quickly" bär ingen egen observation; den är utgivarens fellistpunkt som redan står på bild 02. Rekommenderat uppåt: stryk den ur "What we have seen", eller ersätt med ett loggat faktum från Roberts sessioner om ett finns. Inte uppfunnet. Category: process.

## 2026-09-07 (i) - Knives & Gutters 3D character artist ad: a job ad in a studio's voice is a document, and the recruiter tells are the same tells [knives_and_gutters, document register, my edits, unverified]
- **Register choice: a public job ad written as "the studio speaking" runs on [[voice_register_documents]], not on a mail or DM register.** It has no counterpart, only an audience of strangers, so the anti-selling test (whose value does the sentence carry) and the bruksanvisning test (would this line stand in a manual) both apply at full strength. No Swenglish, no "Tja", no Robert-isms, since it is not him talking. Simulation: Robert has no job-ad corpus in RAG; learn from his edits on post. Category: register (new surface).
- **The recruiter tells map one to one onto the document-register cut list.** Self-grading the project ("visual direction ... looking strong") = grading our own work; the maxim closing the intro ("You are not designing the world, you are building the people who live in it") = quotable aphorism; the "we are not looking for X, we are looking for Y" pair and "early rather than late" = antithesis built to land; "the modular groundwork you lay here carries the whole project" = conclusion drawn for the reader plus the "whole" intensifier; "On scope, honestly" = announced directness in a heading. None of it is classic hype vocabulary, so a word-list scan for "passionate/rockstar/journey" clears an ad that still performs. Scan for shape, not words. Category: register.
- **Keep the fact behind the antithesis, drop the pair.** "We are not looking for someone to hand us generated meshes. We are looking for someone who ..." became the flat fact "Generated meshes are not the deliverable." followed by what the work is. The negative half is a real expectation the candidate has to act on, so it survives as a sentence; only the rhetorical pairing goes. Category: register (mechanical form).
- **Hiring copy gets one extra check: does a sentence give the candidate our side of the rate negotiation?** "it is a real part of why this batch is affordable for us" was self-justification by the register rules and also told a freelancer, before pricing, that the budget is tight. Cut on both grounds. Related content flag, surfaced not fixed: the public ad asks the candidate to price the batch themselves while the shortlist addendum hands over our internal day estimates; if both go in the same mail the private number is not private. Category: process (content vs voice separation).
- **Reassurance is plan-acting when it buys an honest answer.** Kept "If that way of working is not for you, say so now and we part on good terms." unchanged: same reasoning as the lugnande-ram exception (2026-09-02, Carolina), it changes what happens next (the candidate declines early instead of three weeks in). Cut the trailing reassurance on disclosure ("Nothing about the pipeline is hidden, from you or from anyone else") because the fact before it already carries the practice. Category: register.
- **Closing ask on an ad: list the three things to send, in one sentence, and stop.** "Send your portfolio (ArtStation, a reel or a PDF), your rate, and what you would need to deliver the batch." Same rule as the mail-ends-on-the-ask entries (2026-08-31), applied to a public surface. Left as content flags for Robert: the ad has no address or channel to send any of it to, and whose name is on the ad is still open. Category: register + process.

## 2026-09-08 - Colin Cragg (Blue Scarab), Perforce password chaser: second pass in the same thread [bsc / Equinox, mail register]
- Register held from the 2026-09-03 entry (thread `19db48bbc8f4a4c3`): "Hi Colin," / plain paragraphs / "Best" + "Robert" on separate lines / uncontracted verbs in his own mails to Colin ("I am setting up", "so setup is not") even though Colin contracts. His own chaser precedent in this thread is the 28 Apr one-liner "Hey Colin, just checking in where we are with the MNDA," so a chaser to Colin needs no apology and no preamble. Category: person register (mail-evidenced).
- Cuts, all from existing taxonomy: the follow-up escort ("Following up on my note last week.") deleted, the reply sits in-thread and the first fact does the job; the summary-then-"Specifically:"-detail doubling collapsed to the one evidence line, with the real server string ("password invalid or unset") rather than a paraphrase so the admin recognises it. Kept "Still open from my last mail:" as the noun-label lead-in (2026-08-31 rule) and "whichever is less work" since it changes what the tech guys do. Kept the build-machine line as the one urgency fact. My edits, unverified - diff against what he sends. Category: register.

## 2026-09-08 - Disposable Corps deck, five-spot pass after the name sweep: a rename sweep pastes one sentence into two slides [dsc / Rift, document register, my edits, unverified]
- **When a named person is swept out of a deck, the replacement phrase lands verbatim wherever the name was, and the second copy is the filler.** "The first step is a(n) [UX] evaluation pass on the current build to assess what needs to be done" appeared on slide 04 (lede) and slide 07 (ask 1 body) after the Jesper sweep. The fact belongs on both slides (04 introduces the term the panel summary uses, 07 is the ask); the wording belongs on one. The copy to cut is the one that restates its own heading: ask 1's title already said "then a UX evaluation pass", so its body drops to the fragment form Robert had already accepted there ("On the UX seat, slide 04." -> "On the current build. ... slide 04."). Category: register (decks, mechanical form).
- **A sentence explaining how the list below relates to the pass is the document talking about itself.** "What follows below is our own read from the public demo, not that assessment" was carried already by the h4 ("What we have seen in the public build") and the Sources line ("Nobody on our side has had the current build"). Shape 3 of the 2026-09-07 (f) specimen, added by the coordinator one day after the rule; the caveat was real, the sentence was not needed. Category: register.
- **Personified process nouns.** "what the evaluation pass needs to see" (was "what Jesper needs to see"): a pass does not see. When a person is replaced by a process in a heading, re-check the verb. Category: register (rename sweeps).
- Consistency flag surfaced, not fixed: "first step = evaluation pass" (slides 04, 07) beside "the only thing anyone commits to at the start is the review month" (slide 07) and the sizing note tying the designer to the review month. Whether the pass is inside the review month or before it is not stated. Category: process.

## 2026-09-08 - Disposable Corps mail v5 (Rift): "Less cowboy lingo, more bullet point list", och mailet måste följa decket han själv reviderat [dsc / Rift, mail register, HANS ORD + my edits]
- **Roberts instruktion, ordagrant, efter fem registerrättelser igår och två idag:** "Less cowboy lingo, more bullet point list." Tillämpning på ett svenskt peer-mail: tre löpande stycken med uppräkningar (spelets läge, fellistan med sex punkter, hämta-hem-siffrorna för respektive sida) blev streckpunkter, en per faktum, och Roberts egen plats blev punkt 3 under Platserna i stället för en lös mening efter listan. Detta överstyr mailregistrets "prosa, inte punkter" för peer-mail när mailet bär tabellinnehåll; numrerade och strecklistor är rätt form så fort raden är ett faktum ur en tabell. Category: register (his words, mail).
- **När Robert reviderar decket i egen hand ska mailets motiveringar följa decket, inte förra mailpasset.** Hans 8 sep-runda tog bort alla namnade tilltal (fyra ställen) och motiveringen "de tas bättre bredvid gränssnittet än i ett dokument" ur bild 04, och ersatte med "What we expect it to own: ...". Mailet v5 hade kvar båda. Struket: "Victor," före förstapositionsstycket och hela för-satsen om varför PO och design sitter i samma person; kvar blev "Vi räknar med att platsen äger ordersetet, rekryteringsmodellen, skärlistan och onboardingen", alltså hans egen "just describe our expectations". Den behållning jag antecknade 2026-09-07 (f) ("next to the interface ... his own direction language") är därmed **upphävd av hans eget deck**. Ny kontroll i mailpasset: varje motivering och varje tilltal i mailet ska finnas kvar på den bild mailet hänvisar till. Category: register correction (his deck edit, 2026-09-08).
- **Tre formsnitt av gårdagens fyra shapes, i ett mail som redan gått igenom fyra pass:** "så 5v5 fyller en front i stället för att ställa upp tio man" (antites byggd för att landa; deckets egen rad "far more than ten bodies on the field" är platt och tog över), "vad som faktiskt behöver göras" (intensifierare utan mätning), "Nu när vi ligger i samma position påverkar det er lika mycket som oss" (slutsats dragen åt läsaren; finns inte längre på bild 06). Även rubrikhedgen "Nästa steg, som vi ser dem" och "Om siffrorna bakom det" blev etiketter ("Nästa steg", "Önskelistor"). Category: register (my edits, unverified).
- **Plain text-kostnadstabellen: fyra rader i samma ordning, som streckpunkter.** Formen "Plats, procent: kostar A, projektet betalar B, X bär C" med siffrorna i samma ordning på varje rad överlever Gmails proportionella font och läses som tabell utan att vara en. Fyra rader är inte en vägg; det som gjorde det till en vägg i v5 var att de stod som bara rader utan strecken. Category: tooling/register (mail).
- **TL;DR på ett långt svenskt peer-mail: en länkblock + numrerade nästa steg överst gör jobbet, ingen "TL;DR"-etikett.** Hans enda svenska sammanfattningsetikett i korpusen är "Kort sammanfattning" till aktieägare; till Victor är registret bara "Hej," och korta rader. Det som saknades ur TL;DR-regelns fyra delar var "vad som behöver deras beslut": lades som en rad på kodarplatsen ("Vem som tar platsen är er fråga", deckets "your call"), inte som fjärde steg. Innehållstillägg, flaggat till koordinatorn. Category: register + content vs voice separation.

## 2026-09-08 - Disposable Corps mail v5 (Rift): HANS EGEN SKICKADE VERSION mot mitt pass, 59 % bortskuret [dsc / Rift, mail register, VERIFIERAT mot skickat mail]
Skickat 2026-09-08 10:25, tråd `1a07e0b9149bc492`, kopia i
`disposable_corps/drafts/mail_rift_2026-09-08_SENT.txt`. Detta är evidens, inte simulering: diffa
mot mitt pass innan nästa mailpass.

- **Han skar 59 procent av brödtexten, och snittet gick vid en sektionsgräns, inte i meningarna.**
  Allt från "Platserna." och nedåt är borta: platsbeskrivningarna, kostnadstabellen, hämta-hem-
  siffrorna per sida, önskelisteavsnittet och varningen om förstapositionen i vattenfallet. Kvar:
  hälsning, ett stycke om vad vi vill ha hjälp med, länkblocket, fyra numrerade steg, "Spelet.",
  "Läget." och problemlistan. **Första mailet är ett följebrev till decket, inte en sammanfattning
  av det.** Inte en enda siffra i mailet. Category: **structure** (his own send, verified).
- **Det som skars är inte det som var dåligt skrivet.** Kostnadstabellen som fyra streckpunkter,
  som jag noterade som rätt form igår, ströks i sin helhet, inte för formen utan för att den inte
  hörde hemma i mailet. **En röstpassning kan inte rädda ett mail vars fel är strukturellt, och
  frågan jag ställde ("behöver det en TL;DR?") var fel fråga; rätt fråga var om kommersen skulle
  vara med alls.** När koordinatorn lämnar ett långt mail: fråga om varje sektion hör hemma i
  mailet innan du putsar meningarna i den. Category: **process** (scope of a voice pass).
- **Förstapositionen i vattenfallet, den viktigaste kommersiella upplysningen till Victor, skickade
  han inte.** Sekvens före fullständighet: spela demon och reagera på planen först, kommersen i ett
  senare samtal. En upplysning kan vara både sann, viktig och fel i tur och ordning.
  Category: process (sequencing).
- **Tidsuppskattning i en intern plan är inte en instruktion till mottagaren.** Hans egna ord till
  mig var "1. Play the demo (one day)". I mailet blev det "1. Spela demon (lägg inte för mycket tid
  men fokusera på tutorial)". "En dag" mot en jämlike läses som att man tilldelar honom en dag;
  samma siffra internt är en uppskattning. Steg 2:s "En dag" ströks också. Category: register (mail
  vs plan).
- **Antitesen igen, i ett pass som just skrivit regeln om den.** "Listan är ett förslag, inte en
  beställning" blev "Listan är ett förslag." Han stryker den negerande andra halvan varje gång;
  jag skrev regeln 2026-09-07 (i) och producerade formen igen dagen efter. Category: register.
- **"Fellistan från utgivaren." blev "Problemområden enligt LUG"**: mildare substantiv om utvecklarens
  arbete, källan namngiven, och rubriken utan avslutande punkt. Han behöll punktetiketterna
  "Spelet." och "Läget." ordagrant, så punktformen är hans, men en rubrik som pekar ut någon annans
  brister får inte samma etikettform. Category: register.
- **"Platsen vi vill fylla från er sida är X" blev "Vi skulle behöva hjälp från Rift med X".**
  Mot en partner ber han om hjälp, han definierar inte en plats åt dem. Category: register (peer).
- **Han namnger utgivaren: "funded av förläggaren (Light Up Games)"**, mot mitt anonymiserade "hos
  utgivarens finansiärer", och "till LUG och utvecklarna" i steg 3. Två saker: NDA finns, så namnet
  är fritt, **och "funded av" i stället för "hos finansiärerna" säger att pengarna finns, inte att
  de söks.** Swenglish ("funded") mitt i svenskan är hans, inte ett fel. Category: register + content.
- **Parentes i stället för appositionskommatecken.** "Kodarplatsen, gameplay och nätverk, är öppen"
  blev "Kod (gameplay och nätverk) är öppen". Han förkortar också substantivet. Category: register.
- **Han skickade med ett grammatiskt fel: "Vi skulle behöva hjälp från Rift med är produktägare".**
  Rest av hans egen redigering av min mening. Slutsats för mig, inte för honom: **meningar med tung
  förkonstruktion går sönder när han skär i dem.** Korta huvudsatser tål ett snitt; en mening som
  börjar med "Platsen vi vill fylla från er sida är ..." gör det inte. Bygg mailmeningar så att en
  strykning i mitten lämnar något som fortfarande går att läsa. Category: **tooling** (draft for editing).
- **Inget avslutande tilltal.** Mitt "Säg till när ni har spelat, så tar vi ett kort samtal." ströks;
  mailet slutar på problemlistan och "mvh". Regeln "mailet slutar på asken" (2026-08-31) gäller inte
  när asken redan står som numrerade steg överst. Category: register.
- **Steg 4 överlevde ordagrant**, den enda rad jag skrev i den korta uppföljningspassningen och den
  plattaste raden i mailet. Även "Spelet."- och "Läget."-blocken överlevde utan ett ord ändrat.
  Category: register (what survives).
- Rift-fakta (bolag, personer, rater, NDA) ligger nu i [[reference_rift_gaming]]; regeln om första mailet i [[feedback_first_mail_is_a_cover_note]].

## 2026-09-08 - Joel Edström, Steam-accessmailet: signaturen rättad av hans egen hand, och hur kort han faktiskt skickar [cvb / Curveball, mail register]
- **RÄTTELSE av 2026-09-04-entryn: signaturen till Joel är "//R", inte "/Robert".** Robert skickade följemailet 4 sep 15:10 (tråd `19e889144ac3e56a`) med "//R" trots att passet bytt till "/Robert". Bägge formerna finns nu i korpusen till The Gang ("/Robert" 28 och 31 aug till gruppen, "//R" 4 sep till Joel ensam). Följ briefens signatur när den anger en; byt inte "tyst" mellan hans två egna former. Category: person register (VERIFIED, rättelse).
- **Hans 4 sep-sändning är måttet på längd i tråden:** öppning, en rad med länken, "Kort om innehållet:", två faktastycken om två rader, "Två frågor:" med två numrerade enradare, signatur. En numrerad lista med etikett av ett ord ("Två frågor:") är alltså observerad i hans hand till Joel, inte bara min simulation. Category: register (mail-evidenced).
- Passet 8 sep (accessmailet, två asks): strök förklaringen av varför sales@ är rätt konto ("samma identitet hela vägen") till ett faktum om vart appen flyttar, kokade publisher key-motivet från två satser till en ("till session tickets mot vår tjänst"), och flyttade Oskars inbjudan in i accesspunkten (samma tema, jfr hans 6-till-5 28 aug). Mina edits, overifierade: diffa mot vad han skickar. Category: register (my edits, unverified).

## 2026-09-08 - Robert Schmiedl (Tuut) cloud-gaming cover note: person register seeded from three threads, cover-note cuts [aurora_punks / Tuut, mail register]
- **Register to Schmiedl is mail-evidenced (threads `193abd26cf55ad61` Dec 2024, `194acc2739fe84d9` Jan-Feb 2025, `1a05cec4d6bc1225` Sep 2026), no `voice/people/` profile yet; this entry is the seed.** Opener scales "Hello Robert" (4 Sep 2026, in this very thread) / "Hello Robert," / "Hey Robert!" / bare "Hello!" / "Hello -"; he never mirrors Schmiedl's "Hi Robert". Close is **"Best" alone on its own line, no name** (sig block carries it), lowercase "best" once. Plain full-sentence English biz-dev, parenthetical asides ("(as anyone else nowadays)", "(which I think is valid in all markets...)"), casual once the thread is warm ("gimme me until this weekend", "Lol sorry", ":)", one-word "works well!"). Soft close form: "Let me know what you think and if this is a convo to take further." Connector beat is real here ("the intro to Behold is done, keep me in the loop"). Category: person register (mail-evidenced).
- **Cover-note pass ([[feedback_first_mail_is_a_cover_note]]) on a page-linking mail: the page-feature sentence is the "Everything is on one page" cut.** "There is a search and a genre filter on the front page" describes a property of our delivery, not something he acts on; deleted (same species as "Delivery notes.", k2c 2026-08-28, and "Listan ligger här:", nd 2026-09-07). Likewise "the specs your operators will ask for" (foresight display, 2026-08-07 cut 7) became "the specs", and "Happy to share those once..." (helpfulness narration) became the flat fact "Those come once we have the NDA in place." The cloud-fit criteria survived as a parenthesis because the reader needs them to read the score on the page. Category: register (my edits, unverified - diff against what he sends).
- **Judgement call flagged upward, not a rule:** cut "if you can share" on the partner-names ask. His corpus to Schmiedl carries no such hedges and the reservation-door rule (2026-08-28) points the same way, but Schmiedl deliberately left the three partners unnamed in his own mail, so the hedge had a real function. If Robert restores it on send, the rule is: a hedge on an ask for third-party names is courtesy, not padding. Category: register (open).

## 2026-09-08 - Elias Strandberg, Discord-DM om git-åtkomst hemifrån (Tailscale + git.aurorapunks.com) [nd / db-331, Discord register]
- Öppning "Tja" utan namn och komma, direkt från det verifierade registret 2026-09-07 (hans egen ändring i PS5-mailet). Inget avslut. Draftens "Hej Elias!" byttes tyst. Category: person register (verifierad öppning, resten simulation).
- Numrerad steglista (1-7) med två rubrikrader ("Så här kommer du in:", "Sedan koden:") gjordes om till korta sekventiella stycken, samma snitt som Amer-passet 2026-07-17. Kommandona står kvar ordagrant i backticks, ett per rad där mottagaren ska kopiera. Tredje person "Robert skickar" blev "Jag skickar". Category: channel register (Discord, simulation).
- Snitt: "Det här är det viktiga:" (annonserad vikt, jfr "Det viktiga innan du börjar svara:" som ströks 2026-09-07) ersatt av faktumet självt; "oändligt mycket bättre än ingenting i versionshantering" komprimerat till "bättre än ingen". Faktarader (hostname vcsboy, http-inte-https-motiveringen, konto `elias`, datum 2025-12-04, repolistan) orörda. Kontrollerade mot db-331 och devops_learnings 2026-09-08: stämmer. Category: register (my edits, unverified).

## 2026-09-10 - Robert Gandy (NOE Publisher Agreements), Switch 2 access ask inside the PID-transfer thread: platform-holder register in English, NDA-constrained ask [apb / Nintendo, mail register, my edits unverified]
- **The thread itself is the corpus, and it is more contracted than the draft.** Robert's own second mail to Gandy (thread `1a03d5a3bed81b61`, 2026-09-10 10:23) has no greeting at all, runs "we're / don't / That's / It's", three short paragraphs, closes "Let me know what else you need from us to move this forward." then "Best,\nRobert". His first mail (2026-09-08) is the Reed Hunt admin register at full strength: bare "Hi,", TL;DR dash bullets, chain-of-title block, four numbered questions, signed with company name. So "formal German office" on the receiving end does NOT push Robert into uncontracted prose; the formality lives in identifiers and structure, not in "I am / cannot". Draft was fully uncontracted; I contracted lightly ("can't") and left the rest, since his mail register is mixed. Category: register (mail-evidenced from the same thread).
- **His own antithesis in this thread carries content: "in parallel rather than in sequence" (mail 1, point 1).** The 2026-09-08 rule (he strikes the negating second half) applies to antitheses that restate; this one changes what happens (two tracks, not one after the other). Kept it, and reused his exact phrasing for the devkit-queue ask instead of the draft's "rather than after". Cut the draft's "now, not later", which was the restating kind. Test per antithesis, same as per vivid sentence. Category: register.
- **Cuts I made (mine, verify against his send):** the pre-announced question in the opener ("and I am not sure whether it sits with you or elsewhere" - it is asked verbatim as the closing question, so the ingress is the fact alone: "One more thing while the transfer is in motion."); "Two questions." (meta-signposting); "What we would like now is:" kept as a noun-label lead-in ("What we would like now:") because the numbered list is the right form to NOE, as it is to Xbox. Category: register.
- **NDA-constrained ask pattern (simulation, no prior corpus):** one sentence stating the constraint and one sentence stating why it matters to the recipient's process, then straight to the concrete asks. Agreed formulation "a large IP held by a major Swedish publisher" is a content lock, not a voice choice; "RFP process" likewise (Robert: RFP = established supplier asked to quote, "pitch" = begging). Never soften either. Category: content lock + simulation flag.
- **NOE contact map from the 2025 threads (`195d3e2d08a0283a`, `198522e8ba288c75`, `19819eafa3e9e0ba`):** Vincenzo Russo answered the March 2025 Switch 2 devkit ask ("not accepting inquiries related to Nintendo Switch 2 or requests for access to the development environment"), CC Benjamin Engert + Zihan Wang + support@noa. Robert's 2025 register to NOE was "Hello," / "Hello!" + "Best wishes" + full signature block; the 2026 Gandy thread dropped to "Hi," / "Best," with no block on the follow-up. The 2025 mails also sold ("very promising title", wishlist stats) in a way the 2026 admin mails do not; the admin thread is the register to copy for platform-holder mail now. No `voice/people/` profile for Gandy yet (two real mails); seed one if a fourth pass lands in this thread. Category: person register (thin, mail-evidenced).

## 2026-09-10 - Elias Strandberg, uppföljande Discord-DM (Gitea "access approval", tre lägen + tailscale) [nd / db-331, Discord register, my edits unverified]
- **Öppningen är "Tja" på egen rad, utan komma.** Draftens "Tja, vad är det som händer" hade kommat kvar; det verifierade registret (2026-09-07, hans egen ändring) är bart "Tja". Category: person register (verifierad öppning).
- **Etiketten före en särskiljande lista är själva frågan, inte en beskrivning av listan.** "Tre lägen och jag behöver veta vilket:" är samma meta-signal som "Two questions." (2026-09-10 Gandy) och "Två saker jag behöver från er:" (2026-09-08 Joel), fast här skulle listan inte tappa sin etikett: mottagaren ska svara med ett nummer. Blev "Vilket av de här är det:". Regel: när listan är ett val, gör etiketten till valfrågan. Category: register (my edit, unverified).
- Diagnostiska alternativ är innehållslås, inte prosa: de tre lägena behölls ordagrant som separata, ömsesidigt uteslutande rader, och tailscale-raden stod kvar som fristående kommando i backticks (samma form som 2026-09-08-DM:et). Ingen sammanslagning till löptext även om DM:et blir kortare av det. Category: process.
- **Andra DM:et samma dag (Tailscale-inbjudan godkänd, hans enhet ej ansluten):** "Du är inne i tailnet nu" byttes till "Du är godkänd i tailnet nu". Tillståndsordet ska matcha det faktiska läget: kontot är godkänt, ingen enhet har anslutit, och "inne" hade sagt att steget redan är gjort som DM:et ber honom göra. "Godkänd" speglar dessutom hans egen fråga ("access approval"). "När det är klart, kör" (fronted bisats med komma, mailprosa) blev "Kör `tailscale status` efteråt". Branch-namnet sattes i backticks som kommandona, det är en sträng han ska kopiera. Category: register + faktaprecision (my edits, unverified).
- **Tredje DM:et samma dag (crash logs, Group B), mitt i pågående samtal:** ingen öppning alls, första raden svarar rakt på det han nyss bad om. Nästan orört: draften låg redan i registret. "Permalänkar finns på varje" behölls (kortat till "permalänk på varje") trots att det liknar "Listan ligger här"-snittet från 2026-09-07: här är länken det han ska klicka på för att nå tre personer, alltså plan-verkande, inte en egenskap hos leveransen. "trodde att det var ett autentiseringsproblem" blev "gissade på autentisering" (utvecklarnas hypotes, inte ett konstaterande, och kortare), "Den är otestad" blev "Ingen har testat det spåret" så att "den" inte pekar på servern. Fakta kontrollerade mot `followups/nd-003` Activity 2026-09-10: Group B = de tre, ASCT, tre fjärdedelar in i boot, 15 servrar, anonymous, Linkdu47 besvarad 07:36. Category: register + process (my edits, unverified).

## 2026-09-14 - GoCardless support: close a same-day mistaken account [czp, EN vendor-support register, my edits unverified]
- **Transactional support mail to an unknown vendor = the Reed Hunt / NOE-Gandy admin register, not the Swedish authority register.** "Hi," opener, identifiers in one line (mail, entity, country), asks stated plainly, "Best,\nRobert Bäckström" + entity on the line below. No "Best regards" (never in English), no "Hello,". Category: register (simulation from nearest neighbours, no prior EN support-mail corpus checked).
- Cut "I have since seen" / "has no purpose for us" to "That product is closed to new signups, so we don't need the account." Fact stays, explanation shrinks. Subject em-dash replaced by hyphen. Reopen line kept as one short door since it changes what happens next; "would be glad to hear about it" became "let me know". Category: register.

## 2026-09-14 - Robert Gandy (NOE), entitlement-to-outstanding-payments answer: third pass in the PID-transfer thread [apb / Nintendo, mail register, my edits unverified]
- **Direct-question replies to Gandy open with the answer, no greeting.** Robert's own 10 Sep 10:23 mail starts "Yes to the accounts - same people, same logins" with no "Hi"; the Switch 2 ask (a new topic) got "Hi Robert,". So: answer-mail = no greeting, new-topic mail = greeting. Applied here: "Yes, CZP is entitled to..." as line one, no salutation. Category: person register (mail-evidenced, thread `1a03d5a3bed81b61`).
- **His payee phrasing is already in the thread, reuse it.** "What we want is for the account and the payee record to move over to CZP" (10 Sep) became the ask here: "What we want is for the outstanding amount to be paid to CZP once the payee record has moved across." Avoids "please pay", which he does not write to a platform holder. Category: register.
- **Cuts (mine):** "To be clear on the other half of it:" and "So in practice:" - both escort frames per the 2026-08-31 Reed Hunt rule; the concession and the ask just start. "well after the transfer" → "after the transfer" (the "well" argues). Contracted "we are not" → "we're not" and "that is what is" → "that's what is" to match his contracted replies in this thread. Legal reservation kept verbatim in substance (content lock from Robert). Category: register.
- **Tooling: NOE's reply-subject rewrite split the thread.** Gandy's 11 Sep question sits in a NEW Gmail thread `1a08f92ca222216b` (subject gained a trailing "(PID: 291215956)"), not in `1a03d5a3bed81b61`. Drafts and thread reads for this matter must target the new thread ID; a search on the old ID misses his latest mail. Category: tooling.

## 2026-09-14 - Reed Hunt (ID@Xbox), two-week chaser on the entity thread: a nudge reuses his own thread phrases, and a retracted error is not re-admitted [apb / Xbox, mail register, my edits unverified]
- **A chaser to Reed has no escort and no "did not get lost" framing.** The draft opened "Following up on my mail from 31 August. Three things are still open and I want to make sure they did not get lost." Both halves are the follow-up escort cut on the Colin Cragg chaser (2026-09-08) plus the meta-count. Replaced with Robert's own chaser construction from the Colin corpus, "just checking in where we are with", pointed at the noun ("the three open points from 31 August:") so it doubles as the lead-in to the numbered list. One line, then the list. Category: register (chaser, mail-evidenced construction).
- **Every phrase Robert already wrote in the thread beats a paraphrase of it.** "If so I'll start that now, it has its own lead time" (31 Aug) replaced the draft's "If it does I want to start that now"; "a call works well if that is easier" (27 Aug) replaced "Happy to take a call if that is quicker". Same move as the Gandy payee-phrasing reuse (2026-09-14): on message five of a thread the corpus is the thread. Category: register.
- **An error retracted once is not re-admitted in the nudge.** Cut "that one was my own error" (already stated 31 Aug as "I had the cause wrong") and the summary sentence "It is the account and vendor structure that is left" (positional frame, 2026-08-31 rule). Status facts that other alias readers need (agreement 8.11 accepted, payment question closed) stayed as one plain line after the asks. Category: register (no self-flagellation, retraction is a one-time event).
- **Deliberate content omission, not a voice call:** the 16.85 USD on vendor 0003039381 (WLBS, in bankruptcy, open exposure) is dropped by Robert's decision; only the 140.16 USD on 0003066327 is chased. The balance ask stayed as its own paragraph rather than becoming point 4, so the numbering still maps 1:1 onto his 31 Aug "Still open" list, which is the shape Reed answers against. Category: content lock + structure.

## 2026-09-14 (b) - Reed Hunt (ID@Xbox), chaser rebuilt after Robert reversed the 2019-account instruction: the retraction takes the opener slot, not a list item [apb / Xbox, mail register, my edits unverified]
- **When a chaser also walks back an earlier instruction, the walk-back is the opener and the chaser frame goes.** The draft kept "Just checking in where we are with the open points from 31 August, and one correction to what I told you on 28 August" and buried the reversal as point 1 "Accounts. Forget the 2019 Frozen Waffle account...". Robert's own 31 Aug mail in the same thread already fixed the shape for this: retraction first in one plain line ("Scratch the payment part of my last mail, I had the cause wrong"), mechanism, then "Still open from my last mail:" + numbered leftovers. Applied verbatim: "Scratch the 2019 Frozen Waffle account I asked you to reactivate on 28 August, we don't need it." The date reference moved inside the retraction sentence, so the pre-announcement ("and one correction to what I told you...") had nothing left to announce. A second retraction in one thread reuses the first one's construction; the corpus is the thread. Category: register (retraction, thread-evidenced construction).
- **Do not read the counterpart's answer back to him.** "You said CZP needs a new one rather than changing 0003066327, which is fine" restates Reed's own 27 Aug sentence before agreeing with it. Kept only the agreement plus the new fact he needs: "A new one for CZP is fine. It goes on the renamed existing account, not the 2019 one." Same family as the flattering-interpretation cut (Curveball 2026-08-31): narrating the counterpart's position is a frame even when it is accurate. Category: register.
- **Content lock, restated for the next pass on this thread:** 16.85 USD on vendor 0003039381 stays out by Robert's decision (vendor in a different bankrupt company's name, no longer claimed). Only 140.16 USD on 0003066327 is chased. Also noted, not mine to fix: the thread already carries a 14 Sep 09:22 message with API-style headers (-0400, bare To:) that reads as the earlier chaser draft; if it was in fact sent, this mail supersedes it and the parent should know before creating a new draft. Category: content lock + process.

## 2026-09-14 (c) - Reed Hunt (ID@Xbox), third pass same day, the short nudge: Robert rejected both long chasers as "a third change of mind" [apb / Xbox, mail register, HIS VERDICT + my edits unverified]
- **A chaser on a thread where his own last mail already lists the open points does not re-list them.** Both long versions today (entries a and b above) restated the 31 Aug asks, the Frozen Waffle clash, the accepted agreement and opened with a second "scratch that". Robert rejected both: on a thread whose message 4 already opened with a retraction, a long message 5 that retracts again and re-lists everything reads as a third change of mind, whatever the register of each sentence. The (b) rule (retraction takes the opener slot) is correct in isolation and still produced the wrong mail, because it optimised the shape of a message that should not have had that much content. Length is a content decision that comes before any register rule. Category: process correction (his verdict, this pass).
- **The nudge shape that survived: one question, one change, one pointer back.** "Two weeks since my last mail, anything moving on your side?" / the single new fact (2019 account out, existing account renamed, supplier profile on it) / "The rest of my 31 August mail still stands." Five lines. Every open ask lives in the thread already and Reed answers point by point against the last numbered list, so the pointer is enough. Category: register (chaser, short form).
- **Reversal of an instruction to a platform contact, light form:** "Forget the 2019 Frozen Waffle account, there are no titles on it, so no need to reactivate it." No "Scratch ... I asked you to reactivate on 28 August" ceremony on the second reversal in one thread; the fact that it reverses 28 Aug is carried by "reactivate", which only he was ever asked to do. Cut the draft's "One change since then:" lead-in (a fact just starts) and "nothing worth reactivating" (verdict form of the instruction). Category: register (retraction, my edit, unverified).
- **Process:** the thread already carried a live draft (draftId `r5769626867031331986`, message `1a0a01c2447748c7`, 14 Sep 09:29 -0400) holding the (b) long version. Confirmed via `gmail_list_drafts` on the threadId, not sent. Per [[feedback_gmail_draft_dedup]] the short nudge must replace that draft, not stack a second one on the thread. Content lock unchanged: 16.85 USD on vendor 0003039381 and the Hektor/owner-account point stay out. Category: tooling + content lock.

## 2026-09-14 - Tobias Remmers, "Staffing Plan"-svaret (svenska, Victor + Gustav på cc): språket följer tråden, inte personen [sbz / Irons 2, mail register, my edits unverified]
- **Komplettering till 2026-09-03-notisen "Use Hello":** den gäller Roberts egna engelska Irons 2-trådar. När Tobias startar en tråd på svenska svarar Robert på svenska med bart "Hej," och "mvh" ensamt, gemener (hans skickade 3 sep-mail i `1a062c5db34f74e5`). Registret till Tobias är alltså tvåspråkigt och trådstyrt: "Hello X," + "Best" på engelska, "Hej," + "mvh" på svenska. Samma sak gäller när Rift ligger på cc och Victor kör "Hej Tobias," / "Vänligen,": Robert är kortare och skalar bort namn i båda ändar. Category: person register (mail-evidenced).
- Tre snitt i passet, alla ur den kända taxonomin: (1) "Jag fyller på Victors svar." ströks som positionsmening (Reed Hunt-regeln 2026-08-31), listans ingress "De vi har i åtanke utöver planen" bär trådkontinuiteten själv eftersom den plockar upp Victors "personer ... i åtanke"; (2) "Tillgänglighet är färskvara" ströks som aforism, faktumet bakom ("den som ligger i en annan process är uppbokad om vi väntar") stod kvar; (3) "det är byggt för att fungera ihop från dag ett" + kontrasten "PD-erfarenhet ersätter inte att folk har jobbat ihop" blev en enda orsaksmening ("högt förtroende ... mycket för att de flesta har jobbat ihop förut"). Kontrastformen "X är värdefullt men ersätter inte Y" är en maxim som dessutom låter defensiv mot en kund som just sagt "ju fler desto bättre"; orsaksformen bär samma sak utan att argumentera emot honom. Category: register.
- En upprepning i samma mail slogs ihop med sin listpunkt: "Pierrick hade vi gärna haft, som jag skrev tidigare, men han sitter alltså upptagen" flyttade in i punkt 1 som "Honom hade vi gärna haft, men ...". Curveball-regeln (besläktade punkter slås ihop) gäller även mellan brödtext och lista. Flaggat i returen eftersom briefen låste listan. Category: register.
- Tooling, overifierat: RAG har ett "Re: Staffing Plan" från Robert kl 16:55 samma dag (`gmail:msg:1a0a06a20fb33184`) med tom brödtext, bara signatur och citat, som `gmail_thread` på `1a0909ad3d40888b` INTE returnerar bland trådens nio meddelanden. Troligen ett tomt utkast eller ett tomt skickat svar. Innan ett nytt utkast skapas i tråden: kontrollera vilket, per [[feedback_gmail_draft_dedup]]. En RAG-träff med `from: Robert` är inte bevis på att något skickats. Category: tooling.

## 2026-09-15 - Niclas/Ishani/Pontus (Raw Fury), MS4 caveat answer: the concession is a fact and stands alone [k2c / Pharaoh Lands, mail register, my edits unverified]
- **Caveat-answer register to RF is evidenced, not simulated.** His real 25 May 2026 reply to the MS1 asterisk (`gmail:msg:19e5fbf3287b35c4`, thread `19e2cce92e33f047`): "Hello," then each of their points answered underneath in plain prose, no apology, a plan plus a date per point ("This is also due for Friday"), "best wishes". Explains a weak signal with a fact ("Jira today is not a good indication of work done/remaining") rather than defending it. Same shape as the MS4 delivery mail (`1a04a098c9f6e01b`, 28 Aug): "Hi," / "TL;DR:" / `*Noun.*` labels / "Shout if..." / "Thanks,\nRobert". A caveat answer to a publisher is the status-mail register with their headings as the labels. Category: channel register (mail-evidenced).
- **A flourish on a concession is still a flourish.** Draft: "It will not be zero placeholder art, and I would rather say that now than have you find it on the day." The second clause performs candour; the first clause IS the candour. Same species as the shareholder-letter cut 7 ("I would rather show you a number we can hit"), now on a bad-news-to-publisher surface. Concede in one flat sentence and move to the list. Category: register (my edit, unverified).
- **Use the counterpart's own term as the label.** RF wrote "pink stroke marking system"; the draft's label was "Telling final art from placeholder" (a sentence-label, the Curveball rubrikregel). Retitled to "*Pink stroke marking.*": a noun, and their word, so the reader maps it to their own complaint without reading the paragraph. Category: register.
- **One offer, in the close, phrased against their ask.** The walkthrough-call offer sat both in the Visual coherence paragraph ("Happy to walk you through...") and in the close ("Shout if you want the walkthrough call"). His own MS1/MS4 mails carry the offer once, in the close. Merged into "Shout if you want a call on the intended final look before it is all in", which names the thing RF asked for ("we need get a proper sense of the intended final visual experience and review it"). Category: register.
- **Explains-why clauses that answer the complaint stay.** Kept "so the choice has a visible consequence" and "so you know why you are being attacked": they are the payload RF asked for (purpose per island), and he kept the same shape himself in the MS4 mail ("so the intentional rough edges do not get logged as bugs"). Cut "It stops reading as a bug because we stop leaving it unexplained" (restates the fix as an aphorism) and "the weakest asset sets the tone" (maxim + impact promise). The discriminator is unchanged: does the clause tell them what the player sees, or how clever the fix is. Category: register.
- Consistency flag, not fixed: the provisional list says "Island B" while the design section says "Bata". Left as written (facts locked), flagged upward; per 2026-08-24 an internal inconsistency is a question, never a silent fix. Category: process.

## 2026-09-15 - Jesper Staafjord (Rift), Slack-DM efter hans oombedda UX-utvärdering: tack-plus-två-frågor i peer-register [dsc / Rift, Slack DM, simulation, my edits unverified]
- **Slack till Jesper = simulation** ovanpå det verifierade Rift-mailet 2026-09-08 (bart "Hej Jesper och Victor,", "vi skulle behöva hjälp från Rift", antitesens andra halva struken, ingen avslutande uppmaning) plus DM-brevity. Ingen Slack-korpus i RAG. Lär av hans ändringar när han klistrar in.
- **Tackmeddelande om en partners leverans: godkännandet är två ord, inte ett betyg.** "Den är bra och väldigt konkret" blev "Bra och konkret" (intensifieraren bort, hans "Good as is"-form). Faktumet som gör tacket konkret (sex av sex på LUG:s lista utan att ha sett den) fick stå ensamt; "det är det som gör den användbar för oss" ströks som slutsats dragen åt läsaren.
- **Varför-meningen efter en fråga stryks även när den är kort och sann.** "En karta byggd för tio spelare känns tom med en" och "Det är ett trasigt incitament i ett kompetitivt spel" bar båda resonemanget bakom en fråga eller ett fynd; frågan respektive "det hade gått till release" bär det redan. Samma snitt som Joel 2026-08-04, nu på DM-yta.
- **Announced-tone-tic i frågeform: "Det är ingen kritik, jag vill bara veta" -> "Jag vill bara veta".** "jag gissar att det mesta blev solo mot bottar" hedgar redan; att annonsera att frågan inte är kritik är samma familj som "Det jag inte tänker låtsas om:".
- Antitesen igen: "än att den ligger öppen" struken (fjärde gången regeln tillämpas). Två löften slogs ihop till ett verb: "du får se den innan ... och den går inte iväg om du inte är okej" -> "Du får godkänna den innan den går iväg". Innehållet (granskning + veto) intakt.

## 2026-09-15 - Disposable Corps, answer to the dev team (Paul): a refusal is drier without its candour label, and a "nine of twelve" count against a table [dsc / Armoured Dudes via LUG, document register, my edits unverified]
- **A refusal to answer gets the same treatment as any other fact: state it, stop.** "We cannot answer any of them, and we are not going to pretend otherwise until we have the build" became "We cannot answer any of them without the build." The second clause was announced honesty (same tic as "Two honest caveats", 2026-09-07) and the escalating tail after it ("a guess is worth nothing to the person who has to implement it", "the first thing we would be telling you is something we made up") was the conclusion drawn for the reader. Cutting the label makes the refusal blunter, not softer; the brief's "keep it blunt" and the register point the same way. Category: register (my edit, unverified).
- **Headings with "the one X we do have" / "what we did do" are contrast headings.** Both became noun labels ("Player-hosted sessions", "The design and UX pass on the public demo"); "What we intend to accomplish" / "How we intend to work" became "Milestones" / "Working model". Category: register (heading rule, 2026-08-28).
- **Reassurance aimed at a defensive reader is still a tail.** "not a set of orders", "not built before it", "the budget does not carry a line that grows every time the game succeeds", "we would rather be corrected early than be right in a document nobody executes", "this is the cheapest and most valuable window in the whole plan", "a change to how a game explains itself is not verified until people outside the project play it": all cut, the plan facts before each of them untouched. What stayed as plan-acting: "Implementation stays with you", "your call, not ours", "say so and it goes". Category: register (my edits, unverified).
- **Consistency finding, flagged upward, not fixed:** the prose says "Nine of the twelve are hours or days of work", the table below it has 3 Days + 8 Hours + 1 Decision, so 11 of 12. Numbers are locked for The Author. Second, softer one: the doc dates the host region filter to "the December update" while the project CLAUDE.md says January 2026 in one place and December in another. Category: process.

## 2026-09-15 - Kelly Zmak (Exel Gaming Accelerator) prep-call mail + "Exel Riyadh" WhatsApp nudge: register seeded from the real thread and the real group [exel_riyadh / bg-001, mail + WhatsApp register, my edits unverified]
- **Register to Kelly is mail-evidenced (thread `19feb3a740cdbf5a`, 11 Aug 2026), no `voice/people/` profile yet; this entry is the seed.** Robert's two real mails: opener "Hello and great to meet you all!" then straight to availability, and a second mail the same afternoon that is one lead-in line ("To prepare for our call, I would love to understand the following:") plus four dash bullets. Closing is **"Best" alone**, no name (sig block carries it), same as to Schmiedl. Prose is **uncontracted** ("I am available", "I would love", "I am much more flexible"), fast-typed typo left in ("openings form 10am"). So to Kelly the mail draft's uncontracted style was right, not an AI-tell; the contraction rule stays DM-only. Kelly's own register: "Hi Robert," / "Be well," / "Talk soon, K.Z.", American warm-businesslike, answers point by point against a list. Category: person register (mail-evidenced).
- **His WhatsApp voice in the "Exel Riyadh" group (real, 2026-09-08): two-sentence replies, no greeting, one question at the end.** "All of this sounds good. Are there travel expenses added to the money?" / "Ah ok. Sounds great. I am happy to participate. Will we book our own flights or do they do that?" Note **"I am happy" uncontracted even on the phone**, so the 2026-08-07 contract-everything rule is a tendency, not a law: contract where it reads natural, do not force it. Group has Andreea, Fawzi and a fourth member; he addresses the group, not a person. Category: channel register (WhatsApp group, evidenced).
- **Prep-mail cuts, all from the 2026-08-07 taxonomy on the same program, now in mail form:** impact promise ("This is the single most useful hour of the week if it is possible") became his own kept construction "If it is a hard ask on your side, say so and I will plan around it"; maxim ("founders learn a lot watching a peer get picked apart") cut, the concrete argument before it ("each team gets closer to 90 minutes") kept; foresight elaboration ("so nobody walks into an investor meeting with a D1 number they invented") cut, the caveat he kept in his own hand ("prototypes without telemetry, keep it qualitative") stays; option enumeration for the blind testers ("Staff, or anyone local outside the cohort") cut, exactly the 2026-08-07 cut 6; meta-header "One flag" retitled to the noun "Early retention"; why-sentence after the builds question ("For Sunday's feedback to be worth anything I need to have played them") cut per the Jesper 2026-09-15 rule; antithesis half ("than improvise it on the Sunday") cut, "Your call" kept as the decision-stays-with-him form. Subject line carried an em-dash; replaced with a plain noun label. Category: register (mail, my edits unverified - diff against what he sends).
- **Nudge shape for the WhatsApp: one question, one status fact, the two practical questions, stop.** Cut "You said they would reach out Monday" (reading her own message back to her, 2026-09-14 rule), "Happy to be flexible on times but three weeks out I would like it booked" (pre-hedge plus a justification the question already carries) and "two practical ones:" (meta-signposting). Category: register (DM nudge).
- **Consistency flag, not mine to fix:** Kelly's 6 Sep Q&A mail says **22 teams**, his 12 Aug roster lists **23** and the project files say 23. The mail keeps 23 as locked content; the parent should know the counterpart's latest number differs before the 1:1 maths goes out. Also verified: nothing from merak.capital or exelbymerak.com in the work mailbox in the last 7 days, so "nothing has reached me" on flights is true as of today. Category: process.

## 2026-09-15 - Anthony Wong (LUG), Discord group "LUG <> AP Disposable Corps", handover of three links to forward to the devs [dsc / LUG, Discord register, English, simulation, my edits unverified]
- **Register to Anthony = simulation.** No Discord corpus in RAG; the 2026-08-26 pasted log was mined for facts, not stored verbatim. Nearest evidence: the 2025 Hing/LUG mail ("Hello Hing, great to meet you", warm and short), the Kelly WhatsApp group (no greeting when addressing a group, one question at the end) and the English DM contraction tendency (2026-08-07, softened 2026-09-15). Kept "Hey Anthony," because it is a three-person group and the name is addressing, not warmth; no sign-off. Learn from what he actually pastes.
- **Forwarding permission once, up top, covering all three links.** The draft put the permission on item 2 only ("Share as much of it with Hammer and Paul as you think makes sense") plus a frame line ("Three things for you and the devs"). Merged into one line under the greeting so the per-item repeat and the meta-frame go together. Category: register (DM structure).
- **Cut, brief-protected, flagged upward:** "We did this before there is a contract because it is the fastest way to show what the first month actually looks like." Helpfulness narration plus impact claim; the three links are the evidence, the sentence narrates it. Kept its plan-acting residue as "This is more or less what the first month looks like" because it tells LUG how to read the board against the proposal. Also cut "It is written about the game, not about the team" (pre-defence of our own document) and "because we were looking from outside" (pre-hedge). Same taxonomy as 2026-08-07 cuts 5 and 6.
- **Candour label on a refusal, third time this month:** "and we say so in the doc rather than guessing" cut, same as the Paul-answer pass earlier today. "The one thing we do recommend" (contrast construction) became "We do recommend ... but that's a budget call".
- Numbered 1/2/3 removed per the no-numbered-lists-in-messages rule (Amer 2026-07-17, Elias 2026-09-08); links on their own lines carry the structure in Discord. Category: channel register (Discord).

## 2026-09-15 (b) - Raw Fury MS4 caveat answer, v2 after Robert moved the detail to Confluence: a page-contents line is not "Everything is on one page" [k2c / Pharaoh Lands, mail register, my edits unverified]
- Robert's revision of the brief was structural, not voice: the per-island prose, the banner explanation and the provisional list left the mail for two Confluence pages, the commitment (date holds, not zero placeholder art, what is in MS5) stayed in the body. Same lesson as the Rift v5 send (2026-09-08): when a mail is long, the first question is which sections belong in the mail at all, and a commitment belongs in the mail while its supporting detail belongs behind a link. Category: process (scope of a voice pass, his call).
- **A line listing what a linked page contains survives; a line praising the page's completeness does not.** His MS4 mail kept "It covers build access, new features, what got an art or balance pass..." under the link and cut "Everything is on one page". So on a two-link mail the shape is `*Label.*` + link + one contents line ("What is committed for the gate, what stays provisional, and the coherence work in flight"), never a sentence about how well the page gathers things. Category: register (mail-evidenced, his 28 Aug edit).
- **The no-access fallback is his own phrase: "Ping me if you dont have access."** (MS1 delivery mail, 15 May 2026.) A fallback sentence to a publisher states what happens ("you get both pages as a doc") rather than guessing their preference ("would rather have it as a doc"). Category: register.
- Mention-once applied across TL;DR and body: "the provisional list is on the art page" stood in both; kept it where the commitment is, cut it from the TL;DR. Category: register.

## 2026-09-15 (b) - Disposable Corps dev answer v2 (rebuild, not patches): a drum-roll paragraph before a bold finding, and a heading that says who decides [dsc / Armoured Dudes via LUG, document register, my edits unverified]
- **The document was rewritten between passes (twelve fixes became two decisions + a rebuild + one fix) and the new prose carried a new tell: the one-finding drum-roll.** "Everything else on the list either belongs to the new onboarding or can wait ... One finding does not." then the bold finding. Same inversion as 2026-08-26: the bold sentence opens the section, the build-up goes, the "rest waits" fact already lived in the closing paragraph. Category: register (documents).
- **A heading that names who takes a decision the document hands to the counterpart is wrong on the facts, not just the register.** "Two decisions we would take before anything else" over a section that says "your call, not ours" twice became "Two decisions before anything else". Contrast headings again: "The onboarding gets rebuilt, not patched" -> "The onboarding rebuild", "The one fix we would do now" -> "The economy fix". Category: register (heading rule).
- **Brief-protected recommendations kept their framing intact; only the flourish around them moved.** Kept "This is a recommendation, not a requirement" and "The demo is yours, so this is your call, not ours" verbatim (the brief locked both). Cut the quotable antithesis tail after the demo view ("a better reintroduction than a broken demo is a placeholder": also grades their demo), the signpost before the reasons ("The reasoning is commercial rather than aesthetic"), the "writes the reviews at Early Access" punch on the economy tricolon, and the document-about-itself clause ("and this is where the detailed findings end up as requirements rather than as a list of bugs"). An announced refusal in a plan ("We are not going to propose that you fix those one at a time") became the consequence stated flat, same as the candour-label rule from the morning pass. Category: register (my edits, unverified).
- **Not touched, flagged upward:** the third sandbox reason ("the simulation shelf is crowded ... far less competition for a trench game you play with friends") is a market argument to the client, which sits close to [[feedback_no_client_market_sentiment]]. It is inside a brief-locked recommendation, so left as is for Robert to decide. Category: process.

## 2026-09-15 - Ralph Strandberg (DuoBox Legal), Cold Response-följebrev: person register seeded from two real threads [cold_response / cr, mail register, my edits unverified]
- **Register to Ralph is mail-evidenced but thin (threads `198c6d777676e7ed` 2025-08-20, `1a03d22338a9fb80` 2026-08-26).** Robert opens "Hej Ralph,", writes two short lines and one question ("Har du tid att höras någonting i närtid?"), no sign-off word, the Gmail signature block carries the name. His reply in the Case Clash thread is one line plus a screenshot ("Jag fastnade på kontoskapandet:"). Ralph answers in nine words ("Robert, Vi hjälper dig gärna. Ring mig."). So the ceiling for a mail to Ralph is short even by Robert's standard, and the phone is the default channel both ways. No `voice/people/` profile yet; this entry is the seed. Category: person register (mail-evidenced).
- Cover-note pass ([[feedback_first_mail_is_a_cover_note]]) cuts, all from existing taxonomy: "Fysiken är på riktigt." (verdict line, the facts after it carry it); "och inte ett spel" (restating antithesis, 2026-09-08 rule); "Svaret ändrar hur vi lägger upp det." (why-you-should-care clause after the ask); "Enklast är nog att ta det över telefon" compressed to "Enklast över telefon." mirroring his own "Ring mig." Kept "Kort om vad det är." as a noun-label lead-in (his own "Kort om innehållet:" to Joel, 2026-09-04) and "film finns på sidan" since the film is what a lawyer forwarding to an investor will click. Closed "/Robert" from the warm-reply register. Diff against what he sends. Category: register (my edits, unverified).

## 2026-09-15 - Krister Karlsson (1993 Space Machine), avtalsutkastet: registret seedat från fem riktiga sändningar [1993, mail register, my edits unverified]
- **Korpus finns och är tydlig:** 2019 (`16d4e80e2ff77b59`), Outzone-tråden 2025 (`1965e05ed9b5187c`) och Royaltyrapport-tråden 2026 (`1a04a0caf48a6608`). "Hej," ensamt i pågående tråd, "Tja!" vid ny tråd, helsvenska med engelska interjektioner ("All good!", "Sorry"), fakta i korta stycken, "/Robert". Hans egen slutrad till Krister är "Säg till om något ser konstigt ut." och hans egen ingressetikett "Kort om utfallet:". Krister använder smiley i nästan varje mail; Robert speglar det inte, inte ens när Krister skämtar (ChatGPT-avtalet 14 sep). Profil skapad: `skills/voice/people/krister-karlsson.md`. Category: person register (mail-evidenced).
- **Ett leveransmail på en fråga som legat obesvarad länge: ingen ursäkt, ingen förklaring, bara leveransen.** Hans eget 15 sep-mail ("Ja men det låter väl bra, men jag har en mall vi kan utgå ifrån. Återkommer snarast med ett utkast") är mallen. Passet öppnade därför med "Här kommer utkastet." (hans 2019-konstruktion "Här kommer en uppdaterad och signad kopia") och lämnade förseningen okommenterad. Ursäktsregistret (2025) gäller när han själv missat något, inte när han levererar. Category: register (mail, min edit).
- Snitt i passet, små: "Inga kostnader dras av innan vi delar. Bara ..." var en självmotsägelse i två meningar och blev "Det enda som dras av innan vi delar är ..."; "Du har kommentarsrätt på dokumentet" blev "Du kan kommentera direkt i dokumentet" (privatperson, inte Docs-terminologi); slutraden byttes till hans egen "säg till om något ser konstigt ut". Behöll etiketten "Tre saker jag behöver från dig:" före en riktig numrerad lista, för Robert vill ha svaren i nummerordning; det är substantivetikett före lista, inte uppräkningssignal i löptext (jfr 2026-08-28). Category: register.
- **Innehållsflagga, inte röst:** utkastet ber om Kristers postadress, men den står redan i Outzone-tråden från april 2025 (Sommarliden 22, 135 61 Tyresö). Texten lämnad orörd, flaggad uppåt. Category: content vs voice separation.

## 2026-09-16 - CorpBot till Robert själv, handlingsmail om återbetalning till Runatyr [run, mail register, internt, simulation, my edits unverified]
- **Internt handlingsmail från en agent till Robert har ingen korpus; formen är fältlista, inte brev.** Belopp, konto, referens som tre rader överst så det går att agera från telefonen, ingen hälsning, ingen avslutning. Registret är admin-mailets precision utan dess hälsningsfras, för mottagaren är han själv. Lär av vad han ändrar.
- Snitt: "En reservation:" (annonserat förbehåll, samma tic som "Two honest caveats" 2026-09-07) struken, faktumet står själv; "Skulle det ha tillkommit uttag efter det datumet fångas de inte här" var samma sak som "ser inget efter den 7 september"; "när du har en minut" (förhedge på asken) struken; "eftersom du klassade den som privat" blev bisats utan "eftersom" (förklarar inte hans eget beslut för honom). Underlagsraden blev sökväg utan mening runt. Category: register (my edits).
- **Innehållsflagga, inte rörd:** utkastet skriver perioden "5 januari till 7 september", men underlaget (`umbrella/runatyr/uttagsklassificering_2026.md`) täcker Enable Bankings 180 dagar från 2026-03-19, första privata post 2026-03-23, och säger uttryckligen att januari till mars kräver SEB-utdrag. Siffror och datum är låsta för The Author; flaggat till CorpBot. Category: content vs voice separation.

## 2026-09-16 - Deema Almutairi / Kassandra Attara (Merak), due-diligence documents reply: a compliance mail is the list and nothing else, and "he is late" gets checked against the thread before it reaches the mail [exel_riyadh / bg-001, mail register, my edits unverified]
- **The drafter framed Robert as "a week and a half late and being chased". The thread says otherwise:** Kassandra's ask went to Andreea on 14 Sep, reached Robert when Andreea added him on 15 Sep 12:09, and Deema's "urgently" chase came 16 Sep 09:35 (thread `1a0a48bb7cbc8eba`). One day. No apology, no excuse, no reaction to "urgently"; he delivers the list and stops. Rule: before letting any lateness framing into a mail, read the thread's To/Date headers and establish when the ask actually reached him. The no-self-flagellation rule (shareholder letter 2026-07-24, Reed Hunt 2026-08-31) already bans inventing an apology; this adds the mechanical check that stops a drafter's timeline error from becoming one. Category: process + register.
- **Compliance reply to a program admin team = bare "Hi,", one lead-in line, label-dash-value list, "Best".** Kept the drafter's compressed labels over Tim Browne's verbatim restatement of the checklist ("All three mentors' Passport Copy - Attached"); Robert's own list construction to this program is the compressed one (11 Aug: one lead-in, four short dash bullets). Opener dropped to bare "Hi," per his no-name openers ("Hello and great to meet you all!", "Tja!") and to avoid choosing between two chasers on a six-person cc. Nothing else changed; he would send it this short. Category: register (admin/logistics, English).
