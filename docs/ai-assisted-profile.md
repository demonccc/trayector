# AI-Assisted Profile Creation

Trayector can be built manually, with AI assistance, or with a combination of both. AI is useful for extraction, normalization and drafting, but it should not invent professional history or silently resolve contradictions.

The recommended workflow is source-first and guided.

## 1. Collect source material

Start with whatever already exists:

- current and historical CVs;
- LinkedIn profile exports or copied profile sections;
- project notes;
- public repositories;
- articles, talks and presentations;
- recommendation or testimonial text;
- architecture notes;
- personal notes about work that never fit in a CV.

Raw source material is input, not automatically canonical Career as Code content. It MAY remain outside the public profile repository.

## 2. Read Trayector before modeling the career

An AI building a profile SHOULD first read:

1. `README.md` in the Trayector repository;
2. `spec/README.md`;
3. `spec/principles.md`;
4. `docs/getting-started.md`;
5. the relevant templates under `templates/`.

The AI must treat these as modeling guidance, not as career facts.

## 3. Extract before rewriting

The first pass SHOULD preserve source fidelity.

For each source, extract facts and candidate knowledge such as:

- organizations and periods;
- formal roles and role progression;
- responsibilities;
- personal contributions;
- team contributions;
- initiatives and systems;
- architecture and engineering decisions;
- technologies actually used;
- outcomes and metrics;
- projects and open-source work;
- learning, teaching and certifications;
- recommendations and testimonials;
- contradictions or uncertain facts.

Do not turn ambiguous statements into confident claims. Do not infer leadership, ownership, metrics, dates or seniority that the source does not support.

## 4. Resolve contradictions with the person

When sources disagree, the AI SHOULD ask focused questions instead of choosing the most convenient version.

Examples:

- two different start dates for the same employment period;
- a retrospective title that differs from the contemporary title;
- unclear distinction between personal contribution and team outcome;
- a project that may have happened during employment or as freelance work;
- an achievement with unclear ownership.

Only unresolved questions that materially affect the canonical profile need to be escalated. Minor noise can be left out.

## 5. Build canonical knowledge areas

Once the facts are sufficiently clear, create or update the canonical Trayector areas:

- `profile/` for summary, timeline, capabilities and education;
- `experience/` for coherent professional periods;
- `projects/` for personal, open-source, research, lab and freelance work;
- `deep-dives/` for initiatives that need architecture, constraints and trade-offs;
- `stories/` for cross-cutting lessons and career narratives;
- `feedback/` when the profile chooses to preserve recommendations or testimonials;
- `content/` for canonical professional writing.

Do not force every source item into the profile. Recruiter outreach, automated platform events, duplicated claims and irrelevant historical noise can remain outside the canonical career.

## 6. Connect capabilities to evidence

Capabilities SHOULD be supported by links to real experience, projects, deep dives, stories or content whenever possible.

Avoid keyword inventories with no inspectable support.

## 7. Build the README last

`README.md` is a profile view and index, not the canonical source of the career model.

Build it after the canonical profile exists.

The README SHOULD summarize and link to:

- current professional summary;
- major capability areas;
- career timeline;
- selected projects and evidence;
- feedback, when present;
- professional content;
- education and certifications.

It SHOULD NOT explain the Trayector specification in place of presenting the person.

A committed README can be regenerated as the canonical profile evolves.

## 8. Keep Trayector metadata separate from the profile view

A profile MAY include a small `TRAYECTOR.md` file that explains which Trayector version it follows and points to the specification.

`profile.json` remains the machine-readable entry point and declares `trayector_version`.

This keeps implementation details out of the public-facing profile index while preserving explicit compatibility information.

## 9. Generate tailored résumés from the profile

Once the canonical profile exists, an AI can also generate application-specific résumés without rewriting the career itself.

For each tailored résumé, the AI SHOULD read:

1. the target job description;
2. the candidate's `profile.json` and relevant canonical profile documents;
3. the selected résumé template, such as `templates/resume/basic.md`.

The AI MAY select, reorder, summarize and emphasize supported information according to the role.

It MUST NOT add unsupported experience simply because the job description contains a matching keyword.

See [`tailored-resumes.md`](tailored-resumes.md) for the detailed generation workflow and validation rules.

## Suggested AI instruction for profile creation

```text
Build a Career as Code profile using Trayector.

First read the Trayector specification, principles, getting-started guide and relevant templates. Then read all career source material I provide.

Treat the source material as evidence, not as a schema. Extract before rewriting.

Do not invent dates, titles, seniority, metrics, technologies, ownership or outcomes. Do not silently resolve contradictions. Ask me only about ambiguities that materially affect the canonical profile.

Distinguish:
- formal role and organizational context;
- what I personally did;
- what a team did;
- capabilities demonstrated;
- evidence;
- outcomes.

Do not force every source item into the final profile. Exclude irrelevant noise such as recruiter outreach, automated platform events and duplicated information.

Create the canonical profile areas first. Build README.md last as a concise index and presentation view derived from the canonical profile.
```

## Suggested AI instruction for a tailored résumé

```text
Create a tailored résumé for the job description I provide.

Use my Trayector profile as the only source of professional facts. Start at profile.json and read the relevant canonical profile documents.

Use the selected résumé template as presentation guidance.

Analyze the target role first, then select, prioritize and summarize the parts of my real experience that best match it.

Do not invent or infer unsupported dates, titles, seniority, technologies, metrics, certifications, leadership scope, ownership, outcomes or capabilities.

If the job asks for something my profile does not support, do not add it.
```

## Validation mindset

A good AI-assisted Trayector profile or derived view should satisfy three tests:

1. **Human-readable:** a person can understand the career or résumé without special tooling.
2. **Machine-readable:** an AI or tool can traverse the structure and relationships without guessing the schema.
3. **Source-faithful:** claims are no stronger than the available canonical evidence.
