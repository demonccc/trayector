---
classification: [User-defined classification key]
status: [draft / published / archived]
topics:
  - [Topic ID]
publications:
  - channel: [Publication channel key]
    url: [Published URL]
related_content:
  - [Optional local content bundle path or external URL]
---

# [Content Title]

[Canonical content lives here. Publish or adapt it to external channels as needed.]

## Content bundle

Every content item uses the same directory shape, regardless of whether the owner considers it a post, article, note, talk, essay or something else:

```text
<date>-<slug>/
├── content.<language-code>.md
└── assets/
    └── [optional files]
```

Examples:

```text
2026-05-22-t-shape-ia-square-shape/
├── content.esp.md
└── assets/
    └── square-shape-seniority.jpg

2026-05-29-la-ia-no-elimino-la-ingenieria/
├── content.esp.md
├── content.eng.md
└── assets/
    ├── architecture.webp
    └── diagram.webp
```

The directory identifies the content item. `content.<language-code>.md` identifies a language variant of that item. Assets belong to the item and are shared across language variants unless an asset itself is localized.

## User-defined vocabulary

Trayector does not impose a universal list of content classifications or languages. The profile owner defines the vocabulary in `settings.yaml`.

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

A document can then use:

```yaml
classification: linkedin-post
```

and a Spanish variant is stored as:

```text
content.esp.md
```

The key is intentionally owner-defined. A human or AI can resolve its meaning by reading `settings.yaml`.

## Avoid redundant metadata

Do not duplicate information that can be derived reliably from the path. In particular, the content date comes from the bundle directory and the language code comes from the Markdown filename.

Reference assets directly from Markdown so placement and meaning remain part of the canonical content:

```markdown
![Architecture overview](assets/architecture.webp)
```

Use useful alt text. Do not add redundant asset lists to front matter when the Markdown already declares which assets are used.

When linking one content item to another, prefer the content bundle directory rather than a specific language variant unless the relationship is explicitly language-specific.
