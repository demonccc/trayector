# Taxonomy

Trayector uses stable, human-readable IDs to keep repeated concepts consistent across a profile.

Recommended taxonomy groups include:

- `capabilities` — what a person can demonstrate doing;
- `technologies` — tools, platforms, languages and protocols;
- `domains` — business or technical domains;
- `organizations` — stable organization identifiers;
- `topics` — reusable themes for stories and content.

A profile MAY maintain these taxonomies as YAML or JSON.

Example:

```yaml
capabilities:
  platform-engineering:
    label: Platform Engineering
    aliases:
      - developer-platforms

technologies:
  kubernetes:
    label: Kubernetes
    aliases:
      - k8s
  aws-eks:
    label: Amazon EKS
    parent: kubernetes
```

The goal is not to create a universal ontology in v0.1. The goal is to avoid accidental duplication such as `K8s`, `kubernetes`, `Kubernetes/EKS` and `EKS` representing overlapping concepts without explicit relationships.
