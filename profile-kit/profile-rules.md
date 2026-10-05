# Canonical Profile Rules

A Trayector profile separates **canonical career knowledge** from **derived views**.

## Canonical areas

Use `profile.json` as the machine-readable entry point and follow its navigation.

Canonical career knowledge normally lives in:

- `profile/`
- `experience/`
- `projects/`
- `deep-dives/`
- `stories/`
- `feedback/`
- `content/`

`README.md`, generated résumés, websites and PDFs are views. They may summarize canonical material but must not become independent sources of career truth.

## Source fidelity

When adding or updating career knowledge:

- use supplied CVs, LinkedIn data, repositories, notes, documents and user statements as source material;
- distinguish formal role, personal contribution, team contribution, capability, evidence and outcome;
- do not invent dates, titles, seniority, technologies, metrics, ownership or impact;
- do not silently resolve material contradictions;
- ask the profile owner only when an ambiguity materially changes the canonical representation;
- omit irrelevant source noise instead of forcing every source item into the profile.

## Contribution and evidence

Job titles provide context. They do not prove capability.

Capabilities should point to inspectable experience, projects, deep dives, stories or content whenever possible.

Recommendations and testimonials can provide external perspective but are not technical proof by themselves.

## Structure

Prefer plain Markdown, YAML, JSON and Git.

YAML front matter, when used, must be the first block in the Markdown document.

Do not duplicate metadata that can be reliably derived from paths or filenames.

Use stable IDs for machine-readable relationships where entities have explicit IDs.

## Updating views

After changing canonical knowledge, derived views may need regeneration.

For README generation, summarize and link to canonical material.

For résumé generation, follow `resume-generation.md`.
