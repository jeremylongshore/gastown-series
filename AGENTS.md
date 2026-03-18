# AGENTS.md — Gastown Series

## Agent Directives

All agents working in this repository must follow these rules without exception.

### 1. Read Skills Before Starting

Before beginning any task, read the relevant skill file(s) in `/skills/`:

- `WRITER.md` — Script and dialogue creation
- `DIRECTOR.md` — Scene direction, pacing, tone
- `VOICE_DIRECTOR.md` — Voice casting, performance notes, audio direction
- `EDITOR.md` — Review, continuity, quality gates

If your task spans multiple roles, read all applicable skill files first.

### 2. Track All Work as Beads

Every work session must be tracked using `bd`:

```bash
bd update <id> --status in_progress   # Before starting
# ... do the work ...
bd close <id> --reason "evidence"     # After completing
bd sync                               # Push state
```

No work happens without a bead. No bead closes without evidence.

### 3. Never Overwrite Bible Files

Files in `/bible/` are append-only:

- `world.md` — Setting, lore, locations, rules
- `characters.md` — Character profiles, arcs, relationships
- `episodes.md` — Episode log, synopses, continuity notes

When updating bible files, **append new entries** at the end of the relevant section. Never delete or rewrite existing content. If a retcon is needed, add a clearly marked revision note — do not remove the original.

### 4. Log Completed Work to /output

All deliverables go in `/output/` with episode number and timestamp:

```
/output/scripts/E01_cold-open_2026-03-04T1430.md
/output/assets/E01_character-sheet-kai_2026-03-04T1500.md
/output/episodes/E01_full-assembly_2026-03-04T1600.md
```

Format: `E{NN}_{description}_{YYYY-MM-DDTHHmm}.{ext}`

Every output file must include a header noting which agent produced it and the bead ID that tracked the work.
