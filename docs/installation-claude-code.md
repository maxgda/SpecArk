# Installation — Claude Code

SpecArk works with Claude Code by making the SPDD skills available in your project's context. There is no marketplace CLI for Claude Code — installation is a one-time clone or submodule step followed by a CLAUDE.md reference.

## Option A: Git submodule (recommended for teams)

Add SpecArk as a submodule so you can track its version and update it independently:

```bash
git submodule add https://github.com/maxgda/SpecArk.git plugins/specark-plugin
git submodule update --init --recursive
```

Then reference the plugin entry point in your project's `CLAUDE.md`:

```markdown
# My Project

@plugins/specark-plugin/plugins/specark/CLAUDE.md
```

## Option B: Direct clone (quickest start)

Clone the repository into your project's plugin folder:

```bash
git clone https://github.com/maxgda/SpecArk.git plugins/specark-plugin
```

Then add the same reference to your `CLAUDE.md`:

```markdown
@plugins/specark-plugin/plugins/specark/CLAUDE.md
```

## Option C: Copy skills only (minimal footprint)

If you only want the skill files without the full plugin repository:

```bash
mkdir -p .claude/skills
cp -r plugins/specark-plugin/plugins/specark/skills/* .claude/skills/
```

This copies all nine SPDD skills into your project's `.claude/skills/` folder. Claude Code discovers them automatically. No `CLAUDE.md` reference needed.

## Verify the install

Open Claude Code in your project directory and ask:

```text
What SPDD skills are available in this project?
```

Claude Code should list the nine `spdd-*` skills and their purposes. If it does not, confirm the `CLAUDE.md` reference path resolves correctly from your project root.

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

## Invocation syntax

Claude Code skills are invoked by naming them explicitly in your request. Use `@file` to reference repository files:

| Action | Claude Code syntax |
|---|---|
| Run orchestrator | `Use the spdd-orchestrator skill on @idea.md in semi-auto mode.` |
| Create stories | `Use the spdd-story skill on @requirements/brief.md.` |
| Run analysis | `Use the spdd-analysis skill on @requirements/STORY-001.md.` |
| Generate prompt | `Use the spdd-reasons-canvas skill on @spdd/analysis/ANALYSIS-001.md.` |
| Implement | `Use the spdd-generate skill on @spdd/prompt/PROMPT-001.md.` |
| Update prompt | `Use the spdd-prompt-update skill on @spdd/prompt/PROMPT-001.md.` |
| Sync after refactor | `Use the spdd-sync skill on @spdd/prompt/PROMPT-001.md.` |

## Keeping skills up to date

If you used Option A (submodule), update with:

```bash
git submodule update --remote plugins/specark-plugin
```

If you used Option B (clone), pull from the origin:

```bash
git -C plugins/specark-plugin pull origin main
```

## Read next

- [Getting Started](/getting-started) — workflow overview and first run
- [First Feature Tutorial](/first-feature) — end-to-end walkthrough
- [Skill Index](/skills/) — reference for all nine skills
