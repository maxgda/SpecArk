---
name: /spdd-doc-sync
id: spdd-doc-sync
category: Development
description: Keep human-facing in-repo documentation aligned with current behavior and workflow changes, using an explicit routing table and a full affected-vs-untouched report
---

Keep human-facing in-repo documentation aligned after any workflow, skill, or behavior change. The skill determines which documentation surfaces are genuinely affected, updates only those, reports each decision, and leaves unrelated docs untouched.

---

## 1. Purpose and Trigger Conditions

Invoke `spdd-doc-sync` when:

- A new skill was added to the plugin
- An existing skill's behavior, interface, or invocation changed
- A workflow step, artifact path, or phase sequence changed
- Onboarding or tutorial content is stale after a release
- Maintainer notes need updating after contributor-facing behavior changes
- A CHANGELOG entry is needed for a new release or behavioral change

Do **not** invoke `spdd-doc-sync` for:

- Updating the structured SPDD prompt — that is `spdd-sync`
- Publishing the docs site or creating release tags
- Editing canonical source command files unless the underlying workflow contract truly changed
- External documentation systems outside this repository

---

## 2. Scope and Non-Goals

**In scope:**

- `docs/skills/index.md` — skill discovery table
- `docs/skills/<skill-name>.md` — per-skill documentation pages
- `docs/getting-started.md` — onboarding guide
- `docs/first-feature.md` — first-feature tutorial
- `docs/next-steps.md` — next-steps reference
- `docs/index.md` — landing page (update only if the top-level feature list changes)
- `docs/maintainer-notes.md` — contributor-facing guidance
- `docs/.vitepress/config.mjs` — navigation and sidebar config (structural, not prose)
- `CHANGELOG.md` — version history
- `README.md` — project entry point
- `plugins/specark/CLAUDE.md` — plugin overview and skills reference table

**Out of scope:**

- Any file under `spdd/prompt/` — that boundary is exclusively owned by `spdd-sync`
- Any file under `spdd/analysis/`, `spdd/plan/`, or `spdd/tests/`
- `plugins/specark/references/source-commands/` unless the canonical workflow contract truly changed
- External documentation sites or systems
- Version number assignment — version numbers are set during the release process

---

## 3. Required Startup Reads

Before doing any work, read:

1. `plugins/specark/references/orchestrator-contract.md` — for the SPDD_PHASE_RESULT block format
2. The current content of each documentation surface that will be targeted in this invocation — read all target files before writing any of them

Do not read files under `spdd/prompt/` for any reason.

---

## 4. Execution Contract

**Input**: A change description provided after `/spdd-doc-sync`. Input forms:

```
# Free-form description
/spdd-doc-sync Added the spdd-doc-sync skill — update skill index, docs page, VitePress config, and CLAUDE.md

# Description with file reference as enrichment
/spdd-doc-sync The spdd-generate behavior changed per @spdd/prompt/PROMPT-001.md — update the skill docs page and add a CHANGELOG entry

# Reference to an analysis or story for context
/spdd-doc-sync @spdd/analysis/STORY-001-003-[Analysis]-spdd-doc-sync-skill.md was implemented — update all relevant docs surfaces
```

**Input validation rules:**

- If no change description is provided, use the **AskUserQuestion tool** to ask: "Please describe what changed (skill added, behavior modified, workflow updated). You can also reference a story, analysis, or prompt file with @."
- If input is provided but too vague to produce traceable update reasons (e.g., "docs need updating", "things changed"), use the **AskUserQuestion tool** to ask: "Can you be more specific? I need to know what changed in the repository to determine which documentation surfaces to update."
- Do NOT proceed without a specific, traceable change description.

---

## 5. Repository Term Mapping

| Term | Definition |
|------|-----------|
| `ChangeContext` | The user-supplied description of what changed — skill added, behavior modified, workflow updated, or a set of changed files |
| `DocumentationSurface` | A specific in-repo documentation file from the in-scope list above, identified by its file path and audience label |
| `DocumentationRoutingTable` | The decision framework in Section 7 that maps change-context type to documentation surface targets |
| `AffectedVsUntouchedReport` | The structured output that distinguishes updated files from deliberately skipped files, with a reason for each decision |
| `ChangeType` | One of three primary categories: `skill-addition`, `behavior-change`, `workflow-change`; or `unrecognized` if the change does not fit |
| `Audience` | Either `user-facing` (end users of SpecArk) or `maintainer-facing` (contributors and plugin authors) |

