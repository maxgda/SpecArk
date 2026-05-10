# Workflow Overview

SpecArk expresses SPDD as a sequence of explicit phases, with artifacts passed from one phase to the next.

## Standard sequence

The usual progression is:

0. optional `spdd-plan` when the input is still roadmap-sized and needs ordered delivery slices
1. `spdd-story` when a requirement is too broad and needs decomposition
2. `spdd-analysis` for strategic and architectural understanding
3. `spdd-reasons-canvas` to produce the implementation prompt
4. `spdd-generate` to implement from the prompt
5. `spdd-api-test` when API-oriented verification assets are needed

Additional maintenance phases:

- `spdd-prompt-update` when requirements or design constraints change
- `spdd-sync` when implementation reality needs to be written back into the prompt

## Artifact-driven handoff

Each phase should produce repository files that become the next phase’s inputs. The goal is to avoid re-sending the same business context through chat.

Typical artifact path progression:

```text
spdd/plan/PLAN-EXAMPLE.md
requirements/STORY-001-example.md
spdd/analysis/EXAMPLE.md
spdd/prompt/EXAMPLE.md
<implementation files>
spdd/tests/<verification assets>
```

`spdd-plan` is explicitly invoked and optional. The orchestrator still starts broad inputs at `spdd-story` until a separate change updates the start-phase contract.

## Why the workflow matters

This sequence gives you:

- narrower prompts
- cheaper token usage
- clearer review points
- more reproducible outputs
- better traceability from idea to code

## Recommended default

If you are not sure where to start, use the orchestrator in `semi-auto` mode and let it stop at the intended review gates.

- Continue to [Orchestrator Modes](/workflow/orchestrator-modes)
- Continue to [Phase Handoffs](/workflow/phase-handoffs)
