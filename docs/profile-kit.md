# Trayector release layout

**Trayector source repository** holds the editable implementation:

- `skills/`: agent procedures
- `templates/content/`: professional document contracts for profile, experience, project, contribution, publication and article indexes
- `templates/resumes/`: derived CV formats
- `templates/agents/` and `templates/github/`: entry points and workflow callers
- `site/`: HTML templates and static assets
- `scripts/`: site builder
- `profile-kit/settings/`: profile configuration defaults

A **personal repository** stores professional records and an installed release:

```text
PROFILE.md
README.md
profile/
experience/
projects/
contributions/
publications/
articles/
  career-as-code/
    README.md
    es.md
    en.md
    assets/
cv/
.trayector/
  settings/
    trayector.yaml
    site.yaml
  versions/
    0.1.0/
      skills/
      templates/
```

`projects/` describes initiatives created, developed or maintained substantially by the person. `contributions/` describes individual work contributed to other initiatives. `publications/` records external content, public participation and registrations such as copyright. `articles/` contains authored content kept in Markdown, potentially in many languages, with one README index per article. A Markdown article body is completely free-form; the README provides the navigable contract and related links.

The source repository does **not** itself keep the personal `.trayector/versions/` layout. The tagged release supplies a versioned bundle, selected by `.trayector/settings/trayector.yaml`:

```yaml
version: 0.1.0
```

Agents load `PROFILE.md`, the installed matching `skills/index.md`, and the relevant document template before reading or writing career records. The optional updater installs a new skills/templates bundle via a reviewable PR and aligns release-pinned workflows; it does not rewrite personal records.

The site renderer and its scripts remain in Trayector. Site publishing is optional, and authored articles are visible only when explicitly listed in `.trayector/settings/site.yaml` under `articles.include`.
