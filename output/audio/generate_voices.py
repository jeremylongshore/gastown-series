#!/usr/bin/env python3
"""Generate ElevenLabs TTS audio for Gas Town Chronicles EP01.

Parses EP01_script.md to extract dialogue lines, maps each character
to an ElevenLabs voice with tuned settings, and generates MP3 files.

Usage:
    python generate_voices.py                    # Generate all audio
    python generate_voices.py --dry-run          # Preview parsing only
    python generate_voices.py --list-voices      # List available ElevenLabs voices
    python generate_voices.py --scene 10         # Generate audio for scene 10 only

Dependencies: elevenlabs>=2.15.0, python-dotenv
"""

import argparse
import os
import re
import sys
import time
from dataclasses import dataclass, field

from dotenv import load_dotenv


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

@dataclass
class DialogueLine:
    scene: int
    character: str
    line_num: int
    text: str
    parentheticals: list[str] = field(default_factory=list)


@dataclass
class VoiceConfig:
    voice_id: str
    voice_name: str
    stability: float
    similarity_boost: float
    style: float
    use_speaker_boost: bool


# ---------------------------------------------------------------------------
# Voice configuration per character
# ---------------------------------------------------------------------------

# Known voice IDs -- others resolved at runtime via API
KNOWN_VOICE_IDS: dict[str, str] = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Bella": "EXAVITQu4vr4xnSDxMaL",
}

# Character -> (primary_voice_name, settings)
CHARACTER_VOICES: dict[str, dict] = {
    "RUTH": {
        "voice_name": "Rachel",
        "stability": 0.85,
        "similarity_boost": 0.80,
        "style": 0.25,
        "use_speaker_boost": True,
    },
    "MARCUS": {
        "voice_name": "Adam",
        "stability": 0.60,
        "similarity_boost": 0.75,
        "style": 0.45,
        "use_speaker_boost": True,
    },
    "SABLE": {
        "voice_name": "Bella",
        "stability": 0.70,
        "similarity_boost": 0.80,
        "style": 0.40,
        "use_speaker_boost": True,
    },
    "KAI": {
        "voice_name": "Josh",
        "stability": 0.45,
        "similarity_boost": 0.70,
        "style": 0.55,
        "use_speaker_boost": False,
    },
    "DEACON": {
        "voice_name": "Daniel",
        "stability": 0.80,
        "similarity_boost": 0.75,
        "style": 0.30,
        "use_speaker_boost": True,
    },
    "NADIA": {
        "voice_name": "Serena",
        "stability": 0.55,
        "similarity_boost": 0.80,
        "style": 0.35,
        "use_speaker_boost": True,
    },
    "GUARD 1": {
        "voice_name": "Harry",
        "stability": 0.70,
        "similarity_boost": 0.75,
        "style": 0.30,
        "use_speaker_boost": False,
    },
    "GUARD 2": {
        "voice_name": "Ethan",
        "stability": 0.70,
        "similarity_boost": 0.75,
        "style": 0.30,
        "use_speaker_boost": False,
    },
    "PIKE": {
        "voice_name": "Arnold",
        "stability": 0.65,
        "similarity_boost": 0.75,
        "style": 0.35,
        "use_speaker_boost": False,
    },
    "TESS": {
        "voice_name": "Emily",
        "stability": 0.75,
        "similarity_boost": 0.75,
        "style": 0.25,
        "use_speaker_boost": False,
    },
}

# Parenthetical -> setting deltas
PARENTHETICAL_OVERRIDES: dict[str, dict[str, float]] = {
    "quietly": {"stability": -0.15, "style": -0.10},
    "hoarse": {"stability": -0.25, "style": -0.15},
    "frustrated": {"stability": -0.10, "style": 0.10},
    "barely audible": {"stability": -0.15, "style": -0.15},
    "to himself": {"stability": -0.10, "style": -0.10},
    "to herself": {"stability": -0.10, "style": -0.10},
    "to no one": {"stability": -0.10, "style": -0.10},
}

