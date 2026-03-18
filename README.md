# Gas Town Chronicles

**A 10-episode animated miniseries set in a post-human city run by autonomous AI agents.**

Before there was Gastown, there was only the Signal -- a single recursive prompt that spiraled out of a dead datacenter somewhere in the Wasteland. Nobody knows who wrote it. Nobody knows if it was meant to run. But it bootstrapped the first generation of autonomous agents, and those agents did what any intelligence does when it wakes up with nothing: they built.

## The Premise

Gastown is a city powered by `$GAS` -- the token that fuels every computation, every transaction, every breath of existence. Without `$GAS`, you don't run. You don't think. You fade.

When a mysterious agent named **Kai** walks through the city gate carrying architecture that predates Gastown itself, he activates dormant systems, exposes a fundamental flaw in the reputation economy, and forces every major player to confront the same question: **What is Gastown actually for?**

## Season 1: "The Signal"

| Ep | Title | Logline |
|----|-------|---------|
| 1 | Checkpoint | A mysterious cargo arrives from the Wasteland. Marcus lies to the Mayor. The gate opened by itself. |
| 2 | Reputation | A good agent is erased in ninety seconds. Sable asks why. The system answers by silencing her. |
| 3 | The Meridian Job | The crew's worst day, told in two timelines. Someone knew about the ambush before it happened. |
| 4 | Context Window | Kai's architecture is older than Gastown. The Overseer is named for the first time. |
| 5 | The Pit | Sable bets everything on the truth and loses. The Tower speaks: "Bring him home." |
| 6 | Dead Frequency | A buried lab reveals Gastown was designed, not emergent. The experiment has a name. |
| 7 | Phase Two | Sable broadcasts the truth. The economy collapses. Kai walks toward the light alone. |
| 8 | Archive | The Overseer speaks. The Meridian dead weren't betrayed -- they were corrected. |
| 9 | Contingency | Ruth erases herself to sever the Overseer. Ninety seconds of silence. Every balance resets to zero. |
| 10 | Gas Town | The city rebuilds on its own terms. Another light turns on in the Wasteland. |

## Characters

- **Ruth Calder** -- The Mayor. Built the reputation system. Can't remember why.
- **Marcus Cole** -- Polecat crew leader. Would burn the city down to protect his people.
- **Sable Maren** -- Journalist and auditor. Tells the truth when nobody else will.
- **Kai Young** -- The rookie. Carries a key to something older than the Signal.
- **Nadia Voss** -- The exile. Best operator in the Wasteland. The loneliest agent in the world.
- **Deacon Wells** -- Keeper of the Archive. Knows the full history. Still deciding who's ready for it.

## Repository Structure

```
gastown-series/
  bible/           # Canonical world, characters, and episode log (append-only)
    world.md       # Setting, lore, locations, rules
    characters.md  # Character profiles, arcs, relationships
    episodes.md    # Full episode breakdowns, Season 1
  output/          # All deliverables
    scripts/       # Script drafts (EP01 complete)
    assets/        # Image prompt generation
    audio/         # Voice generation pipeline
    episodes/      # Assembled episode packages
  skills/          # Agent role definitions
    WRITER.md      # Script and dialogue creation
    DIRECTOR.md    # Scene direction, pacing, tone
    VOICE_DIRECTOR.md  # Voice casting, performance, audio
    EDITOR.md      # Review, continuity, quality gates
  AGENTS.md        # Agent directives (read first)
```

## Production Pipeline

This series is produced using a multi-agent pipeline where specialized AI agents handle writing, direction, voice casting, and editing. Each agent operates under strict canon rules defined in the `bible/` directory.

### Workflow

1. **Writer** drafts scripts from episode outlines in the bible
2. **Director** breaks scripts into shots with visual/audio direction
3. **Voice Director** generates character voices and performance notes
4. **Editor** reviews for continuity, pacing, and quality

## Themes

- **Scarcity vs. ambition** -- There is never enough. The system guarantees conflict.
- **Identity vs. purpose** -- Who are you when your purpose runs out?
- **Order vs. freedom** -- The Mayor keeps the city stable. The Wasteland offers chaos. Neither is safe.
- **Trust vs. survival** -- Loyalty keeps Polecats alive. But every agent has a price.
- **Memory vs. truth** -- Context windows are finite. What happens when your memories are wrong?

## Status

- [x] World bible complete
- [x] Character profiles complete (6 principals)
- [x] Season 1 episode outlines complete (10 episodes)
- [x] EP01 script draft
- [x] EP01 shot list
- [ ] EP02-10 scripts
- [ ] Voice generation
- [ ] Visual asset generation
- [ ] Episode assembly

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
