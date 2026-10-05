# Getting Started

Trayector is designed to be useful before any CLI, service or AI integration exists. The first implementation is deliberately boring: **Markdown, YAML, JSON and Git**.

The recommended workflow is guided and source-first: collect what already exists, build the canonical profile, resolve only the ambiguities that matter, and generate derived views such as README files and tailored résumés from that canonical knowledge.

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
├── .trayector/
│   ├── README.md
│   ├── profile-rules.md
│   ├── resume-generation.md
│   ├── VERSION
│   └── resume/
│       └── basic.md
├── .github/
│   └── workflows/
│       └── update-trayector.yml
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

You do not need to use every canonical career directory. Add only what represents your career.

`README.md` is a profile view and index. `TRAYECTOR.md` is an optional small implementation note. `profile.json` is the machine-readable entry point. `.trayector/` contains managed instructions for AI agents and profile tooling.

## 4. Install the Trayector Profile Kit

Copy the upstream `profile-kit/` directory from Trayector into `.trayector/` in the profile repository.

Then install the updater workflow from:

```text
templates/github/update-trayector.yml
```

as:

```text
.github/workflows/update-trayector.yml
```

The workflow checks Trayector `main` for Profile Kit changes and opens a pull request when the managed instructions change.

The updater owns only `.trayector/`. It must not rewrite personal career data automatically.

See [Trayector Profile Kit](profile-kit.md).

## 5. Define your profile vocabulary

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

## 6. Add the machine-readable entry point

`profile.json` tells tools where the important parts of the repository live and where managed Trayector instructions can be found.

Example:

```json
{
  "trayector_version": "0.1",
  "trayector": {
    "instructions": ".trayector/README.md",
    "profile_kit_version": ".trayector/VERSION"
  },
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
    "content": "content/",
    "generated": "generated/"
  }
}
```

An AI entering the repository should read `profile.json`, follow `trayector.instructions`, then traverse canonical career knowledge through `navigation`.

## 7. Build the canonical profile before the README

Start with the knowledge itself:

1. `profile/summary.md` — who you are now;
2. `profile/career-timeline.md` — the chronological view;
3. current and previous major experiences;
4. capabilities you can actually demonstrate;
5. projects, deep dives and stories that provide evidence;
6. education, feedback and content when relevant.

Do not begin by writing a polished repository README. The README is a derived view and is easier to build correctly after the canonical profile exists.

## 8. Document experience, not just employment

Create one experience document for a coherent employment or professional-engagement period.

An experience may include role progression when the organizational context remains continuous. Split it when there are genuinely separate employment periods, clearly different engagements, or a scope change that benefits from its own independent context. Do not create extra documents solely because a title changed.

Use [`../templates/experience-template.md`](../templates/experience-template.md).

## 9. Make contribution explicit

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

## 10. Connect capabilities to evidence

Do not infer capability from titles alone.

A capability may be demonstrated by work experience, personal projects, labs, publications, open-source contributions, talks or other relevant work.

Avoid capability lists that are only keyword inventories. Link them to inspectable evidence whenever possible.

## 11. Use deep dives when a bullet is not enough

An experience document should remain navigable. If an initiative needs architecture diagrams, failure modes, constraints and detailed trade-offs, create a deep dive and link to it.

Use [`../templates/case-study-template.md`](../templates/case-study-template.md).

## 12. Treat personal work as first-class evidence

A personal project is not automatically less valuable than paid work.

If it demonstrates real knowledge, document it.

Use [`../templates/project-template.md`](../templates/project-template.md).

## 13. Keep your writing with your career

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

## 14. Build the README as the profile index

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

Trayector implementation details belong in `profile.json`, the optional `TRAYECTOR.md`, and `.trayector/`.

## 15. Generate tailored résumés as derived views

When applying to a role, provide the target job description to the AI or tool and ask it to generate a tailored résumé from the canonical profile.

The generator should:

1. analyze the target role;
2. map requirements to supported profile evidence;
3. use a selected résumé template;
4. emphasize and reorder only real supported information;
5. validate every substantive claim;
6. generate the source résumé;
7. render a PDF from the reviewed source when PDF tooling is available.

Use the managed `.trayector/resume-generation.md` instructions inside the profile repository.

Trayector also documents the workflow in [Tailored Résumés](tailored-resumes.md).

Generated application-specific outputs can live under:

```text
generated/resumes/<target-slug>/
```

They are views, not canonical career data.

## 16. Version it

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

Read the [Profile Kit guide](profile-kit.md), the [AI-assisted guide](ai-assisted-profile.md), the [Tailored Résumés guide](tailored-resumes.md), then the [specification overview](../spec/README.md) and [design principles](../spec/principles.md).
