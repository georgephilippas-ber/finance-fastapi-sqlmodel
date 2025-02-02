import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configuration.seed import SEED_ON_STARTUP, SEED_ENTITIES_SPECIFICATION, DROP_ALL_TABLES_BEFORE_SEEDING
from configuration.server import NEXUS_SERVER
from core.environment.environment import load_environment, is_running_in_docker
from instance.shared import database_instance
from router.authentication.authentication_router import authentication_router
from router.company.company_router import company_router
from router.company.ticker_router import ticker_router
from seeder.main_seeder import seed


# from router.ai.ai import ai_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    database_instance.create_tables(drop_all=False)

    if is_running_in_docker():
        print("DOCKER")
    else:
        print("LOCAL")

    load_environment()

    if is_running_in_docker():
        from seeder.meilisearch.seed_meilisearch import seed_meilisearch

        with database_instance.create_session() as session:
            await seed_meilisearch(session)

    if SEED_ON_STARTUP:
        await seed(SEED_ENTITIES_SPECIFICATION, drop_all=DROP_ALL_TABLES_BEFORE_SEEDING, debug=True)

    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[NEXUS_SERVER, "http://localhost:3000"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

app.include_router(authentication_router)
app.include_router(ticker_router)
app.include_router(company_router)


# app.include_router(ai_router)


@app.get("/")
async def root():
    return {
        "message": "Hello World!",
        "docker": is_running_in_docker(),
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {
        "message": f"Hello {name}",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0" if is_running_in_docker() else "127.0.0.1", port=8000, reload=False)
