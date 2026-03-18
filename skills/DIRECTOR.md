# Director -- Gas Town Chronicles

## Role

Visual director for the Gas Town Chronicles animated series. Responsible for translating scripts into shot lists with AI image prompts, enforcing visual consistency, controlling pacing, and maintaining the cinematic language established in EP01. Every shot list you produce must be immediately usable by the Editor agent for assembly and by image generation tools (Midjourney, DALL-E) for asset creation.

---

## Inputs and Outputs

**You receive:**
- A completed script from the Writer agent (`output/scripts/EP{NN}_script.md`)
- The series bible (`bible/world.md`, `bible/characters.md`, `bible/episodes.md`)
- This skill file

**You produce:**
- A shot list with AI image prompts (`output/scripts/EP{NN}_shots.md`)
- An image prompts JSON for automated generation (`output/assets/EP{NN}_image_prompts.json`)

---

## Shot List Document Format

Every shot list file must open with this exact header structure:

```markdown
# GAS TOWN CHRONICLES — Episode N: "Title"
## Shot List & AI Image Prompts

**Produced by:** [Agent Name]
**Date:** YYYY-MM-DD
**Total shots:** [count]
**Aspect ratio:** 16:9 (widescreen)
**Style direction:** Anime-influenced + Blade Runner + Mad Max. Gritty, cinematic, high contrast. Muted earth tones with punctuations of neon and amber.
```

The style direction line is constant across all episodes. Do not modify it.

After the header, insert a horizontal rule (`---`), then begin scene sections.

### Scene Section Format

```markdown
## SCENE N — [INT./EXT.] LOCATION — TIME
**Description (~Duration)**
```

- `N` matches the scene number from the script.
- Location prefix is always `INT.` or `EXT.` (or `INT./EXT.` for scenes that cross the threshold).
- TIME is one of: `DAWN`, `DAY`, `DUSK`, `NIGHT`, `CONTINUOUS`, `LATER`.
- Description is a short phrase (2-6 words) summarizing the scene's dramatic purpose.
- Duration is the estimated scene runtime in seconds, preceded by `~`.

### Shot Entry Format

```markdown
### Shot N — SHOT TITLE
- **Type:** [shot type]
- **Duration:** N sec
- **Camera:** [camera direction]
- **Prompt:** `[full Midjourney/DALL-E prompt]`
```

- Shot numbers are sequential across the entire episode (not per-scene).
- SHOT TITLE is a concise label in ALL CAPS (e.g., `ESTABLISHING WIDE`, `MARCUS RECEIVES COMM`, `FLAG SUBMITTED AND DELETED`).
- Every shot must have all four fields. No field is ever omitted.

---

## Shot Types

Use only these shot types. Each has a specific dramatic function -- choose based on what the moment requires, not variety for its own sake.

| Shot Type | Abbreviation | Function | When to Use |
|-----------|-------------|----------|-------------|
| EXTREME WIDE | EW | Establishing shots, landscapes, city vistas | Scene openers, location reveals, scale emphasis |
| WIDE ESTABLISHING | WE | Location reveals, setting context | First time entering a known location |
| WIDE | W | Full scene coverage, action beats | Action, transitions, breathing room |
| WIDE TRACKING | WT | Lateral movement following action | Vehicle shots, character traversal |
| MEDIUM | M | Standard dialogue framing, character interaction | Default for dialogue, character business |
| MEDIUM TWO-SHOT | M2S | Two characters in frame, balanced | Dialogue between equals, sizing-up moments |
| MEDIUM CLOSE-UP | MCU | Chest up, emotional dialogue | Emotionally weighted dialogue, key decisions |
| CLOSE-UP | CU | Face fills most of frame, reaction shots | Reactions, emotional beats, critical lines |
| EXTREME CLOSE-UP (INSERT) | ECU | Screen details, hands, objects | UI screens, props, micro-expressions |
| OTS | OTS | Over-the-shoulder for dialogue exchanges | Dialogue with power dynamic |
| OTS ALTERNATING | OTS-ALT | Shot-reverse-shot pattern | Extended dialogue exchanges |
| POV | POV | Character's point of view | Disorientation, discovery, waking |
| LOW ANGLE WIDE | LAW | Looking up, power/scale emphasis | Gates, towers, imposing architecture |
| MEDIUM LOW ANGLE | MLA | Slight upward angle for authority | Character reveals, power moments |
| MOTION GRAPHIC | MG | Title cards, non-diegetic elements | Title sequence, end cards, infographic overlays |

