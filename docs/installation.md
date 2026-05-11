# Installation — Codex

SpecArk installs into Codex through the standard plugin marketplace mechanism. One install registers all nine `spdd-*` skills.

## Install from the marketplace

```bash
codex plugin marketplace add maxgda/spec-ark
codex plugin marketplace upgrade
```

This registers the SpecArk marketplace from GitHub and makes every `spdd-*` skill available in your Codex session.

## Local development install

For local plugin work or testing before publishing:

1. Keep the plugin at `plugins/specark/`.
2. Keep the marketplace file at `.agents/plugins/marketplace.json`.
3. Restart Codex after changing skills, references, or metadata.

This loads the plugin directly from the local directory. Useful when you are developing or modifying the plugin itself.

## Verify the install

After install, every skill is invokable by name. The Codex invocation pattern is:

```text
Use the <skill-name> skill on @<artifact-path>.
```

For example:

```text
Use the spdd-orchestrator skill on @idea.md in semi-auto mode.
```

## First run

Start with the orchestrator for the default guided path:

```text
Use the spdd-orchestrator skill on @idea.md in semi-auto mode.
```

Or jump directly to the matching phase if you already have an artifact:

```text
Use the spdd-story skill on @requirements/brief.md.
Use the spdd-analysis skill on @requirements/STORY-001.md.
Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.
Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.
```

## Skill invocation reference

| Action | Command |
|---|---|
| Full orchestrated workflow | `Use the spdd-orchestrator skill on @idea.md in semi-auto mode.` |
| Planning slice (optional) | `Use the spdd-plan skill on @idea.md.` |
| Create stories | `Use the spdd-story skill on @requirements/brief.md.` |
| Run analysis | `Use the spdd-analysis skill on @requirements/STORY-001.md.` |
| Generate prompt | `Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.` |
| Implement | `Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.` |
| Update prompt after change | `Use the spdd-prompt-update skill on @spdd/prompt/PROMPT-001.md.` |
| Sync after refactor | `Use the spdd-sync skill on @spdd/prompt/PROMPT-001.md.` |
| Generate API tests | `Use the spdd-api-test skill on @spdd/prompt/PROMPT-001.md.` |

## Keeping the plugin up to date

```bash
codex plugin marketplace upgrade
```

## Read next

- [Getting Started](/getting-started) — workflow overview and first run
- [First Feature Tutorial](/first-feature) — end-to-end walkthrough
- [Skill Index](/skills/) — reference for all nine skills
