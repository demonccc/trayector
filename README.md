# Trayector

> **Version your career. Prove what you know.**

**Trayector is an open implementation of Career as Code.**

A career is larger than a résumé, a job title, or an employment history. It also includes the systems you designed, the problems you solved, the projects you built, the teams you led, the things you learned, the ideas you published, the experiments that failed, and the evidence behind all of it.

Trayector provides a structured, versioned, portable way to represent that knowledge so it can be read by people and consumed by machines.

**Human-readable. Machine-readable. Evidence-backed. Portable. Yours.**

## Why

Traditional résumés are optimized for summarization. That is useful, but lossy.

A title can tell someone where you worked and roughly what your role was. It cannot reliably tell them what you actually know or what you actually did.

An Engineering Manager may have designed a large-scale data architecture. A QA Lead may have built an internal platform. A developer may have learned more about distributed systems through a personal lab than through a formal job assignment.

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

## What can live in a Trayector profile?

Anything that forms part of your career or demonstrates professional knowledge, including:

- employment experience and role changes;
- technical and organizational initiatives;
- architecture decisions and trade-offs;
- projects, open source, labs and homelabs;
- courses, research and experiments;
- achievements and failures;
- lessons learned;
- articles, posts, talks and publications;
- mentoring and leadership work;
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

A simplified relationship can look like this:

```text
Person
  ├── held_role ─────────> Engineering Manager
  ├── demonstrated ──────> Big Data Architecture
  ├── designed ──────────> Data Platform
  ├── led ───────────────> Platform Team
  └── published ─────────> Architecture Article
                              │
                              └── evidence / context / outcome
```

## How do I use it?

You create **your own career repository**. Trayector defines the structure and conventions; your repository contains your information.

A typical profile looks like this:

```text
my-career/
├── README.md
├── profile.json
├── profile/
│   ├── summary.md
│   ├── career-timeline.md
│   ├── capabilities.md
│   └── education.md
├── experience/
├── deep-dives/
├── projects/
├── stories/
├── content/
│   ├── posts/
│   ├── articles/
│   └── talks/
└── generated/
```

Then:

1. Create a Git repository for your career profile.
2. Add `profile.json` as the machine-readable entry point.
3. Copy the relevant templates from [`templates/`](templates/).
4. Document your experience using Markdown plus structured front matter.
5. Connect capabilities to real evidence instead of relying on titles alone.
6. Commit changes as your career evolves.
7. Publish anywhere you want. Your repository remains the source of truth.

See **[Getting Started](docs/getting-started.md)** for a complete example.

## The source-of-truth principle

LinkedIn, Medium, a personal website, a résumé PDF, an ATS profile, or an AI assistant are distribution and presentation channels.

Your professional knowledge should not depend on any of them.

With Trayector, the canonical source stays under your control and can later be rendered, indexed, queried, summarized, or exported.

> **LinkedIn is a channel. Your career profile is the source of truth.**

## Repository structure

This repository contains the Trayector specification and reference material:

```text
trayector/
├── README.md
├── LICENSE
├── NOTICE
├── docs/
│   └── getting-started.md
├── spec/
│   ├── README.md
│   └── principles.md
├── templates/
│   ├── profile-template.md
│   ├── experience-template.md
│   ├── case-study-template.md
│   ├── project-template.md
│   ├── story-template.md
│   └── content-template.md
├── schemas/
│   └── profile.schema.json
├── taxonomy/
│   └── README.md
└── examples/
    └── minimal-profile/
```

## Design principles

Trayector is built around a few rules:

- **Evidence over titles.** A title is context, not proof.
- **Contribution must be explicit.** Team achievements and personal contributions are not the same thing.
- **Career is larger than employment.** Personal projects, research, labs, writing and community work count.
- **Humans first, machines too.** Markdown remains useful without any special tooling.
- **Open formats.** Your career should not be trapped in a proprietary platform.
- **One source, many views.** Résumés, websites and social posts can be generated from the same underlying knowledge.
- **Do not invent evidence.** Unknown or unverified information should remain unknown or unverified.

Read the full set in [`spec/principles.md`](spec/principles.md).

## Status

Trayector is currently an early specification (`v0.x`). The information model will evolve as real profiles exercise it.

The initial focus is deliberately simple:

1. define the model;
2. make it pleasant to maintain manually;
3. validate it;
4. generate indexes and views;
5. add query and AI tooling later.

## License

Trayector is licensed under the **Apache License 2.0**.

The specification and reference implementation are intentionally open and may be adopted by individuals, companies, platforms and tools under the terms of that license.

The goal is adoption and portability: if a platform wants to support Trayector profiles, it should be able to do so.

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

## Contributing

Trayector should be shaped by real careers, not just by theoretical schemas.

If the model cannot represent an important part of your professional experience without forcing it into the wrong concept, that is useful feedback.

Issues and pull requests are welcome.
