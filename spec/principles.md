# Design Principles

## 1. Evidence over titles

A title provides organizational context. It does not prove capability.

Trayector represents capabilities independently from formal roles and connects them to work that demonstrates them.

## 2. Career is larger than employment

Professional knowledge can come from paid work, personal projects, open source, labs, courses, research, writing, mentoring, community activity and experimentation.

The model does not assign lower value to knowledge simply because it was acquired outside an employer.

## 3. Contribution over proximity

Being near an initiative is not the same as designing or implementing it.

Profiles should describe what the person personally contributed and separate that from what a team or organization achieved.

## 4. Evidence is contextual

Evidence does not mean every claim requires public source code, a certificate or a public company document.

A useful evidence record may explain the problem, the person's contribution, decisions, constraints and outcome while respecting confidentiality.

## 5. Unknown is better than invented

Templates are guides, not forms that must be completely filled.

If a metric, date, scale or contribution cannot be stated confidently, omit it or mark it as unknown. Never fabricate information to satisfy structure.

## 6. Human-readable first

A Trayector profile should be useful when read directly on GitHub, GitLab, a text editor or any Markdown renderer.

Machine readability is added through structure and metadata, not by replacing prose with opaque data structures.

If a human needs to know Trayector internals to understand a file, the representation is probably too complicated.

## 7. Machine-readable too

Stable structure, metadata, relationships and indexes should make it possible for search engines, agents, recruiters and other tooling to navigate the same source that humans read.

The goal is deterministic interpretation without requiring unnecessary metadata.

## 8. One source, many views

A résumé, website, LinkedIn summary, interview brief, recruiter view or AI answer should be considered a projection of the career knowledge base, not an independent source of truth.

## 9. Portable by design

No proprietary platform should be required to preserve or interpret the core career record.

Plain files and open formats are the baseline.

## 10. Version the evolution

Professional identity changes over time. The repository history should be able to show that evolution naturally rather than pretending a career was always a polished final narrative.

## 11. Structure over imposed taxonomy

Trayector defines how information is represented, not how every person must classify their career.

When a vocabulary is personal or contextual, such as content classifications or language keys, the profile owner should be able to define it in readable configuration.

A consumer should be able to resolve that meaning by reading the repository itself.

## 12. Do not duplicate derivable information

Information that can be derived reliably from a path or filename should not be repeated only for convenience.

Prefer:

```text
2026-05-22-t-shape-ia-square-shape/content.esp.md
```

over repeating the date and language in front matter.

## 13. Plain data over descriptive wrappers

Prefer the simplest representation that preserves meaning.

For example:

```yaml
languages:
  esp: Español
  eng: English
```

is preferable to adding nested `label` fields when the key-to-value mapping already communicates the intended meaning.

## 14. Technical literacy, not coding, is the threshold

Trayector does not require users to be software developers.

It assumes that people working in technology can document their work clearly, maintain structured text and participate in a basic version-controlled workflow.

**No code required. Evidence required.**
