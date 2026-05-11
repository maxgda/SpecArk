<p align="left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/public/logo-dark.svg">
    <img src="docs/public/logo.svg" alt="SpecArk" width="72" height="72">
  </picture>
</p>

# SpecArk

Structured Prompt-Driven Development, packaged as a Git-distributed plugin bundle for **Codex**, **Claude Code**, and **Claude Cowork**.

SpecArk turns SPDD into an explicit, artifact-driven workflow instead of a loose series of prompts. It helps you move from an idea or requirement to analysis, prompt generation, implementation, and optional verification by handing repository files from one phase to the next.

Use it when your repository needs a repeatable path from broad request to implementation without re-pasting the same context at every step.

## Start Here

### Codex — two-command startup

```bash
codex plugin marketplace add maxgda/spec-ark
codex plugin marketplace upgrade
```

### Claude Code &amp; Cowork — two-command startup

```bash
claude plugin marketplace add maxgda/spec-ark
claude plugin install specark
```

Works in both Claude Code (CLI) and Claude Cowork (desktop). One install covers both.

### First real run

**Codex** — starting from a broad idea:

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
```

**Claude Code** — starting from a broad idea:

```text
/specark:spdd-orchestrator @idea-of-the-enhancement.md semi-auto
```

If you already know the exact artifact you have, jump to the matching phase:

```text
# Codex
Use the spdd-analysis skill on @requirements/STORY-001.md.

# Claude Code
/specark:spdd-analysis @requirements/STORY-001.md
```

## Why SpecArk

- explicit `spdd-*` skills instead of ambiguous routing
- file-backed handoffs between workflow phases
- narrower prompts and lower token burn
- clean recovery paths when requirements or code drift
- an optional orchestrator when you want one command surface

## Use SpecArk When

- you want a repeatable path from idea to implementation
- you prefer repository files over re-pasting the same context in chat
- you need prompt updates after requirement changes
- you need prompt sync after refactors or implementation drift
- you want clear phase boundaries instead of free-form prompting

## What Happens Next

The normal SPDD flow is:

0. optional `spdd-plan`
1. `spdd-story`
2. `spdd-analysis`
3. `spdd-reasons-canvas`
4. `spdd-generate`
5. `spdd-api-test` when API verification assets are needed

Expected project-local artifact folders:

- `spdd/plan/`
- `requirements/`
- `spdd/analysis/`
- `spdd/prompt/`
- `spdd/tests/`

These artifacts belong to the consuming project, not the plugin itself.

## First 10 Minutes

1. Install with the marketplace commands above (Codex or Claude Code).
2. Run the orchestrator if you are starting broad, or jump straight to the phase that matches your current artifact.
3. Review the produced artifact before moving forward to the next phase.
4. Continue into the implementation prompt and generated code.

For a guided walkthrough, start with [Getting Started](docs/getting-started.md) and then use the [First Feature Tutorial](docs/first-feature.md).

## Keep Token Usage Low

The cheapest SPDD workflow is the one that keeps every request narrow and artifact-driven.

### Recommended pattern

```text
Use the spdd-story skill on @idea.md.
Use the spdd-analysis skill on @requirements/STORY-001.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

### Anti-pattern

```text
Here is the full requirement again...
Here is the architecture again...
Here is the analysis again...
Now generate everything end to end and also update tests.
```

## Local Development And Docs

For local plugin work:

1. Keep the plugin at `plugins/specark/`.
2. Keep the marketplace file at `.agents/plugins/marketplace.json`.
3. Restart Codex after changing skills, references, or plugin metadata.

Validate the bundle:

```bash
python3 plugins/specark/scripts/validate_plugin_bundle.py
```

Run the docs site locally:

```bash
npm install
npm run docs:dev
```

Other useful docs commands:

```bash
npm run docs:build
npm run docs:preview
```

## Included Skills

- `spdd-orchestrator`: coordinate the workflow across phases and review gates
- `spdd-plan`: turn broad product direction into ordered delivery slices before story generation
- `spdd-story`: split a broad requirement into implementation-sized stories
- `spdd-analysis`: turn a story or requirement into strategic engineering context
- `spdd-reasons-canvas`: generate the implementation-ready REASONS prompt
- `spdd-generate`: implement code from the prompt
- `spdd-prompt-update`: update an existing prompt after requirement or design changes
- `spdd-sync`: sync implementation reality back into the prompt
- `spdd-api-test`: generate or refresh API-oriented verification assets

## Canonical Sources

Source-of-truth workflow text is preserved under:

- `plugins/specark/references/source-commands/spdd-story.md`
- `plugins/specark/references/source-commands/spdd-analysis.md`
- `plugins/specark/references/source-commands/spdd-reasons-canvas.md`
- `plugins/specark/references/source-commands/spdd-generate.md`
- `plugins/specark/references/source-commands/spdd-prompt-update.md`
- `plugins/specark/references/source-commands/spdd-sync.md`
- `plugins/specark/references/source-commands/spdd-api-test.md`

Provenance metadata lives in `plugins/specark/references/source-commands/SOURCES.md`.

## Read More

- [Getting Started](docs/getting-started.md)
- [First Feature Tutorial](docs/first-feature.md)
- [Installation](docs/installation.md)
- [Workflow Overview](docs/workflow/index.md)
- [Skill Index](docs/skills/index.md)
- [Limitations](docs/limitations.md)
- [Next Steps](docs/next-steps.md)
- [Release Notes](docs/release-notes.md)
- [Maintainer Notes](docs/maintainer-notes.md)