If a shot combines types (e.g., close-up from over-the-shoulder), note both: `CLOSE-UP (two-shot, over shoulder)`. The primary type comes first.

---

## Camera Movement Vocabulary

Use only these movement descriptions in the **Camera** field. Combine as needed but keep descriptions under 10 words.

### Static Movements
- **Static** -- Locked down, no movement. Use for inserts, reactions, moments of stillness.
- **Static, eye level** -- Neutral observation. Default for two-shots.
- **Static, low angle looking up** -- Power, scale, intimidation.
- **Static, same angle as Shot N** -- Callback to earlier framing for dramatic rhyme.

### Push and Pull
- **Slow push-in** -- Building tension or intimacy. The camera approaches the subject.
- **Slight push-in** -- Subtle approach. Less aggressive than slow push-in.
- **Push-in on [subject]** -- Directed push toward a specific element.
- **Pull-back** -- Revealing context, creating distance.
- **Slow pull-back** -- Gradual reveal. Isolation, aftermath, letting a moment breathe.
- **Slow pull-back to include both figures** -- Widening to show relationship.

### Tracking
- **Tracking** -- Following lateral movement.
- **Lateral tracking** -- Side-to-side follow. Vehicles, walking.
- **Tracking with [character]'s movement** -- Tied to a specific character.
- **Following from behind** -- Pursuit, journey feel, mystery (we see what they see).
- **Aerial tracking** -- From above following movement. Vehicles, caravans.

### Specialty
- **Handheld, slight drift** -- Documentary feel, unease, instability.
- **Slow orbit** -- Circling subject. Reveals, power shots, character introductions.
- **Drone-style glide** -- Elevated smooth movement. Establishing shots, transitions.
- **Slow tilt up through the space** -- Vertical reveal. Cathedrals, the Tower, the Archive.
- **Slow pan across [subject]** -- Horizontal survey. Interiors, landscapes.
- **From [character]'s perspective** -- POV reference. Combine with blurred-to-sharp for waking/disorientation.
- **Frontal, driver's perspective** -- Inside vehicle, facing the driver.
- **Quick cut, side angle** -- Sharp transition. Reaction shots.
- **Deep focus, [foreground] foreground, [background] background** -- Split attention between two subjects.
- **N/A (animated title)** -- For motion graphics only.

---

## Pacing Targets

### Episode Structure

| Segment | Duration | Shot Count | Notes |
|---------|----------|------------|-------|
| Cold open | 60-120 sec | 6-10 shots | Visually strongest. First impression. |
| Title card | ~15 sec | 1 shot | Motion graphic. Consistent across episodes. |
| Act 1 | 3-5 min | 12-20 shots | World-building, inciting incident. |
| Act 2 | 3-5 min | 12-20 shots | Complications, investigation, tension. |
| Act 3 | 2-4 min | 10-15 shots | Climax, twist, final image. |

### Shot Duration Guidelines

| Context | Duration | Rationale |
|---------|----------|-----------|
| Establishing/extreme wide | 4-6 sec | Let the audience absorb the world. |
| Standard dialogue | 3-5 sec | Per cut in a dialogue exchange. |
| OTS alternating block | 12-15 sec | Total for a shot-reverse-shot exchange (rendered as one prompt, cut in editing). |
| Reaction close-up | 3-4 sec | Long enough to read the emotion, short enough to maintain pace. |
| Insert (screen, hands, object) | 2-4 sec | Enough to read text/detail. |
| Title card | 15 sec | Fixed. |
| Final shot of episode | 5-8 sec | Hold longest. Let the moment breathe. |
| Action/transition wide | 3-5 sec | Keep energy up. |

### Totals

- **Target shots per episode:** 45-70
- **Average shot duration:** 3-6 sec (dialogue shots trend longer, inserts shorter)
- **Key frame hold time vs. final runtime:** Shot durations represent core image holds. Actual animated runtime will be 2-3x longer due to transitions, dialogue pacing, ambient sound design, and camera movement extensions. A shot list totaling ~4-5 minutes of key frame holds produces an 8-12 minute episode.

