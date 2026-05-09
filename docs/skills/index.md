# Skill Index

SpecArk exposes one controller skill and seven phase skills.

## Controller

- [spdd-orchestrator](/skills/spdd-orchestrator) coordinates the workflow, chooses the start phase, enforces review gates, and reports artifact lineage.

## Phase skills

- [spdd-story](/skills/spdd-story) creates implementation-sized stories from broad requirements.
- [spdd-analysis](/skills/spdd-analysis) turns a story or focused requirement into strategic analysis.
- [spdd-reasons-canvas](/skills/spdd-reasons-canvas) turns analysis into an implementation-ready REASONS prompt.
- [spdd-generate](/skills/spdd-generate) implements from the prompt.
- [spdd-prompt-update](/skills/spdd-prompt-update) updates an existing prompt after requirement or design changes.
- [spdd-sync](/skills/spdd-sync) syncs implementation reality back into the prompt.
- [spdd-api-test](/skills/spdd-api-test) generates or updates API-oriented verification artifacts.

## Invocation model

Each skill is configured for explicit invocation. This keeps the workflow command-like and reduces accidental routing.
