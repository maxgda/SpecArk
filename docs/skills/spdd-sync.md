# spdd-sync

`spdd-sync` writes implementation reality back into an existing prompt artifact.

## Quick start

```text
Use the spdd-sync skill on @spdd/prompt/PROMPT-001.md.
```

## Use it when

- code changed first (refactor, rearchitecture, or drift)
- the prompt is now stale relative to the implementation
- a refactor needs to be reflected in the structured prompt before the next feature cycle

## Output

This phase produces:

- an updated prompt under `spdd/prompt/`
- a phase result block recommending completion

## Role in the workflow

```
(implementation changed)
  └─ spdd-sync → spdd/prompt/ (updated to match reality)
```

::: tip Implementation changed first?
Use `spdd-sync` when the code changed and the prompt needs to catch up. If requirements or design changed first, use `spdd-prompt-update` instead.
:::

::: info Keeping prompt and code in sync
Letting the prompt drift means future phases lose the accumulated design rationale. Running `spdd-sync` after significant refactors keeps the prompt usable as the source of intent for the next cycle.
:::
