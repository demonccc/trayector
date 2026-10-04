# [Content Title]

---
type: [post / article / talk / note]
status: [draft / published / archived]
topics:
  - [Topic ID]
publications:
  - channel: [linkedin / medium / blog / other]
    url: [Published URL]
related_content:
  - [Optional local path or external URL]
---

[Canonical content lives here. Publish or adapt it to external channels as needed.]

## File naming

Use the filename to carry information that can be derived reliably from the path instead of duplicating it in metadata.

For standalone content:

```text
<date>-<slug>.<lang>.md
```

Example:

```text
2026-10-04-what-a-cv-does-not-show.es.md
2026-10-04-what-a-cv-does-not-show.en.md
```

Files with the same date and slug represent language variants of the same work.

## Content bundles

When a piece has meaningful assets such as diagrams, images or downloadable material, keep it as a directory:

```text
<date>-<slug>/
├── article.es.md
├── article.en.md
└── assets/
    ├── architecture.webp
    └── diagram.webp
```

Language remains encoded in the Markdown filename. Shared assets MUST NOT be duplicated per language unless the asset itself is localized.

Reference assets directly from Markdown so placement and meaning remain part of the canonical content:

```markdown
![Architecture overview](assets/architecture.webp)
```

Use useful alt text. Do not add redundant asset lists to front matter when the Markdown already declares which assets are used.
