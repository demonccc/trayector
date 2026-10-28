# Publishing a career profile

The default website source lives in **Trayector**, not in the personal career repository.

- `site/`: HTML templates and static assets
- `scripts/build-site.py`: Markdown-to-HTML and selected-CV-to-PDF rendering
- `scripts/requirements.txt`: renderer dependencies
- `.github/workflows/publish.yml`: reusable GitHub Pages workflow

A career repository keeps professional Markdown, `.trayector/settings/site.yaml`, and a small `.github/workflows/publish.yml` caller pinned to the same immutable `vX.Y.Z` Trayector tag as `.trayector/settings/trayector.yaml`.

The reusable workflow checks out its own exact `job.workflow_sha` to obtain site assets and scripts from the same release. It reads the **calling repository's** career content, not Trayector's example files.

Typical settings:

```yaml
enabled: false
articles:
  enabled: true
experience:
  enabled: true
cv:
  enabled: false
  selected: general
```

Enable `cv` only when `cv/<selected>.md` exists. The site displays that CV as HTML and includes a PDF download link generated from the same Markdown file. No AI API is used by publishing.

Users can replace their caller workflows or site implementation. The default site is intentionally minimal: advanced image handling, internal-link rewriting, visual PDF polishing and multilingual navigation still require testing or implementation. It must be tested against a real tagged release before being considered production-ready.
