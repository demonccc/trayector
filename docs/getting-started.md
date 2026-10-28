# Getting started

Trayector helps you version professional knowledge using Markdown, Git, structured templates, and AI-agent instructions. The **profile** is your own Git repository: it contains your professional facts, not Trayector's site source code.

## Create a career repository

Create a new repository from the released Trayector template when available. The template should include `PROFILE.md`, agent entry points, `.trayector/settings/`, the selected release's skills and templates, and optional GitHub Actions caller workflows.

You can start in two ways: supply an existing CV to an AI agent or answer a short, guided interview. The agent should read existing information before asking focused questions. It should ask for the profile language and whether you want to import publications or enable a public site. A first profile should be useful without needing to reconstruct your entire career immediately.

## Source of truth

- `PROFILE.md` is the entry point and index, not a Trayector configuration file.
- `profile/`, `experience/`, `projects/` and `content/` contain structured career records.
- `cv/` contains derived, tailored Markdown résumés.
- `.trayector/settings/trayector.yaml` declares the installed Trayector release.
- `.trayector/versions/<version>/skills/` contains agent procedures.
- `.trayector/versions/<version>/templates/` contains mandatory record contracts.

The agent must load the appropriate template **before reading, writing, or validating** each record, and it must not invent career facts.

## Configure the optional website

In `.trayector/settings/site.yaml` enable the site and select the sections to publish. To show a CV, set `cv.enabled: true` and `cv.selected` to an existing Markdown file stem under `cv/`. The official publish workflow renders that Markdown into HTML and a downloadable PDF without an AI API call.

The site is opt-in. Publishing and importing publications are separate choices.

## Version updates

Run the manual updater when you choose to adopt a newer Trayector tag. It opens a reviewable PR that installs the matching skills and templates bundle and aligns the official Actions reference. You may remain on any installed release indefinitely.

See [Agent-assisted creation](ai-assisted-profile.md), [Tailored résumés](tailored-resumes.md), and [Publishing](site-publishing.md).
