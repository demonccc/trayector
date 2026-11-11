# Getting started

Trayector helps version professional knowledge using human-readable Markdown, Git, templates, and AI-agent instructions. The profile is your own repository; it does not contain Trayector's website source code.

## Create a career repository

Create a repository from the released Trayector template when available. You may supply a CV or start a guided conversation. The agent should inspect the information available before asking targeted questions, and should ask whether you want to import external publications, keep original articles, or enable a public site. These are separate decisions.

## Source of truth

- `PROFILE.md`: canonical navigation entry point
- `profile/`, `experience/`: professional background and work
- `projects/`: initiatives the person developed or maintained significantly
- `contributions/`: work contributed to other initiatives
- `publications/`: externally hosted/published material, talks, videos, podcasts, or registrations, documented with the original Link
- `articles/<slug>/README.md`: authored article index, with Summary, Content links to per-language Markdown files, and optional Related
- `cv/`: derived tailored résumés
- `.trayector/settings/`: version and site settings
- `.trayector/versions/<version>/`: installed skills and mandatory templates

Agents should read the applicable template before interpreting or editing a record. The contents of `articles/<slug>/<language>.md` are free-form, not subject to a fixed set of headings.

## Publish the optional website

Set `enabled: true` in `.trayector/settings/site.yaml` to enable publishing. To publish an article, also add its folder name to `articles.include` with the person's approval. An article that is not included remains a repository document but is not exposed by the website. To show a CV, enable the CV section and select an existing `cv/<selected>.md`. The official publish workflow builds the HTML and PDF without AI.

## Updates

A manually initiated updater can propose a PR to install a newer tagged release's skills and templates without overwriting career data.

See [AI-assisted creation](ai-assisted-profile.md), [Tailored résumés](tailored-resumes.md) and [Publishing](site-publishing.md).
