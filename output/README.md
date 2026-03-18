# Gas Town Chronicles -- Production Pipeline

## Pipeline Stages

```
1. Script  ──►  2. Shot List  ──►  3. Image Prompts  ──►  4. Images  ──►  5. Voice Audio  ──►  6. Assembly
```

| Stage | Input | Output | Tool |
|-------|-------|--------|------|
| 1. Write script | Story outline | `scripts/EP01_script.md` | Manual / Claude |
| 2. Generate shot list | Script | `scripts/EP01_shots.md` | Claude (Director agent) |
| 3. Generate image prompts | Shot list | `assets/EP01_image_prompts.json` | Claude (Director agent) |
| 4. Generate images | Image prompts JSON | `assets/EP01/EP01_SHOT_{nn}.png` | Midjourney / Runway / DALL-E |
| 5. Generate voice audio | Script + voice profiles | `audio/EP01/EP01_S{ss}__{CHAR}__{nnn}.mp3` | `generate_voices.py` (ElevenLabs) |
| 6. Assemble video | Images + audio | `EP01_final.mp4` | `assemble_EP01.sh` (FFmpeg) |

## Prerequisites

- **FFmpeg** with libx264 and AAC support
- **ffprobe** (bundled with FFmpeg)
- **Python 3.8+** (for duration calculations in assembly script)
- **ElevenLabs API key** (for voice generation only -- set `ELEVENLABS_API_KEY` in `.env`)

## Directory Structure

```
output/
  assets/
    EP01/                          # Generated images (one per shot)
      EP01_SHOT_01.png
      EP01_SHOT_02.png
      ...EP01_SHOT_56.png
    EP01_image_prompts.json        # Shot metadata and prompts
  audio/
    EP01/                          # Generated voice audio (per dialogue line)
      EP01_S01__GUARD_1__001.mp3
      EP01_S01__GUARD_2__002.mp3
      ...
    generate_voices.py             # Voice generation script
  scripts/
    EP01_script.md                 # Full screenplay
    EP01_shots.md                  # Shot list with durations and prompts
  assemble_EP01.sh                 # FFmpeg assembly script
  EP01_final.mp4                   # Final output video
```

## Usage

### Generate voice audio

```bash
# Preview what will be generated
python3 audio/generate_voices.py --dry-run

# Generate all audio (requires ELEVENLABS_API_KEY in .env)
python3 audio/generate_voices.py

# Generate audio for a specific scene
python3 audio/generate_voices.py --scene 10
```

### Assemble final video

```bash
# Make script executable
chmod +x assemble_EP01.sh

# Run assembly (images must exist in assets/EP01/)
./assemble_EP01.sh
```

The assembly script will:
1. Validate all inputs (images, audio, tools)
2. Generate title card and end card
3. Build per-shot video segments (image + matched audio)
4. Crossfade all segments together (0.3s fade transitions)
5. Export `EP01_final.mp4` at 1920x1080, H.264, YouTube-ready

### Output specs

- Resolution: 1920x1080 (Full HD)
- Codec: H.264 high profile, CRF 18
- Audio: AAC 192k, 44.1kHz
- Container: MP4 with faststart (streaming-optimized)
