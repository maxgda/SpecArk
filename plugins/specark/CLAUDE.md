# SpecArk — Claude Code Plugin

SpecArk brings Structured Prompt-Driven Development (SPDD) to Claude Code. It turns broad feature requests into artifact-driven workflows with explicit handoffs between phases.

## Skills

All skills live under `plugins/specark/skills/`. Each skill has a `SKILL.md` that is the executable contract.

| Skill | Purpose |
|---|---|
| `spdd-orchestrator` | Coordinate the full workflow across phases with manual, semi-auto, auto, resume, and plan-only modes |
| `spdd-plan` | Turn broad product direction into ordered delivery slices before story generation |
| `spdd-story` | Decompose a broad requirement into INVEST-compliant, implementation-sized stories |
| `spdd-analysis` | Analyze a story against codebase context at a strategic level |
| `spdd-reasons-canvas` | Generate the implementation-ready REASONS Canvas prompt |
| `spdd-generate` | Implement code from the structured prompt |
| `spdd-prompt-update` | Update an existing prompt after requirement or design changes |
| `spdd-sync` | Sync implementation reality back into the prompt |
| `spdd-api-test` | Generate or refresh API-oriented verification assets |

## Skill files

```
plugins/specark/skills/
  spdd-orchestrator/SKILL.md
  spdd-plan/SKILL.md
  spdd-story/SKILL.md
  spdd-analysis/SKILL.md
  spdd-reasons-canvas/SKILL.md
  spdd-generate/SKILL.md
  spdd-prompt-update/SKILL.md
  spdd-sync/SKILL.md
  spdd-api-test/SKILL.md
```

## Invocation

Use skills explicitly by naming them in your request:

```text
Use the spdd-orchestrator skill on @idea.md in semi-auto mode.
Use the spdd-story skill on @requirements/brief.md.
Use the spdd-analysis skill on @requirements/STORY-001.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

## Normal workflow sequence

```
0. spdd-plan       (optional — for roadmap-sized input)
1. spdd-story      → requirements/STORY-NNN.md
2. spdd-analysis   → spdd/analysis/ANALYSIS-NNN.md
3. spdd-reasons-canvas → spdd/prompt/PROMPT-NNN.md
4. spdd-generate   → implementation files
5. spdd-api-test   → spdd/tests/ (optional)
```

## Supporting references

All canonical workflow text lives in `plugins/specark/references/source-commands/`. Skills reference these files directly — do not summarize or skip them.

- `references/source-commands/spdd-story.md`
- `references/source-commands/spdd-analysis.md`
- `references/source-commands/spdd-reasons-canvas.md`
- `references/source-commands/spdd-generate.md`
- `references/source-commands/spdd-prompt-update.md`
- `references/source-commands/spdd-sync.md`
- `references/source-commands/spdd-api-test.md`
- `references/orchestrator-contract.md`

## Helper scripts

```
plugins/specark/scripts/
  derive_spdd_filename.py      — generate SPDD-compliant artifact filenames
  next_story_number.py         — determine next story sequence number
  parse_reasons_sections.py    — parse REASONS Canvas sections
  discover_requirement_files.py — discover requirement markdown files
```

## Installation

See [docs/installation-claude-code.md](../../docs/installation-claude-code.md) for step-by-step setup.
