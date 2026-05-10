# Installation

SpecArk supports two AI coding environments: **Codex** and **Claude Code**. Choose the section that matches your setup.

---

## Codex

<div class="platform-header">
  <img src="/codex-logo.svg" alt="Codex" height="28" />
</div>

### GitHub-backed marketplace install

After publishing this repository to GitHub under a real owner and repository path, install it with the marketplace workflow supported by Codex:

```bash
codex plugin marketplace add <owner>/<repo>
codex plugin marketplace upgrade
```

### Local development install

For local plugin work:

1. Keep the plugin at `plugins/specark/`.
2. Keep the marketplace file at `.agents/plugins/marketplace.json`.
3. Restart Codex after changing skills, references, or metadata.

---

## Claude Code

<div class="platform-header">
  <img src="/claude-logo.svg" alt="Claude Code" height="28" />
</div>

Claude Code uses a direct clone or submodule approach — there is no marketplace CLI equivalent. See the full guide:

→ [Claude Code Installation Guide](/installation-claude-code)

**Quick start:**

```bash
git submodule add https://github.com/maxgda/SpecArk.git plugins/specark-plugin
```

Then add to your `CLAUDE.md`:

```markdown
@plugins/specark-plugin/plugins/specark/CLAUDE.md
```

---

## Validate the bundle

Run the plugin validator from the repo root:

```bash
python3 plugins/specark/scripts/validate_plugin_bundle.py
```

This validates:

- `plugins/specark/.codex-plugin/plugin.json`
- `plugins/specark/CLAUDE.md` (Claude Code entry point)
- `.agents/plugins/marketplace.json`
- canonical source command file presence and recorded byte sizes
- skill wrapper presence
- `agents/openai.yaml` presence and explicit invocation policy

## Publish the docs site

This repository includes a VitePress site deployed to GitHub Pages through GitHub Actions.

Once pushed to GitHub:

1. Open repository settings.
2. Go to `Pages`.
3. Set `Build and deployment > Source` to `GitHub Actions`.
4. Push to `main` and wait for the deploy workflow to finish.

## Local docs commands

```bash
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview
```

If the site is deployed as a project page at `https://<owner>.github.io/SpecArk/`, the VitePress base path in the config is already correct for this repository name.

<style>
.platform-header {
  margin: 12px 0 16px;
}
</style>
