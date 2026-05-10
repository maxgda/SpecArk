# spdd-story

`spdd-story` decomposes broad requirements, epics, or PRDs into implementation-sized story artifacts.

## Quick start

```text
Use the spdd-story skill on @idea.md.
```

## Use it when

- the requirement spans multiple user journeys
- the scope is too broad for direct analysis
- acceptance criteria are missing or under-specified
- you need an artifact under `requirements/` before technical analysis begins

## Do not use it when

::: info Skip spdd-story if
The requirement is already focused and coherent — jump directly to `spdd-analysis`.
:::

## Output

This phase produces:

- a story file under `requirements/`
- a phase result block recommending `spdd-analysis` as the next phase

## Role in the workflow

```
spdd-story → spdd-analysis → spdd-reasons-canvas → spdd-generate
```

This phase is optional. Use it when direct analysis would be too coarse or too expensive. If your input is already a well-defined story or requirement, start at `spdd-analysis` instead.