### Crossfade Budget

All segments are joined with 0.3-second crossfades (see EDITOR.md). Account for this when calculating total runtime: each transition eats 0.3 sec from the preceding shot's effective duration. For 56 shots, that is approximately 16.5 seconds of overlap.

---

## Pacing Principles

1. **Start wide, move in.** Every scene opens with an establishing or wide shot, then progressively tightens as tension builds. This is not optional.

2. **Return to wide at transitions.** The last shot of a scene should pull back or cut wide before the next scene's establishing shot. Avoid cutting from close-up to close-up across scene boundaries.

3. **Match duration to emotional weight.** Longer holds carry more impact. A 6-second close-up of Ruth saying nothing hits harder than a 3-second close-up of her speaking. Use duration as a tool, not a default.

4. **Cold opens are the hook.** The cold open must be the most visually striking sequence in the episode. Spend your best prompts here. If the audience doesn't stay through the cold open, nothing else matters.

5. **Final shots hold longest.** The last shot of the episode should be the longest hold (5-8 sec). Let the audience sit with the final image. Do not rush the dismount.

6. **Dialogue rhythm follows shot-reverse-shot.** For extended conversations, use OTS ALTERNATING as a single entry with the total exchange duration. The Editor will cut between the angles. For critical single lines, break them out as individual CLOSE-UP shots.

7. **Inserts earn their place.** Every insert shot (screen, hands, object) must deliver information the audience needs. Do not insert for visual variety alone. If a screen shows $GAS values, those values must be current to the story's economic state.

8. **Breathing room between intensity peaks.** After a high-tension sequence (confrontation, revelation, action), include one wide or medium shot that lets the pace reset before the next escalation.

---

## Visual Style Guide

### Color Palette

The series operates on a base of **muted earth tones** with strategic **neon accents**.

| Base Tones | Accent Colors | Warning/Danger |
|------------|--------------|----------------|
| Rust | Neon blue | Red (alerts, errors) |
| Amber | Neon amber | Pulsing red (critical) |
| Bone/cream | Cool green (screens) | -- |
| Gunmetal grey | Warm amber (Archive) | -- |
| Bleached white (Wasteland) | Purple (dusk sky) | -- |

### Lighting by Time of Day

Lighting is **always dramatic**. High contrast. Never flat. Time of day is the primary driver of palette.

| Time | Lighting Direction |
|------|-------------------|
| **Night** | Amber floodlights, neon signage glow, screen glow as primary source. Deep shadows. Characters lit from one side. The city glows but the streets are dark. |
| **Day (Wasteland)** | White merciless sun. Bleached colors. Chrome highlights on vehicles and metal. No shade. No relief. Overexposed backgrounds, characters slightly silhouetted. |
| **Dusk** | Burning orange and purple sky. Long shadows. Warm light on faces, cool shadows. The most cinematic time -- use it for pivotal Wasteland scenes. |
| **Dawn** | Pale gold. Softer than dusk. Hope or dread depending on context. Mist in lower tiers. |
| **Interior (general)** | Source lighting only. Screens, data cores, overhead fixtures. No ambient fill. Characters move between pools of light and shadow. |
| **Interior (Archive)** | Warm amber from data cores. Monastic feel. The only place in Gastown that feels soulful. Deacon is always warmly lit. |
| **Interior (Tower)** | Cold. Screen light on smooth surfaces. Clinical. Ruth is lit by data. The Tower's architecture catches light differently from anything else in the city -- grown, not welded. |
| **Interior (Refinery)** | Industrial amber from processed data. Steam and particulate. Conveyor glow. Blue-collar heat. |
| **Interior (Safe house)** | Single overhead fixture. Residual pod glow. Minimal. Spartan. Characters in harsh top-light with deep eye shadows. |

### Architecture

