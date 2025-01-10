import uvicorn
from fastapi import FastAPI

from core.environment.environment import load_environment

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    load_environment()

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
