```markdown
# xiaoshitou-scenes Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill outlines the development patterns, coding conventions, and core workflows for the `xiaoshitou-scenes` TypeScript repository. The codebase focuses on persona-driven scene management, with a strong emphasis on maintainable documentation and asset organization. It is designed for contributors who want to efficiently add new personas, update persona assets, or improve project documentation.

## Coding Conventions

Consistent coding conventions are used throughout the repository to ensure readability and maintainability.

### File Naming

- **Style:** kebab-case
- **Example:**  
  ```
  scene-skill-core/ip-profiles/example-persona/persona-author-assets.md
  ```

### Import Style

- **Relative imports** are used for all modules.
- **Example:**
  ```typescript
  import { getPersonaData } from './utils/persona-utils';
  ```

### Export Style

- **Named exports** are preferred.
- **Example:**
  ```typescript
  // persona-utils.ts
  export function getPersonaData(id: string) { ... }
  ```

### Commit Messages

- **Conventional commits** are used, with prefixes such as `feat` and `refactor`.
- **Example:**
  ```
  feat: add new persona metadata for 'alex'
  refactor: update import paths for persona assets
  ```

## Workflows

### Add or Update Persona Assets and Metadata

**Trigger:** When introducing a new persona or updating an existing persona's assets and documentation  
**Command:** `/add-persona`

1. **Add or update image assets**  
   Place persona images under:  
   ```
   scene-skill-core/ip-profiles/[persona]/assets/persona/
   ```
   *Example:*  
   ```
   scene-skill-core/ip-profiles/alex/assets/persona/alex.png
   ```

2. **Update or create persona metadata files:**  
   - `persona-author-assets.md`
   - `persona-author-identity.md`
   - `persona-author-prompts.md`
   - `persona-author.md`

   *Example structure:*
   ```
   scene-skill-core/ip-profiles/alex/persona-author-assets.md
   ```

3. **Update or create references:**  
   - `references/common-character-lock.md`
   - `references/common-prompt-slots.md`
   - `references/persona-quick-checklist.md`

4. **Optionally update** `QUICK-START.md` to reflect new or changed personas.

**Tip:** Use the `/add-persona` command to scaffold this process.

---

### Documentation Architecture and Quickstart Update

**Trigger:** When improving documentation structure, onboarding guides, or updating architectural diagrams/checklists  
**Command:** `/update-docs`

1. **Create or update** `ARCHITECTURE.md` with diagrams and maintenance checklists.
2. **Create or update** `QUICK-START.md` for onboarding or quick reference.
3. **Update** `SKILL.md` and `README.md` to reflect new navigation or documentation structure.
4. **Update or add** references as needed for new documentation sections.

*Example file locations:*
- `scene-skill-core/ARCHITECTURE.md`
- `scene-skill-core/QUICK-START.md`
- `scene-skill-core/SKILL.md`
- `scene-skill-core/README.md`
- `scene-skill-core/references/*.md`

---

## Testing Patterns

- **Test files** follow the pattern `*.test.*`
- **Testing framework:** Not specified (add or clarify in documentation if needed)
- **Example:**
  ```
  scene-skill-core/utils/persona-utils.test.ts
  ```

## Commands

| Command        | Purpose                                                        |
|----------------|----------------------------------------------------------------|
| /add-persona   | Scaffold and guide the process of adding or updating a persona |
| /update-docs   | Update or create documentation and onboarding guides           |
```
