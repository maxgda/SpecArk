# Next Steps

These are the remaining tasks before a polished public release.

## Publishing readiness

1. Replace placeholder publisher metadata in `plugins/specark/.codex-plugin/plugin.json`.
2. Decide the final license.
3. Supply the real GitHub repository URL and homepage metadata.
4. Add contact, privacy policy, and terms URLs if they are required for distribution.

## Install-surface polish

1. Add branded assets:
   `plugins/specark/assets/icon.png`
   `plugins/specark/assets/logo.png`
   `plugins/specark/assets/screenshot1.png`
2. Verify the plugin renders well inside Codex after install.
3. Check that the marketplace metadata reads cleanly in the UI.

## Release flow

1. Run `python3 plugins/specark/scripts/validate_plugin_bundle.py`.
2. Run `npm run docs:build`.
3. Restart Codex and verify the plugin is discoverable through `.agents/plugins/marketplace.json`.
4. Update `CHANGELOG.md` and move any unreleased summary in `docs/release-notes.md` into the final versioned section.
5. Tag the release after the validation pass is clean.
