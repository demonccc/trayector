# Publishing a Trayector profile

The official site is implemented in `site/` inside **demonccc/trayector**, not copied to personal profiles. The default site is a reference implementation, not a theme framework.

A personal profile contains canonical Markdown and these settings:

```yaml
# .trayector/settings/trayector.yaml
version: 0.1.0
```

```yaml
# .trayector/settings/site.yaml
enabled: false
articles:
  enabled: true
experience:
  enabled: true
cv:
  enabled: false
  selected: general
```

The profile installs `templates/github/publish.yml` as `.github/workflows/publish.yml`. It invokes `demonccc/trayector/.github/workflows/publish.yml@v0.1.0`. This release must exist before the workflow can execute.

On each push to main, the workflow:

1. Checks out the caller profile.
2. Checks out **the exact SHA that contains the called reusable workflow**, using `job.workflow_repository` and `job.workflow_sha`. No use of Trayector main or the caller's ref for site assets.
3. Checks the workflow's tag and the version declared in `.trayector/settings/trayector.yaml`.
4. If publishing is enabled, renders `PROFILE.md`, experience and content Markdown through the release's static site implementation.
5. Publishes the clean static output to GitHub Pages.

The default builder strips unsafe embedded HTML and excludes draft/private articles. The site is intentionally minimal; it does not currently provide rich image handling, semantic content filtering, link rewriting or multilingual navigation. These limitations must be addressed before describing it as production-ready.

The default site reads the selected CV from `cv/<selected>.md`, renders a page and a text-based PDF, and never calls an AI. The source Markdown must already be reviewed. The initial PDF renderer is intentionally simple and needs typography and ATS tests.

The owner can replace the caller workflow entirely to host elsewhere, use a custom site or create separate publication jobs. No theme/provider interface is imposed.

A manual `update-trayector.yml` proposes a PR that installs the target version's skills, updates `trayector.yaml`, and changes the official publish workflow reference to the same tag. Nothing updates automatically.

**Implementation status:** the renderer and workflows are implemented in the feature branch but must be tested on a tagged release and a real calling profile before publishing is enabled in the distributed template.
