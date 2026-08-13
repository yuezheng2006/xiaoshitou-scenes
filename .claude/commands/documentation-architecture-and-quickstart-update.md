---
name: documentation-architecture-and-quickstart-update
description: Workflow command scaffold for documentation-architecture-and-quickstart-update in xiaoshitou-scenes.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /documentation-architecture-and-quickstart-update

Use this workflow when working on **documentation-architecture-and-quickstart-update** in `xiaoshitou-scenes`.

## Goal

Creates or updates high-level documentation files such as ARCHITECTURE.md, QUICK-START.md, and SKILL.md to improve maintainability, onboarding, and clarity for users and developers.

## Common Files

- `scene-skill-core/ARCHITECTURE.md`
- `scene-skill-core/QUICK-START.md`
- `scene-skill-core/SKILL.md`
- `scene-skill-core/README.md`
- `scene-skill-core/references/*.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create or update ARCHITECTURE.md with diagrams and maintenance checklists
- Create or update QUICK-START.md for onboarding or quick reference
- Update SKILL.md and README.md to reflect new navigation or documentation structure
- Update or add references as needed for new documentation sections

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.