# Versioned Trayector Profile Kit

The active release is identified only by `.trayector/settings/trayector.yaml`:

```yaml
version: 0.1.0
```

Each immutable release bundle installs together under `.trayector/versions/<version>/` with `skills/` **and** `templates/`. Agent entry points at root (AGENTS.md, CLAUDE.md, GEMINI.md, .github/copilot-instructions.md) must resolve the version and read `skills/index.md`. Templates are mandatory structural contracts for **understanding, editing and generating** Markdown records; skills define operational procedures. Do not interpret arbitrary Markdown without the matching active template.

The manual update workflow downloads the complete `profile-kit/versions/<version>/` from tag `v<version>`, preserves installed old versions and prepares a PR aligning release version and official reusable workflow references. It must not silently rewrite existing professional records after template changes. Custom agent instructions remain user-managed.

CVs are derived Markdown in `cv/`; `manage-resumes.md` generates and maintains them using `templates/resumes/basic.md`. Site publishing selects an existing CV and renders it, without an AI call.

Releases and end-to-end template builds still require testing before describing the installation as production-ready.
