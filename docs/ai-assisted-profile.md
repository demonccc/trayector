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
2. `skills/index.md`;
3. `skills/profile-rules.md`;
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

Once facts are clear enough, use the corresponding versioned templates to create or update:

- `profile/` for professional background;
- `experience/` for professional work contexts;
- `projects/` for initiatives the person created, developed or maintained significantly;
- `contributions/` for delimited contributions to other initiatives;
- `publications/` for external content, participations and registrations, including copyrights, using Description, My Participation, Link and optional Related;
- `articles/` for authored content stored in Markdown. Each article has one `README.md` index, with Summary, linked language versions under Content and optional Related. Every language file may have entirely free-form content.

Do not duplicate an authored article merely because it has an external distribution URL. Do not invent content, ownership or translations. An article is only added to the website's `articles.include` with explicit approval.

## 6. Connect capabilities to evidence

Capabilities SHOULD be supported by links to real experience, projects, contributions, publications or articles whenever possible.

Avoid keyword inventories with no inspectable support.

## 7. Build the README last

`README.md` is a profile view and index, not the canonical source of the career model.

Build it after the canonical profile exists.

The README SHOULD summarize and link to:

- current professional summary;
- major capability areas;
- career timeline;
- selected projects, contributions and evidence;
- feedback, when present;
- external publications and authored articles;
- education and certifications.

It SHOULD NOT explain the Trayector specification in place of presenting the person.

A committed README can be regenerated as the canonical profile evolves.

## 8. Keep Trayector metadata separate from the profile view

An agent should keep implementation details in `.trayector/` rather than adding an unnecessary profile metadata document.

`PROFILE.md` remains the professional navigation entry point. The active Trayector version is declared separately in `.trayector/settings/trayector.yaml`.

This keeps implementation details out of the public-facing profile index while preserving explicit compatibility information.

## 9. Generate tailored résumés from the profile

Once the canonical profile exists, an AI can also generate application-specific résumés without rewriting the career itself.

For each tailored résumé, the AI SHOULD read:

1. the target job description;
2. the candidate's `PROFILE.md` and relevant canonical profile documents;
3. the selected résumé template, such as `templates/resumes/basic.md`.

The AI MAY select, reorder, summarize and emphasize supported information according to the role.

It MUST NOT add unsupported experience simply because the job description contains a matching keyword.

See [`tailored-resumes.md`](tailored-resumes.md) for the detailed generation workflow and validation rules.

## Suggested AI instruction for profile creation

```text
Build a Career as Code profile using Trayector.

First read the active version's skills, common profile rules and mandatory templates. Then read all career source material I provide.

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

Use my Trayector profile as the only source of professional facts. Start at PROFILE.md and read the relevant canonical profile documents.

Use the selected résumé template as the mandatory structural contract for reading and writing the derived CV.

Analyze the target role first, then select, prioritize and summarize the parts of my real experience that best match it.

Do not invent or infer unsupported dates, titles, seniority, technologies, metrics, certifications, leadership scope, ownership, outcomes or capabilities.

If the job asks for something my profile does not support, do not add it.
```

## Validation mindset

A good AI-assisted Trayector profile or derived view should satisfy three tests:

1. **Human-readable:** a person can understand the career or résumé without special tooling.
2. **Machine-readable:** an AI or tool can traverse the structure and relationships without guessing the schema.
3. **Source-faithful:** claims are no stronger than the available canonical evidence.
