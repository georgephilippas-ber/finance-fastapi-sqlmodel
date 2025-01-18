from fastapi import APIRouter, Query

from concurrency.concurrency import infer

ai_router = APIRouter(prefix="/ai")


@ai_router.get("/query")
async def get_ai(query: str = Query(...)):
    task = infer.delay(query)
    print(task)
    return {"task_id": task.id}


@ai_router.get("/poll-result")
async def get_task_result(task_id: str = Query(...)):
    task_result = infer.AsyncResult(task_id)

    match task_result.state:
        case "SUCCESS":
            return {
                "status": task_result.state,
                "detail": task_result.result
            }
        case "PENDING" | "STARTED":
            return {
                "status": task_result.state,
            }
        case "FAILURE":
            return {
                "status": task_result.state,
                "detail": str(task_result.info)
            }
        case _:
            return {"status": task_result.state}
