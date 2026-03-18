# Contributing to Gas Town Chronicles

Thank you for your interest in contributing to the Gastown series.

## How to Contribute

### Creative Contributions

- **Scripts**: Draft scripts for unwritten episodes following the style established in `output/scripts/EP01_script.md`
- **World-building**: Propose additions to the bible (locations, lore, factions) via pull request
- **Character development**: Suggest character arcs, dialogue samples, or backstory expansions
- **Visual concepts**: Contribute concept art, mood boards, or visual reference material

### Technical Contributions

- **Voice pipeline**: Improve `output/audio/generate_voices.py`
- **Asset generation**: Enhance `output/assets/generate_prompts.py`
- **Assembly pipeline**: Improve `output/assemble_EP01.sh`

## Rules

### The Bible is Append-Only

Files in `bible/` are canonical. When contributing:

- **Never delete or overwrite** existing bible content
- **Append** new entries at the end of the relevant section
- If a retcon is needed, add a clearly marked revision note -- do not remove the original

### Canon Consistency

All contributions must be consistent with the established bible:

- `bible/world.md` -- Setting, locations, rules, economy
- `bible/characters.md` -- Character profiles, arcs, relationships
- `bible/episodes.md` -- Episode outlines and continuity

Read these thoroughly before submitting creative work.

### Style Guide

- Scripts follow the format established in `output/scripts/EP01_script.md`
- Shot lists follow the format in `output/scripts/EP01_shots.md`
- Character dialogue must match established speech patterns in `bible/characters.md`

## Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/ep02-script`)
3. Read `AGENTS.md` for agent directives and `skills/` for role definitions
4. Review the bible for current canon
5. Make your changes
6. Submit a pull request with a clear description of what you've added

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

Open an issue for discussion before starting large contributions.
