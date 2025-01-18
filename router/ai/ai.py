from fastapi import APIRouter

ai_router = APIRouter(prefix="/ai")


@ai_router.get("/example")
async def get_ai():
    return {"message": "Hello World"}
