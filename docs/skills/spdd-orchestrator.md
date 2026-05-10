# spdd-orchestrator

The orchestrator is the recommended entrypoint for users who want the SPDD workflow coordinated end to end.

## Quick start

```text
Use the spdd-orchestrator skill on @your-idea.md in semi-auto mode.
```

::: tip Recommended for first-time users
The orchestrator handles phase selection, artifact routing, and review gates. You do not need to know which phase to start from — it detects the right one from the artifact you provide.
:::

## Responsibility

This skill owns workflow control, not phase internals.

**It should:**

- detect the right starting phase from the input artifact
- invoke one phase at a time
- pass artifact paths between phases
- apply the requested mode semantics
- enforce stop conditions and review gates

**It must not:**

- replace downstream phase skills
- skip required gates silently
- fabricate artifact lineage
- continue past malformed phase results

## Best use cases

Use it when you:

- want one command surface instead of invoking each phase manually
- have an existing artifact and want to resume correctly
- want to see the exact plan before executing any phase (`plan-only` mode)
- need review gates preserved between artifacts

## Modes

| Mode | Behavior |
|---|---|
| `semi-auto` | Run sequentially, stop at review gates |
| `auto` | Run to completion without pausing |
| `manual` | Run exactly one phase |
| `resume` | Pick up from an existing artifact |
| `plan-only` | Show the phase plan, execute nothing |

## Related docs

- [Orchestrator Modes](/workflow/orchestrator-modes)
- [Phase Handoffs](/workflow/phase-handoffs)
- [Orchestrator Contract](/references/orchestrator-contract)