---

## 6. Workflow / Operating Loop

The skill runs in a single invocation. It does not produce intermediate artifacts or iterate.

**Execution sequence:**

1. Validate the change description (see Section 4)
2. Check prompt-stale condition (see Section 10)
3. Classify the change context into a `ChangeType`
4. Apply the routing table (see Section 7) to select target `DocumentationSurface` entries
5. Read every targeted surface completely before writing any of them
6. Execute targeted updates for each surface using per-surface procedures (see Section 8)
7. Produce the `AffectedVsUntouchedReport` covering every surface in the in-scope list
8. Emit the `SPDD_PHASE_RESULT` block (see Section 9)

---

## 7. Decision Rules and Heuristics — The Routing Table

### 7.1 Change type classification

Read the change description and classify it:

| Change type | Characteristics |
|-------------|----------------|
| `skill-addition` | A new skill file set was created; mentions a skill name not previously in the index |
| `behavior-change` | An existing skill's behavior, invocation, output format, or artifact location changed |
| `workflow-change` | Phase sequence, onboarding steps, artifact paths, or the overall SPDD workflow changed |
| `unrecognized` | The change description does not clearly fit a defined type |

A single invocation may describe multiple changes — classify each independently and union the resulting surface sets.

### 7.2 Routing rules

**Skill addition** — always update all of the following:

| Surface | Action | Audience |
|---------|--------|----------|
| `docs/skills/index.md` | Add new row to the phase skills table (or maintenance subsection if applicable) | user-facing |
| `docs/skills/<skill-name>.md` | Create new dedicated skill documentation page | user-facing |
| `docs/.vitepress/config.mjs` | Insert new `skills` array entry in logical position (maintenance skills after `spdd-sync`, before `spdd-api-test`) | structural |
| `plugins/specark/CLAUDE.md` | Add new row to the Skills table after the closest related skill | maintainer-facing |
| `CHANGELOG.md` | Propose a `### Added` entry and ask user to confirm before writing | maintainer-facing |

**Behavior change** — update all that apply:

| Surface | Action | Condition |
|---------|--------|-----------|
| `docs/skills/<skill-name>.md` | Update the affected sections — invocation, output, use-when list, workflow diagram | always |
| `docs/getting-started.md` | Update if invocation syntax or required steps changed | if onboarding is affected |
| `docs/first-feature.md` | Update if the tutorial references the changed skill or artifact path | if tutorial is affected |
| `CHANGELOG.md` | Propose a `### Changed` entry and ask user to confirm before writing | always |

**Workflow change** — update all that apply:

| Surface | Action | Condition |
|---------|--------|-----------|
| `docs/getting-started.md` | Update if phase sequence, artifact paths, or invocation changed | if user-facing |
| `docs/first-feature.md` | Update if the tutorial walkthrough changed | if user-facing |
| `docs/maintainer-notes.md` | Update if contributor-facing workflow changed | if maintainer-facing |
| `plugins/specark/CLAUDE.md` | Update the Normal workflow sequence block | if phase sequence changed |
| `CHANGELOG.md` | Propose a `### Changed` or `### Notes` entry and ask user to confirm | always |

**Unrecognized change type:**

Do NOT default to a broad update. Use the **AskUserQuestion tool** to ask: "This change doesn't fit a recognized pattern. Which documentation surfaces should I update? Options: skill discovery pages, individual skill docs, onboarding pages, maintainer notes, CHANGELOG."

### 7.3 Surfaces not in the routing table output

For every surface in the in-scope list that is NOT selected by the routing table for this invocation, the `AffectedVsUntouchedReport` must include an explicit "not updated because" reason.

---

## 8. Artifact and File Conventions

### 8.1 CHANGELOG.md format

Entries follow this exact structure:

```
## [version] — [date] — [title]

### Added
- Description of what was added

### Changed
- Description of what changed

### Fixed
- Description of what was fixed

### Notes
- Additional context
```

