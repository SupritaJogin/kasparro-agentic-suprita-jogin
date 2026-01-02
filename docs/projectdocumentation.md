## Multi-Agent Architecture Overview

This system is designed as a true multi-agent architecture.

- Agents are autonomous and unaware of each other
- Agents react to task messages using a common interface
- The orchestrator dynamically routes tasks to agents
- Task flow is message-driven, not hard-coded
- Output is generated through a structured pipeline

### Agent Roles
- ProductParserAgent: Validates and normalizes raw product data
- ContentGenerationAgent: Generates structured content from parsed data

### Orchestration
The orchestrator acts as a coordinator, dispatching tasks to agents without embedding business logic.

### Output Pipeline
Final agent outputs are written to structured JSON files using reusable logic blocks.
# \# Applied AI Engineer Challenge – Agentic Content Genera# Applied AI Engineer Challenge – Agentic Content Generation System

# 

# \## 1. Problem Statement

# Design and implement a modular agentic system that transforms structured product data into

# machine-readable content pages.  

# The system must demonstrate clear agent boundaries, reusable logic blocks, orchestration flow,

# and structured JSON outputs.

# 

# ---

# 

# \## 2. Solution Overview

# This project implements a multi-agent content generation pipeline where each agent is responsible

# for a single, well-defined task.  

# An orchestrator coordinates the agents and assembles final outputs using reusable logic blocks

# and template engines.

# 

# The system produces three JSON pages:

# \- FAQ Page

# \- Product Page

# \- Comparison Page

# 

# ---

# 

# \## 3. Scope \& Assumptions

# \- Only provided product data is used (no external enrichment).

# \- Content quality is secondary to system design and correctness.

# \- Product comparison uses a fictional Product B as permitted.

# \- The system is deterministic and reproducible.

# 

# ---

# 

# \## 4. System Design (Core)

# 

# \### 4.1 Agents

# \- \*\*ProductParserAgent\*\*

# &nbsp; - Validates and normalizes raw product input.

# &nbsp; - Outputs a clean internal product representation.

# 

# \- \*\*QuestionGeneratorAgent\*\*

# &nbsp; - Generates categorized user questions from product attributes.

# &nbsp; - Categories include Informational, Usage, Safety, Purchase, and Comparison.

# 

# Each agent has:

# \- Single responsibility

# \- Clear input/output contract

# \- No shared global state

# 

# ---

# 

# \### 4.2 Logic Blocks

# Reusable transformation units:

# \- `generate\_benefits`

# \- `generate\_usage`

# \- `generate\_safety`

# 

# These blocks are shared across templates to ensure composability and reuse.

# 

# ---

# 

# \### 4.3 Template Engine

# Custom templates assemble final pages:

# \- FAQ Template

# \- Product Page Template

# \- Comparison Template

# 

# Templates define:

# \- Output schema

# \- Dependencies on logic blocks

# \- Structured JSON formatting

# 

# ---

# 

# \### 4.4 Orchestration Flow

# The orchestrator executes the pipeline in sequence:

# 

# 1\. Parse product data

# 2\. Generate user questions

# 3\. Build FAQ, Product, and Comparison pages

# 4\. Persist machine-readable JSON outputs

# 

# The pipeline is executed via a central orchestrator module.

# 

# ---

# 

# \## 5. Output Structure

# All outputs are valid JSON and stored under `/outputs`:

# \- `faq.json`

# \- `product\_page.json`

# \- `comparison\_page.json`

# 

# ---

# 

# \## 6. Engineering Principles

# \- Modularity over monolithic design

# \- Explicit contracts between components

# \- Reusability and extensibility

# \- Clarity over cleverness

# tion System

# 

# \## 1. Problem Statement

# Design and implement a modular agentic system that transforms structured product data into

# machine-readable content pages.  

# The system must demonstrate clear agent boundaries, reusable logic blocks, orchestration flow,

# and structured JSON outputs.

# 

# ---

# 

# \## 2. Solution Overview

# This project implements a multi-agent content generation pipeline where each agent is responsible

# for a single, well-defined task.  

# An orchestrator coordinates the agents and assembles final outputs using reusable logic blocks

# and template engines.

# 

# The system produces three JSON pages:

# \- FAQ Page

# \- Product Page

# \- Comparison Page

# 

# ---

# 

# \## 3. Scope \& Assumptions

# \- Only provided product data is used (no external enrichment).

# \- Content quality is secondary to system design and correctness.

# \- Product comparison uses a fictional Product B as permitted.

# \- The system is deterministic and reproducible.

# 

# ---

# 

# \## 4. System Design (Core)

# 

# \### 4.1 Agents

# \- \*\*ProductParserAgent\*\*

# &nbsp; - Validates and normalizes raw product input.

# &nbsp; - Outputs a clean internal product representation.

# 

# \- \*\*QuestionGeneratorAgent\*\*

# &nbsp; - Generates categorized user questions from product attributes.

# &nbsp; - Categories include Informational, Usage, Safety, Purchase, and Comparison.

# 

# Each agent has:

# \- Single responsibility

# \- Clear input/output contract

# \- No shared global state

# 

# ---

# 

# \### 4.2 Logic Blocks

# Reusable transformation units:

# \- `generate\_benefits`

# \- `generate\_usage`

# \- `generate\_safety`

# 

# These blocks are shared across templates to ensure composability and reuse.

# 

# ---

# 

# \### 4.3 Template Engine

# Custom templates assemble final pages:

# \- FAQ Template

# \- Product Page Template

# \- Comparison Template

# 

# Templates define:

# \- Output schema

# \- Dependencies on logic blocks

# \- Structured JSON formatting

# 

# ---

# 

# \### 4.4 Orchestration Flow

# The orchestrator executes the pipeline in sequence:

# 

# 1\. Parse product data

# 2\. Generate user questions

# 3\. Build FAQ, Product, and Comparison pages

# 4\. Persist machine-readable JSON outputs

# 

# The pipeline is executed via a central orchestrator module.

# 

# ---

# 

# \## 5. Output Structure

# All outputs are valid JSON and stored under `/outputs`:

# \- `faq.json`

# \- `product\_page.json`

# \- `comparison\_page.json`

# 

# ---

# 

# \## 6. Engineering Principles

# \- Modularity over monolithic design

# \- Explicit contracts between components

# \- Reusability and extensibility

# \- Clarity over cleverness



