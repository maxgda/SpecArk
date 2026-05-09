# SpecArk Codex Plugin

This repository packages Structured Prompt-Driven Development as a Codex plugin bundle. It is organized for Git-backed marketplace installation and for local development inside a checkout.

The workflow is based on the SPDD process described in Martin Fowler's article, "Structured-Prompt-Driven Development (SPDD)": [martinfowler.com/articles/structured-prompt-driven](https://martinfowler.com/articles/structured-prompt-driven/).

## Documentation

Developer documentation now lives in the VitePress site under `docs/`.

Local docs commands:

```bash
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview
```

The repository also includes a GitHub Pages workflow at `.github/workflows/deploy-docs.yml`.

## Status

- Canonical SPDD command text is preserved under `plugins/specark/references/source-commands/`.
- Skills are lean wrappers that load the canonical command files instead of duplicating them inline.
- A real repo-root marketplace file now exists at `.agents/plugins/marketplace.json`.
- The package is ready for GitHub distribution.
- Public listing in the official Codex Plugin Directory cannot be completed from this repository alone; current Codex docs describe Git-backed marketplaces today and public directory submission as a separate future step.

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/specark/
  .codex-plugin/plugin.json
  references/
    source-commands/
  scripts/
  skills/
    spdd-story/
      SKILL.md
      agents/openai.yaml
    spdd-analysis/
      SKILL.md
      agents/openai.yaml
    spdd-reasons-canvas/
      SKILL.md
      agents/openai.yaml
    spdd-generate/
      SKILL.md
      agents/openai.yaml
    spdd-prompt-update/
      SKILL.md
      agents/openai.yaml
    spdd-sync/
      SKILL.md
      agents/openai.yaml
    spdd-api-test/
      SKILL.md
      agents/openai.yaml
    spdd-orchestrator/
      SKILL.md
      agents/openai.yaml
CHANGELOG.md
README.md
```

## Installation

### GitHub-backed marketplace install

After this repository is published to GitHub with a real `<owner>/<repo>` path:

```bash
codex plugin marketplace add <owner>/<repo>
codex plugin marketplace upgrade
```

### Local development install

1. Keep the plugin at `plugins/specark/`.
2. Keep the marketplace file at `.agents/plugins/marketplace.json`.
3. Restart Codex after adding or changing skills.

## Validation

Run:

```bash
python3 plugins/specark/scripts/validate_plugin_bundle.py
```

This validates:

- `plugins/specark/.codex-plugin/plugin.json`
- `.agents/plugins/marketplace.json`
- canonical source-command file presence and recorded byte sizes
- skill wrapper presence
- `agents/openai.yaml` presence and explicit invocation policy

## Included Skills

- `spdd-orchestrator`: coordinate the full SPDD workflow with manual, semi-auto, auto, resume, and plan-only modes
- `spdd-story`: split a feature or epic into implementable stories in `requirements/`
- `spdd-analysis`: turn a story or requirement into strategic analysis in `spdd/analysis/`
- `spdd-reasons-canvas`: generate an implementation-ready REASONS prompt in `spdd/prompt/`
- `spdd-generate`: implement code from an SPDD prompt
- `spdd-prompt-update`: update an existing SPDD prompt after requirement or design changes
- `spdd-sync`: sync implementation changes back into the prompt
- `spdd-api-test`: generate or update API-oriented verification artifacts

## Quick Start

Use the plugin in the same order as the SPDD workflow in the article.

### 0. Optional: use one orchestrator for the full flow

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
```

The orchestrator coordinates the same phases below and passes artifact file paths from one phase to the next.

### 1. Optional: create stories from a large requirement

```text
Use the spdd-story skill on @idea-of-the-enhancement.md.
```

### 2. Analyze a story or requirement

```text
Use the spdd-analysis skill on @[User-story-1]Multi-Plan-Billing-Foundation-&-Model-Aware-Pricing.md.
```

### 3. Generate the REASONS Canvas prompt

```text
Use the spdd-reasons-canvas skill on @spdd/analysis/<analysis-file>.md.
```

### 4. Generate code from the prompt

```text
Use the spdd-generate skill on @spdd/prompt/<prompt-file>.md.
```

### 5. Optional: generate API tests

```text
Use the spdd-api-test skill on @spdd/prompt/<prompt-file>.md.
```

### 6. If requirements change, update the prompt first

```text
Use the spdd-prompt-update skill on @spdd/prompt/<prompt-file>.md.
```

### 7. If code changes first, sync code back into the prompt

```text
Use the spdd-sync skill on @spdd/prompt/<prompt-file>.md.
```

## Usage Notes

The plugin is designed for explicit invocation. Each skill disables implicit invocation in its `agents/openai.yaml` so the workflow behaves more like a command surface than ambient routing.

The artifact folders are project-local, not plugin-global. When needed, the workflow writes into the active project, for example:

- `requirements/`
- `spdd/analysis/`
- `spdd/prompt/`

Those folders should be created on demand in the consuming project. They are not shared across projects and do not live inside the plugin installation.

Minimal examples:

```text
Use the spdd-story skill to split this feature into implementable stories.
Use the spdd-analysis skill on requirements/STORY-001-example.md.
Use the spdd-reasons-canvas skill on spdd/analysis/EXAMPLE.md.
Use the spdd-generate skill on spdd/prompt/EXAMPLE.md.
Use the spdd-prompt-update skill on spdd/prompt/EXAMPLE.md.
Use the spdd-sync skill on spdd/prompt/EXAMPLE.md after this refactor.
Use the spdd-api-test skill for the billing usage endpoints.
```

