#!/usr/bin/env bash
set -euo pipefail

# =============================================================================
# Gas Town Chronicles -- Parameterized Video Assembly Script
# Assembles still images + voice audio into a final MP4 using FFmpeg.
# Reads shot durations and scene assignments dynamically from shots.md.
# =============================================================================

# ---- Usage ------------------------------------------------------------------
if [[ $# -lt 1 ]]; then
  echo "Usage: ./assemble.sh <episode_number>"
  echo "Example: ./assemble.sh 2"
  echo "         ./assemble.sh 10"
  exit 1
fi

# ---- Normalize episode number to zero-padded format -------------------------
RAW_EP="$1"
EP_NUM=$(printf "%d" "$RAW_EP" 2>/dev/null) || {
  echo "ERROR: '$RAW_EP' is not a valid episode number" >&2
  exit 1
}
EP_PAD=$(printf "%02d" "$EP_NUM")
EP_TAG="EP${EP_PAD}"

echo "=== Assembling ${EP_TAG} ==="
echo ""

# ---- Paths ------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS_DIR="${SCRIPT_DIR}/assets/${EP_TAG}"
AUDIO_DIR="${SCRIPT_DIR}/audio/${EP_TAG}"
JSON_FILE="${SCRIPT_DIR}/assets/${EP_TAG}_image_prompts.json"
SHOTS_FILE="${SCRIPT_DIR}/scripts/${EP_TAG}_shots.md"
TMP_DIR="${SCRIPT_DIR}/.tmp_${EP_TAG}"
OUTPUT="${SCRIPT_DIR}/${EP_TAG}_final.mp4"

# ---- Video specs ------------------------------------------------------------
RESOLUTION="1920:1080"
FPS=24
CRF=18
CROSSFADE=0.3
TITLE_DUR=4
END_DUR=5

# =============================================================================
# Parse shots.md for durations, scene assignments, and episode title
# =============================================================================

if [[ ! -f "$SHOTS_FILE" ]]; then
  echo "ERROR: Shots file not found: $SHOTS_FILE" >&2
  exit 1
fi

echo "=== Parsing shot data from $SHOTS_FILE ==="

# Extract episode title from first line:
#   # GAS TOWN CHRONICLES — Episode N: "Title"
EP_TITLE=$(head -1 "$SHOTS_FILE" | sed -n 's/^# GAS TOWN CHRONICLES.*Episode [0-9]*: *"\?\([^"]*\)"\?$/\1/p')
if [[ -z "$EP_TITLE" ]]; then
  EP_TITLE="Episode ${EP_NUM}"
  echo "  WARNING: Could not parse title from shots.md header; using fallback: $EP_TITLE"
else
  echo "  Episode title: $EP_TITLE"
fi

# Parse scene headers, shot numbers, and durations
declare -a SHOT_DURATIONS=()
declare -a SHOT_SCENES=()
declare -A SHOT_DUR_MAP=()
declare -A SHOT_SCENE_MAP=()

current_scene=0
current_shot=0

while IFS= read -r line; do
  # Match scene headers: ## SCENE N — ...
  if [[ "$line" =~ ^##\ SCENE\ ([0-9]+) ]]; then
    current_scene="${BASH_REMATCH[1]}"
    continue
  fi

  # Match shot headers: ### Shot N — ...
  if [[ "$line" =~ ^###\ Shot\ ([0-9]+) ]]; then
    current_shot="${BASH_REMATCH[1]}"
    continue
  fi

  # Match duration lines: - **Duration:** N sec
  if [[ "$line" =~ \*\*Duration:\*\*\ ([0-9]+)\ sec ]]; then
    dur="${BASH_REMATCH[1]}"
    if [[ $current_shot -gt 0 && $current_scene -gt 0 ]]; then
      SHOT_DUR_MAP[$current_shot]="$dur"
      SHOT_SCENE_MAP[$current_shot]="$current_scene"
    fi
    continue
  fi
done < "$SHOTS_FILE"

# Build ordered arrays from the maps
NUM_SHOTS=${#SHOT_DUR_MAP[@]}
if [[ $NUM_SHOTS -eq 0 ]]; then
  echo "ERROR: No shots parsed from $SHOTS_FILE" >&2
  exit 1
fi

# Find the max scene number for later audio scanning
max_scene=0
for i in $(seq 1 $NUM_SHOTS); do
  if [[ -z "${SHOT_DUR_MAP[$i]:-}" ]]; then
    echo "ERROR: Missing data for shot $i in $SHOTS_FILE" >&2
    exit 1
  fi
  SHOT_DURATIONS+=("${SHOT_DUR_MAP[$i]}")
  SHOT_SCENES+=("${SHOT_SCENE_MAP[$i]}")
  if [[ ${SHOT_SCENE_MAP[$i]} -gt $max_scene ]]; then
    max_scene=${SHOT_SCENE_MAP[$i]}
  fi
done

echo "  Parsed $NUM_SHOTS shots across $max_scene scenes"
echo ""

# =============================================================================
# Phase 1: Validate inputs
# =============================================================================

echo "=== Phase 1: Validating inputs ==="

# Check tools
for cmd in ffmpeg ffprobe python3; do
  if ! command -v "$cmd" &>/dev/null; then
    echo "ERROR: $cmd not found on PATH" >&2
    exit 1
  fi
done

# Check JSON
if [[ ! -f "$JSON_FILE" ]]; then
  echo "WARNING: Image prompts not found: $JSON_FILE (continuing without)"
fi

# Check images exist (try png, jpg, webp)
missing_images=0
declare -a IMAGE_FILES
for i in $(seq 1 $NUM_SHOTS); do
  shot_num=$(printf "%02d" "$i")
  found=""
  for ext in png jpg jpeg webp; do
    candidate="${ASSETS_DIR}/${EP_TAG}_SHOT_${shot_num}.${ext}"
    if [[ -f "$candidate" ]]; then
      found="$candidate"
      break
    fi
  done
  if [[ -z "$found" ]]; then
    echo "WARNING: Missing image for shot $shot_num" >&2
    missing_images=$((missing_images + 1))
    IMAGE_FILES+=("")
  else
    IMAGE_FILES+=("$found")
  fi
done

if [[ $missing_images -gt 0 ]]; then
  echo "WARNING: $missing_images shot image(s) missing. Missing shots will use black frames."
fi

# Scan audio directory
if [[ -d "$AUDIO_DIR" ]]; then
  audio_count=$(find "$AUDIO_DIR" -name "${EP_TAG}_S*.mp3" -type f | wc -l)
  echo "Found $audio_count audio files in $AUDIO_DIR"
else
  echo "WARNING: Audio directory not found: $AUDIO_DIR (all shots will be silent)"
  audio_count=0
fi

echo "Validation complete."
echo ""

# =============================================================================
# Phase 2: Generate title card and end card
# =============================================================================

echo "=== Phase 2: Generating title and end cards ==="

mkdir -p "$TMP_DIR"

# Find a usable font
FONT=""
for f in \
  /usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf \
  /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf \
  /usr/share/fonts/TTF/DejaVuSans-Bold.ttf \
  /usr/share/fonts/truetype/freefont/FreeSansBold.ttf; do
  if [[ -f "$f" ]]; then
    FONT="$f"
    break
  fi
done

FONT_REGULAR=""
for f in \
  /usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf \
  /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf \
  /usr/share/fonts/TTF/DejaVuSans.ttf \
  /usr/share/fonts/truetype/freefont/FreeSans.ttf; do
  if [[ -f "$f" ]]; then
    FONT_REGULAR="$f"
    break
  fi
done

# Title card: "GAS TOWN CHRONICLES" / "Episode N: Title"
# Escape colons for FFmpeg drawtext
ep_subtitle="Episode ${EP_NUM}\\: ${EP_TITLE}"
title_drawtext="drawtext=text='GAS TOWN CHRONICLES':fontsize=72:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-50"
if [[ -n "$FONT" ]]; then
  title_drawtext+=":fontfile='${FONT}'"
fi
title_drawtext+=",drawtext=text='${ep_subtitle}':fontsize=36:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2+40"
if [[ -n "$FONT_REGULAR" ]]; then
  title_drawtext+=":fontfile='${FONT_REGULAR}'"
fi

ffmpeg -y -loglevel warning \
  -f lavfi -i "color=c=black:s=${RESOLUTION/:/x}:d=${TITLE_DUR}:r=${FPS}" \
  -vf "$title_drawtext" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -crf "$CRF" \
  -an "${TMP_DIR}/title_card.mp4"
echo "  Title card: ${TMP_DIR}/title_card.mp4"

# End card
end_drawtext="drawtext=text='New episodes every week':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-30"
if [[ -n "$FONT" ]]; then
  end_drawtext+=":fontfile='${FONT}'"
fi
end_drawtext+=",drawtext=text='Subscribe':fontsize=36:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2+30"
if [[ -n "$FONT_REGULAR" ]]; then
  end_drawtext+=":fontfile='${FONT_REGULAR}'"
fi

ffmpeg -y -loglevel warning \
  -f lavfi -i "color=c=black:s=${RESOLUTION/:/x}:d=${END_DUR}:r=${FPS}" \
  -vf "$end_drawtext" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -crf "$CRF" \
  -an "${TMP_DIR}/end_card.mp4"
echo "  End card: ${TMP_DIR}/end_card.mp4"

echo ""

# =============================================================================
# Phase 3: Build per-shot video segments
# =============================================================================

echo "=== Phase 3: Building per-shot segments ==="

# Build audio mapping: for each scene, collect audio files in sorted order
declare -A SCENE_AUDIO_FILES  # scene_num -> space-separated list of audio files
if [[ -d "$AUDIO_DIR" ]]; then
  for scene_num in $(seq 1 $max_scene); do
    scene_pad=$(printf "%02d" "$scene_num")
    files=$(find "$AUDIO_DIR" -name "${EP_TAG}_S${scene_pad}__*.mp3" -type f 2>/dev/null | sort || true)
    SCENE_AUDIO_FILES[$scene_num]="$files"
  done
fi

# Track which audio files have been assigned per scene
declare -A SCENE_AUDIO_INDEX  # scene_num -> next index to assign
for scene_num in $(seq 1 $max_scene); do
  SCENE_AUDIO_INDEX[$scene_num]=0
done

# Helper: get audio duration via ffprobe
get_audio_duration() {
  ffprobe -v error -show_entries format=duration \
    -of default=noprint_wrappers=1:nokey=1 "$1" 2>/dev/null || echo "0"
}

# Helper: get the next unassigned audio file for a scene
get_next_audio() {
  local scene=$1
  local files="${SCENE_AUDIO_FILES[$scene]:-}"
  local idx="${SCENE_AUDIO_INDEX[$scene]:-0}"

  if [[ -z "$files" ]]; then
    echo ""
    return
  fi

  # Convert to array
  local -a file_arr
  mapfile -t file_arr <<< "$files"

  if [[ $idx -lt ${#file_arr[@]} && -n "${file_arr[$idx]}" ]]; then
    echo "${file_arr[$idx]}"
    SCENE_AUDIO_INDEX[$scene]=$((idx + 1))
  else
    echo ""
  fi
}

VF_SCALE="scale=${RESOLUTION}:force_original_aspect_ratio=decrease,pad=${RESOLUTION}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1"

declare -a SEGMENT_FILES
declare -a SEGMENT_DURATIONS

for i in $(seq 1 $NUM_SHOTS); do
  idx=$((i - 1))
  shot_num=$(printf "%02d" "$i")
  seg_file="${TMP_DIR}/seg_${shot_num}.mp4"
  shot_dur="${SHOT_DURATIONS[$idx]}"
  scene="${SHOT_SCENES[$idx]}"

  image="${IMAGE_FILES[$idx]}"

  # Try to get audio for this shot
  audio_file=$(get_next_audio "$scene")

  if [[ -n "$image" && -f "$image" ]]; then
    if [[ -n "$audio_file" && -f "$audio_file" ]]; then
      # Image + audio segment
      audio_dur=$(get_audio_duration "$audio_file")
      # Use the longer of audio duration or shot duration (min 2s)
      seg_dur=$(python3 -c "print(max(float('${audio_dur}'), float('${shot_dur}'), 2.0))")

      ffmpeg -y -loglevel warning \
        -loop 1 -i "$image" -i "$audio_file" \
        -t "$seg_dur" \
        -vf "$VF_SCALE" \
        -c:v libx264 -profile:v high -pix_fmt yuv420p -r "$FPS" -crf "$CRF" \
        -c:a aac -b:a 192k -ar 44100 \
        -shortest "$seg_file"
      echo "  Shot $shot_num (scene $scene): ${seg_dur}s [with audio: $(basename "$audio_file")]"
    else
      # Image only, no audio
      ffmpeg -y -loglevel warning \
        -loop 1 -i "$image" \
        -t "$shot_dur" \
        -vf "$VF_SCALE" \
        -c:v libx264 -profile:v high -pix_fmt yuv420p -r "$FPS" -crf "$CRF" \
        -an "$seg_file"
      seg_dur="$shot_dur"
      echo "  Shot $shot_num (scene $scene): ${seg_dur}s [silent]"
    fi
  else
    # Missing image: generate black frame
    ffmpeg -y -loglevel warning \
      -f lavfi -i "color=c=black:s=${RESOLUTION/:/x}:d=${shot_dur}:r=${FPS}" \
      -c:v libx264 -profile:v high -pix_fmt yuv420p -crf "$CRF" \
      -an "$seg_file"
    seg_dur="$shot_dur"
    echo "  Shot $shot_num (scene $scene): ${seg_dur}s [BLACK - missing image]"
  fi

  SEGMENT_FILES+=("$seg_file")
  SEGMENT_DURATIONS+=("$seg_dur")
done

echo ""

# =============================================================================
# Phase 4: Concatenate all segments with xfade crossfades
# =============================================================================

echo "=== Phase 4: Building final video with crossfades ==="

# Full segment list: title + shots + end card
ALL_SEGMENTS=("${TMP_DIR}/title_card.mp4")
ALL_DURATIONS=("$TITLE_DUR")
for i in $(seq 0 $((NUM_SHOTS - 1))); do
  ALL_SEGMENTS+=("${SEGMENT_FILES[$i]}")
  ALL_DURATIONS+=("${SEGMENT_DURATIONS[$i]}")
done
ALL_SEGMENTS+=("${TMP_DIR}/end_card.mp4")
ALL_DURATIONS+=("$END_DUR")

total_segs=${#ALL_SEGMENTS[@]}

# Build ffmpeg inputs
inputs=""
for seg in "${ALL_SEGMENTS[@]}"; do
  inputs+=" -i $seg"
done

# Build xfade filter chain
filter=""
offset=0
prev_label="0:v"

for i in $(seq 1 $((total_segs - 1))); do
  # Offset = cumulative duration of all previous segments minus cumulative crossfades
  dur_prev="${ALL_DURATIONS[$((i - 1))]}"
  offset=$(python3 -c "print(round(${offset} + float('${dur_prev}') - ${CROSSFADE}, 4))")

  out_label="v${i}"
  if [[ $i -eq $((total_segs - 1)) ]]; then
    out_label="vout"
  fi

  filter+="[${prev_label}][${i}:v]xfade=transition=fade:duration=${CROSSFADE}:offset=${offset}[${out_label}];"
  prev_label="$out_label"
done

# Remove trailing semicolon
filter="${filter%;}"

echo "  Building xfade filter with $((total_segs - 1)) transitions..."

# First pass: video only with xfade
ffmpeg -y -loglevel warning \
  $inputs \
  -filter_complex "$filter" \
  -map "[vout]" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -r "$FPS" -crf "$CRF" \
  -an "${TMP_DIR}/video_xfade.mp4"
echo "  Video assembled: ${TMP_DIR}/video_xfade.mp4"

# Second pass: extract and concatenate audio from segments that have it
concat_list="${TMP_DIR}/audio_concat.txt"
> "$concat_list"
for seg in "${ALL_SEGMENTS[@]}"; do
  # Check if segment has audio
  has_audio=$(ffprobe -v error -select_streams a -show_entries stream=codec_type \
    -of csv=p=0 "$seg" 2>/dev/null || true)
  if [[ -n "$has_audio" ]]; then
    echo "file '${seg}'" >> "$concat_list"
  fi
done

audio_line_count=$(wc -l < "$concat_list")

# =============================================================================
# Phase 5: Final mux and export
# =============================================================================

echo ""
echo "=== Phase 5: Final export ==="

METADATA_TITLE="Gas Town Chronicles - Episode ${EP_NUM}: ${EP_TITLE}"

if [[ $audio_line_count -gt 0 ]]; then
  # Concat audio from segments
  ffmpeg -y -loglevel warning \
    -f concat -safe 0 -i "$concat_list" \
    -c:a aac -b:a 192k -ar 44100 \
    "${TMP_DIR}/audio_concat.m4a"

  # Mux video + audio
  ffmpeg -y -loglevel warning \
    -i "${TMP_DIR}/video_xfade.mp4" \
    -i "${TMP_DIR}/audio_concat.m4a" \
    -c:v copy -c:a copy \
    -movflags +faststart \
    -metadata title="$METADATA_TITLE" \
    "$OUTPUT"
  echo "  Final video with audio: $OUTPUT"
else
  # No audio, just copy video
  ffmpeg -y -loglevel warning \
    -i "${TMP_DIR}/video_xfade.mp4" \
    -c:v copy \
    -movflags +faststart \
    -metadata title="$METADATA_TITLE" \
    "$OUTPUT"
  echo "  Final video (silent): $OUTPUT"
fi

# Report
final_dur=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "$OUTPUT" 2>/dev/null || echo "unknown")
final_size=$(du -h "$OUTPUT" 2>/dev/null | cut -f1 || echo "unknown")

echo ""
echo "=== Assembly Complete ==="
echo "  Output:   $OUTPUT"
echo "  Duration: ${final_dur}s"
echo "  Size:     $final_size"
echo ""
echo "  To clean up temp files: rm -rf $TMP_DIR"