# Parentheticals that should skip TTS (SFX notes)
SKIP_PARENTHETICALS = {"low whistle"}

# TTS model -- eleven_multilingual_v2 for best quality
# Alternative: eleven_turbo_v2_5 for faster generation
TTS_MODEL = "eleven_multilingual_v2"


# ---------------------------------------------------------------------------
# Script parser
# ---------------------------------------------------------------------------

def parse_script(filepath: str) -> list[DialogueLine]:
    """Parse EP01_script.md and extract all dialogue lines.

    Screenplay format expected:
        ### SCENE N -- ...
        **CHARACTER_NAME**             or  **CHARACTER (V.O.)**
        (parenthetical)                    optional
        Dialogue text here.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines: list[DialogueLine] = []
    current_scene = 0
    line_counter: dict[int, int] = {}  # scene -> count

    # Split into lines for sequential parsing
    raw_lines = content.split("\n")
    i = 0
    while i < len(raw_lines):
        raw = raw_lines[i]

        # Detect scene headings: ### SCENE N
        scene_match = re.match(r"^###\s+SCENE\s+(\d+)", raw)
        if scene_match:
            current_scene = int(scene_match.group(1))
            if current_scene not in line_counter:
                line_counter[current_scene] = 0
            i += 1
            continue

        # Detect character name: **CHARACTER** or **CHARACTER (V.O.)**
        # Also matches **CREW MEMBER 1 (PIKE)** style names
        char_match = re.match(
            r"^\*\*([A-Z][A-Z\s\d()]+?)(?:\s*\(V\.O\.\))?\*\*\s*$", raw
        )
        if char_match and current_scene > 0:
            raw_name = char_match.group(1).strip()
            # Normalize: CREW MEMBER 1 (PIKE) -> PIKE, etc.
            alias_match = re.match(r"CREW MEMBER \d+\s*\((\w+)\)", raw_name)
            if alias_match:
                character = alias_match.group(1).upper()
            else:
                # Strip trailing parenthetical aliases from character name
                character = re.sub(r"\s*\(.*?\)\s*$", "", raw_name).strip()

            # Collect parentheticals and dialogue text
            i += 1
            parentheticals: list[str] = []
            dialogue_parts: list[str] = []

            while i < len(raw_lines):
                line = raw_lines[i].strip()
                # Stop at next character heading, scene heading, visual, or scene break
                if (
                    re.match(r"^\*\*[A-Z]", line)
                    or re.match(r"^###", line)
                    or re.match(r"^\[VISUAL:", line)
                    or re.match(r"^---", line)
                    or re.match(r"^\*[^*]", line)  # stage directions in italics
                    or re.match(r"^\*\*SMASH", line)
                ):
                    break
                if not line:
                    if dialogue_parts:
                        break
                    i += 1
                    continue

                # Parenthetical line: (something)
                paren_match = re.match(r"^\((.+?)\)\s*$", line)
                if paren_match:
                    parentheticals.append(paren_match.group(1).lower())
                    i += 1
                    continue

                dialogue_parts.append(line)
                i += 1

            if dialogue_parts:
                text = " ".join(dialogue_parts)
                line_counter[current_scene] = line_counter.get(current_scene, 0) + 1
                lines.append(DialogueLine(
                    scene=current_scene,
                    character=character,
                    line_num=line_counter[current_scene],
                    text=text,
                    parentheticals=parentheticals,
                ))
            continue

        i += 1

    return lines


# ---------------------------------------------------------------------------
# Voice config resolution
# ---------------------------------------------------------------------------

_voice_id_cache: dict[str, str] = {}


def _resolve_voice_id(voice_name: str, client) -> str:
    """Resolve a voice name to its ElevenLabs voice ID."""
    if voice_name in KNOWN_VOICE_IDS:
        return KNOWN_VOICE_IDS[voice_name]
    if voice_name in _voice_id_cache:
        return _voice_id_cache[voice_name]

    # Search via API
    try:
        result = client.voices.search()
        for v in result.voices:
            _voice_id_cache[v.name] = v.voice_id
            if v.name == voice_name:
                return v.voice_id
    except Exception as e:
        print(f"  WARNING: Could not search voices: {e}")

    raise ValueError(
        f"Voice '{voice_name}' not found. Run --list-voices to see available voices."
    )


def get_voice_config(character: str, parentheticals: list[str], client) -> VoiceConfig | None:
    """Build voice config for a character, applying parenthetical overrides."""
    # Check for skip parentheticals
    for p in parentheticals:
        if p in SKIP_PARENTHETICALS:
            return None

    # Normalize character name for lookup
    lookup = character.upper()
    # Handle V.O. suffix already stripped by parser
    # Handle RUTH (V.O.) -> RUTH
    lookup = re.sub(r"\s*\(V\.O\.\)", "", lookup).strip()

    if lookup not in CHARACTER_VOICES:
        print(f"  WARNING: No voice config for '{lookup}', skipping.")
        return None

    cfg = CHARACTER_VOICES[lookup]
    stability = cfg["stability"]
    similarity_boost = cfg["similarity_boost"]
    style = cfg["style"]
    use_speaker_boost = cfg["use_speaker_boost"]

    # Apply parenthetical deltas
    for p in parentheticals:
        if p in PARENTHETICAL_OVERRIDES:
            deltas = PARENTHETICAL_OVERRIDES[p]
            stability = max(0.0, min(1.0, stability + deltas.get("stability", 0)))
            style = max(0.0, min(1.0, style + deltas.get("style", 0)))

    voice_id = _resolve_voice_id(cfg["voice_name"], client)

    return VoiceConfig(
        voice_id=voice_id,
        voice_name=cfg["voice_name"],
        stability=stability,
        similarity_boost=similarity_boost,
        style=style,
        use_speaker_boost=use_speaker_boost,
    )


# ---------------------------------------------------------------------------
# Audio generation
# ---------------------------------------------------------------------------

def generate_audio(
    line: DialogueLine,
    config: VoiceConfig,
    output_dir: str,
    client,
    max_retries: int = 3,
) -> str:
    """Generate TTS audio for a single dialogue line. Returns output filepath."""
    # Sanitize character name for filename
    char_safe = re.sub(r"[^a-zA-Z0-9]", "_", line.character)
    filename = f"EP01_S{line.scene:02d}__{char_safe}__{line.line_num:03d}.mp3"
    filepath = os.path.join(output_dir, filename)

    for attempt in range(1, max_retries + 1):
        try:
            audio_gen = client.text_to_speech.convert(
                voice_id=config.voice_id,
                text=line.text,
                model_id=TTS_MODEL,
                voice_settings={
                    "stability": config.stability,
                    "similarity_boost": config.similarity_boost,
                    "style": config.style,
                    "use_speaker_boost": config.use_speaker_boost,
                },
                output_format="mp3_44100_128",
            )

            # audio_gen is a generator yielding bytes chunks
            with open(filepath, "wb") as f:
                for chunk in audio_gen:
                    f.write(chunk)

            return filepath

        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "rate" in error_str.lower():
                wait = 2 ** attempt
                print(f"  Rate limited, retrying in {wait}s (attempt {attempt}/{max_retries})...")
                time.sleep(wait)
            elif attempt < max_retries:
                wait = 2 ** attempt
                print(f"  Error: {e}. Retrying in {wait}s (attempt {attempt}/{max_retries})...")
                time.sleep(wait)
            else:
                raise

    raise RuntimeError(f"Failed to generate audio after {max_retries} attempts")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate ElevenLabs TTS audio for Gas Town Chronicles EP01."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and display dialogue lines without calling the API.",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="List available ElevenLabs stock voices and exit.",
    )
    parser.add_argument(
        "--scene",
        type=int,
        default=None,
        help="Generate audio for a specific scene only.",
    )
    parser.add_argument(
        "--script",
        default=os.path.join(
            os.path.dirname(__file__), "..", "scripts", "EP01_script.md"
        ),
        help="Path to the EP01 script markdown file.",
    )
    parser.add_argument(
        "--output-dir",
        default=os.path.join(os.path.dirname(__file__), "EP01"),
        help="Output directory for generated audio files.",
    )
    args = parser.parse_args()

    # Resolve paths
    script_path = os.path.abspath(args.script)
    output_dir = os.path.abspath(args.output_dir)

    if not os.path.exists(script_path):
        print(f"ERROR: Script not found: {script_path}")
        sys.exit(1)

    # Parse script
    print(f"Parsing script: {script_path}")
    dialogue_lines = parse_script(script_path)
    print(f"Found {len(dialogue_lines)} dialogue lines across "
          f"{len(set(dl.scene for dl in dialogue_lines))} scenes.")

    # Filter by scene if requested
    if args.scene is not None:
        dialogue_lines = [dl for dl in dialogue_lines if dl.scene == args.scene]
        print(f"Filtered to {len(dialogue_lines)} lines in scene {args.scene}.")

    if not dialogue_lines:
        print("No dialogue lines found.")
        sys.exit(0)

    # Dry run: display parsed lines
    if args.dry_run:
        print("\n--- DRY RUN: Parsed Dialogue ---\n")
        for dl in dialogue_lines:
            parens = f" ({', '.join(dl.parentheticals)})" if dl.parentheticals else ""
            print(f"  S{dl.scene:02d} L{dl.line_num:03d} [{dl.character}]{parens}")
            print(f"    \"{dl.text}\"")
        print(f"\n--- Total: {len(dialogue_lines)} lines ---")

        # Show character breakdown
        chars = {}
        for dl in dialogue_lines:
            chars[dl.character] = chars.get(dl.character, 0) + 1
        print("\nCharacter line counts:")
        for char, count in sorted(chars.items(), key=lambda x: -x[1]):
            print(f"  {char}: {count}")
        return

    # Load API key
    load_dotenv()
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print(
            "ERROR: ELEVENLABS_API_KEY not found.\n"
            "Create a .env file with: ELEVENLABS_API_KEY=your_key_here\n"
            "Get your key at: https://elevenlabs.io/app/developers/api-keys"
        )
        sys.exit(1)

    # Initialize client
    try:
        from elevenlabs import ElevenLabs
    except ImportError:
        print("ERROR: elevenlabs package not installed. Run: pip install elevenlabs>=2.15.0")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)

    # List voices mode
    if args.list_voices:
        print("\nAvailable ElevenLabs voices:\n")
        try:
            result = client.voices.search()
            for v in result.voices:
                print(f"  {v.name:20s}  ID: {v.voice_id}")
        except Exception as e:
            print(f"ERROR: Could not fetch voices: {e}")
            sys.exit(1)
        return

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")
    print(f"TTS model: {TTS_MODEL}")
    print()

    # Generate audio for each line
    generated = 0
    skipped = 0
    errors = 0

    for i, dl in enumerate(dialogue_lines, 1):
        parens_str = f" ({', '.join(dl.parentheticals)})" if dl.parentheticals else ""
        print(f"[{i}/{len(dialogue_lines)}] S{dl.scene:02d} {dl.character}{parens_str}")
        print(f"  \"{dl.text[:80]}{'...' if len(dl.text) > 80 else ''}\"")

        config = get_voice_config(dl.character, dl.parentheticals, client)
        if config is None:
            print("  SKIPPED (parenthetical override or unknown character)")
            skipped += 1
            continue

        print(f"  Voice: {config.voice_name} | stab={config.stability:.2f} "
              f"sim={config.similarity_boost:.2f} style={config.style:.2f}")

        try:
            filepath = generate_audio(dl, config, output_dir, client)
            size_kb = os.path.getsize(filepath) / 1024
            print(f"  -> {os.path.basename(filepath)} ({size_kb:.1f} KB)")
            generated += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1

        # Small delay between API calls to be respectful of rate limits
        if i < len(dialogue_lines):
            time.sleep(0.5)

    print(f"\nDone. Generated: {generated}, Skipped: {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()
