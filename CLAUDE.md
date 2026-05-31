# Claude Code Instructions — Personal AI OS Starter

@AGENTS.md

## First-run behavior

Before starting substantive work, check whether `ONBOARDING-COMPLETE.md` exists.

- If it does not exist, read `FIRST-RUN-ONBOARDING.md` and guide the user through setup.
- Do not read `private/` or `99-archive/` during onboarding.
- Do not assume the user's name, job, goals, learning style, or privacy preferences.
- Use placeholders until the user confirms their context.

## Memory behavior

Claude may remember non-sensitive workflow preferences, learning preferences, and project organization preferences.

Claude must not store:

- account numbers
- passwords or tokens
- government IDs
- health/medical specifics
- immigration document details
- private addresses
- relationship-sensitive details
- confidential employer/customer information
- contents from `private/` or `99-archive/`

If memory use is ambiguous, ask before storing.

## Safety boundaries

- Keep `private/` as a placeholder-only area unless the user explicitly changes the privacy model.
- Keep real sensitive content outside the Git-backed vault, preferably in encrypted storage.
- Ask before running destructive shell commands.
- Ask before Git write operations.
- Do not use broad automation or computer-use tools unless the user intentionally enables them.

## Recommended first prompt

```text
Read CLAUDE.md and FIRST-RUN-ONBOARDING.md. If onboarding is incomplete, guide me through the first-run setup. Do not read private/ or 99-archive/.
```
