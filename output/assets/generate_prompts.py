#!/usr/bin/env python3
"""Parse EP01_shots.md and generate EP01_image_prompts.json."""

import json
import re
import sys

SHOTS_FILE = "/home/jeremy/gastown-series/output/scripts/EP01_shots.md"
OUTPUT_FILE = "/home/jeremy/gastown-series/output/assets/EP01_image_prompts.json"

# Character canonical visual descriptions for prompt injection
CHARACTER_CANON = {
    "Marcus": "rugged man in his 40s, scarred weathered hands, wind-worn dark jacket, built like a machine designed for hard use, calm competent expression, short dark hair",
    "Kai": "young man in his early 20s, barefoot, clean pale clothes anachronistic for the wasteland, peaceful unfocused expression, ethereal dreamlike quality, lean build",
    "Sable": "sharp-featured young woman in her late 20s, precise movements, intense analytical eyes, determined stride, practical dark clothing",
    "Deacon": "ageless man in monastic-technical clothing, calm composed expression, penetrating knowing eyes, warm but unsettling presence",
    "Ruth": "composed ageless woman, data-screen reflections across her face, eyes that have been reading data for lifetimes, powerful bearing, dark formal attire",
    "Pike": "young male crew member, animated expressions, work-worn clothes, blue-collar attitude",
    "Tess": "female crew member, calm competent bearing, practical work gear",
    "Guards": "two armored guard agents, industrial military aesthetic, checkpoint uniforms, rifle-like tools",
}

# Scene definitions parsed from headers
SCENE_DEFS = {
    1: {"env": "exterior, Checkpoint Charlie", "time": "night"},
    2: {"env": "title card sequence", "time": "N/A"},
    3: {"env": "exterior, Wasteland", "time": "day"},
    4: {"env": "interior, Marcus's vehicle", "time": "day, continuous"},
    5: {"env": "interior, The Refinery", "time": "day"},
    6: {"env": "interior, Sable's workstation", "time": "day, continuous"},
    7: {"env": "exterior, Wasteland fringe", "time": "dusk"},
    8: {"env": "interior, stasis pod close-up", "time": "dusk"},
    9: {"env": "exterior, Gastown perimeter", "time": "night"},
    10: {"env": "interior, The Archive", "time": "night"},
    11: {"env": "interior, Marcus's safe house", "time": "night"},
    12: {"env": "interior, Marcus's safe house", "time": "night, later"},
    13: {"env": "interior, Marcus's safe house", "time": "night, continuous"},
    14: {"env": "interior, The Tower", "time": "night"},
}

# Which shots belong to which scene
SCENE_RANGES = [
    (1, 1, 9),
    (2, 10, 10),
    (3, 11, 16),
    (4, 17, 21),
    (5, 22, 24),
    (6, 25, 26),
    (7, 27, 30),
    (8, 31, 31),
    (9, 32, 34),
    (10, 35, 40),
    (11, 41, 45),
    (12, 46, 48),
    (13, 49, 52),
    (14, 53, 56),
]

def get_scene_for_shot(shot_num):
    for scene, start, end in SCENE_RANGES:
        if start <= shot_num <= end:
            return scene
    return None

# Character presence per shot (manually mapped from script context)
SHOT_CHARACTERS = {
    1: ["Guard 1", "Guard 2"],
    2: ["Guard 1", "Guard 2"],
    3: [],
    4: ["Guard 1", "Guard 2"],
    5: [],
    6: ["Kai Young"],
    7: ["Kai Young", "Guard 1", "Guard 2"],
    8: [],
    9: ["Guard 1", "Guard 2"],
    10: [],
    11: [],
    12: [],
    13: ["Marcus Cole"],
    14: ["Pike", "Tess"],
    15: ["Pike", "Marcus Cole"],
    16: [],
    17: [],
    18: ["Marcus Cole"],
    19: ["Pike"],
    20: ["Marcus Cole"],
    21: [],
    22: [],
    23: ["Sable Maren"],
    24: ["Sable Maren"],
    25: [],
    26: ["Sable Maren"],
    27: [],
    28: ["Marcus Cole"],
    29: ["Marcus Cole"],
    30: ["Marcus Cole", "Kai Young"],
    31: ["Kai Young"],
    32: [],
    33: [],
    34: [],
    35: ["Deacon Wells"],
    36: ["Deacon Wells"],
    37: ["Sable Maren"],
    38: ["Sable Maren", "Deacon Wells"],
    39: ["Deacon Wells"],
    40: ["Sable Maren", "Deacon Wells"],
    41: ["Marcus Cole", "Kai Young"],
    42: ["Kai Young"],
    43: ["Kai Young", "Marcus Cole"],
    44: ["Kai Young"],
    45: ["Kai Young"],
    46: ["Marcus Cole", "Kai Young"],
    47: ["Marcus Cole"],
    48: ["Kai Young"],
    49: ["Marcus Cole", "Kai Young"],
    50: ["Marcus Cole"],
    51: [],
    52: ["Marcus Cole", "Kai Young"],
    53: ["Ruth Calder"],
    54: ["Ruth Calder"],
    55: [],
    56: ["Ruth Calder"],
}