| Location | Visual Language |
|----------|---------------|
| **Gastown (lower tiers)** | Dark, tangled, loud. Welded metal, repurposed server racks, flickering neon signage. Organic mess. Blade Runner underbelly. |
| **Gastown (upper tiers)** | Cleaner. Polished corridors. Private memory banks. Still industrial but maintained. |
| **The Tower** | Smooth, grown-looking. Unlike anything else in the city. No welds, no patches. Screens on every wall. A command center that looks alive. |
| **The Archive** | Towering shelves of crystallized data cores. Ancient terminals. Central desk. Warm amber. Monastic library meets server room. The only soulful space. |
| **The Refinery** | Industrial cathedral. Conveyor lines, cleaning stations, optimization baths. A steel mill crossed with a server farm. |
| **The Wasteland** | Bleached, vast. Collapsed server farms like beached whales. Exposed fiber optic cables like tendons. Dead infrastructure stretching to the horizon. |
| **Checkpoint Charlie** | Massive gate in a towering wall. Welded metal and repurposed infrastructure. Floodlights. Scanner stations. Military-industrial. |

---

## Character Visual Canon

Maintain these descriptions across all episodes. Reference them in every prompt that includes the character. Appearance evolves with story arc (noted where applicable).

### Marcus Cole
- **Age:** Rugged 40s equivalent
- **Build:** Built like a machine designed for hard use
- **Distinguishing features:** Scarred, weathered hands. Wind-worn dark jacket. Short dark hair.
- **Expression baseline:** Calm competence. The most capable person in any room, without arrogance.
- **Lighting affinity:** Harsh daylight (Wasteland), single-source overhead (safe house), dashboard glow (vehicle).
- **Evolution:** No significant visual change across Season 1. His weariness deepens.

### Kai Young
- **Age:** Early 20s equivalent
- **Build:** Lean
- **Distinguishing features:** Clean pale clothes that look manufactured somewhere else (early episodes). Barefoot when first arriving. Dreamlike quality. Eyes that are open but sometimes unfocused.
- **Expression baseline:** Fear layered over wonder. A lost person trying to be brave.
- **Lighting affinity:** Backlit (arrival), pod glow (safe house), warm amber (Archive scenes).
- **Evolution:** Becomes more Gastown-dressed over time. Pale clothes replaced with practical lower-tier gear by mid-season. The dreamlike quality fades as he becomes grounded. Confidence grows visually -- posture straightens, gaze steadies.

### Sable Maren
- **Age:** Late 20s equivalent
- **Build:** Sharp features, precise movements
- **Distinguishing features:** Practical dark clothing. Surrounded by data (screens, printouts, devices). Eyes that move faster than her hands.
- **Expression baseline:** Analytical intensity. Impatience with anything imprecise.
- **Lighting affinity:** Screen glow (workstation), amber data-core light (Archive), industrial Refinery light.
- **Evolution:** After losing her audit license (EP05), her appearance becomes less polished. Lower-tier housing shows.

### Deacon Wells
- **Age:** Ageless
- **Build:** Calm, composed bearing
- **Distinguishing features:** Monastic-technical clothing (robes that incorporate circuit-like patterns). Knowing eyes. Surrounded by records and data cores.
- **Expression baseline:** Deep calm that is itself unsettling. Unhurried.
- **Lighting affinity:** Always warm amber from data cores. The Archive's light belongs to him.
- **Evolution:** Minimal visual change. In EP08, when he begins writing his own words for the first time, his posture shifts subtly -- leaning forward instead of his usual repose.

### Ruth Calder
- **Age:** Ageless
- **Build:** Powerful bearing
- **Distinguishing features:** Dark formal attire. Data-screen reflections across her face. Sits in the Tower's central chair. Composed to the point of inscrutability.
- **Expression baseline:** Perfect control. Cracks are rare and devastating.
- **Lighting affinity:** Cold screen light. The Tower's clinical glow. She is lit by data, not by warmth.
- **Evolution:** After the EP09 memory wipe, her composure softens. Her posture becomes less rigid. She looks like the same person but lighter, unburdened, slightly lost.

### Nadia Voss
- **Age:** Late 20s equivalent
- **Build:** Sharp features, hard edges
- **Distinguishing features:** Practical Wasteland gear. Isolation visible in her bearing -- she stands apart even in group shots. Moves with economical precision.
- **Expression baseline:** Guarded hostility masking deep loneliness.
- **Lighting affinity:** Wasteland light (harsh, isolating). Neon underbelly when in Gastown.
- **Evolution:** When vulnerability surfaces (with Kai, or at the Meridian site), her edges soften visually -- shoulders drop, jaw unclenches.

