# Getting Started

SpecArk is a Codex plugin bundle for Structured Prompt-Driven Development. It is optimized for repositories that want explicit workflow phases instead of ad hoc prompting.

## When to use SpecArk

Use SpecArk when you want:

- a repeatable path from idea or requirement to implementation
- file-backed artifacts between analysis and generation
- prompt updates after requirement changes
- prompt sync after refactors or implementation drift
- a command-like skill surface with explicit invocation

## Fastest path

1. Install or wire the plugin from a Git-backed marketplace.
2. Start with the orchestrator unless you already know the exact phase you need.
3. Move phase by phase using generated artifacts instead of restating the requirement in chat.

## Typical first commands

Broad requirement:

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
```

Existing story:

```text
Use the spdd-analysis skill on @requirements/STORY-001-example.md.
```

Existing prompt:

```text
Use the spdd-generate skill on @spdd/prompt/EXAMPLE.md.
```

## How the repository stays organized

The plugin itself lives under `plugins/specark/`, but generated SPDD artifacts belong to the consuming project, not the plugin.

Expected project-local artifact folders are:

- `requirements/`
- `spdd/analysis/`
- `spdd/prompt/`
- `spdd/tests/`

## Recommended reading order

1. [Installation](/installation)
2. [Workflow Overview](/workflow/)
3. [Skill Index](/skills/)
4. [Plugin Layout](/plugin-layout)
