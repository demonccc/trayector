# Trayector

> **Version your career. Prove what you know.**

**Trayector is an open implementation of Career as Code.**

A career is larger than a résumé, a job title, or an employment history. It also includes the systems you designed, the problems you solved, the projects you built, the teams you led, the things you learned, the ideas you published, the experiments that failed, and the evidence behind all of it.

Trayector provides a structured, versioned, portable way to represent that knowledge so it can be read by people and consumed by machines.

**Human-readable. Machine-readable. Evidence-backed. Portable. Yours.**

## Why

Traditional résumés are optimized for summarization. That is useful, but lossy.

A title can tell someone where you worked and roughly what your role was. It cannot reliably tell them what you actually know or what you actually did.

Trayector treats the job title as **context**, not as proof of capability.

Its central idea is:

> **Professional claims should be inspectable.**

A capability should be connected to context, contribution, evidence, and outcomes whenever possible.

## Career as Code

Career as Code applies familiar engineering practices to professional knowledge:

- plain-text, open formats;
- version control;
- explicit structure and relationships;
- portable data;
- reviewable changes;
- machine-readable metadata;
- human-readable narratives;
- evidence instead of title inference.

Trayector is one implementation of that concept.

It is **not** a résumé generator, an ATS optimizer, a LinkedIn replacement, or a portfolio theme.

Those can all become **views or consumers** of a Trayector profile.

## Canonical knowledge and views

Trayector separates the career model from the way it is presented.

Canonical career knowledge lives in structured profile documents such as experience, projects, capabilities, stories, deep dives, feedback and content.

The repository `README.md` is the default human-facing **profile index**, not the career model itself. It can summarize and link to canonical knowledge, and it can be regenerated when the profile changes.

A profile may also include a small `TRAYECTOR.md` file that identifies the Trayector version and points to the specification without turning the personal README into documentation about Trayector.

See [Profile Views](spec/profile-views.md).

## Local Trayector release

Every personal profile declares one immutable Trayector release in `.trayector/settings/trayector.yaml` using `version: 0.1.0`. A version bundle at `.trayector/versions/<version>/` contains operational **skills** and mandatory **templates**. The agent must use a template as the structural contract when reading, creating or updating any record; templates are not optional examples.

The nine skills are: initialize, profile, experience, projects, publications, contributions, **manage-resumes**, publish and manage-trayector. Agent entry points load the active version and its `skills/index.md`. CVs are derived Markdown under `cv/` and follow `templates/resumes/`.

The optional website implementation remains in the central Trayector repository: HTML/CSS, Markdown renderer and a GitHub Pages reusable workflow pinned to the same release tag. The personal repository keeps only the publishing configuration, professional documents and small GitHub Actions callers. See [Publishing](docs/site-publishing.md) and [Profile Kit](docs/profile-kit.md).

A manually triggered update proposes a PR installing both skills **and templates** for the new release while preserving older versions and personal content. The user chooses when to merge. No automatic migration of canonical career records.

## What can live in a Trayector profile?

Anything that forms part of your career or demonstrates professional knowledge, including:

- employment experience and role changes;
- technical and organizational initiatives;
- architecture decisions and trade-offs;
- projects, open source, labs and homelabs;
- courses, research and experiments;
- achievements and failures;
- lessons learned;
- professional content and publications;
- mentoring and leadership work;
- recommendations and testimonials;
- demonstrated capabilities and the evidence behind them.

No code is required.

**Technical literacy and evidence are.**

## Core model

Trayector separates concepts that résumés frequently collapse together:

```text
Role
  Where were you and what was your formal responsibility?

Contribution
  What did you personally do?

Capability
  What does that work demonstrate you can do?

Evidence
  What supports that claim?

Outcome
  What happened as a result?
```

## How do I use it?

You create **your own career repository**. Trayector defines structural conventions; your repository contains your information and owns local configuration and vocabularies.

A typical profile contains `PROFILE.md`, `profile/`, `experience/`, `projects/`, `content/`, `cv/` and `.trayector/` with versioned skills and templates. An AI agent can initialize the profile from a CV or through guided questions; Git expertise is not required from the profile owner.

See [Getting Started](docs/getting-started.md) for the guided flow.

If AI will help reconstruct the profile, use [AI-Assisted Profile Creation](docs/ai-assisted-profile.md).

For application-specific CVs, use [Tailored Résumés](docs/tailored-resumes.md).

## The source-of-truth principle

LinkedIn, Medium, a personal website, a résumé PDF, an ATS profile, an AI assistant, or the repository README itself are presentation or distribution views.

Your professional knowledge should not depend on any of them.

With Trayector, the canonical source stays under your control and can later be rendered, indexed, queried, summarized, or exported.

> **LinkedIn is a channel. Your career profile is the source of truth.**

## Design principles

Trayector is built around a few rules:

- **Evidence over titles.** A title is context, not proof.
- **Contribution must be explicit.** Team achievements and personal contributions are not the same thing.
- **Career is larger than employment.** Personal projects, research, labs, writing and community work count.
- **Humans first, machines too.** Markdown remains useful without any special tooling.
- **Canonical knowledge, derived views.** README, résumés and PDFs present the profile; they are not independent sources of truth.
- **Local instructions are reviewable configuration.** `.trayector/` can evolve from upstream defaults without losing profile-specific customization.
- **Structure over imposed taxonomy.** The profile owner controls vocabularies that are personal or contextual.
- **Do not duplicate derivable information.** Paths and filenames should carry information when they can do so reliably.
- **Plain data over descriptive wrappers.** Do not add metadata ceremony that contributes no meaning.
- **Open formats.** Your career should not be trapped in a proprietary platform.
- **One source, many views.** Résumés, websites and social posts can be generated from the same underlying knowledge.
- **Do not invent evidence.** Unknown or unverified information should remain unknown or unverified.

Read the full set in [`spec/principles.md`](spec/principles.md).

## Status

Trayector is currently an early specification (`v0.x`). The information model will evolve as real profiles exercise it.

The initial focus is deliberately simple:

1. define the model;
2. make it pleasant to maintain manually or with AI assistance;
3. validate it against real careers;
4. generate indexes and views;
5. add query and automation tooling later.

## License

Trayector is licensed under the **Apache License 2.0**.

The specification and reference implementation are intentionally open and may be adopted by individuals, companies, platforms and tools under the terms of that license.

See [`LICENSE`](LICENSE).

## Contributing

Trayector should be shaped by real careers, not just by theoretical schemas.

If the model cannot represent an important part of your professional experience without forcing it into the wrong concept, that is useful feedback.

Issues and pull requests are welcome.

## AI discovery and updates

The canonical profile starts at `PROFILE.md`. Agent entry files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and Copilot instructions) all direct agents to `.trayector/settings/trayector.yaml` and the selected `.trayector/skills/<version>/index.md`; local extensions remain in `.trayector/skills/custom/`. Updating Trayector AI installs only a new immutable version directory by PR and does not change the active version or site customizations.

## Publishing implementation

The default HTML/CSS and Markdown renderer live in [`site/`](site/). Profiles call the release-pinned reusable [publish workflow](.github/workflows/publish.yml) using the small caller template at [`templates/github/publish.yml`](templates/github/publish.yml). The reusable workflow checks out its own exact release SHA, ensuring the workflow and static assets match. Publishing is opt-in and the default CV download requires an existing PDF. See [Publishing](docs/site-publishing.md).
