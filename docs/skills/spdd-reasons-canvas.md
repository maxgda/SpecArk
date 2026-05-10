# spdd-reasons-canvas

`spdd-reasons-canvas` transforms an analysis artifact into a structured, implementation-ready prompt.

## Quick start

```text
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
```

## Use it when

- analysis is complete enough to produce an implementation-ready prompt
- the next step should be code generation rather than more exploration

## Output

This phase produces:

- a prompt artifact under `spdd/prompt/`
- a phase result block recommending `spdd-generate` as the next phase

## Role in the workflow

```
spdd-analysis → spdd-reasons-canvas → spdd-generate
```

::: info REASONS Canvas
This skill relies on the REASONS Canvas methodology and shared conventions stored in the plugin references. See [REASONS Canvas Notes](/references/reasons-canvas) for terminology details.
:::

::: tip Good signal
After this phase runs, the prompt artifact in `spdd/prompt/` should contain enough structured context that `spdd-generate` can implement the feature without needing additional business context from chat.
:::
