# Getting Started

Trayector is designed to be useful before any CLI, service or AI integration exists. The first implementation is deliberately boring: **Markdown, YAML, JSON and Git**.

## 1. Create your career repository

Create a repository such as:

```text
username-career
my-career
professional-profile
```

The repository name is yours. It does not need to contain `trayector`.

## 2. Start with this structure

```text
my-career/
├── README.md
├── profile.json
├── settings.yaml
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
└── generated/
```

You do not need to use every directory. Add only what represents your career.

## 3. Define your profile vocabulary

`settings.yaml` defines profile-owned vocabulary that humans and AI can understand by reading the file. Trayector does not require one universal classification system or one fixed language-code standard.

Example:

```yaml
languages:
  esp: Español
  eng: English
  br: Português do Brasil

classifications:
  linkedin-post: Publicación profesional en LinkedIn
  article: Artículo largo o de profundidad
  technical-note: Nota técnica enfocada en un tema concreto
```

The keys are intentionally owner-defined. You can rename them, remove them or add new ones.

Use [`../templates/settings.yaml`](../templates/settings.yaml) as a starting point.

## 4. Add the machine-readable entry point

`profile.json` tells tools where the important parts of the repository live.

Example:

```json
{
  "trayector_version": "0.1",
  "profile": {
    "name": "Alex Example",
    "headline": "Engineering Manager and distributed-systems practitioner",
    "location": "Remote"
  },
  "navigation": {
    "summary": "profile/summary.md",
    "timeline": "profile/career-timeline.md",
    "capabilities": "profile/capabilities.md",
    "experience": "experience/",
    "deep_dives": "deep-dives/",
    "projects": "projects/",
    "stories": "stories/",
    "content": "content/"
  }
}
```

## 5. Document experience, not just employment

Create one experience document for a coherent role/seniority period.

If you were promoted, changed scope substantially, or moved from IC to management inside the same company, use separate documents.

Example:

```text
experience/
└── acme/
    ├── senior-engineer.md
    └── engineering-manager.md
```

Use [`../templates/experience-template.md`](../templates/experience-template.md).

## 6. Make contribution explicit

Avoid ambiguous statements such as:

> Migrated the platform to Kubernetes.

Who did what?

Prefer:

```yaml
contribution:
  architecture: primary
  implementation: partial
  leadership: primary
```

Then explain the contribution in prose.

This lets a reader distinguish between work you personally designed, work you implemented, work you led, and achievements produced by a team you managed.

## 7. Connect capabilities to evidence

Do not infer capability from titles alone.

Instead of:

```text
Engineering Manager = Big Data Architect
```

represent the evidence:

```text
Capability: Big Data Architecture
Evidence:
- designed streaming ingestion architecture at ACME
- wrote architecture decision record for partitioning strategy
- built personal Kafka failure-mode lab
```

A capability may be demonstrated by work experience, personal projects, labs, publications, open-source contributions, talks or other relevant work.

## 8. Use deep dives when a bullet is not enough

An experience document should remain navigable. If an initiative needs architecture diagrams, failure modes, constraints and detailed trade-offs, create a deep dive and link to it.

```text
experience/acme/engineering-manager.md
                 │
                 └── ../../deep-dives/realtime-data-platform.md
```

Use [`../templates/case-study-template.md`](../templates/case-study-template.md).

## 9. Treat personal work as first-class evidence

A personal project is not automatically less valuable than paid work.

If it demonstrates real knowledge, document it:

```text
projects/
├── home-kubernetes-lab.md
├── openwrt-audio-platform.md
└── computer-vision-experiments.md
```

Use [`../templates/project-template.md`](../templates/project-template.md).

## 10. Keep your writing with your career

Trayector treats professional writing as content, without forcing the directory structure to decide whether something is a post, article, note, talk or another owner-defined classification.

Every content item uses the same shape:

```text
content/
└── 2026-05-22-t-shape-ia-square-shape/
    ├── content.esp.md
    └── assets/
        └── square-shape-seniority.jpg
```

A content item without assets simply omits `assets/`:

```text
content/
└── 2026-05-08-algoritmo-vs-criterio-seleccion/
    └── content.esp.md
```

Language variants live in the same item directory:

```text
content/
└── 2026-05-29-ai-engineering/
    ├── content.esp.md
    ├── content.eng.md
    └── assets/
        ├── architecture.webp
        └── model-strategies.webp
```

The directory carries the date and slug. The filename carries the language key defined in `settings.yaml`. Do not repeat information in metadata when it can be derived reliably from the path.

Classification belongs in front matter and resolves through `settings.yaml`:

```yaml
---
classification: linkedin-post
status: published
---
```

The publishing platform is a channel. It does not determine the content item's structure.

Use [`../templates/content-template.md`](../templates/content-template.md).

## 11. Version it

Your career evolves. Your profile should too.

Use normal Git workflows:

```bash
git add .
git commit -m "Add data platform case study"
git push
```

The history itself becomes useful context: when a capability appeared, when a project evolved, and how your thinking changed.

## What should I write first?

Do not try to reconstruct your entire career in one sitting.

A practical order is:

1. `profile/summary.md` — who you are now;
2. current and previous major roles;
3. 3–5 capabilities you can actually demonstrate;
4. one strong project or deep dive;
5. one story about something you would do differently;
6. expand backward through your career.

## What Trayector does not require

You do **not** need:

- a public code repository for every claim;
- source code at all;
- confidential company information;
- artificial metrics;
- a specific job title;
- a perfect career narrative;
- a globally fixed list of languages or content classifications.

Evidence can be descriptive while respecting confidentiality. The goal is to make your contribution and reasoning inspectable, not to leak proprietary information.

## Next

Read the [specification overview](../spec/README.md) and [design principles](../spec/principles.md), then copy whichever [templates](../templates/) you need.
