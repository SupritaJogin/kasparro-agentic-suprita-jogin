\# Multi-Agent Content Generation System  

\*\*Applied AI Engineer Assignment – Kasparro\*\*



---



\## 📌 Overview

This project implements a \*\*true multi-agent content generation system\*\* that converts structured product data into production-ready content outputs.



The system is designed to demonstrate:

\- Agent autonomy

\- Dynamic agent coordination

\- Message-driven orchestration

\- Structured output pipelines



This submission aligns with the original intent of the Kasparro Applied AI assignment.



---



\## 🧠 Architecture Philosophy

This system is \*\*not a static pipeline or sequential script\*\*.



Core principles:

\- Agents are \*\*independent and autonomous\*\*

\- Agents operate on \*\*task messages\*\*

\- The orchestrator coordinates agents but does \*\*not\*\* contain business logic

\- Execution flow is \*\*dynamic\*\*, not hard-coded



---



\## 🧩 System Components



\### 1️⃣ Base Agent Interface

All agents inherit from a common interface:



```python

class BaseAgent:

&nbsp;   def handle(self, task: dict):

&nbsp;       ...

This ensures agents independently decide whether to act on a task.



2️⃣ Agents

ProductParserAgent

Handles PARSE\_PRODUCT tasks



Validates and normalizes raw product data



Outputs a PARSED\_PRODUCT message



ContentGenerationAgent

Handles PARSED\_PRODUCT tasks



Generates structured product content



Outputs a GENERATED\_CONTENT message



Agents do not call each other directly and remain unaware of other agents.



3️⃣ Orchestrator

The orchestrator:



Maintains a list of available agents



Dispatches tasks dynamically



Routes tasks based on agent capability



Does not embed transformation logic



This enables true agent coordination instead of static control flow.



4️⃣ Logic Blocks

Reusable logic blocks handle shared functionality.



Example:



Output writing logic generates structured JSON files



Logic blocks are independent of agents and orchestration.



5️⃣ Structured Output Pipeline

Final outputs are written as structured JSON artifacts.



Example:



outputs/product\_page.json



This ensures clarity and production readiness.



▶️ Execution

Run the system using:



bash

Copy code

python -m orchestrator.orchestrator

The generated output will be available in the outputs/ directory.# Multi-Agent Content Generation System  

\*\*Applied AI Engineer Assignment – Kasparro\*\*



---



\## 📌 Overview

This project implements a \*\*true multi-agent content generation system\*\* that converts structured product data into production-ready content outputs.



The system is designed to demonstrate:

\- Agent autonomy

\- Dynamic agent coordination

\- Message-driven orchestration

\- Structured output pipelines



This submission aligns with the original intent of the Kasparro Applied AI assignment.



---



\## 🧠 Architecture Philosophy

This system is \*\*not a static pipeline or sequential script\*\*.



Core principles:

\- Agents are \*\*independent and autonomous\*\*

\- Agents operate on \*\*task messages\*\*

\- The orchestrator coordinates agents but does \*\*not\*\* contain business logic

\- Execution flow is \*\*dynamic\*\*, not hard-coded



---



\## 🧩 System Components



\### 1️⃣ Base Agent Interface

All agents inherit from a common interface:



```python

class BaseAgent:

&nbsp;   def handle(self, task: dict):

&nbsp;       ...

This ensures agents independently decide whether to act on a task.



2️⃣ Agents

ProductParserAgent

Handles PARSE\_PRODUCT tasks



Validates and normalizes raw product data



Outputs a PARSED\_PRODUCT message



ContentGenerationAgent

Handles PARSED\_PRODUCT tasks



Generates structured product content



Outputs a GENERATED\_CONTENT message



Agents do not call each other directly and remain unaware of other agents.



3️⃣ Orchestrator

The orchestrator:



Maintains a list of available agents



Dispatches tasks dynamically



Routes tasks based on agent capability



Does not embed transformation logic



This enables true agent coordination instead of static control flow.



4️⃣ Logic Blocks

Reusable logic blocks handle shared functionality.



Example:



Output writing logic generates structured JSON files



Logic blocks are independent of agents and orchestration.



5️⃣ Structured Output Pipeline

Final outputs are written as structured JSON artifacts.



Example:



outputs/product\_page.json



This ensures clarity and production readiness.



▶️ Execution

Run the system using:



bash

Copy code

python -m orchestrator.orchestrator

The generated output will be available in the outputs/ directory.

