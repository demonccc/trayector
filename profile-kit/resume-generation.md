# Tailored Résumé and PDF Generation

A tailored résumé is a **derived view** of the canonical Trayector profile.

The target role changes selection, ordering, emphasis and wording. It never changes the underlying facts.

## Required inputs

Before generating a résumé, read:

1. `profile.json` at the repository root;
2. the canonical profile documents relevant to the target role;
3. the target job description or role brief;
4. the selected résumé template under `.trayector/resume/`.

If no template is specified, use `.trayector/resume/basic.md`.

## Step 1 — Analyze the target role

Identify:

- role family and expected level;
- core responsibilities;
- required capabilities;
- preferred capabilities;
- technologies and platforms;
- architecture or leadership expectations;
- domain constraints;
- language and location requirements.

Prioritize signals. Do not treat every keyword as equally important.

## Step 2 — Build a match plan

Before drafting, map target requirements to supported canonical evidence.

Example:

```text
Target requirement: AWS architecture
Supported by:
- experience/intive.md
- experience/naranja-x.md
- experience/globant-2015-2019.md

Target requirement: Platform Engineering
Supported by:
- experience/intive.md
- experience/santander-tecnologia-argentina.md
- experience/naranja-x.md
```

Unsupported requirements remain unsupported.

## Step 3 — Tailor without inventing

You MAY:

- rewrite the professional summary around supported strengths relevant to the role;
- reorder capabilities;
- expand relevant experiences and condense unrelated ones;
- select the strongest relevant projects, deep dives, content or feedback;
- adapt wording to the target role when the meaning is genuinely equivalent;
- omit irrelevant information.

You MUST NOT invent or inflate:

- employers;
- dates;
- titles;
- seniority;
- technologies;
- certifications;
- leadership scope;
- project ownership;
- metrics;
- outcomes;
- capabilities.

If the target asks for something unsupported, do not add it.

## Step 4 — Produce the source résumé

Generate a Markdown source following the selected template.

Recommended output location:

```text
generated/resumes/<target-slug>/resume.md
```

Optionally preserve the target role as:

```text
generated/resumes/<target-slug>/target.md
```

The generated résumé is not canonical career data.

## Step 5 — Produce the PDF

When the environment provides document or PDF rendering capability, render the final résumé to:

```text
generated/resumes/<target-slug>/resume.pdf
```

The PDF MUST be rendered from the reviewed résumé source, not independently rewritten during rendering.

Keep the PDF:

- readable by humans;
- text-based and ATS-friendly;
- free of unnecessary graphics or multi-column layouts that break text extraction unless a selected template explicitly requires otherwise;
- visually consistent;
- concise enough for the target context.

If the execution environment cannot create a PDF, produce the complete Markdown résumé and report that PDF rendering is unavailable rather than fabricating a file.

## Step 6 — Validate

Before finalizing:

- trace every substantive claim back to canonical profile material;
- remove unsupported statements;
- check dates and organization names;
- ensure selected technologies actually appear in supported evidence;
- confirm no target requirement was silently converted into fictional experience;
- confirm the PDF content matches the reviewed source résumé.

## AI instruction

```text
Create a tailored résumé and, if your environment supports it, a PDF for the target job description I provide.

This repository is a Trayector Career as Code profile. Read profile.json first, then .trayector/README.md, .trayector/profile-rules.md, the relevant canonical profile documents, and the selected template under .trayector/resume/.

Use the canonical profile as the only source of professional facts.

Analyze the target role first and map its important requirements to supported evidence in the profile before drafting.

You may select, reorder, summarize, shorten and emphasize supported information. You may adapt wording when the meaning remains faithful.

Do not invent or infer unsupported dates, titles, seniority, technologies, certifications, metrics, leadership scope, ownership, outcomes or capabilities.

If the target asks for something unsupported, leave it out.

Generate the Markdown résumé first. Validate its substantive claims against the canonical profile. Then render the PDF from that reviewed source when PDF rendering is available.
```
