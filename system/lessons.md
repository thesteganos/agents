# Global Lessons

> This file stores cross-cutting learnings that apply to multiple skills and scripts.
> The agent reads this file before creating new skills to avoid repeating past mistakes.

## Format

Each lesson should follow this format:

```
- [TAG] Brief description of the lesson or constraint.
```

**Available Tags:**

- `[PYTHON]` - Python-specific patterns and pitfalls
- `[GIT]` - Git workflow and commit rules
- `[API]` - API rate limits, authentication, and idiosyncrasies
- `[IO]` - File system, disk, and I/O operations
- `[SECURITY]` - Security-related constraints
- `[GENERAL]` - Cross-cutting best practices

---

## Lessons

<!-- Add lessons below this line -->

- [GENERAL] Always use absolute paths when referencing files in scripts.
- [PYTHON] Use `encoding='utf-8'` when opening text files for cross-platform compatibility.
