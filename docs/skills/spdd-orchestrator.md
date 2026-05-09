# spdd-orchestrator

The orchestrator is the entrypoint for users who want the SPDD workflow coordinated end to end.

## Responsibility

This skill owns workflow control, not phase internals.

It should:

- detect the right starting phase
- invoke one phase at a time
- pass artifact paths between phases
- apply mode semantics
- enforce stop conditions and review gates

It must not:

- replace downstream phase skills
- skip required gates silently
- fabricate artifact lineage
- continue past malformed phase results

## Best use cases

Use it when the user:

- wants one command surface instead of invoking each phase manually
- has an existing artifact and wants to resume correctly
- wants the exact plan before executing any phase
- needs review gates preserved between artifacts

## Related docs

- [Orchestrator Modes](/workflow/orchestrator-modes)
- [Phase Handoffs](/workflow/phase-handoffs)
- [Orchestrator Contract](/references/orchestrator-contract)
