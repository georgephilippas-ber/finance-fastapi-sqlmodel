# Invest-igator

**Invest-igator** is a search engine designed for equity and ETF investments built with performance,
extensibility, and portability in mind, Invest-igator empowers users to efficiently search and explore investment
opportunities.

---

## **Features**

- **Extensible**: Designed to easily introduce new functionalities, making it adaptable to evolving needs.
- **Database agnostic**: Compatible with underlying databases, ensuring flexibility in deployment environments.
- **Fast and portable**: Optimized for high-speed operations while maintaining lightweight portability.

---

## ** Technology **

---

### 1. **Technologies Used**

- **Meilisearch**: A primary search engine backend delivering blazing search performance and simplicity.
- **FastAPI**: A modern, fast, web framework for Python that powers the API layer.
- **SQLModel**: A database abstraction layer for seamless communication with relational databases.
- **Docker & Docker Compose**: For containerizing and orchestrating the application for easy deployment.
- **Next.js**: React based framework for SSR and dynamic CSR components.

### 2. **Architecture**

Invest-igator follows a **layered architecture**, breaking functionality into specific layers for enhanced organization
and maintainability:

- **Routes**: Handle the external HTTP API endpoints interacted with by users or clients.
- **Orchestrators**: Manage complex workflows and coordinate business logic across services.
- **Services**: Implement business logic and act as an abstraction for the application core.
- **Managers**: Provide direct interactions with data sources.
- **Clients**: High-level abstraction for external APIs
- **Adapters**: Data conversion to and from schemas in the domain model.

This approach ensures:

- Loose coupling between components.
- Easier testing and debugging.
- Enhanced flexibility for future enhancements.

---

## **How to Get Started**

Follow these steps to run and utilize Invest-igator:

### 1. **Requirements**

- Python 3.10+
- Node.js
- Meilisearch instance running locally or in the cloud.
- A database supported by **SQLModel** (e.g., DuckDB, MySQL, PostgreSQL).

**or**

- Docker and Docker Compose (_using DuckDB_).

### 2. **Installation**

## **Docker Deployment Instructions**

Invest-igator comes with a Dockerized setup for seamless deployment.

1. **Run the Application**:
   Navigate to the `scripts` directory and execute the following:
   ```bash
   cd ./scripts
   ./docker-run.sh
   ```

   Once the services are up and running, access the application in your browser at:
   [http://localhost:3000](http://localhost:3000)

2. **Stop the Application**:
   To stop the running Docker services, use:
   ```bash
   ./docker-stop.sh
   ```

   This will cleanly stop the containers.