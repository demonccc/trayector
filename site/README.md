# Trayector default static site

This is an editable **reference implementation** shipped with Trayector releases, not a theme or plugin framework.

The reusable workflow checks out the exact commit defining the invoked workflow (using `job.workflow_sha`), then runs `site/build.py` against the **calling repository**. This keeps the HTML, CSS and generator pinned to one immutable release.

The builder reads `PROFILE.md`, relevant Markdown under `experience/` and `content/`, and the optional `.trayector/settings/site.yaml`. It writes a clean static directory. It does **not** modify canonical information.

The default build publishes an existing general PDF only when it is explicitly configured and present. CV generation from canonical facts is a separate task; do not silently generate an unsupported CV.

The owner can replace the caller workflow or use another website project at any time.
