# spdd-discovery

`spdd-discovery` is a Discovery Interview for early, unclear, or noisy product context. It turns rough ideas, mixed notes, pasted context, and referenced repository files into a durable Discovery Brief before planning, story splitting, or technical analysis begins.

## Quick start

::: code-group

```text [Codex]
Use the spdd-discovery skill on @idea-notes.md.
```

```text [Claude Code]
/specark:spdd-discovery @idea-notes.md
```

:::

You can also invoke it with rough text:

```text
Use the spdd-discovery skill. We need to improve onboarding, but the user problem and scope are still fuzzy.
```

## Use it when

- you have a vague idea that is not ready for story splitting
- your input mixes notes, repository references, and unresolved product context
- the product direction is early and needs a clearer problem frame
- scope boundaries are missing or contested
- you need pre-planning clarification before `spdd-plan`, `spdd-story`, or `spdd-analysis`

## Do not use it when

- you already have a focused story ready for `spdd-analysis`
- you already have an analysis artifact in `spdd/analysis/`
- you need to update an existing prompt
- you need to sync code changes back into a prompt
- you are ready for implementation from `spdd/prompt/`

## Output

Completed runs write exactly one Discovery Brief under `spdd/discovery/` and end with a `SPDD_DISCOVERY_RESULT` block. The result recommends exactly one next phase from `spdd-plan`, `spdd-story`, or `spdd-analysis`.

Blocked runs do not write an artifact. They report `output_files: none` and `recommended_next_phase: none`.

## Workflow placement

```text
spdd-discovery  (optional, manual)
  ├─ spdd-plan       when the brief still needs roadmap slicing
  ├─ spdd-story      when the brief is ready for story creation
  └─ spdd-analysis   when the brief is already focused enough for analysis
```

::: info Manual invocation
`spdd-discovery` is manually invoked in this release. Automatic orchestrator discovery support is a separate follow-up, so the orchestrator does not route into discovery by default.
:::
