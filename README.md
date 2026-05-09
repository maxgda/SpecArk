# SpecArk

Structured Prompt-Driven Development for Codex, packaged as a Git-distributed plugin bundle.

SpecArk turns SPDD into an explicit, artifact-driven workflow instead of a loose series of prompts. You move from requirement to analysis to implementation by handing files from one phase to the next.

> Based on Martin Fowler's article, [Structured Prompt-Driven Development (SPDD)](https://martinfowler.com/articles/structured-prompt-driven/).

## Why SpecArk

- explicit `spdd-*` skills instead of ambiguous routing
- file-backed handoffs between workflow phases
- narrower prompts and lower token burn
- clean recovery paths when requirements or code drift
- optional orchestrator for end-to-end coordination

## Quick Start

### 1. Install

For a GitHub-backed marketplace install:

```bash
codex plugin marketplace add <owner>/<repo>
codex plugin marketplace upgrade
```

For local plugin development:

1. Keep the plugin at `plugins/specark/`.
2. Keep the marketplace file at `.agents/plugins/marketplace.json`.
3. Restart Codex after changing skills, references, or plugin metadata.

### 2. Validate the bundle

```bash
python3 plugins/specark/scripts/validate_plugin_bundle.py
```

This checks the plugin manifest, marketplace file, canonical command references, skill wrappers, and `agents/openai.yaml` files.

### 3. Run the docs locally

```bash
npm install
npm run docs:dev
```

Other useful commands:

```bash
npm run docs:build
npm run docs:preview
```

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/specark/
  .codex-plugin/plugin.json
  references/
  scripts/
  skills/
docs/
README.md
CHANGELOG.md
```

## How To Run The Workflow

The normal SPDD flow is:

1. `spdd-story`
2. `spdd-analysis`
3. `spdd-reasons-canvas`
4. `spdd-generate`
5. `spdd-api-test` when API verification assets are needed

If you want one command surface, start with the orchestrator:

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
```

If you want to run phases manually:

```text
Use the spdd-story skill on @idea-of-the-enhancement.md.
Use the spdd-analysis skill on @requirements/STORY-001.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

Expected project-local artifact folders:

- `requirements/`
- `spdd/analysis/`
- `spdd/prompt/`
- `spdd/tests/`

These artifacts belong to the consuming project, not the plugin itself.

## How To Save Tokens

The cheapest SPDD workflow is the one that keeps every step narrow and artifact-driven.

### Recommended habits

- Use file inputs instead of pasting long requirements into chat.
- Pass one artifact to the next phase instead of restating the same context.
- Split large requirements with `spdd-story` before analysis.
- Use `spdd-prompt-update` for requirement changes instead of regenerating from scratch.
- Use `spdd-sync` when implementation drift happened and the prompt needs to catch up.
- Keep each Codex request single-purpose.

### Low-token pattern

```text
Use the spdd-story skill on @idea.md.
Use the spdd-analysis skill on @requirements/STORY-001.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

### High-token anti-pattern

```text
Here is the full requirement again...
Here is the architecture again...
Here is the analysis again...
Now generate everything end to end and also update tests.
```

## How To Generate Tests

Use `spdd-api-test` when the change affects API behavior or when you want reusable verification artifacts after implementation.

Example:

```text
Use the spdd-api-test skill on @spdd/prompt/PROMPT-001.md.
```

Best times to run it:

- after `spdd-generate` for a new API feature
- after updating an existing prompt with `spdd-prompt-update`
- after syncing prompt drift with `spdd-sync` when API behavior changed

Typical output target:

- `spdd/tests/`

## Included Skills

- `spdd-orchestrator`: coordinate the workflow across phases and review gates
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
- [Installation](docs/installation.md)
- [Workflow Overview](docs/workflow/index.md)
- [Skill Index](docs/skills/index.md)
- [Limitations](docs/limitations.md)
- [Next Steps](docs/next-steps.md)
- [Release Notes](docs/release-notes.md)
- [Maintainer Notes](docs/maintainer-notes.md)
