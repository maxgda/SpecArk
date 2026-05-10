# spdd-api-test

`spdd-api-test` generates or updates API-oriented verification artifacts from prompts or implemented behavior.

## Quick start

```text
Use the spdd-api-test skill on @spdd/prompt/PROMPT-001.md.
```

## Use it when

- the generated change affects API behavior
- you want reusable verification assets after implementation
- the workflow should end with explicit API-oriented checks

## Output

This phase produces:

- changed verification assets under `spdd/tests/`
- a phase result block recommending completion

## Role in the workflow

```
spdd-generate → spdd-api-test (optional) → done
```

::: info Optional phase
This phase is optional. Use it when the implementation warrants API-focused verification. It is not a general test generation skill — it is focused specifically on API-oriented verification assets.
:::

::: tip When to skip it
For changes that do not involve API contracts, endpoints, or API-level behavior, `spdd-api-test` is not the right tool. Use the project's own test infrastructure instead.
:::
