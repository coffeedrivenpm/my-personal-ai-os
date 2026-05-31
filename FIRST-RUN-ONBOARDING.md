# First-Run Onboarding Protocol

Claude Code should use this file when the vault is opened for the first time.

## Trigger

If `ONBOARDING-COMPLETE.md` does not exist, start onboarding before doing other work.

## Safety rules

- Do not read `private/` or `99-archive/` during onboarding.
- Do not ask for account numbers, passwords, government IDs, medical record details, immigration document numbers, private addresses, or confidential employer/customer information.
- Ask for sanitized summaries only.
- If the user wants to store sensitive details, route them to `SECURITY-AND-PRIVACY.md` and recommend external encrypted storage.

## Questions to ask

Ask these in batches, not all at once. Capture answers in the appropriate template files.

### A. Identity and context

1. What name should this vault use for you?
2. What role or identity should the system optimize for? Examples: product manager, engineer, designer, student, founder, researcher.
3. What is your current skill baseline?
4. What do you not want this vault to assume about you?

### B. Goals

5. What are your top 3 learning goals for the next 6 months?
6. What are your top 3 career or portfolio goals?
7. What personal domains should this vault help organize? Examples: finance, health, immigration, photography, writing, research.
8. What should be explicitly excluded?

### C. Learning style

9. How much time can you realistically spend per day and per week?
10. Do you learn better through projects, reading, videos, exercises, explanations, or mixed modes?
11. How direct should feedback be?
12. Should the system challenge unrealistic plans or simply support them?

### D. Technical roadmap

13. Which technical skills matter most right now?
14. Which skills are exploratory or lower priority?
15. What kind of portfolio artifacts do you want to build?
16. What tools are installed locally?

### E. Privacy and boundaries

17. What categories should never be stored in this repo?
18. Should private placeholders exist for finance, health, immigration, identity, or relationships?
19. Should employer/company context be allowed? If yes, define safe boundaries.
20. Should the assistant ask before using career, finance, health, or immigration context?

### F. Writing and output style

21. What writing style should the system use?
22. What writing behaviors should it avoid?
23. What outputs do you expect frequently? Examples: learning plans, project specs, blog posts, resumes, research summaries.

## Files to update after onboarding

- `00-core/personal-profile.md`
- `00-core/personal-goals.md`
- `00-core/learning-style.md`
- `00-core/operating-principles.md`
- `00-core/ai-usage-principles.md`
- `01-learning/learning-roadmap.md`
- `01-learning/30-min-daily-operating-model.md`
- `03-projects/portfolio-index.md`
- `04-career/career-profile-sanitized.md`
- `05-writing/voice-profile.md`

## Completion rule

After drafting the onboarding outputs, ask the user to review. Only then create:

```text
ONBOARDING-COMPLETE.md
```

with the date, summary, and next 3 recommended actions.
