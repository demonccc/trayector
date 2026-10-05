# Trayector Profile Kit

Trayector profiles can carry a managed copy of the instructions an AI or profile tool needs to understand the repository.

This managed copy lives at:

```text
.trayector/
```

The source for those files lives in the Trayector repository under:

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

`profile.json` can expose the managed instruction entry point:

```json
{
  "trayector_version": "0.1",
  "trayector": {
    "instructions": ".trayector/README.md",
    "profile_kit_version": ".trayector/VERSION"
  }
}
```

## Managed, not personal

`.trayector/` is framework guidance, not career content.

Profile owners should not customize those files to describe themselves. Personal career truth belongs in the canonical profile areas.

If project-specific guidance is needed, keep it outside `.trayector/` so upstream updates remain clean and reviewable.

## Keeping the Profile Kit updated

Trayector provides a GitHub Actions template:

```text
templates/github/update-trayector.yml
```

A profile repository installs it as:

```text
.github/workflows/update-trayector.yml
```

The workflow:

1. checks out the profile repository;
2. checks out `demonccc/trayector@main`;
3. copies `profile-kit/` into `.trayector/`;
4. does nothing when there is no difference;
5. when instructions changed, pushes a dedicated update branch;
6. opens a pull request for review.

Updates are intentionally PR-based. Trayector guidance should never silently rewrite a person's profile repository.

The workflow also supports `workflow_dispatch` so an owner can check for updates manually.

## Update boundary

The updater owns only `.trayector/`.

It does not modify canonical career data, generated résumés, README content or other profile files.

This boundary is important: a Trayector framework update can change the instructions an AI follows, but it does not automatically rewrite the person's career.

## AI bootstrap contract

An AI entering a Trayector profile should:

1. read `profile.json`;
2. follow `trayector.instructions` when present;
3. read `.trayector/README.md` and the referenced rules;
4. then traverse canonical career knowledge using `profile.json` navigation;
5. generate or update derived views only after understanding the canonical profile.

This makes the repository itself the handoff between Trayector and whatever AI system is used.
