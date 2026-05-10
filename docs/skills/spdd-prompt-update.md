# spdd-prompt-update

`spdd-prompt-update` updates an existing prompt artifact after requirements, design assumptions, or architecture constraints have changed.

## Quick start

```text
Use the spdd-prompt-update skill on @spdd/prompt/PROMPT-001.md.
```

Include a description of what changed in the request.

## Use it when

- the prompt still exists but the problem definition changed
- you want to preserve the existing prompt structure instead of regenerating from scratch
- requirement or design constraints shifted after the prompt was originally written

## Output

This phase produces:

- an updated prompt under `spdd/prompt/`
- a phase result block recommending `spdd-generate` as the next phase

## Role in the workflow

```
(requirement changes)
  └─ spdd-prompt-update → spdd/prompt/ → spdd-generate
```

::: tip Business intent changed first?
Use `spdd-prompt-update` when the change originated in requirements or design. If instead the implementation changed first (refactor, drift), use `spdd-sync` instead.
:::

::: info Review gate
In `semi-auto` mode, the orchestrator stops after `spdd-prompt-update` for review before continuing to `spdd-generate`.
:::
