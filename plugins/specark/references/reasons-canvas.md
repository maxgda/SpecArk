# REASONS Canvas

The REASONS structure used in this plugin is:

- `Requirements`
  - Business goal, scope, intended value, and constraints.
- `Entities`
  - Domain concepts, relationships, and public data contracts.
- `Approach`
  - High-level solution direction and design choices.
- `Structure`
  - Layers, dependencies, interfaces, and component boundaries.
- `Operations`
  - Ordered implementation tasks and execution sequence.
- `Norms`
  - Coding standards, validation patterns, DI rules, logging, and documentation rules.
- `Safeguards`
  - Non-negotiable constraints, quality bars, security rules, and exact behaviors that must be preserved.

Boundary rules:

- `spdd-analysis` stays strategic and conceptual.
- `spdd-reasons-canvas` makes the design implementation-ready.
- `spdd-generate` executes the prompt.
- `spdd-prompt-update` and `spdd-sync` keep the prompt trustworthy over time.
