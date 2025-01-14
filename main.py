from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session

from configuration.server import NEXUS_SERVER
from core.environment.environment import load_environment
from database.database import Database
from model.user.user import User
from router.router import authentication_router

from fastapi.middleware.cors import CORSMiddleware
from instances.shared import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[NEXUS_SERVER],
    allow_credentials=True,
    allow_headers=["*"],
)

app.include_router(authentication_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users")
async def users(database_: Database = Depends(lambda: database)) -> List[User]:
    pass


if __name__ == "__main__":
    load_environment()

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