# Mood per shot (synthesized from visual direction and scene context)
SHOT_MOODS = {
    1: "ominous isolation, routine about to break",
    2: "procedural tension, boredom masking danger",
    3: "digital dread, system malfunction",
    4: "confusion turning to fear, red alert",
    5: "supernatural awe, mechanical impossibility",
    6: "ethereal intrusion, dreamlike wrongness",
    7: "frozen terror, confrontation with the unknown",
    8: "ominous calm, false welcome",
    9: "unsettling normalcy, aftermath of the impossible",
    10: "dark emergence, digital birth, series identity",
    11: "desolate grandeur, wasteland beauty",
    12: "industrial grit, road warrior energy",
    13: "competent solitude, scanning the horizon",
    14: "blue-collar labor, survival through work",
    15: "working-class friction, crew dynamics",
    16: "epic revelation, civilization amid desolation",
    17: "economic anxiety, cyberpunk finance",
    18: "alertness, the moment before a dangerous deal",
    19: "disbelief and greed, temptation",
    20: "calculation, the weight of poverty vs opportunity",
    21: "decisive action, point of no return",
    22: "industrial cathedral, data as raw material",
    23: "precise intensity, the auditor at work",
    24: "sharp recognition, pattern breaking",
    25: "digital erasure, institutional cover-up",
    26: "dawning horror, the problem is systemic",
    27: "post-apocalyptic beauty, dusk isolation",
    28: "tension and solitude, walking into the unknown",
    29: "alien discovery, something that doesn't belong",
    30: "intimate revelation, first contact through glass",
    31: "beautiful unease, stasis between worlds",
    32: "stealth and desperation, running dark",
    33: "claustrophobic tension, sparks and scraping",
    34: "cyberpunk underbelly, neon poverty",
    35: "monastic warmth, hidden knowledge",
    36: "calm authority, the man who read everything",
    37: "determination meets patience, seeker and oracle",
    38: "intellectual chess, deflection and pursuit",
    39: "devastating calm, philosophical weight",
    40: "solitary revelation, the surface of deeper truth",
    41: "spartan tension, vigil and waiting",
    42: "system boot, consciousness returning",
    43: "disorientation, waking in a stranger's world",
    44: "fractured identity, connection to the unknown",
    45: "vulnerability, existential trembling",
    46: "cautious evaluation, trust being weighed",
    47: "warmth breaking through toughness, generosity",
    48: "fragile hope, choosing to trust",
    49: "secrets and silence, protector's burden",
    50: "perfect deception, the cost of lying",
    51: "blood money, economic transaction over human cargo",
    52: "weight of betrayal, two lives connected by a lie",
    53: "power and isolation, command center reveal",
    54: "controlled omniscience, the city made flesh",
    55: "data alarm, the moment the Tower noticed",
    56: "cracked composure, powerful silence, choosing not to act",
}


def parse_shots(text):
    """Parse all shots from the markdown file."""
    shots = []
    # Match each shot block
    shot_pattern = re.compile(
        r'### Shot (\d+) — (.+?)\n'
        r'- \*\*Type:\*\* (.+?)\n'
        r'- \*\*Duration:\*\* (.+?)\n'
        r'- \*\*Camera:\*\* (.+?)\n'
        r'- \*\*Prompt:\*\* `(.+?)`',
        re.DOTALL
    )
    for m in shot_pattern.finditer(text):
        shots.append({
            "number": int(m.group(1)),
            "title": m.group(2).strip(),
            "type": m.group(3).strip(),
            "duration": m.group(4).strip(),
            "camera": m.group(5).strip(),
            "prompt": m.group(6).strip(),
        })
    return shots


def detect_characters_in_prompt(prompt, characters_present):
    """Return canonical tags for characters detected."""
    tags = []
    for char_name in characters_present:
        first = char_name.split()[0]
        if first in ("Guard",):
            if "Guards" not in [t[0] for t in tags]:
                tags.append(("Guards", CHARACTER_CANON["Guards"]))
        elif first in CHARACTER_CANON:
            tags.append((first, CHARACTER_CANON[first]))
    return tags


