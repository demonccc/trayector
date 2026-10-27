# Trayector AI instructions and updates

Career facts belong in canonical profile documents, not in .trayector. PROFILE.md is the profile entry point.

All agent adapters (AGENTS.md, CLAUDE.md, GEMINI.md and .github/copilot-instructions.md) use the same discovery steps:

1. Read PROFILE.md.
2. Read .trayector/ia/ACTIVE.
3. Read .trayector/ia/<active-version>/index.md and relevant procedures.
4. Read .trayector/ia/custom/index.md if present.

The versioned instructions explain how to read, create, modify, connect and validate canonical career knowledge. They are not an embeddings index. Agent hosts vary in whether they automatically detect their adapter.

## Updating

Versioned instructions are immutable. The manually invoked update-trayector.yml fetches one released tag's profile-kit/ia/<version>/ and opens a PR with only the new version directory. It does not modify ACTIVE, custom instructions, older versions, settings, site or career data. Activation is an explicit subsequent change to ACTIVE.

Local custom instructions can extend behavior but should not contradict career-profile-spec or source-fidelity rules. Public-site code and publishing workflows remain independent and user-owned.

The 0.1.0 directory is a development example. A corresponding release tag must exist and be tested before updates can use it.
