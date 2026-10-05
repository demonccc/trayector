---
classification: example
status: draft
topics: []
---

# [Content Title]

[Canonical content lives here. Publish or adapt it to external channels as needed.]

## Publications

- [Channel]: [Published URL]

## Sources

- [Source title, document, repository, or URL]
- [Additional source]

## Related content

- [Optional local content bundle path or external URL]

## Content bundle

Every content item uses the same directory shape, regardless of whether the owner considers it a post, article, note, talk, essay or something else:

```text
<date>-<slug>/
├── content.<language-code>.md
└── assets/
    └── [optional files]
```

The directory identifies the content item. `content.<language-code>.md` identifies a language variant of that item. Assets belong to the item and are shared across language variants unless an asset itself is localized.

## User-defined vocabulary

Trayector does not impose a universal list of content classifications or languages. The profile owner defines those values under `.trayector/settings/`.

For example:

```text
.trayector/settings/
├── languages.yaml
└── classifications.yaml
```

A document can then use:

```yaml
classification: linkedin-post
```

and a Spanish variant is stored as:

```text
content.esp.md
```

The key is intentionally owner-defined. A human or AI can resolve its meaning by reading the corresponding settings file.

## Avoid redundant metadata

Do not duplicate information that can be derived reliably from the path. In particular, the content date comes from the bundle directory and the language code comes from the Markdown filename.

Keep publications, sources and related content in Markdown lists when they are primarily useful to humans. Use front matter only for compact machine-oriented fields that benefit from structured parsing.

Reference assets directly from Markdown so placement and meaning remain part of the canonical content:

```markdown
![Architecture overview](assets/architecture.webp)
```

Use useful alt text. Do not add redundant asset lists to front matter when the Markdown already declares which assets are used.
