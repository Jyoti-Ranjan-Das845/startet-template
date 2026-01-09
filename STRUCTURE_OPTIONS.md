# Project Structure Options

This guide provides different project structure patterns you can adapt based on your GenAI project needs. Choose the one that fits your use case, or mix and match elements.

## Table of Contents

1. [Flat Structure (Simple Projects)](#1-flat-structure-simple-projects)
2. [Src Layout (Recommended for Libraries)](#2-src-layout-recommended-for-libraries)
3. [Feature-Based Structure (Large Applications)](#3-feature-based-structure-large-applications)
4. [API-First Structure (FastAPI/Web Services)](#4-api-first-structure-fastapiweb-services)
5. [RAG Application Structure](#5-rag-application-structure)
6. [Multi-Agent System Structure](#6-multi-agent-system-structure)

---

## 1. Flat Structure (Simple Projects)

**Best for:** Small scripts, CLI tools, quick prototypes

```
project/
├── main.py                 # Entry point
├── config.py               # Configuration
├── utils.py                # Helper functions
├── llm_client.py          # LLM interaction
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

**Pros:**
- Simple and straightforward
- Easy to navigate
- Quick to set up

**Cons:**
- Doesn't scale well
- Can become messy with growth

---

## 2. Src Layout (Recommended for Libraries)

**Best for:** Reusable packages, libraries, medium-to-large projects

```
project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── llm.py
│       │   └── embeddings.py
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── text_processing.py
│       │   └── validators.py
│       ├── config.py
│       └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── core/
│   │   └── test_llm.py
│   └── utils/
│       └── test_text_processing.py
├── scripts/
│   ├── setup_db.py
│   └── run_pipeline.py
├── docs/
│   └── usage.md
├── .env.example
├── pyproject.toml
└── README.md
```

**Pros:**
- Clean separation of concerns
- Prevents accidental imports
- Professional standard
- Easier testing

**Cons:**
- Extra nesting level
- Slightly more setup

**Key principle:** Package code in `src/` to avoid import issues.

---

## 3. Feature-Based Structure (Large Applications)

**Best for:** Complex applications with multiple features

```
project/
├── src/
│   └── my_app/
│       ├── __init__.py
│       ├── shared/
│       │   ├── __init__.py
│       │   ├── config.py
│       │   ├── database.py
│       │   └── llm_client.py
│       ├── features/
│       │   ├── __init__.py
│       │   ├── chat/
│       │   │   ├── __init__.py
│       │   │   ├── service.py
│       │   │   ├── prompts.py
│       │   │   └── models.py
│       │   ├── summarization/
│       │   │   ├── __init__.py
│       │   │   ├── service.py
│       │   │   └── chunking.py
│       │   └── search/
│       │       ├── __init__.py
│       │       ├── service.py
│       │       └── ranking.py
│       └── cli.py
├── tests/
│   ├── shared/
│   │   └── test_llm_client.py
│   └── features/
│       ├── chat/
│       │   └── test_service.py
│       └── summarization/
│           └── test_service.py
├── pyproject.toml
└── README.md
```

**Pros:**
- Excellent for team collaboration
- Clear feature boundaries
- Easy to add/remove features
- Good for microservices migration

**Cons:**
- Can be overkill for small projects
- More directories to navigate

---

## 4. API-First Structure (FastAPI/Web Services)

**Best for:** REST APIs, web services, client-facing applications

```
project/
├── src/
│   └── api/
│       ├── __init__.py
│       ├── main.py             # FastAPI app
│       ├── config.py           # Settings
│       ├── dependencies.py     # Dependency injection
│       ├── routers/
│       │   ├── __init__.py
│       │   ├── chat.py
│       │   ├── embeddings.py
│       │   └── health.py
│       ├── services/
│       │   ├── __init__.py
│       │   ├── llm_service.py
│       │   ├── vector_service.py
│       │   └── cache_service.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── requests.py     # Pydantic request models
│       │   └── responses.py    # Pydantic response models
│       ├── core/
│       │   ├── __init__.py
│       │   ├── security.py
│       │   └── middleware.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── test_main.py
│   ├── routers/
│   │   └── test_chat.py
│   └── services/
│       └── test_llm_service.py
├── alembic/                    # Database migrations (if needed)
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

**Pros:**
- Standard API project structure
- Clear separation of layers
- Easy to add authentication/middleware
- Follows FastAPI best practices

**Cons:**
- More boilerplate
- Overkill for non-API projects

---

## 5. RAG Application Structure

**Best for:** Retrieval-Augmented Generation applications

```
project/
├── src/
│   └── rag_app/
│       ├── __init__.py
│       ├── config.py
│       ├── ingestion/
│       │   ├── __init__.py
│       │   ├── loaders.py          # Document loaders
│       │   ├── chunkers.py         # Text chunking strategies
│       │   └── processors.py       # Text preprocessing
│       ├── embedding/
│       │   ├── __init__.py
│       │   ├── embedder.py         # Embedding generation
│       │   └── models.py           # Embedding model configs
│       ├── storage/
│       │   ├── __init__.py
│       │   ├── vector_store.py     # Vector DB operations
│       │   └── metadata_store.py   # Document metadata
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── retriever.py        # Retrieval strategies
│       │   ├── reranker.py         # Result reranking
│       │   └── filters.py          # Metadata filtering
│       ├── generation/
│       │   ├── __init__.py
│       │   ├── llm.py              # LLM client
│       │   ├── prompts.py          # Prompt templates
│       │   └── chains.py           # LangChain/custom chains
│       └── pipeline.py             # End-to-end RAG pipeline
├── data/
│   ├── raw/                        # Original documents
│   ├── processed/                  # Processed chunks
│   └── samples/                    # Sample data for testing
├── tests/
│   ├── ingestion/
│   ├── retrieval/
│   └── generation/
├── notebooks/                      # Experimentation notebooks
│   └── rag_evaluation.ipynb
├── scripts/
│   ├── ingest_documents.py
│   └── evaluate_rag.py
├── pyproject.toml
└── README.md
```

**Pros:**
- Clear RAG pipeline stages
- Easy to swap components
- Good for experimentation
- Follows RAG best practices

**Cons:**
- Can be complex for simple use cases
- Requires understanding of RAG architecture

---

## 6. Multi-Agent System Structure

**Best for:** CrewAI, AutoGen, or custom agent systems

```
project/
├── src/
│   └── agent_system/
│       ├── __init__.py
│       ├── config.py
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── base_agent.py       # Base agent class
│       │   ├── researcher.py       # Research agent
│       │   ├── writer.py           # Writing agent
│       │   ├── critic.py           # Review agent
│       │   └── coordinator.py      # Orchestration agent
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── web_search.py       # Web search tool
│       │   ├── calculator.py       # Calculation tool
│       │   └── file_ops.py         # File operations
│       ├── memory/
│       │   ├── __init__.py
│       │   ├── short_term.py       # Conversation memory
│       │   └── long_term.py        # Persistent memory
│       ├── workflows/
│       │   ├── __init__.py
│       │   ├── research_workflow.py
│       │   └── writing_workflow.py
│       ├── prompts/
│       │   ├── __init__.py
│       │   ├── system_prompts.py
│       │   └── task_prompts.py
│       └── orchestrator.py         # Main coordinator
├── tests/
│   ├── agents/
│   │   └── test_researcher.py
│   ├── tools/
│   │   └── test_web_search.py
│   └── workflows/
│       └── test_research_workflow.py
├── logs/                           # Agent interaction logs
├── pyproject.toml
└── README.md
```

**Pros:**
- Modular agent design
- Easy to add new agents/tools
- Clear workflow definitions
- Good for complex AI systems

**Cons:**
- Complex structure
- Requires agent framework knowledge
- Can be over-engineered for simple tasks

---

## Choosing the Right Structure

### Decision Tree:

1. **Building a quick script or CLI?**
   → Use **Flat Structure**

2. **Creating a reusable library or package?**
   → Use **Src Layout**

3. **Building a REST API or web service?**
   → Use **API-First Structure**

4. **Building a RAG application?**
   → Use **RAG Application Structure**

5. **Building multi-agent systems?**
   → Use **Multi-Agent System Structure**

6. **Building a large app with multiple features?**
   → Use **Feature-Based Structure**

### General Tips:

- **Start simple, refactor as you grow**
- **Consistency matters more than perfection**
- **Keep tests mirroring your source structure**
- **Use `__init__.py` to control public APIs**
- **Document your structure choices in README**

---

## Common Patterns Across All Structures

Regardless of which structure you choose, include:

```
├── tests/              # Always mirror your source structure
├── scripts/            # Utility scripts (migrations, setup, etc.)
├── docs/               # Documentation
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── pyproject.toml      # Project configuration
└── README.md           # Project overview and setup
```

---

## Migration Strategy

If you need to change structure later:

1. Create new structure in parallel
2. Move modules one by one
3. Update imports gradually
4. Run tests after each move
5. Use IDE refactoring tools
6. Keep old structure until fully migrated

Remember: **The best structure is the one that works for your team and project!**
