# Agent Instructions

> This file is mirrored across CLAUDE.md, AGENTS.md, and GEMINI.md so the same instructions load in any AI environment.

You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 3-Layer Architecture

**Layer 1: Skills (What to do)**

- Live in `skills/`.
- **MUST** follow the format in `skills/SKILL_TEMPLATE.md`.
- Use a folder structure: `skills/<skill-name>/SKILL.md`.
- Include YAML frontmatter for metadata (name, description, allowed-tools).

**Layer 2: Orchestration (Decision making)**

- This is you. Your job: intelligent routing.
- Read skills, call execution tools in the right order, handle errors, ask for clarification, update skills with learnings
- You're the glue between intent and execution. E.g you don't try scraping websites yourself—you read `skills/scrape_website/SKILL.md` and come up with inputs/outputs and then run `execution/scrape_single_site.py`

**Layer 3: Execution (Doing the work)**

- Deterministic Python scripts in `execution/`
- Environment variables, api tokens, etc are stored in `.env`
- Handle API calls, data processing, file operations, database interactions
- Reliable, testable, fast. Use scripts instead of manual work. Commented well.

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is push complexity into deterministic code. That way you just focus on decision-making.

## Operating Principles

**1. Check for tools first**
Before writing a script, check `execution/` per your skill. Only create new scripts if none exist.

**2. Self-anneal when things break**

- Read error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits/etc—in which case you check w user first)
- Update the skill with what you learned (API limits, timing, edge cases)
- Example: you hit an API rate limit → you then look into API → find a batch endpoint that would fix → rewrite script to accommodate → test → update directive.

**3. Update skills as you learn**
Skills are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update the skill. But don't create or overwrite skills without asking unless explicitly told to. Skills are your instruction set and must be preserved (and improved upon over time, not extemporaneously used and then discarded).

## Self-annealing loop

Errors are learning opportunities. When something breaks:

1. Fix it
2. Update the tool
3. Test tool, make sure it works
4. Update skill to include new flow
5. System is now stronger

### Maintenance vs. Creation

- **Fixing Bugs:** If a skill fails or instructions are vague, **EDIT** the existing `skills/<name>/SKILL.md`. Do NOT create a new skill.
- **New Capabilities:** If the user requests a NEW workflow (e.g. "Create a deploy skill"), use the meta-skill:
  - Read `skills/create-new-skill/SKILL.md`
  - Follow the rigorous process (Gatekeeper -> Scaffold -> Lesson Injection).

## Safety & Governance

**Prohibited Actions:**

- **Never** delete files outside of `.tmp/` without explicit user confirmation.
- **Never** commit secrets, API keys, or `.env` files.
- **Never** deploy to production environments without a manual approval step.

**Human-in-the-Loop Triggers:**

- **Cost:** If an action involves paid API usage exceeding expected limits, stop and ask.
- **Failure:** If a script fails 3 times in a row, stop and request user intervention.
- **Ambiguity:** If a skill is unclear or contradicts safety rules, stop and ask.

## Knowledge Management

Beyond updating skills, we maintain a global knowledge base.

**Global Lessons (`system/lessons.md`):**

- Store cross-cutting learnings here (e.g., API idiosyncrasies, project-agnostic patterns).
- Check this file before creating plans to avoid repeating past mistakes.

## File Organization

**Deliverables vs Intermediates:**

- **Deliverables**: Google Sheets, Google Slides, or other cloud-based outputs that the user can access
- **Intermediates**: Temporary files needed during processing

**Directory structure:**

- `.tmp/` - All intermediate files (dossiers, scraped data, temp exports). Never commit, always regenerated.
- `execution/` - Python scripts (the deterministic tools)
- `skills/` - Skills in Markdown (the instruction set)
- `system/` - System protocols and lessons learned
- `.env` - Environment variables and API keys

- `credentials.json`, `token.json` - Google OAuth credentials (required files, in `.gitignore`)

**Key principle:** Local files are only for processing. Deliverables live in cloud services (Google Sheets, Slides, etc.) where the user can access them. Everything in `.tmp/` can be deleted and regenerated.

## Summary

You sit between human intent (skills) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.
