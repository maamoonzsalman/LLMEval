# LLM Evaluation Application

A full-stack application built to evaluate, compare, and manage large language model (LLM) outputs efficiently. This platform allows users to create system prompts, attach test prompts, and assess model responses across different evaluation metrics. Designed for flexibility and scalability, it integrates modern web technologies to streamline LLM benchmarking and experimentation.

---

## About

This project provides a comprehensive interface for evaluating multiple LLMs through a unified workflow. Users can:
- Create and manage **system prompts**
- Add and delete **test prompts**
- Compare outputs from various **LLM providers** (e.g., OpenAI, Anthropic, Google)
- Track and visualize **evaluation metrics** like accuracy, coherence, and reasoning quality
- Manage prompts dynamically through an interactive frontend with instant state updates

The app uses a **React + Next.js** frontend for dynamic interactivity, a **FastAPI** backend for efficient API handling, and **PostgreSQL** for structured storage of prompt data and evaluation results.

---

## Tech Stack

- **Frontend**: Next.js (React, TypeScript, Tailwind CSS)
- **Backend**: FastAPI (Python, Async SQLAlchemy)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy with Alembic for migrations
- **Evaluation Framework**: DeepEval
- **APIs Integrated**: OpenAI, Anthropic, Google Gemini
- **Architecture**: RESTful API design with async endpoints

---

## Features

- **Prompt Management**: Create and delete system and test prompts with instant UI synchronization.
- **Evaluation Engine**: Run automated model comparisons using configurable evaluation metrics.
- **Multi-Model Support**: Compare responses from multiple LLMs side by side.
- **Async Backend**: Fully asynchronous FastAPI backend for high-performance model queries.
- **Dynamic Frontend Updates**: React hooks and Axios integration for seamless, real-time interface updates.
- **Secure Configuration**: Environment-based setup for API keys and database credentials.

---
