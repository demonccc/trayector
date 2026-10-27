# Trayector IA instructions and updates

The canonical profile entry point is `PROFILE.md`. The same agent discovery rule is installed in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and `.github/copilot-instructions.md`:

1. Read `PROFILE.md`.
2. Read `.trayector/settings/trayector.yaml` to resolve `ia.version`.
3. Read `.trayector/ia/<ia.version>/index.md` and its relevant operational procedures.

The versioned instruction set teaches agents to read, add, change, link, and validate career information. Version folders are read-only released content. User custom AI instructions are managed independently, are not automatically loaded by Trayector, and cannot be overwritten by its updater.

## Updating

The manual `update-trayector.yml` workflow fetches a selected immutable release folder `profile-kit/ia/<version>/` and opens a PR. The workflow only installs the requested folder. It never modifies `.trayector/settings/trayector.yaml`, previously installed versions, professional content, site code, or user-specific instructions.

A user may activate a newly installed version by explicitly changing `ia.version` in `.trayector/settings/trayector.yaml`.

Example:

```yaml
ia:
  version: 0.1.0
```

The `0.1.0` layout is currently an unreleased example; tagged releases must be published and verified before using the updater.
