---
layout: home

hero:
  name: "SpecArk"
  text: "Structured Prompt-Driven Development"
  tagline: "A native Claude Code and Codex plugin for spec-driven, traceable engineering."
  actions:
    - theme: brand
      text: Get Started →
      link: /getting-started
    - theme: alt
      text: First Feature Tutorial
      link: /first-feature
    - theme: alt
      text: View on GitHub
      link: https://github.com/maxgda/spec-ark

features:
  - title: Start with one artifact
    details: Use a real repository file as the input, then hand artifacts from one phase to the next instead of re-pasting the same context.
  - title: Explicit workflow control
    details: Use the orchestrator for guided routing or invoke a single spdd-* phase directly when you already have the right artifact.
  - title: Low-token delivery
    details: Narrow requests and file-backed handoffs keep prompts smaller, reviews clearer, and iteration cheaper.
  - title: First-user to ship path
    details: Move from install to a first successful feature with guided onboarding, a tutorial path, and clear phase handoffs.
  - title: Clean recovery paths
    details: Use spdd-prompt-update or spdd-sync to correct drift after requirement changes or implementation refactors — no guesswork.
  - title: Full traceability
    details: Every phase leaves a reviewable artifact. Go from idea to code with a clear audit trail in your repository.
---

<div class="platform-compat">
  <span class="compat-label">Works with</span>

  <a href="./installation" class="compat-thumb compat-codex" title="Codex">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="white" aria-label="OpenAI / Codex">
      <path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/>
    </svg>
  </a>

  <a href="./installation-claude-code" class="compat-thumb compat-claude" title="Claude Code">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="white" aria-label="Anthropic / Claude Code">
      <path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z"/>
    </svg>
  </a>

  <a href="./installation-claude-code#cowork" class="compat-thumb compat-cowork" title="Claude Cowork">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="white" aria-label="Claude Cowork">
      <path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z"/>
    </svg>
  </a>
</div>

<style>
.platform-compat {
  display: flex;
  align-items: center;
  gap: 10px;
  justify-content: center;
  padding: 28px 0 12px;
}
.compat-label {
  font-size: 12px;
  font-weight: 500;
  color: var(--vp-c-text-2);
  letter-spacing: 0.04em;
}
.compat-thumb {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  text-decoration: none;
  transition: opacity 0.15s, transform 0.15s;
}
.compat-thumb svg {
  width: 18px;
  height: 18px;
}
.compat-thumb:hover {
  opacity: 0.82;
  transform: translateY(-1px);
}
.compat-codex {
  background: #000;
}
.compat-claude {
  background: #D97757;
}
.compat-cowork {
  background: #7C3AED;
}
/* unused — kept for installation.md */
.compat-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}
</style>

## Quick start

Three commands to install SpecArk and hand the orchestrator a real request. Pick your platform.

<Terminal title="your-project">

::: code-group

```bash [Claude Code]
# 1. Add the marketplace
claude plugin marketplace add maxgda/spec-ark

# 2. Install the plugin
claude plugin install specark

# 3. Hand the orchestrator a real artifact (auto mode runs end-to-end)
/specark:spdd-orchestrator mode=auto Add a thumbnail-upload step to
the profile editor. See @src/components/ProfileEditor.tsx and the
existing upload helper in @src/lib/upload.ts.
```

```bash [Codex]
# 1. Add the marketplace
codex plugin marketplace add maxgda/spec-ark
codex plugin marketplace upgrade

# 2. Hand the orchestrator a real artifact (auto mode runs end-to-end)
Use the spdd-orchestrator skill on @idea.md in auto mode.
# where idea.md describes the feature and references the relevant files,
# e.g. @src/components/ProfileEditor.tsx and @src/lib/upload.ts.
```

:::

</Terminal>

## What that produces

`auto` mode runs every phase end-to-end. Each one writes a reviewable artifact to your repository before the next phase starts:

<ArtifactFlow :steps="[
  { file: 'requirements/STORY-001.md', note: 'Focused story decomposed from the free-text request — clarifies scope and acceptance criteria.' },
  { file: 'spdd/analysis/ANALYSIS-001.md', note: 'Architecture-aware analysis of the referenced files, the existing upload helper, and where the new step plugs in.' },
  { file: 'spdd/prompt/PROMPT-001.md', note: 'The implementation prompt — the only input spdd-generate reads. Reviewable before any code changes.' },
  { file: 'src/components/ProfileEditor.tsx (+)', note: 'Edits generated from the prompt artifact — new thumbnail-upload step wired into the existing editor.' },
  { file: 'src/lib/upload.ts (~)', note: 'Targeted touch-ups to the helper called out in the request.' }
]" />

**End result.** The feature ships with a four-step audit trail: story → analysis → prompt → code. If anything looks off in the implementation, fix the prompt and regenerate — the artifacts stay in sync.

**Further steps.** Walk the same path with your own input in the [First Feature Tutorial](/first-feature), or read the [Workflow Overview](/workflow/) for phase-by-phase detail.

## Start here if you are new

SpecArk is built for teams and repositories that want a disciplined SPDD workflow instead of loose prompt chains. If you are evaluating the plugin for the first time, start with:

1. [Getting Started](/getting-started)
2. [First Feature Tutorial](/first-feature)
3. [Workflow Overview](/workflow/)

## The workflow at a glance

```
idea.md
  └─ spdd-plan (optional: when input is roadmap-sized)
       └─ spdd-story → requirements/STORY-001.md
            └─ spdd-analysis → spdd/analysis/ANALYSIS-001.md
                 └─ spdd-reasons-canvas → spdd/prompt/PROMPT-001.md
                      └─ spdd-generate → implementation files
                           └─ spdd-api-test → spdd/tests/ (optional)
```

Each phase produces a repository file. The next phase reads that file directly — no context re-pasting.

## What this site covers

Use this documentation when you need to:

- install the plugin into Codex or Claude Code from a Git-backed source
- choose the right SPDD phase for the artifact you already have
- understand how handoff artifacts move from story to analysis to prompt to implementation
- keep token usage low while still preserving reviewable workflow checkpoints
- maintain or extend the plugin after the first-user path is already clear

## Read next

- Start with [Getting Started](/getting-started).
- Continue with the [First Feature Tutorial](/first-feature).
- Review the [Workflow Overview](/workflow/).
- Browse the [Skill Index](/skills/).
- Use [Maintainer Notes](/maintainer-notes) only when you are extending the plugin itself.
