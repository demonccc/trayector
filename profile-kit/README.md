# Trayector Profile Kit

This directory is a **local copy of Trayector guidance for AI agents and profile tooling**.

It belongs inside a Career as Code profile so an AI can understand how to read the repository, update canonical career knowledge, and generate derived views such as README files and tailored résumés without needing prior conversational context.

## Important

The files under `.trayector/` may be customized by the profile owner.

That means they are not disposable generated files and an update from Trayector MUST NOT replace them blindly.

Trayector provides the upstream defaults and evolution path, while each profile may adapt those instructions to its own workflow, preferred résumé templates, presentation rules or additional guidance.

Personal career facts still belong in the canonical profile areas such as `profile/`, `experience/`, `projects/`, `deep-dives/`, `stories/`, `feedback/` and `content/`. `.trayector/` contains instructions and profile configuration about how to interpret and present that knowledge.

## AI: start here

When working on this profile:

1. Read `profile.json` at the repository root.
2. Read this file and `profile-rules.md`.
3. Read the configuration files under `.trayector/settings/` when present.
4. Follow the canonical navigation from `profile.json`.
5. Treat canonical profile documents as the source of professional truth.
6. Never invent missing career facts.
7. Treat README files, tailored résumés and PDFs as derived views.
8. For a tailored résumé, read `resume-generation.md` and the selected template under `resume/`.
9. Respect local changes inside `.trayector/`; they are part of this profile's instructions and configuration.
10. Read `.trayector/VERSION` when you need to know which Trayector release this local kit is based on.

## Settings

Profile-owned configuration lives under:

```text
.trayector/settings/
```

Each file represents one configuration section instead of putting unrelated settings into one root file.

Typical examples are:

```text
.trayector/settings/
├── languages.yaml
└── classifications.yaml
```

Profiles may add more settings files when a new configurable area is needed. Do not create configuration files preemptively when there is nothing to configure yet.

## Version

The installed Profile Kit carries one provenance file:

- `VERSION` — semantic Profile Kit/specification version, such as `0.1.0`.

Trayector uses immutable release tags named from that version. By convention, `VERSION` `0.1.0` maps to Trayector tag `v0.1.0`.

A separate release-ref file is unnecessary.

## Updating this kit

Updates are intentionally **manual and review-driven**.

The repository owner chooses when to run the Trayector update workflow and explicitly selects a target version. There is no scheduled update.

The workflow uses the current `.trayector/VERSION` as the previous release baseline, derives the corresponding Trayector tag, compares it with the selected new release and preserves local customizations through a three-way merge.

If both the local profile and Trayector changed the same instruction in incompatible ways, the workflow preserves the local file and opens a pull request containing the incoming candidate and a conflict report. The profile owner reviews and resolves those differences before merging.

Trayector updates MUST NOT silently overwrite profile-specific customizations.

## Profile Kit contents

Typical Profile Kit files include:

- `profile-rules.md` — how to read and modify the canonical career profile.
- `resume-generation.md` — how to generate truthful tailored résumés and PDFs.
- `resume/basic.md` — default résumé presentation template.
- `settings/` — profile-owned configuration split by concern.
- `VERSION` — Profile Kit version and release baseline.

A profile may add more files or customize these files locally.

Source: https://github.com/demonccc/trayector
