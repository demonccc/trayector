# Managing tailored résumés

The `manage-resumes` skill creates and updates Markdown CVs as **derived views** of career records. Start from `PROFILE.md`, the applicable canonical records, and the installed `templates/resumes/basic.md` contract. A vacancy is a selection criterion, never a source of personal career facts.

For example, an agent can generate `cv/cloud-architect.md` or `cv/general.md` by selecting and accurately summarizing supported skills, experiences and outcomes. The template defines the required YAML metadata and sections for both reading and writing. Source paths must refer to real records.

Never fabricate dates, employers, qualifications, individual contributions, metrics or seniority. Describe unsupported job requirements honestly.

CVs remain available in the repository even when none is public. The owner selects one for the default website in `.trayector/settings/site.yaml`:

```yaml
cv:
  enabled: true
  selected: cloud-architect
```

The official publishing workflow reads `cv/cloud-architect.md`, creates the HTML CV page, and renders a PDF from the same Markdown source. Publishing must not invoke a language model or regenerate résumé facts. The current PDF renderer is an initial implementation and requires typography and ATS validation.
