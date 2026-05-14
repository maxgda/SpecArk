# spdd-doc-sync

`spdd-doc-sync` keeps in-repo human-facing documentation aligned after workflow, skill, or behavior changes.

## Quick start

```text
Use the spdd-doc-sync skill. Added the spdd-doc-sync skill — update the skill index, docs page, VitePress config, and CLAUDE.md.
```

You can also reference a story, analysis, or prompt artifact for context:

```text
Use the spdd-doc-sync skill on @spdd/analysis/STORY-001-003-[Analysis]-spdd-doc-sync-skill.md.
```

## Use it when

- a new skill was added to the plugin and needs a docs page, index entry, and VitePress config update
- an existing skill's behavior, invocation syntax, or artifact output changed
- an onboarding or tutorial step is stale after a release
- maintainer notes need updating after contributor-facing behavior changes
- a CHANGELOG entry is needed for a release or behavior change

## Do not use it for

- syncing the structured SPDD prompt — use `spdd-sync` for that
- publishing the docs site or creating release tags
- editing canonical source command files unless the underlying workflow contract truly changed
- documentation outside this repository

## Output

This skill produces:

- targeted in-place updates to whichever documentation surfaces are matched by the routing table for the given change context
- an **affected-vs-untouched report** that lists every in-scope documentation surface, whether it was updated or skipped, and the reason for each decision

No intermediate artifacts are created. All changes are direct file edits.

## Role in the workflow

```
(skill added, behavior changed, or workflow updated)
  └─ spdd-doc-sync → docs/, README.md, CHANGELOG.md, plugins/specark/CLAUDE.md
                      (only the surfaces matched by the change type)
```

`spdd-doc-sync` is a standalone maintenance skill. It is not part of the orchestrator's forward workflow sequence (story → analysis → reasons-canvas → generate). Invoke it after any cycle that produces user-visible or maintainer-visible changes.

::: info spdd-doc-sync vs spdd-sync
`spdd-doc-sync` updates **human-facing documentation** — the pages, index entries, and changelogs that users and contributors read.

`spdd-sync` updates the **structured SPDD prompt** — the REASONS Canvas artifact that drives code generation.

They are complementary and independent. Running one does not replace the other.
:::