Rules:
- Do NOT assign a version number — use `[Unreleased]` as the placeholder or ask the user which version to use
- Propose the entry text and ask for user confirmation before writing it
- Do not add entries for behavior changes that did not occur
- New entries go at the top of the file, before existing version blocks

### 8.2 `docs/.vitepress/config.mjs` skills array

The `skills` array controls sidebar ordering. When adding a new entry:

- Maintenance skills (`spdd-sync`, `spdd-doc-sync`) belong together
- Insert new maintenance skill entries after `spdd-sync` and before `spdd-api-test`
- Insert new phase skill entries in workflow order: orchestrator → plan → story → analysis → reasons-canvas → generate → prompt-update → sync → doc-sync → api-test → session-health
- Do not append entries at the end of the array out of order

### 8.3 `docs/skills/index.md` table

Rows in the phase skills table follow this format:

```
| [spdd-<name>](/skills/spdd-<name>) | <input description> | <output location> | <use-when condition> |
```

Add maintenance skill rows after `spdd-sync`. If a "Maintenance" subsection does not exist, create it before adding the row.

### 8.4 `plugins/specark/CLAUDE.md` skills table

Rows follow this format:

```
| `spdd-<name>` | `/specark:spdd-<name>` | <purpose description> |
```

Insert after the closest related skill row.

### 8.5 `docs/skills/<skill-name>.md` page

New skill pages follow the format established by `docs/skills/spdd-sync.md`:

- One-sentence summary opening
- `## Quick start` — invocation example
- `## Use it when` — bulleted list of trigger conditions
- `## Output` — what the skill produces
- `## Role in the workflow` — code-block diagram showing standalone or sequenced position
- Tip or info callouts for key distinctions (e.g., boundary with `spdd-sync`)

---

## 9. Validation and Completion Contract

### 9.1 AffectedVsUntouchedReport format

After all updates are complete, produce this report:

```
## Documentation Update Report

### Updated
| File | Audience | Reason |
|------|----------|--------|
| docs/skills/index.md | user-facing | New spdd-doc-sync row added to maintenance skills section |
| ... | ... | ... |

### Not Updated
| File | Reason |
|------|--------|
| docs/index.md | Landing page feature list does not enumerate individual skills; no change needed |
| ... | ... |
```

The report must cover every surface in the in-scope list. No surface may be silently omitted.

### 9.2 SPDD_PHASE_RESULT block

End with this exact block:

```text
SPDD_PHASE_RESULT
phase: spdd-doc-sync
status: completed|blocked
artifact_type: docs
output_files:
- <path of each file updated>
next_phase: complete
review_recommended: yes
summary: <single-line summary of what was updated and why>
END_SPDD_PHASE_RESULT
```

---

## 10. Stop Conditions and Failure Handling

| Condition | Action |
|-----------|--------|
| Change description is missing | Ask with AskUserQuestion before proceeding |
| Change description is too vague to route | Ask for clarification with AskUserQuestion before proceeding |
| Change context implies the prompt artifact is stale | Stop and say: "The change you described may require updating the structured prompt first. Run `spdd-sync` on the affected prompt before I make documentation claims that depend on prompt accuracy." |
| A skill referenced in the change description has no matching file in `docs/skills/` | Surface the ambiguity and ask whether to create a new page or update an existing one |
| Change context implies a skill was renamed | Detect both old and new page names; surface the ambiguity explicitly rather than silently creating a new page and leaving the old one in place |
| An attempted write would target a file under `spdd/prompt/` | Stop immediately and explain: "That path is owned by `spdd-sync`. `spdd-doc-sync` only updates documentation surfaces." |

Do not silently fill in gaps. When in doubt, ask.

---

## 11. Output and Reporting Expectations

After completing all updates:

1. Print the `AffectedVsUntouchedReport` (Section 9.1)
2. Print the `SPDD_PHASE_RESULT` block (Section 9.2)
3. If a CHANGELOG entry was proposed but the user has not yet confirmed, remind them: "The CHANGELOG entry has not been written. Confirm the text above and I will add it."

Multiple-change handling: if the change description covers several distinct changes, handle them all in one invocation but report separately in the AffectedVsUntouchedReport which surface was updated for which change.

Audience labeling: the report must label each changed file as `user-facing` or `maintainer-facing`. This preserves the distinction between end-user docs and contributor docs.
