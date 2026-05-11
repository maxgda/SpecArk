# Maintainer Notes

This page is for people extending the plugin itself, not end users running the workflow.

## Design rules

- Keep phase skills lean when canonical source commands already define the behavior.
- Put shared rules in references or scripts instead of duplicating them across `SKILL.md` files.
- Preserve file-backed handoff contracts between phases.
- Treat the orchestrator as workflow control, not as a substitute for downstream phase skills.

## Development workflow

1. Edit the relevant `SKILL.md`, script, or reference file.
2. Update `agents/openai.yaml` if user-facing labels or invocation wording changed.
3. Refresh docs when visible behavior changed.
4. Run `python3 plugins/specark/scripts/validate_plugin_bundle.py`.
5. Run `npm run docs:build` before publishing docs changes.

## Source of truth

Canonical command text lives under `plugins/specark/references/source-commands/`.

That material should stay authoritative. The skill wrappers should point to it, not re-express it in slightly different ways.

## Docs site

Local commands:

```bash
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview
```

GitHub Pages setup (one-time):

1. Open repository settings → Pages.
2. Set `Build and deployment > Source` to `GitHub Actions`.
3. Push to `main` and wait for the deploy workflow to finish.

## Notes for further development

- Keep documentation split between user-facing operation and maintainer-facing release work.
- Expand skill docs when behavior changes, but avoid turning them into copies of the canonical command files.
- If you broaden test generation beyond API workflows, document the new scope clearly in both the README and the skill pages.
