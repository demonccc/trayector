# Optional site and publishing

Trayector is a Career as Code template implementing career-profile-spec. The canonical profile is always versioned in Git and directly readable by AI, whether or not a public site is enabled.

A public website is an **optional derived view**. It must never become a second source of career truth.

## Configuration

The Profile Kit ships `profile-kit/settings/site.yaml`. Installed in an individual's repository, it lives at `.trayector/settings/site.yaml`.

```yaml
enabled: false

articles:
  enabled: true

experience:
  enabled: true

cv:
  enabled: true
  profile: general

deployment:
  provider: github-pages
```

- `enabled` controls whether a site is built and deployed.
- `articles.enabled` controls the published article section, **not** storage or Git history of `content/`.
- `experience.enabled` controls the published experience section, **not** canonical `experience/`.
- `cv.enabled` controls whether the public site offers a general CV to view/download. `cv.profile` selects the CV generation profile; it does not alter canonical facts.
- `deployment.provider` selects a deployment adapter. The initial provider is `github-pages`.

The section switches have no public-facing effect while the site is disabled. AI understanding, canonical knowledge, and Git versioning are never switches.

## Build and deployment are separate

The **site builder** reads `profile.json`, canonical profile content, and `site.yaml`. It generates a clean, self-contained static output directory. It must omit disabled sections and their formerly generated files.

The **deployment provider** consumes that output directory. It must not edit canonical documents or invent professional claims. Providers may differ without requiring changes to the site's data model or generator.

The intended integration contract is:

```text
canonical profile + site.yaml
         |
     site builder
         |
   static output dir
         |
  deployment adapter
```

A GitHub Pages adapter should use the official Pages artifact/deploy actions; it should not embed site rendering logic. A future provider may be another script, action, or external workflow, so long as it accepts the same static output.

## GitHub Actions lifecycle

An installed profile may opt into a publishing workflow triggered by pushes to `main` (and optionally manual dispatch). The workflow should:

1. Read and validate `.trayector/settings/site.yaml`.
2. If `enabled: false`, skip building and deploying.
3. Otherwise build a **fresh** site output directory from the canonical profile.
4. Invoke the selected provider with the output directory.
5. Fail clearly if the provider is unknown, not configured, or its deployment fails.

Avoid hard-coding all providers into the generator. A repository owner may replace the deployment job/action with a custom adapter, without forking career-profile-spec or duplicating the site builder.

A workflow that stops publishing does **not** unpublish previously deployed files by itself. Disabling an already-live site requires explicit teardown or replacement of the published content; document that action rather than implying that skipping a workflow removes a deployment.

## CV profiles and publication

A public downloadable CV is a selected, derived view. The configured general CV profile must be resolved explicitly; a missing profile should fail the CV build instead of silently choosing another. Job-targeted résumés must not be exposed automatically.

The site may render HTML for viewing and a PDF for download, using the same canonical facts and the selected profile.

## Implementation status

This document defines the configuration and adapter boundaries. The site builder and production publishing workflow are **not yet implemented**. Neither committing `site.yaml` nor selecting `github-pages` alone makes a site live.
