# Publishing a career profile

The website implementation lives in the central Trayector release, not in the personal repository:

- `site/`: static HTML templates and assets
- `scripts/build-site.py`: Markdown-to-HTML and selected-CV-to-PDF renderer
- `.github/workflows/publish.yml`: reusable GitHub Pages workflow

The personal repository keeps career documents, `.trayector/settings/site.yaml`, and a thin workflow pinned to the same immutable Trayector release as `.trayector/settings/trayector.yaml`.

## Configuration

```yaml
enabled: false
languages:
  - es
  - en
articles:
  enabled: true
  include:
    - career-as-code
experience:
  enabled: true
cv:
  enabled: false
  selected: general
```

Site publishing is opt-in. **An article is never exposed merely because it exists in Git.** The site builds only article folders explicitly approved in `articles.include`, and only if the site and articles section are enabled. An empty list publishes no articles. Enabling the site does not authorize publication of drafts. Article references in `publications/` do not automatically publish anything.

## Multilingual article layout

```text
articles/career-as-code/
  README.md
  es.md
  en.md
  pt-BR.md
  assets/
```

The `languages` list configures which language versions the site offers, in preferred order. Articles may have additional translations; only linked versions whose filename language code is configured in `site.yaml` are rendered. Articles with no matching language version are omitted. This does not translate any content or yet localize the site's shared navigation and professional profile pages.

The README is a human-readable index, following `templates/content/article.md`. Its `## Content` section links to each language file, for example `- Spanish: [es.md](es.md)`. The renderer reads only the linked files, renders the unrestricted Markdown of each language, copies shared assets, and provides language links. No front matter or mandatory body headings are required. `## Summary` supplies the site index excerpt; `## Related` links professional records. Content files not linked in README are not article versions.

`publications/` instead documents content hosted externally (including copyright registrations) through a description, personal participation, original-content `## Link`, and optional `## Related`. It is not the storage location for authored Markdown articles.

The selected CV `cv/<selected>.md` is rendered to an HTML page and downloadable PDF without AI calls. Publishing needs testing against a real release before production use.