def get_lighting(prompt, scene_num):
    """Extract lighting description from prompt and scene context."""
    scene_time = SCENE_DEFS[scene_num]["time"]

    # Extract lighting keywords from the prompt
    lighting_keywords = []

    light_patterns = [
        r'(amber\s+\w+)', r'(floodlight[s]?\s*\w*)', r'(neon\s+\w*)',
        r'(harsh\s+\w+light)', r'(warm\s+\w+\s+light\w*)', r'(cool\s+\w+\s+light\w*)',
        r'(dim\s+\w*\s*light\w*)', r'(single\s+overhead\s+light)',
        r'(dramatic\s+\w+\s*light\w*)', r'(side\s+light\w*)',
        r'(backlit\b)', r'(god\s+rays)', r'(screen\s+light)',
        r'(dashboard\s+glow)', r'(data\s+\w*\s*glow)', r'(amber\s+\w*\s*glow)',
        r'(green\s+and\s+red\s+glow)', r'(red\s+terminal\s+glow)',
        r'(cinematic\s+light\w*)', r'(orange\s+and\s+purple)',
        r'(dusk\s+light\w*)', r'(golden\s+hour)', r'(white\s+merciless\s+sun)',
        r'(CRT\s+screen)', r'(soft\s+blue-white)',
    ]

    prompt_lower = prompt.lower()
    found = set()
    for pat in light_patterns:
        m = re.search(pat, prompt_lower)
        if m:
            found.add(m.group(1).strip())

    if found:
        lighting = ", ".join(sorted(found))
    else:
        lighting = "cinematic lighting"

    # Append time of day
    if scene_time != "N/A":
        lighting += f", {scene_time}"

    return lighting


def enhance_prompt(prompt, characters_present):
    """Inject character canonical descriptions and standardize style suffix."""
    enhanced = prompt

    # Ensure style suffix is present
    if "--ar 16:9 --style raw" not in enhanced:
        enhanced += " --ar 16:9 --style raw"

    # Inject character tags as a prefix block if characters are present
    char_tags = detect_characters_in_prompt(prompt, characters_present)
    if char_tags:
        tag_block = " | ".join(f"[{name}: {desc}]" for name, desc in char_tags)
        # Insert character tags right after the first sentence/clause
        enhanced = f"{tag_block} :: {enhanced}"

    return enhanced


def build_camera_angle(shot_type, camera):
    """Combine type and camera into camera_angle field."""
    return f"{shot_type}, {camera}"


def get_negative_prompt(scene_num, shot_num):
    """Generate negative prompt with base exclusions plus scene-specific items."""
    base = [
        "modern clothing", "smartphones", "cars", "happy expressions",
        "bright daylight", "cartoon style", "low quality", "blurry",
        "watermark", "text overlay"
    ]

    # Scene-specific negatives
    scene_env = SCENE_DEFS[scene_num]["env"]
    if "interior" in scene_env:
        base.extend(["outdoor scenery", "sky", "horizon"])
    if "night" in SCENE_DEFS[scene_num].get("time", ""):
        base.extend(["sunny", "bright sky"])
    if scene_num == 2:  # title card
        base.extend(["characters", "faces", "human figures"])

    # Remove bright daylight from night scenes to avoid redundancy with "sunny"
    # and remove duplicates
    seen = set()
    result = []
    for item in base:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return ", ".join(result)


STYLE_REFERENCE = "post-apocalyptic noir, muted earth tones, neon accents, cinematic 2.39:1 aspect ratio, photorealistic"


def main():
    with open(SHOTS_FILE, "r") as f:
        text = f.read()

    shots = parse_shots(text)

    if len(shots) != 56:
        print(f"WARNING: Expected 56 shots, found {len(shots)}", file=sys.stderr)

    entries = []
    for shot in shots:
        num = shot["number"]
        scene = get_scene_for_shot(num)
        characters = SHOT_CHARACTERS.get(num, [])
        scene_def = SCENE_DEFS[scene]

        entry = {
            "shot_id": f"EP01_SHOT_{num:02d}",
            "scene_number": scene,
            "characters_present": characters,
            "environment": scene_def["env"],
            "lighting": get_lighting(shot["prompt"], scene),
            "camera_angle": build_camera_angle(shot["type"], shot["camera"]),
            "mood": SHOT_MOODS.get(num, "cinematic tension"),
            "full_prompt": enhance_prompt(shot["prompt"], characters),
            "negative_prompt": get_negative_prompt(scene, num),
            "style_reference": STYLE_REFERENCE,
        }
        entries.append(entry)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(entries, f, indent=2)

    print(f"Generated {len(entries)} entries -> {OUTPUT_FILE}")

    # Verification
    scenes_covered = sorted(set(e["scene_number"] for e in entries))
    print(f"Scenes covered: {scenes_covered}")
    ids = [e["shot_id"] for e in entries]
    print(f"Duplicate IDs: {len(ids) - len(set(ids))}")

    # Check all required fields
    required = ["shot_id", "scene_number", "characters_present", "environment",
                 "lighting", "camera_angle", "mood", "full_prompt",
                 "negative_prompt", "style_reference"]
    for e in entries:
        missing = [f for f in required if f not in e]
        if missing:
            print(f"MISSING FIELDS in {e['shot_id']}: {missing}", file=sys.stderr)


if __name__ == "__main__":
    main()
