# Optional website and publishing

Trayector is a Career as Code template based on career-profile-spec. Canonical professional information remains in the profile repository, versioned by Git and understandable by AI regardless of public publishing.

Trayector ships **one editable example**, not a website framework or deployment-provider architecture.

## Repository-owned implementation

After installing the template, a profile may contain:

```text
.trayector/
├── settings/
│   └── site.yaml
└── site/
    ├── pages/
    ├── components/
    ├── styles/
    ├── assets/
    └── scripts/
.github/
└── workflows/
    └── publish.yml
```

`.trayector/site/` contains the default site implementation; `.github/workflows/publish.yml` owns the entire example build and deployment flow to GitHub Pages. Both belong to the profile owner, who is free to modify or replace them. The folder breakdown is illustrative and may depend on the selected implementation.

There is **no mandatory theme system, renderer interface, deployment provider registry, or plugin contract**. Users may adopt another framework, customize the default implementation, publish elsewhere, or maintain their own workflows. Trayector does not claim to support every customization.

## Optional site configuration

The Profile Kit supplies `profile-kit/settings/site.yaml`, installed as `.trayector/settings/site.yaml`:

```yaml
enabled: false

articles:
  enabled: true

experience:
  enabled: true

cv:
  enabled: true
  profile: general
```

- `enabled` is the switch for the **example** website workflow.
- `articles.enabled` controls the article section on that site, not whether content is stored or versioned.
- `experience.enabled` controls the experience section on that site, not whether experience exists in the profile.
- `cv.enabled` controls whether that site exposes the general CV; `profile` selects the CV generation profile.
- There is no `ai.enabled`: AI readability is intrinsic to Career as Code.
- There is no `deployment.provider`: publication lives in the editable GitHub Actions workflow, not in the data settings.

## Default workflow

The example `publish.yml` should trigger on pushes to `main` (optionally also manually), read `site.yaml`, and, when enabled, build a clean site from the canonical profile and publish it with GitHub Pages. Only enabled sections should be included. Rebuilding cleanly avoids retaining pages for disabled sections.

Disabling a deployment workflow does **not** automatically take down previously published content. Removing an existing site must be handled explicitly.

The website and CV remain derived views. They must not introduce new professional claims or become competing sources of career truth. The configured CV profile must exist; targeted/private CVs are not published automatically.

## Beyond the default

A profile owner may create separate workflows, for example `publish-articles.yml` that runs only for changes under `content/articles/**`, or deploy a custom site to another hosting service. Those choices need no registration with Trayector and require no changes to career-profile-spec.

The only durable boundary: custom publishing code can read canonical profile content but should not mix visual/layout data into the canonical career facts.

## Implementation status

This change establishes the configuration and ownership model. The sample site implementation and functional `publish.yml` still need to be developed and tested; the configuration alone does not publish a website.
