# spdd-generate

`spdd-generate` implements code from a structured SPDD prompt artifact.

## Quick start

```text
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

## Use it when

- a valid prompt artifact already exists under `spdd/prompt/`
- implementation work should now follow the prompt rather than free-form design discussion

## Do not use it when

::: warning Requires a prompt artifact first
Do not invoke `spdd-generate` with only an idea, story, or analysis file. You need a prompt artifact in `spdd/prompt/` first. Run `spdd-reasons-canvas` to produce one.
:::

## Output

This phase produces:

- changed implementation files (project-specific paths)
- a phase result block recommending either `spdd-api-test` or completion

## Role in the workflow

```
spdd-reasons-canvas → spdd-generate → spdd-api-test (optional)
```

::: tip Prompt-first rule
If the generated code has an issue that stems from the prompt contract, fix the prompt first and regenerate. Patching generated code without updating the prompt creates drift that `spdd-sync` will need to clean up later.
:::
