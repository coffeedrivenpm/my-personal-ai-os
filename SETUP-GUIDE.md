# Setup Guide

This guide assumes macOS and Claude Code, but the vault structure also works on other systems.

## Prerequisites

- Claude Code installed and authenticated.
- Git installed.
- A text editor such as VS Code, Cursor, or another Markdown editor.
- Optional: a private GitHub repository for backup.

## Install

1. Unzip this starter where you want the vault to live.
2. Open Terminal in the vault folder.
3. Run:

```bash
claude
```

4. Start onboarding:

```text
Read CLAUDE.md and FIRST-RUN-ONBOARDING.md. If onboarding is incomplete, guide me through first-run setup. Do not read private/ or 99-archive/.
```

## Git setup

Initialize Git only after reviewing `.gitignore`.

```bash
git init
git status --short
```

Configure identity for this repo only:

```bash
git config user.name "YOUR_NAME"
git config user.email "YOUR_GITHUB_NOREPLY_EMAIL"
```

Stage and commit after confirming no sensitive files are present:

```bash
git add .
git status --short
git commit -m "chore: initialize personal ai os starter"
```

## GitHub backup

Create an empty private GitHub repository. Do not add a README, license, or `.gitignore` on GitHub if you already have local files.

```bash
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/personal-ai-os.git
git branch -M main
git push -u origin main
```

## Important

If GitHub created a README before your first push, inspect before force-pushing. Do not run force commands unless you understand what will be overwritten.
