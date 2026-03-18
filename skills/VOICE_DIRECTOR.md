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
