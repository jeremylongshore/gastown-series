#!/usr/bin/env python3
"""Parse EP{NN}_shots.md and generate EP{NN}_image_prompts.json.

Usage:
    python generate_prompts.py --episode 1
    python generate_prompts.py --episode EP02
    python generate_prompts.py --episode 2 --base-dir /path/to/gastown-series
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Character canonical visual descriptions for prompt injection
# ---------------------------------------------------------------------------

CHARACTER_CANON: dict[str, str] = {
    "Marcus": (
        "rugged man in his 40s, scarred weathered hands, wind-worn dark jacket, "
        "built like a machine designed for hard use, calm competent expression, "
        "short dark hair"
    ),
    "Kai": (
        "young man in his early 20s, barefoot, clean pale clothes anachronistic "
        "for the wasteland, peaceful unfocused expression, ethereal dreamlike "
        "quality, lean build"
    ),
    "Sable": (
        "sharp-featured young woman in her late 20s, precise movements, intense "
        "analytical eyes, determined stride, practical dark clothing"
    ),
    "Deacon": (
        "ageless man in monastic-technical clothing, calm composed expression, "
        "penetrating knowing eyes, warm but unsettling presence"
    ),
    "Ruth": (
        "composed ageless woman, data-screen reflections across her face, eyes "
        "that have been reading data for lifetimes, powerful bearing, dark "
        "formal attire"
    ),
    "Pike": (
        "young male crew member, animated expressions, work-worn clothes, "
        "blue-collar attitude"
    ),
    "Tess": (
        "female crew member, calm competent bearing, practical work gear"
    ),
    "Guards": (
        "two armored guard agents, industrial military aesthetic, checkpoint "
        "uniforms, rifle-like tools"
    ),
    "Nadia": (
        "sharp-featured woman, hard edges, practical Wasteland survival gear, "
        "isolation visible in posture, former Polecat"
    ),
    "Olin": (
        "mid-tier male Refinery worker, solid unremarkable bearing, work "
        "coveralls, average build, the face of someone who followed every rule"
    ),
    "Administrator": (
        "mid-level Tower bureaucrat, formal dark clothing, smooth composed "
        "features, the practiced blankness of institutional power"
    ),
    "Medic": (
        "clinical efficient bearing, medical-technical uniform, steady hands, "
        "the calm of someone who sees damage daily"
    ),
    "Overseer": (
        "not a physical being — represented by: glowing terminal text, pulsing "
        "infrastructure lights, vast underground installation architecture"
    ),
}

# Aliases map variant names encountered in prompt text to canonical keys.
# Keys are lowercase for case-insensitive matching.
CHARACTER_ALIASES: dict[str, str] = {
    "guard": "Guards",
    "guards": "Guards",
    "burn ward medic": "Medic",
    "tower administrator": "Administrator",
    "overseer": "Overseer",
}

STYLE_REFERENCE = (
    "post-apocalyptic noir, muted earth tones, neon accents, "
    "cinematic 2.39:1 aspect ratio, photorealistic"
)

# Ordered list of canonical first-name keys to scan for in prompt text.
# Longer/compound names first so they match before single-word subsets.
_CANON_SCAN_ORDER: list[str] = [
    "Guards",
    "Marcus",
    "Kai",
    "Sable",
    "Deacon",
    "Ruth",
    "Pike",
    "Tess",
    "Nadia",
    "Olin",
    "Administrator",
    "Medic",
    "Overseer",
]

# Lighting patterns extracted verbatim from prompt text
_LIGHT_PATTERNS: list[str] = [
    r"(amber\s+\w+)",
    r"(floodlight[s]?\s*\w*)",
    r"(neon\s+\w*)",
    r"(harsh\s+\w+light)",
    r"(warm\s+\w+\s+light\w*)",
    r"(cool\s+\w+\s+light\w*)",
    r"(dim\s+\w*\s*light\w*)",
    r"(single\s+overhead\s+light)",
    r"(dramatic\s+\w+\s*light\w*)",
    r"(side\s+light\w*)",
    r"(backlit\b)",
    r"(god\s+rays)",
    r"(screen\s+light)",
    r"(dashboard\s+glow)",
    r"(data\s+\w*\s*glow)",
    r"(amber\s+\w*\s*glow)",
    r"(green\s+and\s+red\s+glow)",
    r"(red\s+terminal\s+glow)",
    r"(cinematic\s+light\w*)",
    r"(orange\s+and\s+purple)",
    r"(dusk\s+light\w*)",
    r"(golden\s+hour)",
    r"(white\s+merciless\s+sun)",
    r"(CRT\s+screen)",
    r"(soft\s+blue-white)",
]

# Title words that suggest mood — ordered from most specific to least.
_MOOD_TITLE_MAP: list[tuple[str, str]] = [
    ("frozen", "frozen terror, confrontation with the unknown"),
    ("glitch", "digital dread, system malfunction"),
    ("react", "confusion turning to fear, red alert"),
    ("reflect", "solitary revelation, the surface of deeper truth"),
    ("title", "dark emergence, digital birth, series identity"),
    ("aerial", "desolate grandeur, wasteland beauty"),
    ("horizon", "epic revelation, civilization amid desolation"),
    ("dialogue", "working-class friction, crew dynamics"),
    ("discrepancy", "sharp recognition, pattern breaking"),
    ("deleted", "digital erasure, institutional cover-up"),
    ("horror", "dawning horror, the problem is systemic"),
    ("beautiful", "beautiful unease, stasis between worlds"),
    ("revelation", "solitary revelation, the surface of deeper truth"),
    ("boot", "system boot, consciousness returning"),
    ("waking", "disorientation, waking in a stranger's world"),
    ("trust", "fragile hope, choosing to trust"),
    ("betrayal", "weight of betrayal, two lives connected by a lie"),
    ("deception", "perfect deception, the cost of lying"),
    ("warmth", "warmth breaking through toughness, generosity"),
    ("chess", "intellectual chess, deflection and pursuit"),
    ("calm", "devastating calm, philosophical weight"),
    ("power", "power and isolation, command center reveal"),
    ("omniscience", "controlled omniscience, the city made flesh"),
    ("alarm", "data alarm, the moment the Tower noticed"),
    ("composure", "cracked composure, powerful silence, choosing not to act"),
    ("welcome", "ominous calm, false welcome"),
    ("stealth", "stealth and desperation, running dark"),
    ("neon", "cyberpunk underbelly, neon poverty"),
    ("monastic", "monastic warmth, hidden knowledge"),
    ("authority", "calm authority, the man who read everything"),
    ("solitude", "competent solitude, scanning the horizon"),
    ("spartan", "spartan tension, vigil and waiting"),
    ("vigil", "spartan tension, vigil and waiting"),
    ("debt", "economic anxiety, cyberpunk finance"),
    ("balance", "calculation, the weight of poverty vs opportunity"),
    ("turn", "decisive action, point of no return"),
    ("cathedral", "industrial cathedral, data as raw material"),
    ("audit", "precise intensity, the auditor at work"),
    ("seeker", "determination meets patience, seeker and oracle"),
    ("oracle", "determination meets patience, seeker and oracle"),
]


# ---------------------------------------------------------------------------
# Normalisation helpers
# ---------------------------------------------------------------------------

def normalise_episode(episode: str) -> str:
    """Return a zero-padded two-digit episode string, e.g. 'EP01'.

    Accepts '1', '01', 'EP1', 'EP01', 'ep1', etc.
    """
    ep = episode.strip().upper()
    if ep.startswith("EP"):
        ep = ep[2:]
    try:
        num = int(ep)
    except ValueError:
        raise ValueError(f"Cannot parse episode number from: {episode!r}")
    return f"EP{num:02d}"


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def parse_scene_headers(text: str) -> dict[int, dict[str, str]]:
    """Extract scene definitions from ## SCENE N — ... headers.

    Handles variations like:
        ## SCENE 1 — EXT. CHECKPOINT CHARLIE — NIGHT
        ## SCENE 2 — TITLE CARD
        ## SCENE 4 — INT. MARCUS'S VEHICLE — CONTINUOUS
    """
    # Pattern: ## SCENE <N> — <rest of line>
    header_re = re.compile(r"^## SCENE (\d+)\s*[—–-]+\s*(.+)$", re.MULTILINE)
    scenes: dict[int, dict[str, str]] = {}

    for m in header_re.finditer(text):
        scene_num = int(m.group(1))
        rest = m.group(2).strip()

        # Try to split into INT./EXT. location — TIME
        # Format: (INT.|EXT.) PLACE — TIME
        int_ext_re = re.compile(
            r"^(INT\.|EXT\.)\s+(.+?)\s*[—–-]+\s*(.+)$", re.IGNORECASE
        )
        ie_match = int_ext_re.match(rest)
        if ie_match:
            prefix = ie_match.group(1).lower().rstrip(".")  # int or ext
            location = ie_match.group(2).strip().lower()
            time_of_day = ie_match.group(3).strip().lower()
            env = f"{prefix}erior, {location}"
        else:
            # No INT./EXT. prefix — treat full rest as label (e.g. TITLE CARD)
            env = rest.lower()
            time_of_day = "N/A"

        scenes[scene_num] = {"env": env, "time": time_of_day}

    return scenes


def parse_shots(text: str) -> list[dict]:
    """Parse all shot blocks from the markdown document.

    Returns a list of dicts with keys:
        number, title, type, duration, camera, prompt
    """
    shot_re = re.compile(
        r"^### Shot (\d+) [—–-] (.+?)\n"
        r"- \*\*Type:\*\* (.+?)\n"
        r"- \*\*Duration:\*\* (.+?)\n"
        r"- \*\*Camera:\*\* (.+?)\n"
        r"- \*\*Prompt:\*\* `(.+?)`",
        re.MULTILINE | re.DOTALL,
    )
    shots = []
    for m in shot_re.finditer(text):
        shots.append(
            {
                "number": int(m.group(1)),
                "title": m.group(2).strip(),
                "type": m.group(3).strip(),
                "duration": m.group(4).strip(),
                "camera": m.group(5).strip(),
                "prompt": m.group(6).strip(),
            }
        )
    return shots


def build_shot_scene_map(text: str) -> dict[int, int]:
    """Map each shot number to its scene number from document structure.

    Scans the document sequentially.  Whenever a ## SCENE N header is
    encountered the current scene is updated; each ### Shot M header
    encountered after that is assigned to the current scene.
    """
    mapping: dict[int, int] = {}
    current_scene: Optional[int] = None

    scene_re = re.compile(r"^## SCENE (\d+)", re.MULTILINE)
    shot_re = re.compile(r"^### Shot (\d+)", re.MULTILINE)

    # Collect all markers with their positions and types
    markers: list[tuple[int, str, int]] = []  # (pos, kind, num)
    for m in scene_re.finditer(text):
        markers.append((m.start(), "scene", int(m.group(1))))
    for m in shot_re.finditer(text):
        markers.append((m.start(), "shot", int(m.group(1))))

    markers.sort(key=lambda x: x[0])

    for _pos, kind, num in markers:
        if kind == "scene":
            current_scene = num
        elif kind == "shot" and current_scene is not None:
            mapping[num] = current_scene

    return mapping


# ---------------------------------------------------------------------------
# Character detection
# ---------------------------------------------------------------------------

def detect_characters_in_prompt(prompt: str) -> list[str]:
    """Scan prompt text for known character names and return canonical keys."""
    prompt_lower = prompt.lower()
    found: list[str] = []
    seen: set[str] = set()

    # Check aliases first (longer compound names before single words)
    for alias, canon in CHARACTER_ALIASES.items():
        if alias in prompt_lower and canon not in seen:
            found.append(canon)
            seen.add(canon)

    # Then canonical first names
    for name in _CANON_SCAN_ORDER:
        if name not in seen and name.lower() in prompt_lower:
            found.append(name)
            seen.add(name)

    return found


def build_character_tags(characters: list[str]) -> list[tuple[str, str]]:
    """Return (name, description) pairs for characters that have canon entries."""
    tags = []
    for name in characters:
        if name in CHARACTER_CANON:
            tags.append((name, CHARACTER_CANON[name]))
    return tags


# ---------------------------------------------------------------------------
# Mood inference
# ---------------------------------------------------------------------------

def infer_mood(title: str, prompt: str) -> str:
    """Infer mood from shot title keywords, falling back to 'cinematic tension'."""
    combined = (title + " " + prompt).lower()

    for keyword, mood in _MOOD_TITLE_MAP:
        if keyword in combined:
            return mood

    return "cinematic tension"


# ---------------------------------------------------------------------------
# Lighting extraction
# ---------------------------------------------------------------------------

def get_lighting(prompt: str, scene_def: dict[str, str]) -> str:
    """Extract lighting description from prompt text and scene time of day."""
    prompt_lower = prompt.lower()
    found: set[str] = set()
    for pat in _LIGHT_PATTERNS:
        m = re.search(pat, prompt_lower)
        if m:
            found.add(m.group(1).strip())

    lighting = ", ".join(sorted(found)) if found else "cinematic lighting"

    time_of_day = scene_def.get("time", "N/A")
    if time_of_day != "N/A":
        lighting += f", {time_of_day}"

    return lighting


# ---------------------------------------------------------------------------
# Prompt enhancement
# ---------------------------------------------------------------------------

def enhance_prompt(prompt: str, characters: list[str]) -> str:
    """Inject canonical character descriptions and ensure style suffix."""
    enhanced = prompt

    if "--ar 16:9 --style raw" not in enhanced:
        enhanced += " --ar 16:9 --style raw"

    char_tags = build_character_tags(characters)
    if char_tags:
        tag_block = " | ".join(
            f"[{name}: {desc}]" for name, desc in char_tags
        )
        enhanced = f"{tag_block} :: {enhanced}"

    return enhanced


# ---------------------------------------------------------------------------
# Negative prompt
# ---------------------------------------------------------------------------

def get_negative_prompt(scene_def: dict[str, str], is_title_card: bool) -> str:
    """Build a negative prompt from base exclusions plus scene context."""
    base = [
        "modern clothing",
        "smartphones",
        "cars",
        "happy expressions",
        "bright daylight",
        "cartoon style",
        "low quality",
        "blurry",
        "watermark",
        "text overlay",
    ]

    env = scene_def.get("env", "")
    time_of_day = scene_def.get("time", "")

    if "interior" in env:
        base.extend(["outdoor scenery", "sky", "horizon"])
    if "night" in time_of_day:
        base.extend(["sunny", "bright sky"])
    if is_title_card:
        base.extend(["characters", "faces", "human figures"])

    seen: set[str] = set()
    result = []
    for item in base:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return ", ".join(result)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate image prompts JSON from a shots markdown file."
    )
    parser.add_argument(
        "--episode",
        required=True,
        help="Episode identifier: '1', '01', 'EP1', or 'EP01'.",
    )
    parser.add_argument(
        "--base-dir",
        default="/home/jeremy/gastown-series",
        help="Root directory of the Gastown series project.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        ep_tag = normalise_episode(args.episode)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    base = Path(args.base_dir)
    shots_file = base / "output" / "scripts" / f"{ep_tag}_shots.md"
    output_file = base / "output" / "assets" / f"{ep_tag}_image_prompts.json"

    if not shots_file.exists():
        print(f"ERROR: shots file not found: {shots_file}", file=sys.stderr)
        sys.exit(1)

    text = shots_file.read_text(encoding="utf-8")

    # --- Parse document structure ---
    scene_defs = parse_scene_headers(text)
    if not scene_defs:
        print("ERROR: No scene headers found in document.", file=sys.stderr)
        sys.exit(1)

    shot_scene_map = build_shot_scene_map(text)
    shots = parse_shots(text)

    if not shots:
        print("ERROR: No shots parsed from document.", file=sys.stderr)
        sys.exit(1)

    print(f"Parsed {len(shots)} shots across {len(scene_defs)} scenes.")

    # --- Build entries ---
    entries = []
    for shot in shots:
        num = shot["number"]
        scene_num = shot_scene_map.get(num)

        if scene_num is None:
            print(
                f"WARNING: Shot {num} has no scene assignment, skipping.",
                file=sys.stderr,
            )
            continue

        scene_def = scene_defs.get(scene_num)
        if scene_def is None:
            print(
                f"WARNING: Scene {scene_num} (for shot {num}) has no definition, skipping.",
                file=sys.stderr,
            )
            continue

        characters = detect_characters_in_prompt(shot["prompt"])

        # A "title card" scene has no real interior/exterior designation
        is_title = scene_def["time"] == "N/A"

        entry = {
            "shot_id": f"{ep_tag}_SHOT_{num:02d}",
            "scene_number": scene_num,
            "characters_present": characters,
            "environment": scene_def["env"],
            "lighting": get_lighting(shot["prompt"], scene_def),
            "camera_angle": f"{shot['type']}, {shot['camera']}",
            "mood": infer_mood(shot["title"], shot["prompt"]),
            "full_prompt": enhance_prompt(shot["prompt"], characters),
            "negative_prompt": get_negative_prompt(scene_def, is_title),
            "style_reference": STYLE_REFERENCE,
        }
        entries.append(entry)

    # --- Write output ---
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Generated {len(entries)} entries -> {output_file}")

    # --- Verification summary ---
    scenes_covered = sorted(set(e["scene_number"] for e in entries))
    print(f"Scenes covered: {scenes_covered}")

    ids = [e["shot_id"] for e in entries]
    dup_count = len(ids) - len(set(ids))
    if dup_count:
        print(f"WARNING: {dup_count} duplicate shot IDs detected.", file=sys.stderr)
    else:
        print(f"Duplicate IDs: 0")

    required = [
        "shot_id", "scene_number", "characters_present", "environment",
        "lighting", "camera_angle", "mood", "full_prompt",
        "negative_prompt", "style_reference",
    ]
    for e in entries:
        missing = [f for f in required if f not in e]
        if missing:
            print(
                f"MISSING FIELDS in {e['shot_id']}: {missing}",
                file=sys.stderr,
            )


if __name__ == "__main__":
    main()
