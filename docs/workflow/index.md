# Workflow Overview

SpecArk expresses SPDD as a sequence of explicit phases, with artifacts passed from one phase to the next.

## Standard sequence

```
0. spdd-plan          (optional — for roadmap-sized input)
1. spdd-story         → requirements/STORY-*.md
2. spdd-analysis      → spdd/analysis/*.md
3. spdd-reasons-canvas → spdd/prompt/*.md
4. spdd-generate      → implementation files
5. spdd-api-test      → spdd/tests/*  (optional)

Maintenance:
   spdd-prompt-update  when requirements change
   spdd-sync           when implementation drifts from the prompt
```

## Artifact-driven handoff

Each phase produces repository files that become the next phase's inputs. The goal is to avoid re-sending the same business context through chat.

::: tip Why file-backed handoffs matter
- Each artifact is reviewable before moving forward.
- Later phases read the file directly — no copy-pasting context.
- If anything goes wrong, you have a clear checkpoint to return to.
:::

Typical artifact path:

```text
spdd/plan/PLAN-EXAMPLE.md
requirements/STORY-001-example.md
spdd/analysis/EXAMPLE.md
spdd/prompt/EXAMPLE.md
<implementation files>
spdd/tests/<verification assets>
```

::: info spdd-plan and the orchestrator
`spdd-plan` is explicitly invoked and optional. The orchestrator still starts broad inputs at `spdd-story` until a separate change updates the start-phase contract.
:::

## Why the workflow matters

::: info Benefits
- **Narrower prompts** — each request stays focused on one phase.
- **Cheaper token usage** — no repeated context in every message.
- **Clearer review points** — every major transition has an artifact to inspect.
- **More reproducible outputs** — same inputs produce consistent artifacts.
- **Better traceability** — idea to code with a clear file history.
:::

## Recommended default

::: tip Just getting started?
Use the orchestrator in `semi-auto` mode. It stops at the natural review gates so you can inspect each artifact before the next phase begins.

```text
Use the spdd-orchestrator skill on @your-idea.md in semi-auto mode.
```
:::

- Continue to [Orchestrator Modes](/workflow/orchestrator-modes)
- Continue to [Phase Handoffs](/workflow/phase-handoffs)