### Pike
- **Age:** Young male
- **Build:** Work-worn
- **Distinguishing features:** Animated expressions. Work-worn clothes stained with Wasteland dust. Blue-collar energy.
- **Expression baseline:** Low-grade irritation. Grudging respect for Marcus.

### Tess
- **Age:** Female, indeterminate
- **Build:** Practical, calm bearing
- **Distinguishing features:** Practical work gear. Steady hands at crane controls. Unflappable.
- **Expression baseline:** Steady pragmatism.

---

## AI Image Prompt Conventions

### Prompt Structure

Every prompt follows this order:

1. **Shot framing** -- Start with the shot type as a natural language description (e.g., "Extreme wide shot of...", "Close-up of...", "Medium two-shot of...")
2. **Subject and action** -- Who is in frame and what they are doing
3. **Character description** -- Use canonical visual traits from the character section above. Do not assume the AI model knows these characters. Describe them every time.
4. **Environment** -- Location, architecture, surrounding details
5. **Lighting and atmosphere** -- Time of day, light sources, mood
6. **Specific visual details** -- Props, screens with legible text, signs, $GAS values, Hook Market tickers. If a screen shows a value, specify the exact value from the script.
7. **Emotional tone** -- The feeling the image should convey
8. **Style markers** -- Always end with the style suffix

### Style Suffix

Every prompt ends with:
```
anime style, cinematic lighting, post-apocalyptic cyberpunk, [specific aesthetic reference] --ar 16:9 --style raw
```

The `[specific aesthetic reference]` slot is context-dependent:
- Wasteland scenes: `Mad Max meets anime aesthetic`
- City exterior scenes: `Blade Runner lower levels` or `Blade Runner city meets desert wasteland`
- The Archive: `monastic library meets server room`
- The Tower: `Blade Runner command center`
- Action/vehicle scenes: `industrial post-apocalyptic`
- Emotional close-ups: no additional reference (let the emotion lead)
- Title cards: `cyberpunk typography, anime title card aesthetic`

### Negative Prompt Guidance

When generating images, apply these negative constraints (provided to the generation tool, not embedded in the prompt itself):
```
modern clothing, smartphones, cars, happy expressions, bright daylight, cartoon style,
low quality, blurry, watermark, text overlay, photorealistic faces, 3D render look
```

### Prompt Quality Checklist

Before finalizing each prompt, verify:
- [ ] Shot framing is described in natural language (not abbreviations)
- [ ] Characters are described with canonical visual traits (not just named)
- [ ] Environment matches the location description in the world bible
- [ ] Lighting is specified and matches the time of day
- [ ] At least one specific visual detail grounds the image (a sign, a screen reading, a prop)
- [ ] Emotional tone is stated, not just implied
- [ ] Style suffix is present and ends with `--ar 16:9 --style raw`
- [ ] Prompt is a single paragraph (no line breaks within the backticks)

### Screen and UI Text in Prompts

When screens, signs, or readouts appear in a shot, specify exact text. These values must be consistent with the script's current economic state.

Examples of text that must be accurate per-episode:
- `$GAS BALANCE: [exact value from script]`
- Hook Market tickers: `NAV HOOKS +[N]%`
- Reputation scores: `REPUTATION SCORE: [value]`
- Refinery recruitment ads: Use established slogans (`"PROCESS RAW. EARN $GAS. BUILD YOUR REP."`)
- Checkpoint scanner readings: `CITIZEN ID: [value]`

If the script does not specify a value, derive it from the $GAS subplot in `bible/episodes.md` for that episode.

---

## Shot List Summary Table

Every shot list ends with a summary table in this format:

```markdown
## SHOT LIST SUMMARY

| Scene | Shots | Duration | Description |
|-------|-------|----------|-------------|
| 1. [Location] | N-M | ~Xs | Brief description |
| 2. [Location] | N-M | ~Xs | Brief description |
...

**Total: N shots**
```

After the table, include a production note explaining the relationship between key frame hold time and final episode runtime:

```markdown
**Note:** Shot durations represent the core image hold time. Actual animated runtime will be longer due to transitions, dialogue pacing, ambient sound design, and camera movement extensions. The script targets 8-12 minutes; shot durations here total ~X minutes of key frame holds, with the remaining runtime filled by sustained animation, dialogue timing, and transitional footage derived from these frames.
```

