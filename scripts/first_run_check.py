#!/usr/bin/env python3
from pathlib import Path
root = Path(__file__).resolve().parents[1]
complete = root / "ONBOARDING-COMPLETE.md"
print("Onboarding complete:" if complete.exists() else "Onboarding incomplete:", complete.exists())
if not complete.exists():
    print("Run Claude Code and follow FIRST-RUN-ONBOARDING.md")
