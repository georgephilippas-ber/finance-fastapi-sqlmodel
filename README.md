# Invest-igator

**Invest-igator** is a search engine designed for equity and - in the future - Exchange-Traded Fund investments built
with
performance,
extensibility, and portability in mind. It enables value investors to efficiently search and explore investment
opportunities with respect to a variety of economic, financial and accounting performance metrics.

---

## Features

- **Extensible** in terms of data sources (multi-client), data nature (macroeconomic, financial etc.) and performance
  metrics (e.g. ROI or MCAP etc.)
- **Database agnostic** by leveraging SQLModel, an `SQLAlchemy` based ORM for Python and by abstracting functionalities
  of
  search engines (e.g. `meilisearch`, `elasticsearch` etc.)
- **Fast and portable** by employing the asynchronous capabilities of modern Python frameworks (e.g. using FastAPI for
  routing and `celery` for parallel execution) for efficiently distributing both I/O and CPU-bound intensive workloads

---

## Technology

---

### 1. **Technologies Used**

- **Meilisearch**: A Rust-based search engine backend delivering fast search performance and simplicity
- **FastAPI**: A modern, fast, web framework for Python that powers the API layer
- **SQLModel**: A database abstraction layer for seamless communication with relational databases
- **Next.js**: React based frontend framework for SSR and dynamic CSR components
- **Docker & Docker Compose**: For containerizing and orchestrating (locally) the application for easy deployment

### 2. **Architecture**

Invest-igator follows a **layered architecture**, breaking functionality into specific layers for enhanced organization
and maintainability:

- **Managers**: Provide direct interactions with persistent data sources (i.e. database tables)
- **Services**: Implement business logic and act as an abstraction for the application core
- **Orchestrators**: Manage complex workflows and coordinate business logic across services

- **Routes**: Handle the external HTTP API endpoints interacted with by users or clients
- **Clients**: High-level abstraction for external APIs
- **Adapters**: Data conversion to and from schemas in the domain model

This approach ensures:

- Loose coupling between components.
- Easier testing and debugging.
- Enhanced flexibility for future enhancements.

A customized dependency injection pattern for data seeding was developed and used alongside FastAPI's dependency
injection
mechanism that is meant to serve the HTTP API routes.

---

## **How to Get Started**

Follow these steps to run **Invest-igator**:

### **Requirements**

- Python 3.10+
- Node.js
- Meilisearch instance running locally or in the cloud.
- A SQL database server (MySQL, PostgreSQL) or a file-based SQL database (DuckDB)

**or**

- Docker (_exclusively DuckDB_)

## **Docker Deployment Instructions**

Invest-igator comes with a Dockerized setup for seamless deployment. It is based on Docker compose and scripts for
UNIX/Linux and Linux-like environments (MINGW, WSL) are provided:

1.**Run the Application**:
Navigate to the `scripts` directory and execute docker compose using:

   ```bash
   cd ./scripts
   ./docker-run.sh
   ```

Once the services are up and running, access the application in your browser at:
[http://localhost:3000](http://localhost:3000)

2.**Please use the following credentials to evaluate**:

* username: `user`
* password: `user!1A`

3.**Stop the Application**:
To stop the running Docker services, use:

   ```bash
   ./docker-stop.sh
   ```

This will cleanly stop the containers.
