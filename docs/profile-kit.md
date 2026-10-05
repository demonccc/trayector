# Trayector Profile Kit

Trayector profiles can carry a local copy of the instructions an AI or profile tool needs to understand the repository.

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
- generate a README without turning it into the data model;
- generate a tailored résumé without inventing facts;
- render a PDF from the reviewed résumé source when its environment supports PDF generation.

`profile.json` can expose the instruction entry point and local release metadata:

```json
{
  "trayector_version": "0.1",
  "trayector": {
    "instructions": ".trayector/README.md",
    "profile_kit_version": ".trayector/VERSION",
    "profile_kit_ref": ".trayector/REF"
  }
}
```

## Version and release reference

Every installed Profile Kit SHOULD contain both:

```text
.trayector/VERSION
.trayector/REF
```

`VERSION` identifies the Profile Kit/specification version, for example:

```text
0.1.0
```

`REF` identifies the exact Trayector release tag the local kit is based on, for example:

```text
v0.1.0
```

Trayector uses Git tags as released Profile Kit baselines. A profile therefore knows both the semantic version it implements and the upstream release it was derived from.

Released tags SHOULD be treated as immutable.

## Local and customizable

`.trayector/` is framework guidance, but it belongs to the profile repository once installed.

The profile owner MAY customize it. Examples include:

- adding a preferred résumé template;
- refining instructions for how an AI should present the profile;
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

The repository owner chooses when to update and explicitly supplies the target Trayector release tag, such as `v0.2.0`. There is no scheduled background update and the updater does not follow `main` as a release source.

The workflow performs a three-way comparison using:

1. the previously accepted Trayector release stored in `.trayector/REF`;
2. the current local `.trayector/` files, including custom modifications;
3. the newly selected Trayector release tag.

This lets the workflow distinguish:

- upstream-only changes, which can be applied safely;
- local-only changes, which must be preserved;
- compatible changes on both sides, which can be merged automatically;
- incompatible changes on both sides, which require human resolution.

When there are changes, the workflow opens or updates a dedicated pull request. The PR is the review boundary: an update is never considered accepted until that PR is reviewed and merged.

## Conflict handling

The updater MUST NOT solve conflicts by blindly replacing local files.

When the same instruction changed locally and upstream and cannot be merged safely:

- the local file remains untouched;
- the incoming candidate is written under `.trayector/.update/incoming/`;
- `.trayector/.update/README.md` explains what needs review;
- `.trayector/REF` and `.trayector/VERSION` are not advanced automatically.

The profile owner resolves the conflict in the pull request, removes `.trayector/.update/`, updates `REF` and `VERSION` to the selected release, and only then merges.

This makes custom instructions first-class and reviewable rather than temporary local deviations.

## Update boundary

The updater only proposes changes inside `.trayector/`.

It does not modify canonical career data, generated résumés, README content or other profile files.

This boundary is important: a Trayector framework update can evolve the instructions an AI follows, but it does not automatically rewrite the person's career or presentation.

## AI bootstrap contract

An AI entering a Trayector profile should:

1. read `profile.json`;
2. follow `trayector.instructions` when present;
3. read `.trayector/README.md` and the referenced rules;
4. read `.trayector/VERSION` and `.trayector/REF` when provenance matters;
5. treat the local instructions as authoritative for this profile unless they contradict required Trayector semantics;
6. traverse canonical career knowledge using `profile.json` navigation;
7. generate or update derived views only after understanding the canonical profile.

This makes the repository itself the handoff between Trayector and whatever AI system is used.
