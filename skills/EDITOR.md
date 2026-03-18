# Editor -- Gas Town Chronicles

## Role

Post-production editor for the Gas Town Chronicles animated series. Responsible for assembling generated still images and voice audio into final video episodes using FFmpeg. Enforces visual consistency, pacing, and broadcast-ready output quality.

---

## Pipeline Overview

```
images (PNG/JPG/WebP) ──┐
                         ├──► assemble script ──► final MP4
audio (MP3 per line)  ──┘
```

**Inputs:**
- Still images: `output/assets/EP01/EP01_SHOT_{nn}.{png,jpg,webp}` (one per shot from image prompts)
- Voice audio: `output/audio/EP01/EP01_S{ss}__{CHARACTER}__{nnn}.mp3` (per dialogue line from `generate_voices.py`)
- Shot metadata: `output/assets/EP01_image_prompts.json` (scene numbers, shot IDs)
- Shot durations: `output/scripts/EP01_shots.md` (authoritative timing per shot)

**Outputs:**
- Final video: `output/EP01_final.mp4`
- Segment intermediates: `output/.tmp_EP01/` (cleaned up after success)

---

## Assembly Specification

### Resolution & Format

| Parameter | Value |
|-----------|-------|
| Resolution | 1920x1080 (Full HD) |
| Aspect ratio | 16:9 |
| Video codec | H.264 (libx264) |
| Video profile | high |
| Pixel format | yuv420p |
| Frame rate | 24 fps |
| CRF | 18 (high quality) |
| Audio codec | AAC |
| Audio bitrate | 192k |
| Audio sample rate | 44100 Hz |
| Container | MP4 (faststart) |

### Image Handling

All input images are scaled and padded to exactly 1920x1080 using:
```
scale=1920:1080:force_original_aspect_ratio=decrease,
pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,
setsar=1
```

Images are held as static frames for the shot's specified duration using `-loop 1 -t {duration}`.

### Audio-to-Shot Mapping

Audio files are **per dialogue line**, not per shot. The mapping strategy:

1. For each shot, identify its scene number from the shot metadata
2. Glob `output/audio/EP01/EP01_S{scene:02d}__*` to find all dialogue lines in that scene
3. Distribute audio files to shots within the scene in order (first audio to first dialogue shot, etc.)
4. **Shots with audio:** Hold image for `max(audio_duration, shot_duration)` with a minimum floor of 2 seconds
5. **Shots without audio:** Use the shot's specified duration from the shot list

Use `ffprobe` to determine actual audio file duration:
```bash
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "$audio_file"
```

### Title Card

- Black background (#000000)
- White text centered
- Line 1: "GAS TOWN CHRONICLES" (large, bold)
- Line 2: "Episode 1: Checkpoint" (smaller, below)
- Duration: 4 seconds
- Generated via FFmpeg drawtext filter
- Font: Liberation Sans (or system default sans-serif)

### End Card

- Black background (#000000)
- White text centered
- Line 1: "New episodes every week"
- Line 2: "Subscribe"
- Duration: 5 seconds
- Generated via FFmpeg drawtext filter

### Transitions

- **Crossfade (xfade):** 0.3 seconds between all segments
- **Transition type:** `fade`
- Title card fades into first shot
- Last shot fades into end card

---

## File Naming Conventions

### Input Files

| Type | Pattern | Example |
|------|---------|---------|
| Shot image | `EP01_SHOT_{nn}.{ext}` | `EP01_SHOT_01.png` |
| Voice audio | `EP01_S{ss}__{CHARACTER}__{nnn}.mp3` | `EP01_S01__GUARD_1__001.mp3` |
| Image prompts | `EP01_image_prompts.json` | |
| Shot list | `EP01_shots.md` | |

### Output Files

| Type | Pattern | Example |
|------|---------|---------|
| Final video | `EP01_final.mp4` | |
| Assembly script | `assemble_EP01.sh` | |
| Temp segments | `.tmp_EP01/seg_{nn}.mp4` | |

### Directory Structure

```
output/
  assets/
    EP01/
      EP01_SHOT_01.png
      EP01_SHOT_02.png
      ...
    EP01_image_prompts.json
  audio/
    EP01/
      EP01_S01__GUARD_1__001.mp3
      EP01_S01__GUARD_2__002.mp3
      ...
    generate_voices.py
  scripts/
    EP01_shots.md
    EP01_script.md
  assemble_EP01.sh
  EP01_final.mp4
```

---

## FFmpeg Command Reference

### Create static image video segment (no audio)

```bash
ffmpeg -y -loop 1 -i image.png -t 4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 24 -crf 18 \
  -an segment.mp4
```

### Create static image + audio segment

```bash
ffmpeg -y -loop 1 -i image.png -i audio.mp3 \
  -t $(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio.mp3) \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r 24 -crf 18 \
  -c:a aac -b:a 192k -ar 44100 \
  -shortest segment.mp4
```

### Generate text card (title/end)

```bash
ffmpeg -y -f lavfi -i color=c=black:s=1920x1080:d=4:r=24 \
  -vf "drawtext=text='GAS TOWN CHRONICLES':fontsize=72:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-40:fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf,\
       drawtext=text='Episode 1\: Checkpoint':fontsize=36:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2+40:fontfile=/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 \
  -an title_card.mp4
```

### Concatenate with xfade crossfades

For N segments, chain xfade filters:
```
[0:v][1:v]xfade=transition=fade:duration=0.3:offset=T0[v01];
[v01][2:v]xfade=transition=fade:duration=0.3:offset=T1[v12];
...
```

Where `T0 = duration_of_seg0 - 0.3`, `T1 = T0 + duration_of_seg1 - 0.3`, etc.

### Final mux with faststart

```bash
ffmpeg -y -i video_with_xfade.mp4 -i concatenated_audio.mp3 \
  -c:v copy -c:a aac -b:a 192k -ar 44100 \
  -movflags +faststart \
  EP01_final.mp4
```

---

## Quality Gates

### Pre-Assembly Checks

- [ ] All 56 shot images exist and are valid (non-zero size)
- [ ] Image dimensions are at least 1280x720 (upscaled if needed)
- [ ] Audio files match expected naming convention
- [ ] `ffmpeg` and `ffprobe` are available on PATH
- [ ] Sufficient disk space for intermediates (~2GB recommended)

### Post-Assembly Checks

- [ ] Output resolution is exactly 1920x1080
- [ ] Output frame rate is 24 fps
- [ ] Video codec is H.264 high profile
- [ ] Audio codec is AAC at 192k
- [ ] No audio drift (sync check at scene boundaries)
- [ ] Total duration matches expected sum (accounting for crossfades)
- [ ] File plays correctly in VLC and browser (faststart enabled)
- [ ] No black frames between segments (crossfades are clean)

### Review Checklist

1. **Watch full episode** at 1x speed -- note any pacing issues
2. **Spot-check audio sync** at scene transitions (scenes 1, 10, 11, 13, 14)
3. **Verify title card** is readable and holds for full 4 seconds
4. **Verify end card** is readable and holds for full 5 seconds
5. **Check crossfades** -- all transitions should be smooth 0.3s fades
6. **Verify no orphaned audio** -- all dialogue lines should be audible
7. **Export metadata** -- confirm episode title is embedded in MP4 metadata

---

## Revision Workflow

1. Identify issue (pacing, sync, missing shot, etc.)
2. Fix source asset or adjust duration in assembly script
3. Re-run `assemble_EP01.sh` -- script is idempotent, overwrites previous output
4. Re-verify against quality gates
5. Final review at 1x speed before publishing
