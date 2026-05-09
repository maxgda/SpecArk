# Limitations

SpecArk is intentionally narrow. It favors explicit workflow control over invisible automation.

## Current constraints

- Skills are designed for explicit invocation, not ambient intent matching.
- Public listing in an official Codex plugin directory is not handled by this repository alone.
- Generated SPDD artifacts belong to the consuming project, not the plugin installation.
- `spdd-api-test` is optional and focused on API-oriented verification assets rather than broad test generation for every stack.
- The workflow depends on file handoffs staying clean. If teams skip artifact updates, later phases lose precision.

## Operational implications

- Small changes do not always need the full workflow.
- Large changes should usually start with story splitting to avoid bloated prompts.
- Prompt drift should be corrected with `spdd-prompt-update` or `spdd-sync`, not by improvising from stale chat history.

## Practical recommendation

Use SpecArk when you want traceability and repeatability. Do not use it as a replacement for basic engineering judgment or for every trivial edit.
