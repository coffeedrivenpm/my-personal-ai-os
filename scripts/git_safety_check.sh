#!/usr/bin/env bash
set -euo pipefail

echo "Git status:"
git status --short || true

echo
echo "Untracked private files visible to Git:"
git ls-files --others --exclude-standard private/ || true

echo
echo "Untracked archive files visible to Git:"
git ls-files --others --exclude-standard 99-archive/ || true
