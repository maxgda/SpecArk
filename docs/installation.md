# Installation

SpecArk supports two AI coding environments. Choose the section that matches your setup.

---

## <span class="platform-icon platform-codex"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/></svg></span> Codex

### GitHub-backed marketplace install

After publishing this repository to GitHub under a real owner and repository path:

```bash
codex plugin marketplace add <owner>/<repo>
codex plugin marketplace upgrade
```

### Local development install

1. Keep the plugin at `plugins/specark/`.
2. Keep the marketplace file at `.agents/plugins/marketplace.json`.
3. Restart Codex after changing skills, references, or metadata.

---

## <span class="platform-icon platform-claude"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true"><path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z"/></svg></span> Claude Code &amp; Cowork

Both products share the same plugin format and marketplace. One install covers both.

```bash
claude plugin marketplace add maxgda/spec-ark
claude plugin install specark
```

→ Full guide: [Claude Code &amp; Cowork Installation](/installation-claude-code)

---

## Validate the bundle

```bash
python3 plugins/specark/scripts/validate_plugin_bundle.py
```

This validates:

- `plugins/specark/.codex-plugin/plugin.json` (Codex manifest)
- `plugins/specark/.claude-plugin/plugin.json` (Claude Code manifest)
- `.agents/plugins/marketplace.json` (Codex marketplace)
- `.claude-plugin/marketplace.json` (Claude Code marketplace)
- canonical source command file presence and recorded byte sizes
- all nine skill wrappers, `agents/openai.yaml` presence, and `disable-model-invocation: true` in frontmatter

## Publish the docs site

This repository includes a VitePress site deployed to GitHub Pages through GitHub Actions.

Once pushed to GitHub:

1. Open repository settings → Pages.
2. Set `Build and deployment > Source` to `GitHub Actions`.
3. Push to `main` and wait for the deploy workflow to finish.

## Local docs commands

```bash
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview
```

<style>
.platform-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  padding: 4px;
  vertical-align: middle;
  margin-right: 6px;
}
.platform-icon svg {
  width: 20px;
  height: 20px;
}
.platform-codex {
  background: #000;
  color: white;
}
.platform-claude {
  background: #D97757;
  color: white;
}
</style>
