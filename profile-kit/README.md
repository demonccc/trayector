# Trayector Profile Kit

This directory is a **local copy of Trayector guidance for AI agents and profile tooling**.

It belongs inside a Career as Code profile so an AI can understand how to read the repository, update canonical career knowledge, and generate derived views such as README files and tailored résumés without needing prior conversational context.

## Important

The files under `.trayector/` may be customized by the profile owner.

That means they are not disposable generated files and an update from Trayector MUST NOT replace them blindly.

Trayector provides the upstream defaults and evolution path, while each profile may adapt those instructions to its own workflow, preferred résumé templates, presentation rules or additional guidance.

Personal career facts still belong in the canonical profile areas such as `profile/`, `experience/`, `projects/`, `deep-dives/`, `stories/`, `feedback/` and `content/`. `.trayector/` contains instructions about how to interpret and present that knowledge.

## AI: start here

When working on this profile:

1. Read `profile.json` at the repository root.
2. Read `settings.yaml` when present.
3. Read this file and `profile-rules.md`.
4. Follow the canonical navigation from `profile.json`.
5. Treat canonical profile documents as the source of professional truth.
6. Never invent missing career facts.
7. Treat README files, tailored résumés and PDFs as derived views.
8. For a tailored résumé, read `resume-generation.md` and the selected template under `resume/`.
9. Respect local changes inside `.trayector/`; they are part of this profile's instructions.
10. Read `.trayector/VERSION` and `.trayector/REF` when you need to know which Trayector release this local kit is based on.

## Version and release reference

An installed Profile Kit carries two small provenance files:

- `VERSION` — semantic Profile Kit/specification version, such as `0.1.0`.
- `REF` — immutable Trayector release tag used as the upstream baseline, such as `v0.1.0`.

Trayector uses release tags rather than `main` as update baselines.

## Updating this kit

Updates are intentionally **manual and review-driven**.

The repository owner chooses when to run the Trayector update workflow and explicitly selects a target release tag. There is no scheduled update.

The workflow compares three states:

- the previous Trayector release recorded in `.trayector/REF`;
- the current local `.trayector/` files, including custom changes;
- the newly selected Trayector release tag.

Non-conflicting upstream changes can be merged automatically while preserving local modifications.

If both the local profile and Trayector changed the same instruction in incompatible ways, the workflow preserves the local file and opens a pull request containing the incoming candidate and a conflict report. The profile owner reviews and resolves those differences before merging.

Trayector updates MUST NOT silently overwrite profile-specific customizations.

## Profile Kit contents

Typical Profile Kit files include:

- `profile-rules.md` — how to read and modify the canonical career profile.
- `resume-generation.md` — how to generate truthful tailored résumés and PDFs.
- `resume/basic.md` — default résumé presentation template.
- `VERSION` — Profile Kit version identifier.

A profile may add more files or customize these files locally.

`REF` is written in the profile repository when a tagged Trayector release is installed or accepted. It is not part of the reusable upstream defaults because its value depends on the release chosen by that profile.

Source: https://github.com/demonccc/trayector
