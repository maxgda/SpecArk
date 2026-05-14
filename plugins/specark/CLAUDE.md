# SpecArk Plugin — Reference Overview

This file is a human-readable overview of the SpecArk plugin. For installation, use the Claude Code marketplace (see `../.claude-plugin/marketplace.json`).

## Skills

| Skill | Invocation | Purpose |
|---|---|---|
| `spdd-orchestrator` | `/specark:spdd-orchestrator` | Coordinate the full workflow across phases |
| `spdd-plan` | `/specark:spdd-plan` | Turn broad product direction into delivery slices |
| `spdd-story` | `/specark:spdd-story` | Decompose a requirement into INVEST-compliant stories |
| `spdd-analysis` | `/specark:spdd-analysis` | Analyze a story against codebase context |
| `spdd-reasons-canvas` | `/specark:spdd-reasons-canvas` | Generate the REASONS Canvas implementation prompt |
| `spdd-generate` | `/specark:spdd-generate` | Implement code from the structured prompt |
| `spdd-prompt-update` | `/specark:spdd-prompt-update` | Update a prompt after requirement changes |
| `spdd-sync` | `/specark:spdd-sync` | Sync implementation reality back into the prompt |
| `spdd-doc-sync` | `/specark:spdd-doc-sync` | Sync human-facing in-repo documentation with current behavior and workflow changes |
| `spdd-api-test` | `/specark:spdd-api-test` | Generate API-oriented verification assets |
| `spdd-session-health` | `/specark:spdd-session-health` | Pre-flight session health check before phase invocation |

## Normal workflow sequence

```
0. /specark:spdd-plan       (optional — for roadmap-sized input)
1. /specark:spdd-story      → requirements/STORY-NNN.md
2. /specark:spdd-analysis   → spdd/analysis/ANALYSIS-NNN.md
3. /specark:spdd-reasons-canvas → spdd/prompt/PROMPT-NNN.md
4. /specark:spdd-generate   → implementation files
5. /specark:spdd-api-test   → spdd/tests/ (optional)
```

## Supporting references

- `references/source-commands/` — canonical workflow text for each phase skill
- `references/orchestrator-contract.md` — shared phase result block format
- `scripts/` — helper utilities for filename derivation and artifact discovery
