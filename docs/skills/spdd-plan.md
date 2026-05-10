# spdd-plan

`spdd-plan` is an explicit pre-story planning skill for broad initiatives, noisy PRDs, and mixed business context that still needs roadmap slicing before story generation.

## Quick start

```text
Use the spdd-plan skill on @roadmap-brief.md.
```

## Use it when

- the input spans multiple capabilities, dependency chains, or rollout phases
- you need ordered delivery slices before writing stories
- you want a durable planning artifact under `spdd/plan/`
- you need the skill to decide between planning, redirecting, or reusing an existing repository path

## Do not use it when

::: warning Skip spdd-plan if
- The request is already a coherent implementation story — use `spdd-story` directly.
- The requirement is already focused enough for `spdd-analysis`.
- The capability already exists and the right move is reuse instead of replanning.
:::

## Output

This skill produces:

- a planning artifact under `spdd/plan/`
- ordered delivery slices with dependency notes and sequencing rationale
- exactly one recommended next slice for `spdd-story`
- a completion block that reports consumed inputs, the produced plan path, the next command shape, and any material validation notes

## Where it fits

```
spdd-plan → spdd-story → spdd-analysis → spdd-reasons-canvas → spdd-generate
```

::: info Relationship to the orchestrator
`spdd-plan` is explicitly invoked and optional. It exists before `spdd-story` in the conceptual sequence, but it does not replace `spdd-story` or alter the orchestrator's current automatic start-phase detection.
:::
