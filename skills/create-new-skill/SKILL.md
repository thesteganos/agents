---
name: create-new-skill
description: Meta-skill to create other skills reliably. Use ONLY when explicitly requested or for high-repetition workflows.
allowed-tools:
  - run_command
  - read_file
  - write_to_file
  - multi_replace_file_content
  - view_file
---

# [create-new-skill]

## Goal

To rigorously create a new Skill file structure and content, ensuring compliance with architectural standards, safety protocols, and past lessons.

## Inputs

- **User Request**: The natural language description of what the skill should do.
- **Skill Name**: A proposed `kebab-case` name (e.g., `git-commit-helper`).

## Tools & Context

- `execution/scaffold_skill.py`: Python script to generate the folder and file structure.
- `system/lessons.md`: Global database of past mistakes and constraints.
- `skills/SKILL_TEMPLATE.md`: The reference for what a skill looks like.

## Step-by-Step Procedure

### 1. The Gatekeeper Check

**STOP and Verify:**

- Is this a request to fix a _bug_ in an existing skill? -> **ABORT**. Edit the existing skill instead.
- Is this a one-off task (e.g., "delete this file")? -> **ABORT**. Do it manually.
- Is this explicitly requested by the user regarding a NEW capability? -> **PROCEED**.
- Is this a complex workflow you have performed >3 times manually? -> **PROCEED**.

### 2. Scaffold the Structure

Run the deterministic python script to create the files.

```bash
python3 execution/scaffold_skill.py --name "your-skill-name" --description "Brief description"
```

_Wait for the JSON output confirming success and the path to the new file._

### 3. Lesson Injection (Memory Lookup)

Read the global lessons file:

```
read_file system/lessons.md
```

**Analyze:**

- Look for tags relevant to the new skill (e.g., if the skill uses Python, look for `[PYTHON]`).
- Note down any "WARNINGS" or "RESTRICTIONS" that must be applied.

### 4. Write Content (Intelligence)

Read the newly created `SKILL.md`. You will see that the Header (YAML) is correctly filled, but the Body contains generic placeholders like `[Step 1]` or `[Goal]`.
Use `replace_file_content` to **rewrite the body sections** with the specific logic for this capability.

**Drafting Rules:**

- **allowed-tools**: LIST ONLY EXISTING TOOLS (run_command, read_file, etc.). Do NOT invent tools.
- **Instructions**: Write atomic steps.
- **Critical Edge Cases**:
  - Add standard edge cases.
  - **TRANSPLANT LESSONS**: Add a subsection `WARNING (from lessons.md)` and insert the relevant lessons found in Step 3.

### 5. Final Review

Read the file you just wrote.

- Did you use `kebab-case`?
- Did you Hallucinate any tools in `allowed-tools`?
- Are the instructions clear?

## Critical Edge Cases

- **Scaffold Failure**: If the python script error says "Directory exists", ask the user if they want to overwrite or choose a different name.
- **Empty Lessons**: If `lessons.md` does not exist or is empty, proceed without injection (but create the file if missing).
