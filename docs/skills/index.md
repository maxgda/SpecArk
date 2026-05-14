# Skill Index

SpecArk exposes one controller skill, one optional planning skill, seven phase skills, two maintenance skills, and one pre-flight utility. Each skill is configured for explicit invocation — you name the skill you want, and it runs that phase only.

## Controller

### [spdd-orchestrator](/skills/spdd-orchestrator)

Coordinates the workflow end to end. Detects the right starting phase, invokes phase skills in sequence, enforces review gates, and reports artifact lineage.

::: tip Use this for a guided first run
The orchestrator in `semi-auto` mode is the recommended starting point for new users. It handles phase selection and pauses at each review gate.
:::

## Planning

### [spdd-plan](/skills/spdd-plan)

Turns broad or noisy product direction into ordered delivery slices before story generation begins. Produces a durable planning artifact under `spdd/plan/`.

Use it when the input still spans multiple capabilities, dependency chains, or rollout phases.

## Phase skills

| Skill | Input | Output location | Use when |
|---|---|---|---|
| [spdd-story](/skills/spdd-story) | Broad requirement or idea | `requirements/` | Requirement is too broad for direct analysis |
| [spdd-analysis](/skills/spdd-analysis) | Story or focused requirement | `spdd/analysis/` | Need architecture-aware context before prompting |
| [spdd-reasons-canvas](/skills/spdd-reasons-canvas) | Analysis artifact | `spdd/prompt/` | Ready to produce the implementation prompt |
| [spdd-generate](/skills/spdd-generate) | Prompt artifact | implementation files | Ready to implement from the prompt |
| [spdd-prompt-update](/skills/spdd-prompt-update) | Existing prompt + change description | `spdd/prompt/` | Requirements or design changed after prompting |
| [spdd-sync](/skills/spdd-sync) | Prompt artifact + implementation | `spdd/prompt/` | Implementation drifted from the prompt |
| [spdd-api-test](/skills/spdd-api-test) | Implementation files or prompt | `spdd/tests/` | API-oriented verification assets are needed |

## Maintenance skills

| Skill | Input | Output location | Use when |
|---|---|---|---|
| [spdd-doc-sync](/skills/spdd-doc-sync) | Change description or `@` reference | `docs/`, `README.md`, `CHANGELOG.md`, `plugins/specark/CLAUDE.md` | In-repo docs need updating after a skill addition, behavior change, or workflow update |

## Pre-flight utility

### [spdd-session-health](/skills/spdd-session-health)

Assesses whether the current session is in good shape before committing to a phase invocation. Checks for prior phase completions, context spinning, instruction reversals, and input load. Produces a `SPDD_HEALTH_RESULT` block — not a repository artifact.

The orchestrator runs this automatically before the first phase when multiple inputs are detected or a prior phase already completed in the session. You can also invoke it directly before any heavy phase.

## Invocation model

Each skill is configured for explicit invocation. This keeps the workflow command-like and reduces accidental routing.

::: info How to invoke a skill
Reference the skill by name in your Codex request:
```text
Use the spdd-analysis skill on @requirements/STORY-001.md.
```
:::
