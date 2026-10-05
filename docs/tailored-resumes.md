# Tailored Résumés

A résumé generated from a Trayector profile is a **derived view** of canonical career knowledge.

The job description changes what is selected, emphasized, ordered and summarized. It does **not** change the underlying career facts.

## Inputs

A tailored résumé SHOULD be generated from:

1. the candidate's Trayector profile;
2. the target job description or role brief;
3. a selected résumé template;
4. optional presentation constraints such as language, page target or region.

The canonical profile remains the source of truth.

## Non-negotiable rule

**Tailoring may change selection and emphasis, never truth.**

A generator or AI MUST NOT invent:

- dates;
- titles;
- employers;
- seniority;
- technologies;
- metrics;
- certifications;
- leadership scope;
- project ownership;
- outcomes;
- capabilities not supported by the profile.

If the target role asks for something that the canonical profile does not support, omit it or state the closest supported capability without pretending equivalence.

## Recommended workflow

### 1. Read the target role

Extract the signals that actually matter:

- role family and level;
- core responsibilities;
- required and preferred capabilities;
- technologies and platforms;
- leadership expectations;
- domain constraints;
- language and location requirements.

Do not treat every keyword as equally important.

### 2. Read the canonical profile

Start at `profile.json` and traverse the relevant profile areas.

Prefer evidence-backed material from:

- `experience/`;
- `projects/`;
- `deep-dives/`;
- `stories/`;
- `content/`;
- `feedback/` when useful for leadership or collaboration context;
- `profile/capabilities.md` as an index, not as the sole source of claims.

### 3. Build a match plan before writing

Create an internal mapping between target requirements and supported career evidence.

Example:

```text
Target: AWS architecture
Supported by:
- intive experience
- Naranja X experience
- Globant experience

Target: Platform Engineering
Supported by:
- intive
- Santander
- Naranja X

Target: people leadership
Supported by:
- Santander
- Naranja X
- Globant
```

Unsupported requirements stay unsupported.

### 4. Select a template

Trayector ships with a basic template under `templates/resume/basic.md`.

Implementations MAY add more templates, for example:

```text
templates/resume/
├── basic.md
├── architect.md
├── engineering-leadership.md
└── technical-specialist.md
```

Templates define **presentation strategy and section shape**, not career facts.

A profile MAY also maintain personal templates outside the Trayector repository when the owner wants a specific visual or regional format.

### 5. Generate the résumé

Tailoring MAY:

- rewrite the professional summary using only supported claims;
- reorder capabilities by relevance;
- choose the most relevant experiences;
- shorten unrelated older experience;
- expand highly relevant initiatives;
- select projects and evidence that strengthen the target profile;
- adapt terminology when two terms are genuinely equivalent;
- omit information that does not help the target application.

Tailoring MUST NOT turn absence into experience.

### 6. Validate every claim

Before finalizing, the generator SHOULD be able to trace each substantive résumé claim back to canonical profile material.

If a statement cannot be supported, remove or weaken it.

## Suggested AI instruction

```text
Create a tailored résumé for the job description I provide.

Use my Trayector profile as the only source of professional facts. Start at profile.json and read the relevant canonical experience, projects, capabilities, deep dives, stories, feedback and content.

Use the selected résumé template as presentation guidance.

Analyze the target role first, then select and prioritize the parts of my real experience that best match it.

You may summarize, reorder, shorten and emphasize. You may rewrite wording to match the language of the role when the meaning is genuinely equivalent.

Do not invent or infer unsupported dates, titles, seniority, technologies, metrics, certifications, leadership scope, ownership, outcomes or capabilities.

If the job asks for something my profile does not support, do not add it.

Keep the result concise and recruiter-readable. The résumé is a derived view of the profile, not a new source of truth.
```

## Output location

Generated résumés SHOULD live outside canonical career areas.

A profile MAY store committed outputs under:

```text
generated/resumes/<target-slug>/
```

For example:

```text
generated/resumes/aws-solutions-architect/
├── resume.md
└── target.md
```

`target.md` can preserve the job description or a concise role brief used to create that view.

Generated outputs MAY also remain ephemeral and never be committed.

## Multiple templates

Multiple templates are useful when the presentation strategy materially changes.

Examples:

- **basic** — broadly applicable chronological résumé;
- **architect** — architecture, decisions, systems and technical scope first;
- **engineering-leadership** — organizational scope, leadership and outcomes first;
- **technical-specialist** — technical depth, projects and evidence first.

The same canonical profile can produce all of them without duplicating the underlying career data.
