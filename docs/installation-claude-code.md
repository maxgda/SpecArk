# Installation — Claude Code

SpecArk works in both **Claude Code** (CLI) and **Claude Cowork** (desktop). Both use the same plugin format and the same marketplace install commands — one install covers both. See the [Cowork section](#cowork) for Cowork-specific notes.

## Install from the marketplace

```bash
claude plugin marketplace add maxgda/spec-ark
claude plugin install specark
```

This registers the SpecArk marketplace from GitHub and installs the `specark` plugin, making all twelve `spdd-*` skills available as namespaced slash commands.

## Local development install

For local plugin work or testing before publishing:

```bash
claude --plugin-dir ./plugins/specark
```

This loads the plugin directly from the local directory. Useful when you are developing or modifying the plugin itself.

## Verify the install

Check that the skills are available:

```bash
claude plugin list
```

You should see `specark` listed. All twelve skills are then invokable as:

```
/specark:spdd-orchestrator
/specark:spdd-discovery
/specark:spdd-plan
/specark:spdd-story
/specark:spdd-analysis
/specark:spdd-reasons-canvas
/specark:spdd-generate
/specark:spdd-prompt-update
/specark:spdd-sync
/specark:spdd-api-test
/specark:spdd-doc-sync
/specark:spdd-session-health
```

## First run

Start with the orchestrator for the default guided path:

```text
/specark:spdd-orchestrator @idea.md semi-auto
```

Or jump directly to the matching phase if you already have an artifact:

```text
/specark:spdd-story @requirements/brief.md
/specark:spdd-analysis @requirements/STORY-001.md
/specark:spdd-reasons-canvas @spdd/analysis/ANALYSIS-001.md
/specark:spdd-generate @spdd/prompt/PROMPT-001.md
```

## Skill invocation reference

| Action | Command |
|---|---|
| Full orchestrated workflow | `/specark:spdd-orchestrator @idea.md semi-auto` |
| Discovery Interview (manual) | `/specark:spdd-discovery @idea.md` |
| Planning slice (optional) | `/specark:spdd-plan @idea.md` |
| Create stories | `/specark:spdd-story @requirements/brief.md` |
| Run analysis | `/specark:spdd-analysis @requirements/STORY-001.md` |
| Generate prompt | `/specark:spdd-reasons-canvas @spdd/analysis/ANALYSIS-001.md` |
| Implement | `/specark:spdd-generate @spdd/prompt/PROMPT-001.md` |
| Update prompt after change | `/specark:spdd-prompt-update @spdd/prompt/PROMPT-001.md` |
| Sync after refactor | `/specark:spdd-sync @spdd/prompt/PROMPT-001.md` |
| Generate API tests | `/specark:spdd-api-test @spdd/prompt/PROMPT-001.md` |
| Sync documentation | `/specark:spdd-doc-sync "Update docs for this workflow change"` |
| Check session health | `/specark:spdd-session-health spdd-analysis @requirements/STORY-001.md` |

## Keeping the plugin up to date

```bash
claude plugin marketplace upgrade
```

---

## Using SpecArk in Claude Cowork {#cowork}

Claude Cowork uses the **identical plugin format and marketplace system** as Claude Code. No separate install is needed — once the plugin is installed, it is available in both.

**How to invoke skills in Cowork:**

- Click the **+** button in the Cowork input bar to browse available skills, or
- Type `/specark:` to filter to SpecArk skills directly.

The skill invocation syntax is the same as Claude Code:

```
/specark:spdd-orchestrator @idea.md semi-auto
/specark:spdd-analysis @requirements/STORY-001.md
```

**Cowork-specific notes:**

- Skills appear in the "+" skill picker alongside any other installed plugins.
- File references (`@file.md`) work the same way as in Claude Code sessions.
- The SPDD artifact handoff model (each phase writing a repository file) fits naturally with Cowork's longer agentic work model.

## Read next

- [Getting Started](/getting-started) — workflow overview and first run
- [First Feature Tutorial](/first-feature) — end-to-end walkthrough
- [Skill Index](/skills/) — reference for all twelve skills
