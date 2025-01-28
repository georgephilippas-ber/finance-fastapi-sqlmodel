import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configuration.server import NEXUS_SERVER
from core.environment.environment import load_environment
from instance.shared import database_instance
from router.ai.ai import ai_router
from router.authentication.authentication import authentication_router
from router.company.company import company_router
from seeder.meilisearch.seed_meilisearch import seed_meilisearch

app = FastAPI()

database_instance.create_tables(drop_all=False)

session_ = database_instance.create_session()
asyncio.run(seed_meilisearch(session_))

app.add_middleware(
    CORSMiddleware,
    allow_origins=[NEXUS_SERVER],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

app.include_router(authentication_router)
app.include_router(company_router)
app.include_router(ai_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    load_environment()

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
