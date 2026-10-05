# Trayector Profile Kit

Trayector profiles can carry a local copy of the instructions and configuration an AI or profile tool needs to understand the repository.

This copy lives at:

```text
.trayector/
```

The upstream source for those files lives in the Trayector repository under:

```text
profile-kit/
```

## Why keep instructions inside the profile?

An AI should not need prior knowledge of Trayector or an external conversation to work correctly with a profile.

A repository should be self-describing enough that an agent can:

- find the canonical entry point;
- distinguish canonical knowledge from derived views;
- understand contribution and evidence rules;
- resolve local configuration such as language and classification keys;
- generate a README without turning it into the data model;
- generate a tailored résumé without inventing facts;
- render a PDF from the reviewed résumé source when its environment supports PDF generation.

`profile.json` can expose the instruction entry point, local Profile Kit version and settings directory:

```json
{
  "trayector_version": "0.1",
  "trayector": {
    "instructions": ".trayector/README.md",
    "profile_kit_version": ".trayector/VERSION",
    "settings": ".trayector/settings/"
  }
}
```

## Version and release baseline

Every installed Profile Kit SHOULD contain:

```text
.trayector/VERSION
```

Example:

```text
0.1.0
```

Trayector uses immutable Git tags for released versions. By convention, Profile Kit version `0.1.0` maps to Trayector tag `v0.1.0`.

The version therefore identifies both the local Profile Kit contract and the upstream release baseline. A separate local `REF` file is unnecessary.

Released tags SHOULD be treated as immutable.

## Settings

Profile-owned configuration lives under:

```text
.trayector/settings/
```

Each file represents one configurable area rather than accumulating unrelated settings in one root file.

The default Profile Kit includes:

```text
.trayector/settings/
├── languages.yaml
└── classifications.yaml
```

A profile MAY add more settings files when a real configurable concern appears.

Settings are configuration, not canonical career facts.

## Local and customizable

`.trayector/` is framework guidance and configuration, but it belongs to the profile repository once installed.

The profile owner MAY customize it. Examples include:

- adding a preferred résumé template;
- refining instructions for how an AI should present the profile;
- changing language or classification keys;
- adding local conventions for generated artifacts;
- adapting wording or ordering rules while preserving Trayector semantics.

Those customizations are intentional profile configuration and MUST NOT be discarded by an upstream update.

Career facts themselves still belong in the canonical profile areas, not in `.trayector/`.

## Keeping the Profile Kit updated

Trayector provides a GitHub Actions template:

```text
templates/github/update-trayector.yml
```

A profile repository installs it as:

```text
.github/workflows/update-trayector.yml
```

The update is **manual only** through `workflow_dispatch`.

The repository owner chooses when to update and explicitly supplies the target Trayector version, such as `0.2.0`. The updater resolves it to tag `v0.2.0`. There is no scheduled background update and the updater does not follow `main` as a release source.

The workflow performs a three-way comparison using:

1. the previously accepted version in `.trayector/VERSION`, resolved to its Trayector release tag;
2. the current local `.trayector/` files, including custom instructions, templates and settings;
3. the newly selected Trayector release version.

This lets the workflow distinguish upstream-only changes, local-only changes, compatible changes on both sides, and conflicts that require human resolution.

When there are changes, the workflow opens or updates a dedicated pull request. The PR is the review boundary: an update is never considered accepted until that PR is reviewed and merged.

## Conflict handling

The updater MUST NOT solve conflicts by blindly replacing local files.

When the same instruction, template or setting changed locally and upstream and cannot be merged safely:

- the local file remains untouched;
- the incoming candidate is written under `.trayector/.update/incoming/`;
- `.trayector/.update/README.md` explains what needs review;
- `.trayector/VERSION` is not advanced automatically.

The profile owner resolves the conflict in the pull request, removes `.trayector/.update/`, updates `VERSION` to the selected release version, and only then merges.

## Update boundary

The updater only proposes changes inside `.trayector/`.

It does not modify canonical career data, generated résumés, README content or other profile files.

## AI bootstrap contract

An AI entering a Trayector profile should:

1. read `profile.json`;
2. follow `trayector.instructions` when present;
3. read `.trayector/README.md` and the referenced rules;
4. read the relevant files under `.trayector/settings/`;
5. read `.trayector/VERSION` when provenance matters;
6. treat the local instructions and settings as authoritative for this profile unless they contradict required Trayector semantics;
7. traverse canonical career knowledge using `profile.json` navigation;
8. generate or update derived views only after understanding the canonical profile.

This makes the repository itself the handoff between Trayector and whatever AI system is used.
