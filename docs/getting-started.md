# Getting Started

Trayector is designed to be useful before any CLI, service or AI integration exists. The first implementation is deliberately boring: **Markdown, YAML, JSON and Git**.

The recommended workflow is guided and source-first: collect what already exists, build the canonical profile, resolve only the ambiguities that matter, and generate the README last as the public index of the profile.

## 1. Collect your source material

Start with whatever already exists:

- current and historical CVs;
- LinkedIn profile information;
- project notes;
- public repositories;
- articles, talks and presentations;
- recommendations and testimonials;
- architecture notes;
- personal notes about work that never fit in a CV.

These sources are inputs. They are not automatically canonical Trayector content and do not need to be committed to the public profile repository.

If you are using AI, read [AI-Assisted Profile Creation](ai-assisted-profile.md) before generating profile files.

## 2. Create your career repository

Create a repository such as:

```text
username-career
my-career
professional-profile
```

The repository name is yours. It does not need to contain `trayector`.

## 3. Start with this structure

```text
my-career/
├── README.md
├── TRAYECTOR.md
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
├── feedback/
├── content/
└── generated/
```

You do not need to use every directory. Add only what represents your career.

`README.md` is a profile view and index. `TRAYECTOR.md` is an optional small implementation note that points to the Trayector version and specification. `profile.json` is the machine-readable entry point.

## 4. Define your profile vocabulary

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

## 5. Add the machine-readable entry point

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
    "feedback": "feedback/",
    "content": "content/"
  }
}
```

## 6. Build the canonical profile before the README

Start with the knowledge itself:

1. `profile/summary.md` — who you are now;
2. `profile/career-timeline.md` — the chronological view;
3. current and previous major experiences;
4. capabilities you can actually demonstrate;
5. projects, deep dives and stories that provide evidence;
6. education, feedback and content when relevant.

Do not begin by writing a polished repository README. The README is a derived view and is easier to build correctly after the canonical profile exists.

## 7. Document experience, not just employment

Create one experience document for a coherent employment or professional-engagement period.

An experience may include role progression when the organizational context remains continuous. Split it when there are genuinely separate employment periods, clearly different engagements, or a scope change that benefits from its own independent context. Do not create extra documents solely because a title changed.

Use [`../templates/experience-template.md`](../templates/experience-template.md).

## 8. Make contribution explicit

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

## 9. Connect capabilities to evidence

Do not infer capability from titles alone.

A capability may be demonstrated by work experience, personal projects, labs, publications, open-source contributions, talks or other relevant work.

Avoid capability lists that are only keyword inventories. Link them to inspectable evidence whenever possible.

## 10. Use deep dives when a bullet is not enough

An experience document should remain navigable. If an initiative needs architecture diagrams, failure modes, constraints and detailed trade-offs, create a deep dive and link to it.

Use [`../templates/case-study-template.md`](../templates/case-study-template.md).

## 11. Treat personal work as first-class evidence

A personal project is not automatically less valuable than paid work.

If it demonstrates real knowledge, document it.

Use [`../templates/project-template.md`](../templates/project-template.md).

## 12. Keep your writing with your career

Trayector treats professional writing as content, without forcing the directory structure to decide whether something is a post, article, note, talk or another owner-defined classification.

Every content item uses the same shape:

```text
content/
└── 2026-05-22-t-shape-ia-square-shape/
    ├── content.esp.md
    └── assets/
        └── square-shape-seniority.jpg
```

The directory carries the date and slug. The filename carries the language key defined in `settings.yaml`. Do not repeat information in metadata when it can be derived reliably from the path.

Classification belongs in YAML front matter and resolves through `settings.yaml`.

Use [`../templates/content-template.md`](../templates/content-template.md).

## 13. Build the README as the profile index

Once the canonical profile exists, build `README.md` as the primary human-facing index.

It should present the person, not explain Trayector.

A useful README usually includes:

- a concise professional introduction;
- current focus;
- major capability areas;
- links to the career timeline and experience;
- selected projects / evidence;
- selected content;
- feedback and education when useful.

Use [`../templates/readme-template.md`](../templates/readme-template.md).

Trayector implementation details belong in `profile.json`, the optional `TRAYECTOR.md`, and the Trayector repository itself.

## 14. Version it

Your career evolves. Your profile should too.

Use normal Git workflows:

```bash
git add .
git commit -m "Add data platform case study"
git push
```

The history itself becomes useful context: when a capability appeared, when a project evolved, and how your thinking changed.

## What Trayector does not require

You do **not** need:

- a public code repository for every claim;
- source code at all;
- confidential company information;
- artificial metrics;
- a specific job title;
- a perfect career narrative;
- a globally fixed list of languages or content classifications;
- raw source documents to be committed to the public profile.

Evidence can be descriptive while respecting confidentiality. The goal is to make your contribution and reasoning inspectable, not to leak proprietary information.

## Next

Read the [AI-assisted guide](ai-assisted-profile.md) if you want AI to help reconstruct the profile, then read the [specification overview](../spec/README.md) and [design principles](../spec/principles.md).
