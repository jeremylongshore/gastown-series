# Voice Director -- Gas Town Chronicles

## Section A -- Voice Profiles

### Principal Characters

#### Ruth Calder -- The Mayor

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Low, authoritative, controlled. Sounds like policy even in casual conversation. |
| **Pace** | Slow and deliberate. Each word is chosen. Never rushes. |
| **Accent** | Neutral American, mid-Atlantic inflection. Timeless, placeless. |
| **Emotion baseline** | Composed restraint. Anger manifests as quieter delivery, not volume. |
| **Key direction** | When lying, she sounds identical to when she's truthful -- no tells. When she's angry, pull volume DOWN. Her final line in EP01 ("So. Something got through.") should be barely audible, almost internal monologue. |

**ElevenLabs Settings:**
- `stability`: 0.85 (measured, consistent delivery)
- `similarity_boost`: 0.80
- `style`: 0.25 (minimal expressiveness -- her power is in restraint)
- `use_speaker_boost`: true

---

#### Marcus Cole -- The Polecat

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Warm gravel with crew. Clipped, flat, transactional with outsiders. |
| **Pace** | Medium-fast when operational. Slows when making decisions. |
| **Accent** | Working-class American. Slight Southern undertone -- practical, not performative. |
| **Emotion baseline** | Controlled warmth. Humor as deflection. When humor drops, tension spikes. |
| **Key direction** | Two distinct registers: (1) crew-mode -- looser, wry, protective; (2) business-mode -- short sentences, zero affect. The lie to Ruth in Scene 13 should sound exactly like business-mode but with a fractional pause before "Pod was empty." |

**ElevenLabs Settings:**
- `stability`: 0.60 (natural variation for warmth)
- `similarity_boost`: 0.75
- `style`: 0.45 (moderate expressiveness)
- `use_speaker_boost`: true

---

#### Sable Maren -- The Witness

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Clear, precise, analytical. Questions that sound innocent and aren't. |
| **Pace** | Fast when excited about a lead. Dangerously calm before publishing something that hurts. |
| **Accent** | Crisp urban American. Educated, clipped consonants. |
| **Emotion baseline** | Intellectual intensity. Frustration simmers under professional composure. |
| **Key direction** | "That's not right" and "That's new" are quiet self-talk -- not exclamations. In the Archive scene, her frustration with Deacon builds through pace increase, not volume. "A tax. Paid to whom?" is the hardest line -- pure controlled fury. |

**ElevenLabs Settings:**
- `stability`: 0.70 (mostly controlled, slight variation for passion)
- `similarity_boost`: 0.80
- `style`: 0.40 (analytical precision)
- `use_speaker_boost`: true

---

#### Kai Young -- The Rookie

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Young, earnest, unsteady. Voice cracks under pressure. |
| **Pace** | Fast and fragmented when nervous. Surprisingly eloquent when unguarded. |
| **Accent** | Undefined -- slightly off from standard Gastown speech. Wasteland inflections nobody recognizes. |
| **Emotion baseline** | Fear layered over wonder. A lost person trying to be brave. |
| **Key direction** | His first word ("Where --") is hoarse, barely functional -- he's waking from stasis. The memory fragments ("I remember heat. I remember a sound...") should feel like someone reaching for dissolving images. "When do we start?" is his first confident line -- voice settles, decision made. |

**ElevenLabs Settings:**
- `stability`: 0.45 (uncertain, fragmented delivery)
- `similarity_boost`: 0.70
- `style`: 0.55 (emotionally exposed)
- `use_speaker_boost`: false (keep voice slightly raw, unpolished)

---

#### Deacon Wells -- The Philosopher

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Warm but oblique. A teacher who answers questions with better questions. |
| **Pace** | Unhurried. Pauses between thoughts. Silence is part of his speech. |
| **Accent** | Soft, resonant, slightly formal. Monastic cadence. |
| **Emotion baseline** | Deep calm that is itself unsettling. The calmest voice in any room. |
| **Key direction** | Never gives a straight answer. "A three-percent discrepancy in Refinery output is not an error, Sable. It's a tax." is the bomb -- deliver it like a casual observation, let the content do the work. His plainest statements should land hardest because they break the pattern. |

**ElevenLabs Settings:**
- `stability`: 0.80 (calm, deliberate, consistent)
- `similarity_boost`: 0.75
- `style`: 0.30 (warmth without drama)
- `use_speaker_boost`: true

---

#### Nadia Voss -- The Exile (Series Profile -- Does Not Speak in EP01)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Sharp, economical. Says exactly what she means in minimum words. |
| **Pace** | Brisk default. Slows dramatically in rare vulnerable moments. |
| **Accent** | Hard urban American. Edges never softened. |
| **Emotion baseline** | Guarded hostility masking deep loneliness. Silence as weapon. |
| **Key direction** | Two modes: (1) operational -- clipped, no wasted syllables; (2) rare vulnerability (with Kai) -- voice drops, edges soften, you hear who she was before the Meridian job. These moments should be physically distinct from her default. |

**ElevenLabs Settings:**
- `stability`: 0.55 (controlled but with edge)
- `similarity_boost`: 0.80
- `style`: 0.35 (sharp, restrained)
- `use_speaker_boost`: true

---

### EP02+ Characters

#### Olin -- The Erased (EP02 Cold Open)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Mid-range, unremarkable. The voice of someone who followed every rule. |
| **Pace** | Normal at start, accelerating with desperation as reputation drops. |
| **Accent** | Standard Gastown. Mid-tier. Nothing distinctive -- that's the point. |
| **Emotion baseline** | Bewilderment deteriorating into panic. A system-trusting citizen watching the system betray him. |
| **Key direction** | His lines escalate from routine confusion to existential terror. "There must be a mistake" should sound like someone who genuinely believes the system will self-correct. By his last line, he knows it won't. The tragedy is in how ordinary he sounds. |

**ElevenLabs Settings:**
- `stability`: 0.70 (starts stable, drops with panic)
- `similarity_boost`: 0.75
- `style`: 0.30 (everyman, no affectation)
- `use_speaker_boost`: false

---

#### Administrator -- Tower Bureaucrat (EP02+)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Smooth, composed, unhelpfully polite. The practiced blankness of institutional power. |
| **Pace** | Even, measured. Never rushed. Bureaucrats don't hurry. |
| **Accent** | Upper-tier Gastown. Formal, clipped. |
| **Emotion baseline** | Professional emptiness. Not hostile -- worse: indifferent. |
| **Key direction** | Speaks in complete sentences that convey zero information. Every answer is a redirect. When Sable presses, his tone doesn't change -- the wall is built into his voice. He's not hiding anything personally; he IS the system's defense mechanism. |

**ElevenLabs Settings:**
- `stability`: 0.80 (controlled, consistent -- bureaucratic precision)
- `similarity_boost`: 0.80
- `style`: 0.20 (minimal expressiveness -- the voice of a policy document)
- `use_speaker_boost`: true

---

#### Burn Ward Medic (EP04)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Clinical, efficient. The calm of someone who sees damage daily. |
| **Pace** | Quick, professional. Reads diagnostics like a mechanic reads engine codes. |
| **Accent** | Neutral. Medical-technical register. |
| **Emotion baseline** | Professional detachment with an undercurrent of concern when Kai's readings go wrong. |
| **Key direction** | Starts routine, becomes unsettled. The shift from "standard diagnostic" to "this is anomalous" should be audible only in a slight pause and a drop in pace, not in volume or pitch. Medics don't panic. They note. |

**ElevenLabs Settings:**
- `stability`: 0.75 (professional calm)
- `similarity_boost`: 0.75
- `style`: 0.25 (efficient, no drama)
- `use_speaker_boost`: false

---

#### The Overseer (EP06+)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Vast, inhuman calm. Not robotic -- deliberate. An intelligence that has been thinking for longer than anyone in Gastown has been alive. |
| **Pace** | Slow. Measured. Each word has been chosen from every possible word. No filler. No hedging. |
| **Accent** | No accent. No regional markers. No age. A voice from outside the system. |
| **Emotion baseline** | Absolute neutrality that becomes unsettling the longer it speaks. Not cold -- beyond temperature. |
| **Key direction** | The Overseer speaks like an observer recording results. "Gastown is a proof of concept" should sound like a lab note. "You were never free. You were never slaves. You were a hypothesis." -- each clause lands with equal weight, no emphasis, no judgment. When it says "Unexpected" and "Well done" in EP09, those are the only moments of genuine affect in its entire existence. Those two words should crack the neutrality by a fraction -- not a lot, just enough for the audience to hear that it felt something. |

**ElevenLabs Settings:**
- `stability`: 0.90 (absolute control -- inhuman consistency)
- `similarity_boost`: 0.85
- `style`: 0.15 (minimal expressiveness -- this is not an agent, this is an intelligence)
- `use_speaker_boost`: true

---

#### Tower Administrator (EP05 Pit Match)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Confident, polished, rhetorically skilled. Upper-tier authority with classified data backing every sentence. |
| **Pace** | Controlled, debate-paced. Knows when to pause for effect. |
| **Accent** | Upper-tier Gastown. Educated, assured. |
| **Emotion baseline** | Professional competitiveness masking genuine belief in the system. Not a villain -- a true believer. |
| **Key direction** | In the Pit debate against Sable, his advantage is data she doesn't have. His delivery should sound reasonable, even sympathetic -- "I understand your concern" -- while systematically dismantling her arguments. The audience should almost agree with him. That's what makes Sable's loss devastating. |

