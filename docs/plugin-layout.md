# Plugin Layout

This repository is intentionally small. The plugin bundle is concentrated under `plugins/specark/`, while repo-root files handle distribution and top-level documentation.

## Top-level structure

```text
.agents/plugins/marketplace.json
plugins/specark/
  .codex-plugin/plugin.json
  references/
  scripts/
  skills/
README.md
CHANGELOG.md
docs/
```

## Key directories

### `plugins/specark/skills/`

Contains the callable skill folders. Each skill includes:

- `SKILL.md`
- `agents/openai.yaml`

The callable skills are intentionally thin wrappers. They point either to upstream source command text or to SpecArk-authored local command text.

### `plugins/specark/references/`

Contains shared reference material that multiple skills may rely on, including:

- orchestration rules
- REASONS Canvas terminology
- upstream source command files in `source-commands/`
- SpecArk local command files in `local-commands/`
- authoring guidance for future skills

### `plugins/specark/scripts/`

Contains helper scripts used by skills or by repository validation. These exist to keep repetitive or deterministic logic out of skill prose.

## Design principle

The bundle follows progressive disclosure:

- lightweight metadata triggers a skill
- `SKILL.md` names the authoritative command file and maps repository terms
- reference files and scripts carry deeper detail only when needed

This keeps callable skills small without losing rigor.