### Orchestrator Modes

The `spdd-orchestrator` skill supports these modes:

- `manual`: run one phase and stop
- `semi-auto`: run sequentially and stop at review gates. This is the default.
- `auto`: run the whole workflow unless blocked
- `resume`: continue from an existing artifact such as a story, analysis, or prompt file
- `plan-only`: show the exact phase plan without executing it

Examples:

```text
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in semi-auto mode.
Use the spdd-orchestrator skill on @requirements/STORY-001.md in auto mode.
Use the spdd-orchestrator skill in resume mode on @spdd/analysis/EXAMPLE.md.
Use the spdd-orchestrator skill on @spdd/prompt/EXAMPLE.md with code drift context.
Use the spdd-orchestrator skill on @idea-of-the-enhancement.md in plan-only mode.
```

### Phase Handoff Contract

The orchestrator expects every SPDD phase skill to end with the same machine-readable handoff block:

```text
SPDD_PHASE_RESULT
phase: <phase-name>
status: completed|blocked
artifact_type: story|analysis|prompt|code|api-test
output_files:
- <repo-relative-path>
next_phase: <phase-name|complete|review>
review_recommended: yes|no
summary: <single-line summary>
END_SPDD_PHASE_RESULT
```

This keeps the workflow file-driven even when a single orchestrator controls the process.

## Saving Tokens

SPDD can consume a lot of tokens if every step re-reads broad context or if users keep restating the same requirement in free text. The cheapest workflow is the one that keeps each step narrow and artifact-driven.

Use these rules:

- Prefer file inputs over long pasted text.
  - Good: `Use the spdd-analysis skill on @requirements/STORY-001.md.`
  - Avoid: pasting the entire requirement again into the chat if it already exists in a file.

- Move through the workflow by artifact.
  - `spdd-story` writes a story file.
  - `spdd-analysis` should read that story file.
  - `spdd-reasons-canvas` should read the analysis file.
  - `spdd-generate` should read the prompt file.
  - This avoids re-sending the same business context at every step.

- Keep the input scope tight.
  - Point to one story or one analysis file whenever possible.
  - Avoid asking the skill to scan many unrelated documents unless that is actually required.

- Split large requirements first.
  - Use `spdd-story` before `spdd-analysis` when a feature is large.
  - Smaller stories lead to smaller analysis scope, smaller prompts, and cheaper generation.

- Use `spdd-prompt-update` and `spdd-sync` instead of regenerating from scratch.
  - If requirements changed, update the existing prompt.
  - If code changed, sync the prompt back to reality.
  - Do not restart the whole SPDD chain for a small change.

- Avoid adding extra free-text instructions around the skill call unless they are truly run-specific.
  - Good: `Use the spdd-generate skill on @spdd/prompt/ABC.md.`
  - More expensive: repeating architectural context that is already in the prompt file.

- Keep project context in files, not in repeated chat messages.
  - Put stable domain language or architecture notes in project files.
  - Then point the workflow at those files when needed instead of retyping them.

- Reuse canonical artifacts as the source of truth.
  - The prompt file should become the main implementation contract.
  - Once it exists, prefer updating it over reconstructing intent from old chat history.

- Run optional steps only when needed.
  - `spdd-story` is optional for small changes.
  - `spdd-api-test` is optional when API verification artifacts are not needed.

- Keep each Codex request single-purpose.
  - Better: one request per phase.
  - Worse: asking Codex to story-split, analyze, generate the prompt, implement, and test in one giant request.

### Low-token Example Flow

```text
Use the spdd-story skill on @idea.md.
Use the spdd-analysis skill on @requirements/STORY-001.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

### High-token Anti-Pattern

```text
Here is the full requirement again...
Here is the analysis again...
Here is the architecture again...
Now generate everything end to end and also update tests.
```

In practice, the biggest token savings usually come from three habits:

- keep requirements and prompts in files
- pass only the next artifact to the next phase
- update existing artifacts instead of regenerating the whole chain

## Canonical Sources

The source-of-truth workflow text is preserved verbatim under:

- `plugins/specark/references/source-commands/spdd-story.md`
- `plugins/specark/references/source-commands/spdd-analysis.md`
- `plugins/specark/references/source-commands/spdd-reasons-canvas.md`
- `plugins/specark/references/source-commands/spdd-generate.md`
- `plugins/specark/references/source-commands/spdd-prompt-update.md`
- `plugins/specark/references/source-commands/spdd-sync.md`
- `plugins/specark/references/source-commands/spdd-api-test.md`

Provenance metadata lives in:

- `plugins/specark/references/source-commands/SOURCES.md`

## Release Checklist

Before publishing or tagging a release:

1. Replace missing publisher metadata in `plugins/specark/.codex-plugin/plugin.json`.
2. Add real plugin assets if you want install-surface polish:
   - `plugins/specark/assets/icon.png`
   - `plugins/specark/assets/logo.png`
   - `plugins/specark/assets/screenshot1.png`
3. Run `python3 plugins/specark/scripts/validate_plugin_bundle.py`.
4. Restart Codex and verify the plugin appears through the marketplace file.
5. Tag a release and update `CHANGELOG.md`.

## Information Still Required Before Public Publishing

This repository cannot truthfully invent the following values. Supply them before public release:

- GitHub repository URL
- publisher/developer name
- contact email, if you want it in the manifest
- homepage URL, if any
- privacy policy URL, if any
- terms of service URL, if any
- license choice
- branded icon, logo, and screenshots
