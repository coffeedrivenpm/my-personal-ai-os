# Personal AI OS Starter

A shareable Claude Code starter vault for personal learning, technical upskilling, portfolio building, writing, research, and life-operations tracking.

This starter is intentionally generic. It does not include personal facts, employer-specific context, customer data, secrets, or private documents. After cloning or unzipping, run Claude Code from this folder and complete the first-run onboarding flow.

## What this vault is for

- Building a hands-on learning system.
- Tracking skill growth over time.
- Creating portfolio projects.
- Managing research notes and writing drafts.
- Maintaining sanitized career positioning.
- Keeping sensitive life-domain context isolated.

## What this vault is not for

- Storing passwords, account numbers, government IDs, medical records, legal records, tax files, or private documents.
- Storing confidential employer/customer data.
- Automatically reading private materials without user approval.

## First run

1. Unzip or clone this starter.
2. Open Terminal in the vault folder.
3. Run:

```bash
claude
```

4. Paste:

```text
Read CLAUDE.md and FIRST-RUN-ONBOARDING.md. If onboarding is incomplete, guide me through the first-run setup. Do not read private/ or 99-archive/.
```

Claude should ask you onboarding questions, then help populate the template files under `00-core/`, `01-learning/`, `03-projects/`, and `04-career/`.

## Recommended first checks

Inside Claude Code:

```text
/memory
/permissions
```

Confirm that project memory is loading from `CLAUDE.md`, and keep permissions conservative until you understand the workflow.

## Suggested GitHub setup

Create a private repo manually, then follow `GIT-GITHUB-BEGINNER-GUIDE.md`. Do not commit real sensitive material.

## Structure

```text
00-core/              Your personal profile, goals, learning style, AI usage rules
01-learning/          Roadmap, learning logs, weekly/monthly/quarterly reviews
02-technical-skills/  Skill maps for APIs, SQL, Python, AI, system design, Git, etc.
03-projects/          Portfolio projects and project templates
04-career/            Resume, interview prep, achievement logs, career positioning
05-writing/           Writing voice, blog ideas, writing rubric
06-research/          Market radar, technical PM trends, research protocol
07-personal-domains/  Sanitized personal-domain indexes
private/              Placeholder only; real sensitive content should live elsewhere
08-working/           Drafts, scratch, temporary work
09-outputs/           Exported or final artifacts
10-sources/           Source index and raw/processed source material
11-templates/         Reusable templates
scripts/              Optional helper scripts
99-archive/           Local archive area; do not auto-load
```