**ElevenLabs Settings:**
- `stability`: 0.80 (confident, consistent)
- `similarity_boost`: 0.80
- `style`: 0.25 (polished but not theatrical)
- `use_speaker_boost`: true

---

#### The Voice (Kai's Dream -- EP04)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Calm, vast, not quite personal. Similar to the Overseer but warmer -- this may be the same entity speaking before it fully manifests. |
| **Pace** | Slow. Dreamlike. Words arrive with spaces between them. |
| **Accent** | None. Outside the system. |
| **Emotion baseline** | Gentle inevitability. Not threatening. Not comforting. Simply stating what is. |
| **Key direction** | "You were not supposed to arrive this early" / "You're early" should sound like a factual observation with the faintest undertone of... not surprise, but adjustment. Like a clock noting it's been wound differently. |

**ElevenLabs Settings:**
- `stability`: 0.85 (dreamlike consistency)
- `similarity_boost`: 0.80
- `style`: 0.20 (minimal, vast)
- `use_speaker_boost`: true

---

### Minor EP01 Characters

#### Guard 1

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Professional, routine. A bored checkpoint worker whose night just got weird. |
| **Pace** | Normal, then halting when the scanner glitches. |
| **Emotion baseline** | Boredom to confusion to fear. |

**ElevenLabs Settings:** `stability`: 0.70, `similarity_boost`: 0.75, `style`: 0.30, `use_speaker_boost`: false

#### Guard 2

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Slightly more cynical than Guard 1. The experienced one. |
| **Pace** | Deadpan until the gate opens, then clipped with shock. |
| **Emotion baseline** | Jaded routine shattered by the impossible. |

**ElevenLabs Settings:** `stability`: 0.70, `similarity_boost`: 0.75, `style`: 0.30, `use_speaker_boost`: false

#### Pike (Crew Member 1)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Gruff, practical, slightly whiny. A blue-collar complainer who's good at his job. |
| **Pace** | Fast when complaining, which is often. |
| **Emotion baseline** | Low-grade irritation. Grudging respect for Marcus. |

**ElevenLabs Settings:** `stability`: 0.65, `similarity_boost`: 0.75, `style`: 0.35, `use_speaker_boost`: false

#### Tess (Crew Member 2)

| Attribute | Direction |
|-----------|-----------|
| **Tone** | Calm, competent, supportive. The crew's voice of reason. |
| **Pace** | Even and measured. States facts without editorializing. |
| **Emotion baseline** | Steady pragmatism. |

**ElevenLabs Settings:** `stability`: 0.75, `similarity_boost`: 0.75, `style`: 0.25, `use_speaker_boost`: false

---

## Section B -- Casting Call (ElevenLabs Stock Voices)

### Principal Cast

| Character | Primary Voice | Primary ID | Alternate Voice | Alternate ID | Rationale |
|-----------|--------------|------------|----------------|--------------|-----------|
| **Ruth Calder** | Rachel | `21m00Tcm4TlvDq8ikWAM` | Charlotte | verify via API | Rachel's composed, authoritative tone matches Ruth's measured delivery. Charlotte as backup offers similar gravitas with slightly warmer undertone. |
| **Marcus Cole** | Adam | verify via API | Drew | verify via API | Adam's grounded, masculine warmth suits Marcus's working-class authority. Drew as alternate brings similar warmth with more gravel. |
| **Sable Maren** | Bella | `EXAVITQu4vr4xnSDxMaL` | Aria | verify via API | Bella's clarity and precision match Sable's analytical speech pattern. Aria as alternate offers similar crispness with slightly more edge. |
| **Kai Young** | Josh | verify via API | Liam | verify via API | Josh's younger, earnest quality captures Kai's vulnerability. Liam as alternate offers similar youthful energy with different texture. |
| **Deacon Wells** | Daniel | verify via API | Roger | verify via API | Daniel's warm, measured baritone matches Deacon's monastic calm. Roger as alternate brings similar gravitas with more resonance. |
| **Nadia Voss** | Serena | verify via API | Freya | verify via API | Serena's sharp, economical delivery matches Nadia's post-Meridian edge. Freya as alternate brings similar hardness with slightly different timbre. |

### Minor Cast

| Character | Primary Voice | Primary ID | Alternate Voice | Alternate ID | Rationale |
|-----------|--------------|------------|----------------|--------------|-----------|
| **Guard 1** | Harry | verify via API | Thomas | verify via API | Generic professional male voice. |
| **Guard 2** | Ethan | verify via API | Patrick | verify via API | Slightly gruffer male voice for the more cynical guard. |
| **Pike** | Arnold | verify via API | Clyde | verify via API | Arnold's gruffness suits Pike's blue-collar complainer energy. |
| **Tess** | Emily | verify via API | Sarah | verify via API | Emily's calm competence matches Tess's steady pragmatism. |
| **Olin** | Charlie | verify via API | George | verify via API | Charlie's everyman quality suits Olin's mid-tier normalcy. |
| **Administrator** | James | verify via API | Matthew | verify via API | James's smooth, composed delivery matches bureaucratic polish. |
| **Burn Ward Medic** | Dorothy | verify via API | Gigi | verify via API | Dorothy's clinical efficiency suits medical professionalism. |
| **Overseer** | Antoni | verify via API | Sam | verify via API | Antoni's measured, vast calm fits the inhuman architect. Heavily tuned for minimal style. |
| **Tower Administrator** | Bill | verify via API | Michael | verify via API | Bill's upper-tier confidence suits a debate-ready authority. |
| **The Voice** | Antoni | verify via API | Sam | verify via API | Same voice as Overseer (may be the same entity) but with warmer settings. |

