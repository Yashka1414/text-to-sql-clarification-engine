# 🗄️ Text-to-SQL System with Clarification Engine

A high-performance Natural Language to SQL conversion engine powered by **Groq Cloud API (Llama-3.3-70B)** and **Streamlit**. Features dynamic schema parsing, structured output verification, and an active clarification engine to prevent faulty queries on ambiguous inputs.

## 🚀 Live Demo
🔗 [Click Here to View Live App](https://text-to-sql-clarification-engine-kn6p6vbfu8.streamlit.app)

## ✨ Core Features & Technical Architecture
* **Schema-Aware SQL Generation:** Dynamically ingests database DDL schemas to formulate accurate, syntactically correct ANSI SQL statements.
* **Clarification Engine:** Detects ambiguous user intents (e.g., missing aggregate metrics or multi-table column ambiguities) and prompts key clarifying questions before execution.
* **Structured Parsing & Guardrails:** Configured with deterministic low temperature controls ($0.1$) to ensure reliable SQL synthesis.
* **Dynamic Security:** Zero hardcoded credentials with sidebar key handling.

## 🛠️ Tech Stack & Demonstrated Skills
* **LLM Engine:** Groq Cloud API (`llama-3.3-70b-versatile`)
* **Data Validation & Parsing:** Pydantic & System Prompt Engineering
* **Frontend & Infrastructure:** Streamlit Cloud
