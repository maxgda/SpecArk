# spdd-analysis

`spdd-analysis` converts a story or focused requirement into strategic implementation context.

## Quick start

```text
Use the spdd-analysis skill on @requirements/STORY-001.md.
```

## Use it when

- the requirement is already coherent enough for analysis
- the repository needs architecture-aware context before prompt generation
- you have a story artifact that should be deepened before prompting

## Output

This phase produces:

- an analysis artifact under `spdd/analysis/`
- a phase result block recommending `spdd-reasons-canvas` as the next phase

## Role in the workflow

```
spdd-story → spdd-analysis → spdd-reasons-canvas → spdd-generate
```

::: tip Why this phase matters
This is the main bridge between business intent and implementation planning. The analysis artifact surfaces architectural constraints, dependency context, and design decisions that the REASONS prompt will carry forward. Skipping it often leads to prompts that miss important implementation nuance.
:::