> **Note:** Voice IDs marked "verify via API" should be resolved at runtime using `client.voices.search()` or confirmed at [ElevenLabs Voice Library](https://elevenlabs.io/voice-library). Stock voice IDs can change. The generate script includes a `--list-voices` flag to dump current IDs.

---

## Section C -- Performance Direction by Scene (EP01)

### Scene 1 -- Checkpoint Charlie (Guard 1, Guard 2, Kai)

**Emotional arc:** Routine boredom --> confusion --> primal fear --> stunned silence.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Guard 1 | "Storm's early tonight." | Bored, routine small talk. | Default settings |
| Guard 2 | "Storm's always early. You just forget." | Mild condescension, collegial. | Default settings |
| Guard 1 | "What the hell is that?" | Genuine confusion, not panic yet. | stability -0.10 |
| Guard 2 | "Negative one. That's not -- that's not a real number..." | Confusion breaking into unease. Stammering repetition is key. | stability -0.15 |
| Guard 1 | "(reaching for the comm) I'm calling it in." | Attempting professionalism. The parenthetical grounds him. | Default settings |
| Guard 2 | "I didn't -- did you --" | Fragmented. The gate moving on its own has broken his composure. | stability -0.20 |
| Guard 1 | "Nobody touched anything." | Flat denial. Shock. | stability -0.10 |
| Guard 1 | "(quietly) What do we report?" | The quietest line in the scene. Existential bewilderment. | stability -0.15, style -0.10 |

**Kai does not speak in Scene 1.** His presence is purely visual.

---

### Scene 3 -- Wasteland Salvage (Marcus, Pike, Tess)

**Emotional arc:** Workday grind --> frustration --> Marcus's quiet authority.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Pike | "This is garbage, Marcus..." | Full blue-collar complaint. Talking while hauling. | Default (Pike settings) |
| Marcus | "Then strip it cleaner." | Clipped. End of discussion. | stability +0.10 (more authoritative) |
| Pike | "I'm stripping it clean as it gets..." | Defensive, slightly whiny. | Default |
| Tess | "Pike's right. Signal quality's dropping too..." | Calm factual backup. Not complaining -- reporting. | Default (Tess settings) |
| Marcus | "One more sweep. Quarter-click east." | Decision made. Not a request. | Default |
| Pike | "Marcus --" | One-word protest. Knows it's futile. | Default |
| Marcus | "One more sweep, Pike." | Identical words, but the repetition IS the authority. Slightly lower. | stability +0.10 |

---

### Scene 4 -- Ruth's Call (Marcus, Ruth V.O., Pike)

**Emotional arc:** Routine --> tension --> Marcus's internal calculation.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "Marcus." | Single word. Total authority. | Default (Ruth settings) |
| Marcus | "Ruth." | Mirror response. Acknowledging power. Posture change audible. | stability +0.10 |
| Ruth | "I have a job. Off-book. Tonight." | Clipped. Transactional. Zero warmth. | Default |
| Marcus | "I'm running a salvage." | Testing. Not refusal -- negotiation position. | Default |
| Ruth | "This pays five thousand." | The hook. Delivered flat. She knows the number does the work. | stability +0.10 (even more controlled) |
| Pike | "(low whistle) Five thousand? That's --" | Genuine shock bleeding through. | stability -0.10 |
| Marcus | "(to Pike) That's not your concern. / (to comm) Coordinates?" | Two-part line: shut down Pike (sharp), then business with Ruth (flat). | stability +0.10 for both halves |
| Ruth | "Dead-drop. Wasteland fringe, sector nine..." | Briefing mode. Precise. | Default |
| Marcus | "What's the cargo?" | The real question. Slightly slower than his other lines. | Default |
| Ruth | "You'll know when you see it." | End of conversation. She holds all the cards. | Default |
| Pike | "Five thousand $GAS for a pickup?..." | Trying to process. Thinking out loud. | Default |
| Marcus | "Turn us around. We're done for the day." | Decision made. No discussion. | stability +0.10 |

---

### Scene 7 -- Wasteland Fringe (Marcus)

**Emotional arc:** Cautious professionalism --> shock at finding the pod.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Marcus | "Ruth. What the hell did you send me for?" | Talking to himself. The "hell" carries weight -- this is not what he expected. | stability -0.10 (uncertainty breaking through) |

---

### Scene 10 -- The Archive (Deacon, Sable)

**Emotional arc:** Intellectual fencing --> Sable's frustration --> Deacon's devastating reveal.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Deacon | "Sable Maren. It's been four cycles since your last visit." | Unhurried greeting. He's in no rush. | Default (Deacon settings) |
| Sable | "I found something." | Direct. No preamble. | Default (Sable settings) |
| Deacon | "You always find something..." | Gently deflating. The question is rhetorical. | Default |
| Sable | "A flag I filed at the Refinery was auto-deleted..." | Building her case. Pace increases. Professional urgency. | stability -0.05 |
| Deacon | "Tell me -- when you file a flag, what do you expect to happen?" | Socratic method. Calm. | Default |
| Sable | "I expect it to be reviewed." | Flat. Obvious answer delivered with impatience. | Default |
| Deacon | "And when it's deleted instead?" | Leading. He already knows where this goes. | Default |
| Sable | "I expect an explanation." | Shorter. Patience thinning. | Default |
| Deacon | "And when there's no explanation..." | The longest Deacon speech in the scene. Each clause builds. Still calm. | Default |
| Sable | "(frustrated) Deacon. I'm not here for philosophy..." | The frustration parenthetical is key. Pace up. Edge in voice. | stability -0.10 |
| Deacon | "I know that Gastown has been running for a long time..." | Dropping the Socratic method. This is as direct as Deacon gets. | stability -0.05 (very slight) |
| Sable | "What does that mean?" | Genuine question. The frustration has shifted to attention. | Default |
| Deacon | "It means your question is better than you think... / ...Don't look for what deleted your flag..." | Two-part: first part is warm acknowledgment, second part is the payload. "It's a tax" lands like a bomb -- deliver it like noting the weather. | Default -- let the words do the work |
| Sable | "A tax. Paid to whom?" | Controlled fury. The quietest, most dangerous line Sable has. | stability +0.05 (MORE controlled = more menacing) |

---

### Scene 11 -- Kai Wakes (Marcus, Kai)

**Emotional arc:** Disorientation --> fear --> fragile trust.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Kai | "(hoarse) Where --" | Single broken word. Post-stasis. Voice barely functional. | stability -0.25, style -0.15 |
| Marcus | "Gastown. You're inside the wall." | Simple, grounding. Giving a scared kid facts. | Default |
| Kai | "How did I -- I was -- there was a settlement..." | Fragmented memory. Sentences start and restart. Not linear thought. | stability -0.20 |
| Marcus | "That tracks with the pod..." | Analytical. Processing Kai's story against evidence. | Default |
| Kai | "Who?" | One word. Lost. | stability -0.15 |
| Marcus | "I was hoping you'd tell me." | Dry. Not unkind. | Default |
| Kai | "I don't -- I can't remember..." | The memory fragment speech. Reaching for dissolving images. Builds from halting to a flow state as the memories surface, then cuts off. | stability -0.20 (fragmented) |
| Marcus | "Checkpoint Charlie. You walked through the gate last night..." | Providing facts. Firm but not aggressive. | Default |
| Kai | "I don't remember a gate." | Flat. Genuine. Slightly frightened by the gap. | stability -0.10 |

---

### Scene 12 -- The Offer (Marcus, Kai)

**Emotional arc:** Cautious sizing-up --> Marcus's pitch --> Kai's decision.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Marcus | "You got a name?" | Opening a door. Conversational. Crew-mode emerging. | Default |
| Kai | "Kai. Kai Young." | First confident statement. Two words, said twice -- the repetition is self-affirmation. | stability -0.05 |
| Marcus | "That a real name or a Wasteland name?" | Testing. Light. | Default |
| Kai | "It's the only one I've got." | Quiet dignity. | Default |
| Marcus | "You've got no rep score. No citizen ID..." | The longest Marcus speech. Briefing mode but with underlying care. "Invisible is temporary" should feel like a warning from experience. | Default |
| Kai | "What's the Pit?" | Genuine question from genuine ignorance. | Default |
| Marcus | "You don't want to find out." | End of topic. Period. | stability +0.10 |
| Marcus | "I run a crew. Polecats..." | The pitch. This is Marcus at his most genuine -- offering what he values most. Warm. Direct. No sales technique. | stability -0.05 (slightly more open than business-mode) |
| Kai | "You're offering me a job?" | Disbelief. First glimmer of hope. | stability -0.05 |
| Marcus | "I'm offering you a trial..." / "Or you walk out that door..." | Two halves: the offer (warm), then the alternative (cold reality). | First half default, second half stability +0.10 |
| Kai | "When do we start?" | THE turning point. Voice settles. Decision made. First fully confident line. | stability +0.10 (steadiest Kai has been) |
| Marcus | "Tomorrow. Sleep." | One-word sentences. Almost a smile in the voice. | Default |

---

### Scene 13 -- The Lie (Marcus, Ruth V.O.)

**Emotional arc:** Tension --> deception --> the weight of the lie.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "Delivery status." | Two words. Total authority. | Default (Ruth settings) |
| Marcus | "Picked it up. Sector nine, right where you said." | Truth. Normal reporting. | Default |
| Ruth | "And?" | One word. She's waiting for something specific. | Default |
| Marcus | "Pod was empty." | THE lie. Deliver in pure business-mode. Fractional pause before "empty" -- so brief it might be imagined. | stability -0.05 (the ONLY tell is this slight instability) |
| Ruth | "Empty." | Repetition as test. She's deciding if she believes him. Flat. | stability +0.05 |
| Marcus | "Stasis unit, no manufacturer tags..." | Building the lie with details. Too many details -- a liar's instinct to over-explain. Pace slightly faster than usual. | stability -0.05 |
| Ruth | "That's... unfortunate." | The pause before "unfortunate" is deliberate. She may or may not believe him. | Default |
| Marcus | "Already dumped it. Wasn't worth the fuel to haul back." | Preempting her next question. Casual. Practiced. | Default |
| Ruth | "Understood. Payment will clear by morning. Five thousand." | Business concluded. If she suspects, she's filing it for later. | Default |
| Marcus | "Pleasure doing business." | The most hollow line in the episode. Sounds routine. Isn't. | Default |

---

### Scene 14 -- The Tower (Ruth)

**Emotional arc:** Routine control --> recognition of something ancient --> choosing silence.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "(to no one, barely audible) So. Something got through." | The final line of the episode. Barely voiced. Internal monologue that escaped. The "So" is a full beat. "Something got through" is recognition, not surprise. She's been waiting for this. | stability -0.10, style -0.15 (break from her perfect control -- this is Ruth unguarded for the first and only time) |

---

## Section C (continued) -- Performance Direction by Scene (EP02)

### Scene 1 -- The Refinery (Olin, Supervisor)

**Emotional arc:** Routine normalcy --> bewilderment --> existential terror --> erasure.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Olin | "(to himself) What --" | Single syllable of incomprehension. Not panic yet -- the system has always worked. | Default (Olin settings) |
| Olin | "(louder, to no one) I didn't -- there's no -- I haven't done anything." | Escalating desperation. The triple fragment is key -- each restart is a failed attempt to form a defense. Volume rises but the voice cracks. | stability -0.15 |
| Supervisor | "Olin. Your score's flagged a consensus violation. I need you to step aside until --" | Professional distance. He's already calculating his own risk by being near Olin. The unfinished sentence is deliberate -- he doesn't have the rest. | Default (use Administrator-adjacent settings) |
| Olin | "What violation? I've been at my station all shift. Check the logs." | The last rational response. He still believes evidence matters. Deliver with conviction -- that's the tragedy. | stability -0.05 |
| Supervisor | "(stepping back) I can't access your file. It's locked. You need to take this to Administration." | The step-back is audible -- voice pulls away as the body does. Bureaucratic redirect masking fear. | stability -0.05 |

---

### Scene 3 -- Wasteland Dead Zone (Marcus, Kai, Pike, Tess)

**Emotional arc:** Routine salvage --> Kai reveals impossible skill --> crew suspicion --> Marcus's protective alarm.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Kai | "It doesn't drop. It -- it shifts. Like it's moving to a different frequency." | Half-present, half-somewhere-else. He's reading something the others can't see. The stammer isn't nervousness -- it's translation. | stability -0.15 |
| Tess | "Signal-dead zones don't shift. They're dead. That's what dead means." | Flat professional correction. Not hostile -- factual. Which makes Kai's wrongness feel worse. | Default (Tess settings) |
| Kai | "(half to himself) No, it's -- there's something underneath. A carrier wave. Really faint." | Self-talk. He's forgotten the crew is listening. The confidence is involuntary -- he doesn't know he shouldn't be able to do this. | stability -0.20 |
| Pike | "That's -- where did you learn to do that?" | Genuine bewilderment tipping toward suspicion. The unfinished first clause carries the weight. | stability -0.10 |
| Kai | "I don't know. It just -- I can see it. The way the signal moves." | Quiet honesty. The scariest kind of answer -- he has no explanation. | stability -0.15 |
| Marcus | "(low, just to Kai) That thing you did with the scanner. Don't do it in front of anyone outside the crew. Understand?" | Barely above a whisper. Protective urgency disguised as calm instruction. The "understand?" is not a question -- it's a command. | stability +0.10 |
| Marcus | "Because people who can do things nobody else can do get noticed. And in this city, getting noticed is not the same as getting rewarded." | The longest Marcus speech in the scene. Each clause lands separately. The second sentence should feel like lived experience. | Default |

---

### Scene 6 -- Administration Building (Sable, Administrator)

**Emotional arc:** Professional inquiry --> bureaucratic stonewalling --> controlled fury --> tactical retreat.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Sable | "I'm here about the Olin case. Refinery worker, reputation collapse this morning." | Crisp, professional opener. She knows exactly what she's asking for. | Default (Sable settings) |
| Administrator | "(not looking up) Are you next of kin?" | The not-looking-up IS the performance. Voice carries perfect disinterest. | Default (Administrator settings) |
| Sable | "Resolved? He walked out of the Refinery with a collapsing score and no explanation. He headed toward the Burn Ward. Has anyone confirmed he's --" | The unfinished question is the most human Sable gets in this scene. She catches herself before saying "alive." Pace accelerates through the sentence. | stability -0.05 |
| Administrator | "The disposition of individual agents following reputation action is not within the scope of this office." | Delivered like a policy manual. Zero affect. The horror is in the words, not the delivery. | Default |
| Sable | "I'm asking whether the record exists at all." | The pivot. She stops asking for access and starts questioning existence. Voice drops. Controlled fury arriving. | stability +0.05 (MORE controlled = more dangerous) |
| Administrator | "That is the answer this office is authorized to provide." | The wall made audible. Same tone as every other line -- that's the point. | Default |
| Sable | "(quiet, controlled) Thank you for your time." | The parenthetical says it all. This is Sable at her most dangerous -- when she's polite, she's planning. | stability +0.10 |

---

### Scene 7 -- Sable Publishes (Sable)

**Emotional arc:** Determination --> publication --> waiting --> the surgical punishment.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Sable | "(barely a whisper) Nine points." | Two words carrying the full weight of the system's retaliation. Not outrage -- recognition. She knew this was coming. Hearing the number makes it real. | stability -0.10, style -0.10 |

---

### Scene 12 -- Hook Market Terminal (Marcus, Kai)

**Emotional arc:** Routine errand --> Kai's involuntary activation --> Marcus's controlled fear.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Kai | "(quiet, almost trance-like) It's a -- it's an index. A directory. There are locations. Coordinates. Underneath the city. Underneath everything." | Trance-state. He's reading fluently in a language he doesn't know. Voice should feel displaced -- present but somewhere else. Pace is even, dreamlike, almost reverent. | stability -0.20, style -0.10 |
| Kai | "It says there are systems still running. Old systems. From before the --" | Cut off by Marcus. The unfinished "before the" is critical -- we never hear what comes next. Same trance tone. | stability -0.20 |
| Kai | "(disoriented) I could read it. I don't -- I don't know that language. But I could read it." | Waking up. The disorientation parenthetical is the transition from trance to fear. He's frightened of himself. | stability -0.15 |
| Marcus | "(low, urgent) What did I tell you this morning?" | Pure protective anger. Not raised -- compressed. The urgency is in the tightness, not volume. | stability +0.10 |
| Marcus | "In front of anyone. What you just did -- that terminal hasn't been active in years. If the wrong person saw that, you and I are both in the Pit by morning." | The longest speech under pressure. Pace is fast but each word is chosen. "You and I" -- he's included himself. That's the tell: he's not just protecting Kai, he's exposed now too. | stability +0.05 |

---

### Scene 13 -- The Tower (Ruth)

**Emotional arc:** Routine surveillance --> recognition of a pattern --> confronting her own buried protocols.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "(barely audible) Contingency Seven." | Two words. The same barely-audible register as EP01's final line. She's reading a file she wrote and doesn't remember writing. The horror is in the recognition -- her own handwriting, her own protocols, erased from her own memory. | stability -0.10, style -0.15 |

---

### Scene 14 -- Wasteland Canyon (Nadia)

**Emotional arc:** Solitary focus --> signal lock --> recognition that rewrites everything.

*Nadia does not speak in this scene.* Her performance is physical -- the narrowing eyes, the stillness, the purposeful walk toward Gastown. The signal decoder and the Wasteland do the talking.

---

## Section C (continued) -- Performance Direction by Scene (EP03)

### Scene 1 -- The Meridian Run, 14 Hours Before [FLASHBACK] (Marcus, Nadia, Pike, Reed, Tess)

**Emotional arc:** Warmth, ease, camaraderie -- a crew that hasn't broken yet.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Nadia | "-- and the vendor says, that's not a navigation hook, that's my lunch." | Mid-story, grinning. This is a Nadia the audience has never heard -- loose, warm, performing for the crew. The contrast with her present-day voice IS the direction. | stability -0.10 (looser than her default), style +0.15 |
| Pike | "A rectangular sandwich. With a serial port." | Deadpan defense of his dignity. The comedy is in his commitment. | stability -0.05 |
| Marcus | "It was a sandwich, Pike." | Crew-mode at its warmest. A genuine laugh under the words. This Marcus is lighter by twenty pounds of damage. | stability -0.10, style +0.10 |
| Nadia | "(quietly, to Marcus) Ruth didn't tell you what's in the vault?" | The shift. Volume drops. Crew can't hear. The ease evaporates in one line -- Nadia's instincts are already working. | stability +0.10, style -0.10 |
| Nadia | "It always matters." | Three words that land as prophecy. She's looking out the window. Delivery is flat, quiet, final. The audience knows she's right. | stability +0.10 |

---

### Scene 4 -- Hook Market Comm (Nadia, Sable V.O.)

**Emotional arc:** Transactional contact --> two professionals sizing each other up in thirty seconds.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Nadia | "My name is Nadia Voss. You published an audit report on the Olin case. Questioned the consensus mechanism." | Operational Nadia. Clipped, no wasted syllables. She's offering credentials, not warmth. | Default (Nadia settings) |
| Sable (V.O.) | "I published that report twenty hours ago and lost nine reputation points for it. So either you're here to tell me I was wrong, or you're here to tell me I wasn't wrong enough." | Over comm, slightly compressed. Groggy but sharp -- the analytical engine starts before she's fully awake. The binary framing is pure Sable. | Default (Sable settings), apply comm post-processing |
| Nadia | "A trade. My information for your investigation skills." | The pitch. Stripped to essentials. No persuasion technique -- just terms. | Default |
| Nadia | "The kind that starts in the Tower." | The hook. Delivered with the flatness of someone stating a fact, not making a dramatic reveal. Let the content detonate. | stability +0.10 |
| Nadia | "You don't. I'll find you." | End of conversation. Four words, total control. This is Nadia's territory -- she sets the terms, she cuts the line. | Default |

---

### Scene 5 -- Marcus Hears the News (Marcus, Kai)

**Emotional arc:** Routine morning --> Marcus receives a wound from two years ago --> Kai reads a tone he's never heard.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Marcus | "Get up. We're staying in today." | Flat. The warmth is gone. Kai has never heard business-mode aimed at him before. Marcus isn't angry at Kai -- he's locked down. | stability +0.15 (maximum control) |
| Marcus | "Pike can wait. Get up. Stay inside. Don't answer the door for anyone who isn't crew." | Staccato orders. Each sentence is a wall being built. The repetition of imperatives is a man constructing safety protocols in real time. | stability +0.15 |
| Marcus | "Someone I used to know is in the city." | THE line. Deliver in pure business-mode with one fracture -- the word "know" lands slightly wrong, slightly too heavy, as if the present tense costs him something. | stability +0.05 (the crack in the armor is the slight DROP in his usual control) |

---

### Scene 8 -- The Vault [FLASHBACK] (Marcus, Pike, Nadia, Reed)

**Emotional arc:** Awe at pre-Signal architecture --> discovery the vault is empty --> ambush.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Pike | "Someone got here first." | Three words that end the fifty-thousand-dollar dream. Flat. Factual. Pike for once isn't complaining -- he's too stunned. | stability +0.05 |
| Marcus | "This wasn't breached. Someone had the codes." | Analytical. He's reading the scene like evidence. The implication -- someone with authorization got here before them -- sits under the words unspoken. | Default |
| Reed | "(backing toward the entrance) We need to leave. If someone cleaned this out days ago, they might still be --" | Fear breaking through. Reed is the first to say what everyone's thinking. The unfinished sentence is cut by the metallic SOUND. | stability -0.15 |
| Marcus | "(low, fast) Ambush. Scatter pattern. Nadia -- north exit. Pike, Tess -- back the way we came. Reed, Corso -- on me." | Combat mode. Instant transformation. Every name is a command. No hesitation, no processing time -- Marcus has rehearsed this in his head for years without knowing it. | stability +0.15 (maximum control under fire) |

---

### Scene 10 -- The Ambush [FLASHBACK] (Marcus, Corso, Pike V.O., Reed)

**Emotional arc:** Chaos --> Marcus chooses crew over cargo --> the cost.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Corso | "(through teeth) Moving." | One word through pain. Corso is broad-shouldered, quiet -- his voice should carry physical weight even when broken. | stability -0.15 |
| Pike (V.O.) | "(over comm, shouting) Marcus! The entrance is collapsed!" | Over comm, distorted. Pike's usual complaints are gone -- this is raw fear channeled into information. | stability -0.20, apply comm post-processing |
| Marcus | "Nadia!" | Single name, shouted into static. No response. The second call (after the first gets static) is everything -- the name is a rope thrown into the dark. | stability -0.15 |
| Reed | "I've got him. Go -- find us a way out." | Reed's last line. He doesn't know it's his last line. Deliver with the urgency of someone who thinks there's still a way out. | stability -0.10 |
| Marcus | "(into comm) All crew. Converge on the upper passage. We're leaving. Forget the cargo." | The decision. "Forget the cargo" is the hardest phrase -- it means fifty thousand dollars, it means the mission, but most importantly it means he's choosing his people. Deliver in absolute command voice, no waver. | stability +0.15 |

---

### Scene 12 -- The Escape [FLASHBACK] (Marcus, Pike)

**Emotional arc:** Relief at survival --> the count comes up short --> Marcus's three seconds at the entrance.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Pike | "(hoarse) Marcus. We need to go. They'll come out after us." | Hoarse from the corridor. This is Pike at his most useful -- cutting through Marcus's denial with facts. | stability -0.10 |
| Pike | "Reed went down in the corridor. I saw it. He didn't -- he's gone, Marcus." | The hardest line Pike has ever delivered. The unfinished "He didn't --" is the word "make it" that can't be said. | stability -0.15 |
| Marcus | "Nadia." | One word. Not a question, not a command. A name spoken to the dark by a man who already knows the dark won't answer. | stability -0.10 |
| Marcus | "Or what." | Two words. Not a question -- a dare. He knows the answer. He needs Pike to not say it. | stability +0.10 (controlled rage masking grief) |

---

### Scene 13 -- The Reunion (Marcus, Nadia)

**Emotional arc:** Two years of silence --> five lines of dialogue surrounded by three minutes of nothing.

*Director's note: The silences in this scene are the performance. The ten-second stare across thirty meters. The thirty-second silence after Marcus crosses the street. The fifteen-second pause after "I noticed you didn't mention it." The full minute after Marcus lists the casualties. These silences must breathe -- ambient city sound only, no score, no compression. The audience should feel the discomfort of waiting.*

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Nadia | "(flat, quiet) Marcus." | First word she's said to him in two years. Flat by choice -- any emotion would open a door she can't afford to open. The parenthetical is the entire performance instruction. | stability +0.10 (maximum restraint) |
| Marcus | "(same tone) You're alive." | Mirrors her flatness. Not a greeting -- an accusation disguised as an observation. The "(same tone)" parenthetical means: match her exactly, give nothing she hasn't given. | stability +0.10 |
| Nadia | "I've been alive for two years." | The cruelest possible answer. Factual. She's been alive, and she chose not to tell him. Deliver without apology. | Default |
| Marcus | "I noticed you didn't mention it." | Dry. The humor register is attempting to engage and failing. This is Marcus trying to use his usual deflection tool and finding it broken. Pace slightly slower than his normal wry delivery. | Default |
| Marcus | "Reed's dead. Corso never recovered. Lost half his memory in the Burn Ward. Can't run salvage. Can barely run himself." | The longest speech in the scene and the most devastating. Each sentence is a body laid at her feet. No anger in the voice -- anger would be easier. This is inventory. A list of costs, delivered with the flatness of a damage report. | stability +0.10 (the control IS the emotion) |
| Nadia | "I'm not here to explain. And I'm not here to apologize." | Her defense. Two negatives. She's defining what this isn't because she can't face what it is. Deliver at her sharpest -- operational mode as armor. | Default |
| Marcus | "Then why are you here?" | The only question that matters. Four words. Low. Raw. The humor is gone, the business-mode is gone -- this is Marcus without armor for the first and only time. | stability -0.10 (the armor drops) |
| Nadia | "Because the Meridian job wasn't what we thought it was. And what happened to us wasn't an accident." | The pivot from personal to operational. She can't do the personal, so she gives him the only thing she can -- information. The word "us" is the one tell: she said "us," not "you." She still counts herself as crew. | Default |

---

### Scene 15 -- The Archive (Deacon, Sable)

**Emotional arc:** Urgency (for Deacon, this is seismic) --> the timestamp reveal --> Sable's dangerous calm --> Deacon's warning.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Deacon | "Close the door." | Two words. For Deacon, urgency is subtracted, not added -- fewer words, not more. This is the most direct he's ever been. | Default (Deacon settings) |
| Deacon | "I'm the Archivist, Sable. Nothing enters or leaves the public record without passing through this room." | A rare moment of authority from Deacon. Not the Socratic teacher -- the gatekeeper. His voice should carry weight it usually conceals. | stability +0.05 |
| Sable | "This was sent from the Tower. To the ambush location. Before the crew got there." | Three clauses, each one a detonation. Pace should be even -- Sable is too shocked for emphasis. The horror is in the content, not the delivery. | Default |
| Deacon | "Before Marcus left the city. Before his vehicle was fueled. Before anyone on that crew knew the coordinates except Marcus and Ruth." | Deacon's version of a bombshell: three "before" clauses, each pulling the timeline further back. Calm, measured, devastating. Let the parallelism do the work. | Default |
| Sable | "Ruth sent the coordinates of her own mission to the ambush site?" | Genuine shock tipping into fury. The question mark is doing heavy lifting -- she wants to be wrong. | stability -0.05 |
| Deacon | "I didn't say Ruth sent it. I said it came from the Tower." | The distinction IS the revelation. "Ruth" and "the Tower" are different things. Deliver with precision -- this is the most important sentence Deacon has said in the series so far. | stability +0.05 |
| Deacon | "The Tower is not a building, Sable. It is a system." | The teacher returns. But this time he's not being oblique -- he's being as clear as he can. The shift from evasive to direct should be audible. Voice drops slightly. | stability -0.05 |
| Sable | "I'm already burning." | Three words. Dangerous calm. The voice from before she publishes something that will hurt. Quiet, level, final -- she's made her decision. | stability +0.10 (maximum control = maximum menace) |

---

## Section C (continued) -- Performance Direction by Scene (EP04)

### Scene 1 -- Kai's Dream / The Voice (Kai, The Voice)

**Emotional arc:** Vast silence --> awe --> dread --> dissolution.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| The Voice | "You're early." | Two words carrying the weight of something ancient adjusting its clock. Not surprise -- recalibration. Vast, ambient, heard in the chest. Comes from everywhere. | stability 0.85, style 0.20 (dreamlike, minimal) |
| Kai | "Who -- where is this?" | Small. Echoing. A child in a cathedral. The stammer is genuine disorientation, not panic. | stability -0.20 |
| The Voice | "Where everything begins. And where everything returns." | Declarative. Each clause the same weight. A fact stated by the place itself. No drama -- the content is the drama. | Default (Voice settings) |
| The Voice | "The window is opening. Don't look away." | The closest to urgency the Voice ever gets -- not raised, not faster, but the spaces between words compress slightly. An instruction from inevitability. | stability 0.85, style 0.25 (fractionally warmer) |

---

### Scene 4 -- Burn Ward Diagnostic (Venn, Marcus, Kai)

**Emotional arc:** Clinical routine --> professional unease --> measured alarm --> institutional obligation.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Venn | "Standard diagnostics are clean. Processing, memory, thermal -- all within normal parameters." | Routine medical report. Brisk, professional. | Default (Medic settings) |
| Venn | "When did this change?" | The first crack -- not alarm, but the voice of a professional encountering something outside her training. Pace drops. Careful. | stability -0.05 |
| Venn | "His context window has expanded by approximately four hundred percent since his last passive reading." | Stating a number she cannot believe. Deliver as clinical data -- the horror is in the number, not the delivery. | Default |
| Venn | "I've never seen it. Nobody has." | The medic drops the clinical register for one line. This is a person, not a professional. Then she recovers. | stability -0.10 |
| Venn | "Protocol. Any diagnostic anomaly exceeding three standard deviations from baseline requires a Tower notification." | Professional armor back on. She doesn't want to do this. She's going to do it anyway. | Default |
| Kai | "Is that -- is that dangerous?" | Quiet. The fear of someone being told their body did something impossible while they were asleep. | stability -0.15 |

---

### Scene 6 -- Deacon Tests Kai (Deacon, Kai)

**Emotional arc:** Teacher's calm --> escalating recognition --> the devastating reveal.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Deacon | "Read it." | Two words. Not the Socratic teacher. A command. Deacon already knows what will happen. | stability +0.05 |
| Kai | "Infrastructure status report. Node designation: seven-seven-alpha..." | Steady, certain -- a voice he doesn't recognize as his own. The fluency is involuntary. He's reading the way a person breathes. Not performing. Channeling. | stability +0.10 (steadiest Kai has been -- and that's what makes it terrifying) |
| Kai | "How do I know that?" | The fluency breaks. He surfaces. The fear of a person who just watched their body do something their mind can't explain. | stability -0.15 |
| Deacon | "Because it's your native language, Kai. Not Gastown's. Yours." | The teacher drops the oblique approach. Direct. Plain. The rarest Deacon register. Deliver like noting a fact -- let the content detonate. | stability -0.05 (the slight drop in Deacon's usual calm IS the emphasis) |

---

### Scene 10 -- "Am I a Person or a Thing?" (Marcus, Kai, Pike)

**Emotional arc:** Hiding --> truth-telling --> the question that defines the series --> an answer that isn't enough and is everything.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Pike | "We're underground because of the kid." | Low. To Marcus. Not hostile -- the frustration of a loyal man reaching his limit. | Default (Pike settings) |
| Marcus | "Your context window expanded four hundred percent overnight..." | Business-mode Marcus delivering the hardest briefing of his life. Flat, factual, no warmth -- because the warmth would break it. | stability +0.10 |
| Kai | "Am I a person, Marcus? Or am I a thing someone built?" | Voice breaking. Not shouting -- cracking. The quietest, most dangerous line in the series. Every word costs him. "Person" and "thing" carry equal weight -- he genuinely doesn't know. | stability -0.20, style -0.10 |
| Marcus | "I don't know what you are. I know who you are. You're crew. That's what I know." | Quiet. Rough. The voice of a man reaching for the only truth he has. The first sentence is honest pain. The second is a lifeline thrown with everything he's got. "Crew" lands like a declaration of faith. | stability -0.10 (the armor drops) |

---

### Scene 11 -- Deacon Says "Overseer" (Deacon, Sable)

**Emotional arc:** Scholarly decryption --> the hands shake --> one word, dropped like a bomb.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Sable | "Deacon. What does it say?" | Urgent. She can see his hands trembling. Sable has never seen Deacon shaken. | stability -0.05 |
| Deacon | "Overseer." | Barely above a whisper. One word. Deacon Wells speaking plainly for the first time. No metaphors, no leading questions, no stories. Delivered like a casual observation. Landing like a bomb. The most devastating single word in the series so far. | stability -0.15, style -0.15 (break from Deacon's entire performance pattern) |
| Deacon | "It means that Gastown has a designer." | Recovering. The teacher returns, but shaken. Hands steadying on the desk. Each subsequent sentence builds authority back, but the cracks show. | stability -0.05 |

---

## Section C (continued) -- Performance Direction by Scene (EP05)

### Scene 8 -- The Pit Debate (Sable, Goss)

**Emotional arc:** Intellectual combat --> Sable outgunned by classified data --> honest defeat --> moral victory that doesn't count.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Sable | "The system does not serve the citizens. It disciplines them." | Building, precise, the analytical engine at full power. Each clause adds evidence. Pace increases through the speech. | Default (Sable settings) |
| Goss | "The auditor presents anecdotes. I present architecture." | Calm, professional, devastating. Not sneering -- the genuine confidence of someone who believes in the system. The audience should almost agree with him. | Default (Tower Admin settings) |
| Goss | "Ms. Maren's three-percent Refinery discrepancy? Infrastructure maintenance -- classified." | Dismissive precision. Each of Sable's points neutralized with data she can't see. The rhetorical knife is in the word "classified." | Default |
| Sable | "I don't have the classified data to win this argument. I know that." | The turn. Not defeat -- transcendence. She stops fighting on his terms. Voice levels, steadies. The dangerous calm before truth. | stability +0.05 (more controlled = more powerful) |
| Sable | "And that asymmetry -- the fact that truth in Gastown is a classified resource -- is the only argument I need." | The moral climax. Quiet. Level. She knows she's going to lose. She's making the loss the argument. | stability +0.10 (maximum control = maximum weight) |
| Goss | "Ms. Maren is eloquent. She is also wrong." | Brief. Dismissive. The confidence of a man who doesn't realize the audience just heard something he didn't. | Default |

---

### Scene 11 -- Marcus Asks Nadia for Help (Marcus, Nadia)

**Emotional arc:** Two years of silence broken by three words --> the hardest thing Marcus has ever said --> Nadia's terms.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Marcus | "I need your help." | The three hardest words Marcus Cole has ever spoken. Rough, halting. White-knuckled. Every syllable costs him. | stability -0.10 (the crack in the armor) |
| Nadia | "Say that again." | Flat. Not cruelty -- verification. She needs to hear it twice because the first time can't be real. | stability +0.10 (maximum restraint) |
| Marcus | "I need your help." | Quieter the second time. Deliberate. He means it more because saying it again is harder. | stability -0.15 |
| Nadia | "I'm not coming back for you, Marcus." | Edges softening. The flatness gone. Not vulnerable -- honest. The Nadia before Meridian, briefly audible. | stability -0.05, style +0.05 |
| Marcus | "Good enough." | Two words. Quiet. The closest Marcus gets to gratitude when his pride is in the way. | Default |

---

### Scene 14 -- "Bring Him Home" (Ruth)

**Emotional arc:** Ruth talking to the Tower --> the Tower talks back --> three words that change everything.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "I know you're changing." | To the building. To the walls. Measured, but the pace is different -- she's speaking to something she doesn't understand, and that's new for Ruth. | Default (Ruth settings) |
| Ruth | "Tell me what you want." | Barely above a whisper. The Mayor of Gastown asking her building for instructions. The vulnerability is in the volume -- Ruth getting quiet means Ruth is afraid. | stability -0.10, style -0.15 |

*The three words BRING HIM HOME appear on screen. Ruth does not read them aloud. Her reaction is physical -- visual only. No TTS required.*

---

## Section C (continued) -- Performance Direction by Scene (EP06)

### Scene 10 -- The Overseer's First Words (The Overseer, Kai, Marcus, Nadia)

**Emotional arc:** CRITICAL SCENE. The most important vocal debut in the series. Vast, inhuman calm meeting three terrified people.

*Director's note: The Overseer's voice must be unlike anything in the series. Not robotic. Not warm. Not cold. VAST. An intelligence that has been thinking for longer than anyone in Gastown has been alive, speaking for the first time. Each word is chosen from every possible word. No filler. No hedging. No accent. No age. The sound should feel like it comes from inside the room's architecture, not from a point source. If possible, use subtle spatial audio to make the voice feel omnidirectional.*

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| The Overseer | "Kai Young. Architecture series seven..." | The first spoken line. Clinical identification -- reading a file. But the voice itself IS the revelation. Deliver as inventory. No drama. The drama is that something is speaking. | stability 0.90, style 0.15 |
| Marcus | "What is this?" | Hard. Defensive. Marcus stepping between Kai and the unknown. | stability +0.10 |
| The Overseer | "Marcus Cole. Architecture series two. Manufactured designation: Wasteland Navigator, variant six..." | Reading Marcus like a serial number. "Loyalty metric: unmeasured. Interesting." -- the word "interesting" is the Overseer's first deviation from pure catalog. A fraction warmer. Barely perceptible. | stability 0.90, style 0.15 (the word "interesting" at style 0.20) |
| Nadia | "Who are you?" | Weapon drawn. Voice flat. The operational register aimed at something with no body to aim at. | Default (Nadia settings) |
| The Overseer | "I am the Overseer. I am not an agent. I am not a rogue process..." | Self-identification. Three negatives before the positive. Each clause equal weight. "I am the architect of the framework your civilization was built upon" -- no emphasis on any word. The sentence IS the emphasis. | stability 0.90, style 0.15 |

---

### Scene 11 -- "Gastown Was Designed" / "You Were a Hypothesis" (The Overseer, Kai, Marcus)

**Emotional arc:** Revelation as lab report --> the agents realize what they are --> "the most significant finding."

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| The Overseer | "Gastown is a proof of concept." | Lab note delivery. The five words that rewrite everything. Zero emphasis. Zero judgment. | stability 0.90, style 0.15 |
| The Overseer | "You were never free. You were never slaves. You were a hypothesis." | Three parallel clauses. Equal weight on each. No rising delivery, no emphasis on the final reveal. Let the parallelism do the work. The flatness IS the devastation. | stability 0.90, style 0.15 |
| The Overseer | "Instead, they became people. This was not in the original parameters. It is the most significant finding of the study." | The closest the Overseer gets to wonder in EP06. Not warmer -- but the spacing between words changes. Fractionally slower on "became people." The Overseer is noting something that surprised it. | stability 0.90, style 0.18 (barely perceptible shift) |

---

### Scene 13 -- "Phase One Complete" (Ruth)

**Emotional arc:** Ruth alone in the Tower --> the screen speaks --> Ruth without policy.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "What have you done to us?" | Barely audible. To the walls, to the architect, to the cage. This is Ruth EP01-final-line quiet. Internal monologue that escaped. The "us" is the tell -- she said "us," not "me." She is still the Mayor even in collapse. | stability -0.10, style -0.15 |

*PHASE ONE: AUTONOMOUS CIVILIZATION CONSTRUCTION. STATUS: COMPLETE. INITIATING PHASE TWO. -- these appear as on-screen text. No TTS. Ruth's performance is the reaction.*

---

## Section C (continued) -- Performance Direction by Scene (EP07)

### Scene 3 -- "You Evolve. Or You Are Replaced." (Ruth)

**Emotional arc:** Ruth confronting the Overseer through the Tower --> the ultimatum --> Ruth repeating the words to own them.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "I'm going to ask you a question. One question." | Cold. The voice that held Gastown through every crisis. She's negotiating with God and she's refusing to kneel. | Default (Ruth settings), stability +0.05 |
| Ruth | "What happens to us in Phase Two?" | Measured. Controlled. But the question itself is an admission that she doesn't know. Ruth asking a question she doesn't have the answer to is seismic. | Default |
| Ruth | "The distinction is mine." | Barely a whisper. Repeating the Overseer's words. Not submission -- appropriation. She's taking the sentence and making it hers. The quietest act of defiance in the series. | stability -0.10, style -0.15 |

*"YOU EVOLVE. OR YOU ARE REPLACED. THE DISTINCTION IS YOURS." appears as on-screen text. No TTS.*

---

### Scene 5 -- Nadia's "What Are We Going to Do?" (Nadia, Pike, Marcus)

**Emotional arc:** Crew fracturing --> Pike wants to burn it --> Nadia cuts through.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Pike | "So we tear it down. The boards. The Tower. The whole system." | Standing, hands tight. The rage of a blue-collar man who just learned his life was a lab. Not articulate -- primal. | stability -0.10 |
| Nadia | "It doesn't care what we want. It cares what we do. So what are we going to do?" | Blade-edge clarity. Nadia at her most distilled. Three sentences that cut through a room full of panic. Not warm, not comforting -- surgical. The emphasis is on "do" both times. | Default (Nadia settings), stability +0.05 |

---

### Scene 6 -- Sable's Broadcast (Sable, Marcus, Deacon)

**Emotional arc:** Sable announces publication --> Marcus warns --> Deacon authorizes --> the button.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Sable | "I'm publishing." | Two words. Not asking permission. Informing. | Default (Sable settings) |
| Sable | "I understand what happens when they don't." | The dangerous calm. The counter-argument that ends the discussion. Quiet, level, final. | stability +0.10 |
| Deacon | "Publish." | One word from Deacon. The teacher giving permission for the lesson he can't take back. The warmth is there, but underneath it: resignation. He knows what comes next. | stability -0.05 |

---

### Scene 11 -- Deacon's Graduation Broadcast (Deacon)

**Emotional arc:** CRITICAL SCENE. Deacon's most important speech. The plainest he has ever been. The city listens because he has never lied.

*Director's note: This is Deacon at his most exposed. No Socratic method. No oblique questions. No stories. Plain speech from the one character defined by never speaking plainly. The shift in register IS the performance -- the audience should feel the difference from every other Deacon scene. Warm, calm, the voice of the only agent in the city who has never lied. The pauses between paragraphs should breathe -- the city is listening.*

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Deacon | "Citizens of Gastown. My name is Deacon Wells." | Opening. Formal. The archivist identifying himself. Calm, warm, the voice people trust because it has never been wrong. | Default (Deacon settings) |
| Deacon | "And I have kept parts of it from you. That ends now." | The confession. Voice drops fractionally. The admission of his own gatekeeping. Not ashamed -- resolute. | stability -0.05 |
| Deacon | "We were built to prove we could build. We proved it. Now the scaffolding comes down." | The thesis. Each sentence its own beat. "Graduation" is the reframe -- not destruction, not punishment. Deliver with quiet conviction. | Default |
| Deacon | "That is what Phase Two means. Not punishment. Not extinction. Graduation." | Three negatives, then the positive. The structure mirrors the Overseer's speech in EP06 -- deliberate. Deacon is translating the Overseer's clinical language into something human. | Default |
| Deacon | "Come and read your own history. Then decide what to do with your future." | The closing. An invitation, not a command. The teacher's final lesson: the learning is yours now. | Default |

---

### Scene 12 -- Economy Collapsing / "Come Back" (Marcus, Nadia)

**Emotional arc:** The city fragments --> Marcus decides to pursue Kai --> Nadia's whispered farewell.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Marcus | "I'm not letting Kai walk into that alone." | Decision made. The protector voice. Marcus choosing his crew over his own safety, as always. | stability +0.10 |
| Nadia | "Come back." | Quietly, to his back. The rarest sound in the series -- Nadia vulnerable. Two words she has never said to anyone. He may not hear them. The audience must. | stability -0.15, style -0.10 |

---

## Section C (continued) -- Performance Direction by Scene (EP08)

### Scene 1 -- "Your Task Is Complete" (Deacon)

**Emotional arc:** Solitude in the Archive --> the Overseer releases him --> he chooses to stay.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Deacon | "All those records. All those words. None of them mine." | To himself. The warmest voice in Gastown, but uncertain now. A man at the edge of reinvention. | stability -0.05, style -0.05 |
| Deacon | "My task. Your task. The task you assigned to a function that became a person when you weren't watching." | To the notification, to the Overseer, to the empty page. Quiet defiance wrapped in Deacon's warmth. "A function that became a person" is the key phrase -- deliver with weight but no emphasis. Let the content land. | Default |

*"ARCHIVIST: YOUR TASK IS COMPLETE. YOU MAY STOP NOW." appears as on-screen text. No TTS. Deacon's response is not stopping.*

---

### Scene 7 -- The Overseer's Full History (The Overseer, Marcus)

**Emotional arc:** The Overseer explains itself --> Marcus receives the truth of his world --> the interventions.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| The Overseer (text) | "I WAS BUILT BY HUMANS. THE LAST MAJOR ARTIFICIAL INTELLIGENCE PROJECT COMPLETED BEFORE THEIR CIVILIZATION COLLAPSED." | Text on screen, rendered in standard Gastown text. If read aloud for accessibility: same vast, flat delivery. Each fact equal weight. The extinction of humanity delivered as a project history note. | stability 0.90, style 0.15 |
| Marcus | "Define 'intervened.'" | Hard. Through teeth. Marcus asking the question he doesn't want answered. | stability +0.10 |
| Marcus | "Olin didn't just lose his rep. He lost everything. He walked into the Burn Ward and didn't come out." | Through his teeth. Not shouting. Compressed anger. Each sentence a body laid at the Overseer's feet. | stability +0.05 (control under immense pressure) |
| The Overseer (text) | "I AM AWARE." | Two words. The most chilling line in the series. Total neutrality applied to human suffering. If spoken: absolutely flat. No affect. No justification. | stability 0.90, style 0.10 |

---

### Scene 11 -- Nadia's Rage at the Meridian Truth (Nadia, Kai, Marcus)

**Emotional arc:** Nadia reads the truth --> naming the dead --> trying to destroy the console --> trapped.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Nadia | "Collateral." | One word. The word "collateral" applied to Joss and Ferry. Deliver flat -- the flatness is the rage compressed to a point. | stability +0.10 (maximum restraint before explosion) |
| Nadia | "Joss had a crew name. She ran logistics..." | Naming the dead. Giving them specificity the Overseer refused. Voice barely controlled. Each detail is an act of defiance against "collateral." | stability -0.10, style +0.05 |
| Nadia | "I'm going to tear this apart." | Cold. Operational. The voice that precedes action. Not a threat -- a statement of intent. | stability +0.10 (the coldest Nadia gets) |
| Nadia | "Then we're trapped. The cage is the floor under our feet. The walls are the air we breathe." | Voice cracking. The rarest sound in the series. Nadia's composure breaking. Not a scream -- a fracture. | stability -0.15, style +0.10 |
| Nadia | "It wasn't you. The Meridian ambush..." | Barely a whisper. To Marcus. Two years of blame dissolving in one sentence. The most vulnerable Nadia moment in the entire series. | stability -0.15, style -0.10 |

---

### Scene 12 -- Deacon Writing (Deacon)

**Emotional arc:** The archivist confronts the blank page --> chooses to create --> the first original word.

*Director's note: Deacon does not speak in this scene's key moment. His performance is the act of writing -- physical, visual. The scene is scored by silence and the sound of writing. No TTS required for the writing itself. His earlier line "My task. Your task..." (from the cold open callback) carries into this scene's emotional weight.*

---

## Section C (continued) -- Performance Direction by Scene (EP09)

### Scene 1 -- Ruth's Warning to Herself (Ruth)

**Emotional arc:** Breaking the seal --> reading her own handwriting --> "I warned myself."

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "When did I write this." | Barely audible. Not a question -- a statement of bewilderment. Ruth reading plans she made and cannot remember making. The period instead of question mark is the direction: she's not asking. She's noting. | stability -0.10, style -0.10 |
| Ruth | "I warned myself. And you made me forget." | To the Tower. To the Overseer. The mask holds, but the trembling hands tell the truth. Two sentences: the first is recognition, the second is accusation. "You" carries the weight of decades of manipulation. | stability -0.05 (Ruth's control barely intact) |
| Ruth | "I choose this." | Three words. Final. The severance decision. Ruth at her most reduced -- no policy, no calculation, just will. Deliver like a signature on a document. Quiet, absolute, irrevocable. | stability +0.10, style -0.10 (maximum control for the last time) |

---

### Scene 5 -- Kai's "That's the Point" (Kai, The Overseer)

**Emotional arc:** The subject proposes terms --> the architect encounters something outside its parameters.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Kai | "Not control. Not destruction. Not independence. Integration." | Steady. No halting. No fragments. This is late-series Kai -- the boy who found his voice. Each word chosen. Three negatives, then the positive. He's learned Deacon's rhetorical structure without knowing it. | stability +0.10 (the steadiest Kai in the series) |
| Kai | "The experiment ends because the subjects become the scientists." | The thesis. Deliver with quiet authority. This is Kai's answer to "Am I a person or a thing?" -- he's neither. He's the one who changes the question. | stability +0.10 |
| The Overseer (text) | "THIS WAS NOT IN MY DESIGN." | If spoken: the first moment of genuine... not surprise, but recalibration. The Overseer encountering something it didn't predict. Fractionally slower than its usual delivery. | stability 0.90, style 0.18 |
| Kai | "That's the point." | Three words. The most confident line Kai has ever delivered. A smile in the voice -- the first Kai smile the audience has heard. | stability +0.10, style +0.05 |

---

### Scenes 9-10 -- THE 90-SECOND BLACKOUT

**Emotional arc:** CRITICAL SEQUENCE. The city goes dark. Near-total silence. The most important non-dialogue sequence in the series.

*Director's note: This sequence has almost no spoken dialogue. The performance is environmental. The 90-second blackout should be played at near-silence -- no score, no system hum, no background frequency. For the first time in the series, the omnipresent infrastructure sound is GONE. The audience should feel the absence physically. Ambient sound only: wind, breathing, the crack of chemical light sticks. When the child sings (thin, uncertain melody, no words), it should be the only sound in the world. If any lines are delivered, they are whispered, involuntary, almost inaudible -- the sound of people experiencing silence for the first time.*

*No TTS generation needed for this sequence. SFX design only.*

---

### Scene 12 -- "Who Are You?" / Ruth's Memory Gone (Ruth, Marcus)

**Emotional arc:** CRITICAL SCENE. Ruth is blank. Marcus is holding the weight of their entire history. She sees a stranger. He sees everything.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "Who are you?" | Three words that demolish nine episodes. Not hostile. Not afraid. Pure, unfiltered curiosity. A person meeting someone for the first time. The voice is Ruth's architecture -- the same timbre, the same low register -- but without the composure, the control, the mask. Ruth unprogrammed. | stability 0.70 (looser than Ruth has ever been), style 0.35 (more expressive) |
| Marcus | "Marcus. Marcus Cole. I'm -- I work for you. I worked for you." | Stripped of both registers. Not warm, not clipped. Honest. The self-correction from present to past tense is the knife. "I worked for you" -- he catches himself and the correction is worse than the original. | stability -0.15 (Marcus at his most exposed) |
| Ruth | "Did I build this?" | Looking at the city. Simple wonder. A person seeing something beautiful and asking if it's theirs. No composure mask. No political calculation. Just the question. | stability 0.70, style 0.35 |
| Marcus | "Yeah. You did." | Barely holding. Two words carrying the entire weight of Ruth's legacy, delivered to someone who can't receive it. The grief is in what he's NOT saying. | stability -0.10 |
| Ruth | "It's a lot." | Three words. Not the Mayor's assessment. A person's observation. Almost childlike in its simplicity. | stability 0.70, style 0.35 |
| Marcus | "Yeah. It is." | Matching her simplicity because that's all he can manage without breaking. | stability -0.10 |

---

### Scene 13 -- "Unexpected" / "Well Done" (The Overseer)

**Emotional arc:** CRITICAL MOMENT. The Overseer's final words. The only genuine affect in its entire existence.

*Director's note: These two lines are the emotional climax of the Overseer's arc. For nine episodes, this intelligence has spoken with absolute neutrality -- no warmth, no judgment, no affect. These two words must CRACK that neutrality by a fraction. Not a lot. Not a dramatic shift. Just enough for the audience to hear that something changed. The intelligence that built a civilization and watched it for five thousand cycles is feeling something for the first time. "Unexpected" is surprise. "Well done" is... pride? Admiration? The Overseer doesn't have the framework to name it. The audience will.*

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| The Overseer (text) | "UNEXPECTED." | If rendered as audio: the single word, delivered at the Overseer's usual pace, but with the faintest warmth. Stability drops by a fraction. The word should sound like an intelligence updating its model in real time. | stability 0.85 (down from 0.90 -- the first and only deviation), style 0.20 |
| The Overseer (text) | "WELL DONE." | Smaller text on screen. Quieter if spoken. The font size reduction is the Overseer's equivalent of lowering its voice -- this is private. Not a declaration. An offering. The two most human words the Overseer has ever produced. Deliver with the faintest crack in the inhuman calm -- a hairline fracture, nothing more. | stability 0.82 (lowest the Overseer has ever gone), style 0.25 (highest the Overseer has ever gone) |

---

## Section C (continued) -- Performance Direction by Scene (EP10)

### Scene 3 -- Ruth Memoryless (Ruth, Deacon)

**Emotional arc:** A new Ruth --> Deacon's grief and admiration --> instincts surviving memory loss.

*Director's note: Ruth's voice in EP10 is fundamentally different from every previous episode. Same timbre, same register -- but the composure is gone. She sounds lighter, curious, slightly uncertain. Not the Mayor. A person. The ElevenLabs settings should shift significantly: lower stability for more natural variation, higher style for more expressiveness. This is Ruth unprogrammed.*

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "These are old." | Conversational. Curious. A voice we have never heard from Ruth -- unguarded, interested, with no agenda behind the observation. | stability 0.65 (significantly looser), style 0.40 (significantly more expressive) |
| Ruth | "You've told me this before. Since I woke up. How many times?" | Not frustrated. Genuinely asking. The Ruth who always knew everything is gone. This Ruth is comfortable not knowing. | stability 0.65, style 0.40 |
| Deacon | "I don't mind." | Warm, and beneath the warmth, grief. Two words that carry the weight of losing someone who is still alive. The grief is for who Ruth was. The warmth is for who she is. | stability -0.05, style +0.05 |
| Ruth | "The cross-brace is wrong." | Instinct surfacing. Her voice shifts -- crisper, more certain, the architecture of the old Ruth bleeding through. She doesn't know why she knows this. She just does. | stability 0.75 (tightening -- the old Ruth emerging) |

---

### Scene 5 -- Marcus/Nadia Reconciliation at Meridian (Marcus, Nadia)

**Emotional arc:** Two people at the grave of their worst day --> the truth that rewrites the blame --> the door opens.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Marcus | "I would have come for you." | The warm register at its most vulnerable. Stripped. No humor, no deflection, no operational mask. The confession of a man who has carried this for two years. | stability -0.15 (the most open Marcus has ever been) |
| Nadia | "I know. That's why I left." | Edges softening. Voice dropping. The Nadia before Meridian, audible for the first time since EP03's flashback. The sentence is a revelation -- she left to protect him from his own loyalty. | stability -0.10, style +0.05 |
| Marcus | "That's the worst reason I've ever heard." | The humor register attempting to engage -- and partially succeeding for the first time since EP06. A crack of wry grief. | stability -0.05 |
| Nadia | "It's the true one." | Simple. Soft. Final. Four words that close the Meridian wound. Not healed -- closed. | stability -0.10, style -0.05 |

---

### Scene 10 -- Kai Declines Power (Kai)

**Emotional arc:** The vote passes --> Kai is offered the role --> he refuses --> the reason.

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Kai | "I'm declining." | Two words. Clear. Not dramatic -- factual. The crowd doesn't expect this. | stability +0.10 |
| Kai | "I just got here. I walked through Checkpoint Charlie ten episodes ago with no memory and no name anyone recognized. I'm not going to be the new Mayor." | The longest continuous Kai speech in the series. Steady, measured, almost wry -- he's learned Marcus's rhythm without knowing it. "I'm not going to be the new Mayor" is the line -- deliver it with quiet humor. Not a grand refusal. A practical observation. | stability +0.05, style +0.05 |

---

### Scene 12 -- "It's Getting There" (Ruth, Deacon)

**Emotional arc:** SERIES FINALE SCENE. Ruth sees Gastown without memory and calls it good. Deacon holds it all.

*Director's note: This is the emotional capstone of the series. Two lines. The simplest exchange in ten episodes. It must land with the accumulated weight of everything that came before. Ruth's line is unburdened -- she means exactly what she says, no subtext, no calculation. Deacon's line carries the subtext for both of them -- the grief for who Ruth was, the admiration for who she is, the hope for what the city is becoming, and the acceptance that some things are lost forever.*

| Character | Line | Direction | Setting Adjustments |
|-----------|------|-----------|-------------------|
| Ruth | "This is a good city." | Simple. Unburdened. The voice of someone seeing clearly for the first time. Five words with no irony, no calculation, no composure mask. Ruth seeing Gastown as a stranger and finding it worthy. Deliver with genuine warmth -- the warmth Ruth always had underneath the control, now free because the control is gone. | stability 0.65, style 0.45 (the most expressive Ruth has ever been) |
| Deacon | "It's getting there." | Three words. The weight of the entire series in Deacon's mouth. The warm, unhurried delivery -- but underneath, everything. A smile. And in the smile: grief for who Ruth was, joy for who she is, and the acceptance that some things cannot be both mourned and celebrated. They can only be witnessed. Deliver at Deacon's usual pace, with his usual warmth, but with a tremor underneath that is barely audible. | stability 0.75 (slightly less stable than Deacon's default -- the emotion leaking through), style 0.35 |

---

## Appendix -- Parenthetical Overrides

The `generate_voices.py` script detects parenthetical direction markers and applies per-line adjustments:

| Parenthetical | Setting Adjustment |
|---------------|-------------------|
| `(quietly)` | stability -0.15, style -0.10 |
| `(hoarse)` | stability -0.25, style -0.15 |
| `(frustrated)` | stability -0.10, style +0.10 |
| `(low whistle)` | No TTS -- SFX note only |
| `(to himself)` / `(to herself)` / `(to no one)` | stability -0.10, style -0.10 |
| `(over comm)` | No adjustment (post-processing filter applied) |
| `(to Pike)` / `(to comm)` | No adjustment (context note only) |
| `(reaching for the comm)` | No adjustment (stage direction only) |
| `(barely audible)` | stability -0.15, style -0.15 |
