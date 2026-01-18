# Agent Protocol 🤖

> **Standardized Instruction Set for Autonomous AI Agents**
> Compatible with **Claude Code** and **Gemini CLI**.

This repository hosts the **3-Layer Agent Architecture**, a reliable framework that separates high-level decision making from deterministic execution. It allows AI agents to operate with higher reliability, safety, and self-improvement capabilities.

## 🌟 Core Concepts

The system is built on three distinct layers ensuring that the AI knows _what_ to do, _how_ to decide, and _how_ to execute securely.

### The 3-Layer Architecture

| Layer                | Component     | Function                                           | File Location |
| :------------------- | :------------ | :------------------------------------------------- | :------------ |
| **1. Skills**        | **Protocol**  | Step-by-step SOPs (Standard Operating Procedures). | `skills/`     |
| **2. Orchestration** | **The Agent** | Decision making, routing, and error handling.      | `AGENTS.md`   |
| **3. Execution**     | **Scripts**   | Deterministic, safe, and fast Python scripts.      | `execution/`  |

## 🚀 Key Features

### 🧠 Meta-Skill (Self-Replication)

The agent is capable of creating its own tools using the **Meta-Skill** (`skills/create-new-skill`).

- **Safe:** Uses a deterministic Python scaffold (`execution/scaffold_skill.py`) to prevent structure errors.
- **Smart:** Injects lessons learned from `system/lessons.md` into new skills automatically.
- **Rigorous:** Follows a strict Gatekeeper process to avoid over-engineering.

### 🔄 Self-Annealing Loop

The system gets stronger with every failure.

1. Script fails -> 2. Agent fixes script -> 3. Agent updates Skill -> 4. Agent records Lesson -> 5. System is robust.

### 🛡️ Safety & Governance

- **Prohibited Actions:** strict rules against deleting files or committing secrets.
- **Human-in-the-Loop:** Mandatory stops for cost-intensive or ambiguous tasks.
- **Lesson Injection:** Past mistakes are permanently recorded in `system/lessons.md` and "transplanted" into future skills.

## 📦 Usage

### For Claude Code

The instructions are mirrored in `CLAUDE.md`. Claude Code will automatically detect and respect these rules when initialized in this directory.

### For Gemini CLI

The instructions are mirrored in `GEMINI.md`. Load this file into your Gemini context to activate the protocol.

## 🛠️ Repository Structure

```
├── AGENTS.md             # Master Instruction File (Orchestration Layer)
├── CLAUDE.md             # Mirror for Claude Code
├── GEMINI.md             # Mirror for Gemini CLI
├── skills/               # The "Brain" - Specific Capabilities
│   ├── create-new-skill/ # The Meta-Skill
│   └── SKILL_TEMPLATE.md # Standard Template
├── execution/            # The "Hands" - Python Scripts
│   └── scaffold_skill.py # Automation for creating skills
└── system/               # The "Memory"
    └── lessons.md        # Global Knowledge Base
```

## 🤝 Contributing

1. **Don't create skills manually.** Ask the agent to use `create-new-skill`.
2. **Review `lessons.md`** regularly to prune obsolete warnings.