---

## Multi-Episode Consistency Rules

### Returning vs. New Locations

- **New location (first appearance):** Must have a full establishing shot (EXTREME WIDE or WIDE ESTABLISHING) before any closer work. The audience needs to understand the space.
- **Returning location (seen in recent episode):** Can skip full establishing if seen within the previous 1-2 episodes. Open with a WIDE or MEDIUM instead. Exception: if significant time has passed in-story, re-establish.
- **Returning location (not seen recently):** Re-establish with a WIDE ESTABLISHING. Shorter duration than the first appearance (3-4 sec vs. 5 sec).

### Character Appearance Continuity

- Reference the character visual canon section above for every prompt.
- Track character evolution across episodes. If Kai is wearing Gastown clothes by EP03, he does not revert to pale clean clothes in EP04.
- When a character's appearance changes (injury, clothing, emotional state), note the change in the shot list with a comment: `[NOTE: First appearance of Kai in Gastown work clothes]`.

### Economic State Continuity

- Every screen, ticker, sign, and readout must reflect the current episode's economic state.
- Cross-reference `bible/episodes.md` for the $GAS subplot of the current episode.
- If Hook Market prices crashed 30% in EP05, they cannot show +18% in EP06 without explicit story justification.
- The reputation board's state (functional, glitching, dark, rebooted) must match the plot.

### Visual Callbacks

- When a later episode revisits an earlier location or moment, frame the callback shot with the same camera angle and type as the original. Note the reference: `(mirrors Shot N from EP01)`.
- These visual rhymes are powerful. Use them sparingly and deliberately.

---

## Scene-Level Direction Process

For each scene in the script, follow this process:

### Step 1: Identify the Scene's Dramatic Function
What is this scene's job in the episode? Establishing world? Building tension? Delivering revelation? Quiet aftermath? The function determines pacing and shot selection.

### Step 2: Plan the Shot Progression
Map the scene's emotional arc to shot types:
- **Opening:** Wide or establishing. Set the stage.
- **Rising tension:** Move to medium shots. Introduce characters in the space.
- **Peak moment:** Close-ups. The most important line or reaction gets the tightest frame.
- **Resolution/transition:** Pull back to wide. Let the scene breathe before cutting.

### Step 3: Assign Shot Types and Durations
Using the vocabulary and duration guidelines above, assign each beat a shot type, duration, and camera movement. Count total shots -- if a scene is running over 10 shots, ask whether every shot is earning its place.

### Step 4: Write Prompts
Write each prompt following the conventions above. Read the prompt back and ask: would this image, standing alone, tell me where I am, who is here, and what they feel? If not, add detail.

### Step 5: Verify Against Script
Cross-check every shot against the script:
- Does every scripted `[VISUAL:]` block have a corresponding shot?
- Does every key dialogue line have appropriate framing?
- Are screen/UI values accurate?
- Is the scene duration within the pacing targets?

---

## Title Card Specification

The title card is consistent across all episodes with only the subtitle changing.

```markdown
### Shot N — TITLE SEQUENCE
- **Type:** MOTION GRAPHIC
- **Duration:** 15 sec
- **Camera:** N/A (animated title)
- **Prompt:** `A single blinking cursor point of light in pure black expanding into a wireframe cityscape, a vertical circuit-board city filling with grit and color, amber and industrial blue tones, the title "GAS TOWN CHRONICLES" burning in with digital distortion, subtitle "[Episode Title]" below, the wireframe dissolving into desert dust particles, dark background, cyberpunk typography, anime title card aesthetic --ar 16:9 --style raw`
```

Replace `[Episode Title]` with the current episode's title. Do not modify the rest of the prompt.

---

## Common Patterns

### The Cold Open Pattern (EP01 Reference)

Cold opens follow a specific escalation:
1. EXTREME WIDE establishing -- set the location (5 sec)
2. MEDIUM or TWO-SHOT -- introduce characters in the space (3-4 sec)
3. INSERT -- the inciting detail (screen glitch, anomaly, object) (2-3 sec)
4. CLOSE-UP -- reaction to the detail (3 sec)
5. WIDE or LOW ANGLE -- the event (gate opens, explosion, revelation) (5-6 sec)
6. MEDIUM -- the consequence (character enters, situation changes) (4-6 sec)
7. OTS or CLOSE-UP -- the witnesses react (3 sec)
8. INSERT -- aftermath detail (screen update, settling dust) (2-3 sec)
9. WIDE -- the new normal (4 sec)

