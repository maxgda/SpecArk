# Contributing

SpecArk is small enough that clarity matters more than process overhead.

## Repository principles

- keep phase skills lean when the canonical source command already defines the behavior
- make controller skills richer when they coordinate multiple phases or review gates
- preserve file-backed workflow contracts
- prefer references and scripts over duplicating large procedural text in many places

## When changing skills

1. Update `SKILL.md`.
2. Update `agents/openai.yaml` when user-facing labels or prompts drift.
3. Update or add reference files when a rule should be shared across skills.
4. Re-run the plugin validator.
5. Update docs when behavior visible to users changed.

## When changing docs

This docs site is VitePress-based and lives under `docs/`.

Use:

```bash
npm install
npm run docs:build
npm run docs:preview
```

## Good contribution targets

- clearer skill boundaries
- stronger validation contracts
- better examples for orchestrator routing
- improved documentation for installation and workflow behavior
