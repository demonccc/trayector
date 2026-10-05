# Trayector Specification

Current status: **v0.1 draft**

Trayector defines an open representation for Career as Code: professional knowledge expressed as structured, versioned, human-readable and machine-readable information.

The specification is intentionally file-based and tool-independent. A valid profile should remain useful when opened directly in a text editor or rendered by Git hosting, without requiring Trayector software.

## Core entities

A Trayector profile may contain the following entities:

- **Profile** — identity, headline and navigation entry point.
- **Experience** — a coherent employment or professional engagement period.
- **Capability** — something the person can demonstrate knowing or doing.
- **Contribution** — the person's actual participation in an initiative or outcome.
- **Evidence** — material or narrative supporting a professional claim.
- **Deep Dive** — detailed technical or organizational case study.
- **Project** — personal, open-source, lab, research or other project work.
- **Story** — cross-cutting career narrative that does not belong to one job.
- **Content** — professional writing, talks, notes and other intellectual output, without imposing a universal content taxonomy.

## Canonical knowledge and views

Trayector distinguishes the **canonical career model** from its **presentation views**.

Canonical knowledge lives in profile documents, structured metadata and relationships. A README, résumé, website, portfolio, ATS export or AI-generated summary is a view over that knowledge.

`README.md` SHOULD be treated as the default human-facing profile index, not as the canonical definition of the career itself.

A profile MAY include `TRAYECTOR.md` as a small human-readable implementation note that identifies the Trayector version and points to the specification. `profile.json` remains the machine-readable version declaration and navigation entry point.

See [Profile Views](profile-views.md).

## Required principles

Implementations MUST preserve these semantics:

1. Job titles MUST NOT be treated as proof of capability.
2. Individual contribution SHOULD be distinguished from team outcome.
3. Claims SHOULD reference evidence when evidence exists.
4. Unknown information MUST NOT be invented to satisfy a schema.
5. Markdown content SHOULD remain understandable without specialized tooling.
6. Machine-readable metadata SHOULD use stable identifiers where relationships are required.
7. Profiles MAY omit sections that are not relevant to the person.
8. Metadata SHOULD NOT duplicate information that can be derived reliably from the file path.
9. Trayector SHOULD define structure and semantics without imposing personal taxonomies that can be owned by the profile author.
10. Derived views SHOULD NOT become independent sources of professional truth when canonical knowledge exists elsewhere in the profile.

## Document format

Trayector documents use Markdown. Structured metadata SHOULD be represented with YAML front matter where relationships, classification or indexing are useful.

When YAML front matter is used, it MUST be the first block in the Markdown file so standard front-matter parsers can read it without Trayector-specific logic.

Example:

```yaml
---
id: exp-acme-engineering-manager
type: experience
organization: acme
period:
  from: 2024-01
  to: 2026-03
roles:
  - engineering-manager
capabilities:
  - distributed-systems
  - platform-engineering
related:
  deep_dives:
    - realtime-data-platform
---
```

The prose below the front matter describes context, contribution, decisions, evidence and outcomes.

Metadata fields are optional unless a specific schema says otherwise. Do not add fields such as `seniority` merely to fill a template when the source does not establish them or the role already carries the useful meaning.

## Profile-owned vocabulary

A profile MAY define human-readable vocabularies in `settings.yaml`. These vocabularies are intentionally owner-controlled rather than hard-coded into Trayector.

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

Keys MAY be renamed, removed or extended by the profile owner. Consumers SHOULD resolve the meaning of a key by reading `settings.yaml` rather than assuming a fixed external taxonomy.

A vocabulary entry SHOULD prefer a direct key-to-meaning mapping when that is sufficient. Wrapper fields such as `label` SHOULD NOT be required when they add no useful semantics.

## Content items

All content items SHOULD use the same structural convention regardless of classification:

```text
content/
└── <date>-<slug>/
    ├── content.<language-code>.md
    └── assets/
        └── [optional files]
```

A content item without local assets simply omits `assets/`.

The bundle directory identifies the content item. The date is derived from the directory name. The language key is derived from the Markdown filename and SHOULD resolve through `settings.yaml`.

Language variants of the same item live in the same directory.

Implementations SHOULD NOT require redundant `date`, `language`, `work_id` or `translation_of` metadata solely to express information already present in the path.

## Content classification and publication

Content classification is profile-owned metadata, not directory structure.

Example:

```yaml
---
classification: linkedin-post
status: published
publications:
  - channel: linkedin
    url: https://example.com/post
---
```

The publishing platform does not determine the content item's structure. A piece classified as `article`, `linkedin-post`, `technical-note` or any other owner-defined value uses the same bundle convention.

When linking one content item to another, implementations SHOULD prefer the content bundle directory rather than a specific language variant unless the relationship is explicitly language-specific.

## Content assets

Assets SHOULD be referenced directly from Markdown so their placement and semantic role remain part of the canonical content:

```markdown
![Architecture overview](assets/architecture.webp)
```

Shared assets SHOULD NOT be duplicated across language variants unless the asset itself is localized. Implementations SHOULD use meaningful alternative text for accessibility and machine interpretation.

## Contribution model

Trayector SHOULD make personal contribution explicit when an accomplishment could otherwise be ambiguous.

Recommended values are descriptive rather than numeric:

```yaml
contribution:
  ideation: primary
  architecture: primary
  implementation: partial
  leadership: primary
```

Implementations MAY extend contribution dimensions when necessary.

## Capability and evidence model

Capabilities are independent from formal positions.

A capability can be supported by one or more evidence references:

```yaml
capabilities:
  - id: big-data-architecture
    evidence:
      - deep-dive:realtime-data-platform
      - project:kafka-failure-lab
      - content:stream-partitioning-notes
```

A profile MAY contain claimed capabilities without evidence, but consumers SHOULD distinguish them from evidenced capabilities rather than silently treating both as equivalent.

## AI-assisted creation

AI MAY assist with profile reconstruction, normalization, linking and view generation.

An AI SHOULD read Trayector's specification and guidance before modeling supplied career sources. It SHOULD extract before rewriting, preserve source fidelity, flag material contradictions and ask the person to resolve ambiguities that materially affect the canonical profile.

The AI SHOULD create or update canonical knowledge before generating presentation views such as `README.md`.

See [AI-Assisted Profile Creation](../docs/ai-assisted-profile.md).

## Extensibility

Trayector is designed to be extensible.

Implementations MAY add metadata fields, document types and taxonomies as long as they do not change the meaning of required fields or break basic human readability.

Future versions will formalize compatibility and extension rules as real-world implementations expose the need.

## Versioning

Profiles declare the specification version in `profile.json`:

```json
{
  "trayector_version": "0.1"
}
```

The `0.x` series is experimental and may introduce breaking changes.

## Reference implementation

The repository itself is the reference specification. Tooling such as validation, generated indexes, exporters, query interfaces and AI integrations can be built on top of this model without becoming prerequisites for maintaining a profile.
