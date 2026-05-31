# Security and Privacy

This starter is designed to reduce accidental exposure, not to guarantee security.

## Rules

- Do not store secrets, account numbers, government IDs, medical records, legal documents, tax documents, or passwords in this Git-backed vault.
- Use `private/` only for placeholder README files unless you intentionally change the model.
- Store real sensitive files outside the repo, ideally in encrypted storage.
- Review `git status --short` before every commit.
- Review `git diff --cached` before pushing.

## Recommended model

Use the vault for:

- sanitized summaries
- learning plans
- project work
- career positioning
- writing drafts
- research notes

Keep sensitive details elsewhere:

- encrypted disk image
- password manager
- secure document storage
- local encrypted folder

## Claude Code behavior

The project settings and rules ask Claude not to read `private/` or `99-archive/` unless explicitly asked. Treat this as a guardrail, not a legal/security boundary.