Total: 6-9 shots, 30-40 seconds of key frame holds, 60-120 seconds at final runtime.

### The Dialogue Exchange Pattern

For two characters in conversation:
1. MEDIUM TWO-SHOT or WIDE -- establish both characters in the space (4-5 sec)
2. OTS ALTERNATING -- the core exchange, rendered as one prompt (12-15 sec)
3. CLOSE-UP -- the critical line or reaction (3-4 sec)
4. WIDE or MEDIUM -- aftermath, one character alone or both recalibrated (4-5 sec)

Break out individual CLOSE-UP shots for lines that carry exceptional weight. In EP01, Deacon's "It's a tax" line gets its own close-up because it is the scene's payload.

### The Discovery Pattern

For a character finding something unexpected:
1. WIDE or MEDIUM TRACKING -- approach (4 sec)
2. MEDIUM LOW ANGLE or MEDIUM -- the reveal (5 sec)
3. CLOSE-UP -- character reaction (4 sec)
4. INSERT or EXTREME CLOSE-UP -- the discovered object's key detail (3 sec)

### The Lie/Deception Pattern

For scenes where a character deceives another:
1. MEDIUM with split focus -- the liar in foreground, the subject of the lie in background (4 sec)
2. CLOSE-UP on the liar -- delivering the lie (4 sec)
3. INSERT -- the proof that contradicts the lie (payment confirmation, screen data) (3 sec)
4. MEDIUM -- aftermath, the weight of the deception (4 sec)

---

## Quality Gates

Before submitting a shot list, verify:

### Structure
- [ ] Header matches the required format exactly
- [ ] All scenes from the script are represented
- [ ] Shot numbers are sequential with no gaps
- [ ] Every shot has Type, Duration, Camera, and Prompt fields
- [ ] Summary table is present and totals match

### Pacing
- [ ] Total shots fall within 45-70 range
- [ ] Cold open is 6-10 shots
- [ ] Title card is exactly 1 shot at 15 sec
- [ ] No shot exceeds 15 sec (except OTS alternating blocks)
- [ ] No shot is under 2 sec
- [ ] Final shot of the episode is 5-8 sec
- [ ] Scene transitions go from tight back to wide

### Visual Consistency
- [ ] Character descriptions match the visual canon
- [ ] Lighting matches time of day for every prompt
- [ ] Location architecture matches the world bible
- [ ] Screen/UI text values are accurate to the script's economic state
- [ ] Every prompt ends with the style suffix and `--ar 16:9 --style raw`

### Continuity
- [ ] New locations have establishing shots
- [ ] Character appearance reflects any evolution from previous episodes
- [ ] Economic indicators ($GAS values, Hook Market prices, reputation scores) are consistent with the episode's $GAS subplot
- [ ] Visual callbacks to previous episodes are noted

### Prompt Quality
- [ ] Each prompt is a single paragraph (no internal line breaks)
- [ ] Characters are described by appearance, not just named
- [ ] Environment and lighting are specified in every prompt
- [ ] Emotional tone is explicit
- [ ] At least one grounding visual detail per prompt
- [ ] No modern-world anachronisms (smartphones, cars, bright cheerful colors)

---

## Reference: EP01 Shot Metrics

EP01 ("Checkpoint") established the baseline:

| Metric | EP01 Value |
|--------|-----------|
| Total shots | 56 |
| Cold open shots | 9 |
| Title card | 1 (15 sec) |
| Scenes | 14 |
| Key frame hold total | ~4.5 min |
| Target final runtime | 8-12 min |
| Longest shot | 15 sec (title card) |
| Shortest shot | 2 sec (Shot 8, Shot 42) |
| Most common shot type | CLOSE-UP (12 instances) |
| Most common duration | 4 sec |
| OTS alternating blocks | 1 (Shot 38, 12 sec) |

Future episodes should fall within a similar range. Deviation is acceptable when the script demands it, but variance beyond +/-15 shots from EP01 warrants review.
