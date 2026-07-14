---
name: add-or-update-persona-assets-and-metadata
description: Workflow command scaffold for add-or-update-persona-assets-and-metadata in xiaoshitou-scenes.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-or-update-persona-assets-and-metadata

Use this workflow when working on **add-or-update-persona-assets-and-metadata** in `xiaoshitou-scenes`.

## Goal

Adds or updates persona-related assets (images, prompts, identity, etc.) and synchronizes references and quick checklists for new or updated personas.

## Common Files

- `scene-skill-core/ip-profiles/*/assets/persona/*.png`
- `scene-skill-core/ip-profiles/*/persona-author-assets.md`
- `scene-skill-core/ip-profiles/*/persona-author-identity.md`
- `scene-skill-core/ip-profiles/*/persona-author-prompts.md`
- `scene-skill-core/ip-profiles/*/persona-author.md`
- `scene-skill-core/references/common-character-lock.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add or update image assets under scene-skill-core/ip-profiles/[persona]/assets/persona/
- Update or create persona metadata files: persona-author-assets.md, persona-author-identity.md, persona-author-prompts.md, persona-author.md
- Update or create references: references/common-character-lock.md, references/common-prompt-slots.md, references/persona-quick-checklist.md
- Optionally update QUICK-START.md to reflect new persona or changes

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.