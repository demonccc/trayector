# Trayector release layout

**Trayector repository** holds the editable source of truth for its implementation:

- `skills/`: agent procedures and operational instructions
- `templates/`: mandatory Markdown structural contracts for reading and writing career records
- `site/`: HTML templates and static website assets
- `scripts/`: site builder and supporting scripts
- `profile-kit/settings/`: default configuration files copied into a new career repository

**A personal career repository** contains its own career records plus an installed, immutable release bundle:

```text
.trayector/
  settings/
    trayector.yaml
    site.yaml
  versions/
    0.1.0/
      skills/
      templates/
```

This version folder is **not** part of the Trayector source layout. It is assembled from the repository-root `skills/` and `templates/` directories at release tag `v0.1.0`.

A career repository is what these docs call a **profile**: the repository owned by a person containing their professional history, projects, publications, and derived résumés. There is no central account or hosted profile service.

The active release is selected by `.trayector/settings/trayector.yaml`:

```yaml
version: 0.1.0
```

Agents read `PROFILE.md`, then the matching installed `skills/index.md` and mandatory matching record template. A template is required to **understand** existing documents and to create or update them consistently.

The manual `update-trayector.yml` workflow fetches the new tag's root skills and templates, installs them at `.trayector/versions/<version>/` without changing older releases, and proposes a PR that aligns the declared version and official reusable publish workflow. It does not migrate professional records silently or overwrite modified installed bundles. All updates are optional.

The official site renderer remains in Trayector, not the personal repository. The local publish caller references the matching tag. Its templates and scripts are checked out from the same workflow commit.
