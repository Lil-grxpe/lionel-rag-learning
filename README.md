# AI Application Engineering & SecOps Curriculum

A rigorous, project-driven self-learning roadmap designed to master production-grade **Retrieval-Augmented Generation (RAG)**, **Autonomous Multi-Agent Systems**, **Evaluation & Observability (RAGAS)**, and **LLM Security Hardening (OWASP Top 10 for LLMs)**.

---

## 📌 Repository Overview

This repository documents my end-to-end learning journey through 15 hands-on projects, rigorous engineering benchmarks, and daily development logs.

```text
.
├── etape0_setup/           # Environment setup, dependencies & API client validation
├── etape1_prompting/       # Prompt engineering, Pydantic structured parsing & API resilience
│   ├── resources/          # Raw test data (invoices, emails)
│   └── test_results/       # Benchmark JSON outputs and metrics
├── etape2_rag/             # Vector databases (Qdrant), document parsing & hybrid search
├── etape3_agents/          # Autonomous agents, ReAct loop, tool-calling & multi-agent systems
├── etape4_evaluation/      # RAGAS metrics, LLM-as-a-judge, latency and cost observability
├── etape5_secops/          # AI Security (prompt injections, guardrails, data leak prevention, audit)
└── learning_log/           # Daily engineering dev logs (architectural decisions & learnings)
```

---

## 🎯 Engineering Standards
- **Strict Typing & Schema Validation**: 100% of structured LLM outputs are enforced using Pydantic models.
- **Security-First Architecture**: Zero hardcoded secrets, strict input sanitization, and defensive guardrails.
- **Scientific Evaluation**: System improvements are measured with reproducible quantitative benchmarks (accuracy, latency, cost per query).
- **Production Resilience**: Implementation of exponential backoff, rate-limit retry strategies, and streaming responses.
