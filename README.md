# LLM Evaluation Application

A full-stack application designed to evaluate and compare the performance of multiple large language models (LLMs) such as GPT, Claude, and Gemini. This platform enables users to define **system prompts**, assign **test prompts**, and automatically assess model outputs using metrics like accuracy, coherence, and relevance. Built with a FastAPI backend and a React + TypeScript frontend, it provides a clean UI for managing experiments and visualizing evaluation results.

---

## About

This project serves as an end-to-end framework for benchmarking and analyzing large language model responses.  
Users can:

- Create and manage **System Prompts**
- Add and link **Test Prompts** to System Prompts
- Run evaluations across multiple LLMs (OpenAI, Anthropic, Gemini)
- View, compare, and analyze results with automated scoring metrics
- Manage data persistently using a PostgreSQL database

The app leverages **FastAPI** for the backend API, **PostgreSQL + SQLAlchemy ORM** for database operations, and **React with TypeScript** for a responsive, modular frontend interface.

---

## Tech Stack

- **Frontend**: React, TypeScript, Tailwind CSS  
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **ORM & Validation**: Pydantic, Alembic (for migrations)
- **Testing & Metrics**: DeepEval integration for model performance comparison
- **Containerization**: Docker (client, server, and database services)
- **API Architecture**: RESTful design

---

## Features

- **System & Test Prompt Management**:  
  Create, view, and delete system and test prompts dynamically through the frontend UI.

- **Dynamic UI Updates**:  
  React components automatically update upon CRUD operations without page refresh.

- **Multi-Model Evaluation**:  
  Evaluate system prompts across GPT, Claude, and Gemini simultaneously.

- **Automated Metrics**:  
  Integrated evaluation pipeline with DeepEval for computing metrics such as relevance, accuracy, and similarity.

- **RESTful API Endpoints**:  
  Organized backend routes for system prompts, test prompts, and evaluation modules.

- **Responsive Design**:  
  Modern, minimalistic frontend with Tailwind CSS for a clean and intuitive workflow.

---
