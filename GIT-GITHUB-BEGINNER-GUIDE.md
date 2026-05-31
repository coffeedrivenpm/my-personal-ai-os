# Git and GitHub Beginner Guide

## Mental model

- Git is local version history.
- GitHub is remote backup and collaboration.
- A commit is a saved checkpoint.
- A push sends local commits to GitHub.
- A pull brings remote changes down.

## Safe daily workflow

```bash
git status --short
```

If files changed, inspect:

```bash
git diff
```

Stage only what is safe:

```bash
git add FILE_OR_FOLDER
```

Review staged changes:

```bash
git diff --cached
```

Commit:

```bash
git commit -m "clear message"
```

Push:

```bash
git push
```

## Before committing

Check that you are not committing:

- `.env`
- API keys
- private documents
- account statements
- screenshots of private information
- employer/customer confidential files
- raw exports from private systems

## GitHub noreply email

Use GitHub's noreply email if you do not want your personal email in commit history. Find it in GitHub settings under Emails.
