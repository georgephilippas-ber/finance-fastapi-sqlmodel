import json
from http import HTTPStatus
from typing import Any

from fastapi import Depends, HTTPException, APIRouter, Response, Body, Query, Request
from pydantic import BaseModel
from sqlmodel import Session

from configuration.security import JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES
from core.security.encryption.encryption import generate_session_id
from instance.dependency.dependency import get_user_manager, get_session
from instance.shared import json_web_token_instance, session_manager_instance
from manager.user.user_manager import UserManager

authentication_router = APIRouter(prefix="/authentication")


class UserLoginSchema(BaseModel):
    identifier: str
    password: str


@authentication_router.post("/login")
async def login(user_login_schema: UserLoginSchema, response: Response,
                user_manager: UserManager = Depends(get_user_manager), session: Session = Depends(get_session)):
    user_ = user_manager.verify_and_retrieve(user_login_schema.identifier, user_login_schema.password)
    session.close()
    print(user_manager.all())

    if user_ is not None:
        token_ = json_web_token_instance.encode(user_.model_dump(exclude={"password", "id"}))

        response.set_cookie(key="Authorization",
                            value=token_,
                            path="/",
                            httponly=True,
                            samesite="strict",
                            max_age=JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES * 60, secure=False)

        session_id_: str = generate_session_id()

        response.set_cookie(key="SESSION_ID", value=session_id_, path="/", httponly=True, samesite="strict",
                            max_age=JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES * 60)

        return {
            "access_token": token_,
            "SESSION_ID": session_id_,
        }
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Incorrect user identifier or password")


@authentication_router.post("/logout")
async def logout(request: Request, response: Response):
    session_id_ = request.cookies.get("SESSION_ID")
    if session_id_ is not None:
        session_manager_instance.close_session(session_id_)

    response.delete_cookie(key="Authorization", path="/", httponly=True, samesite="strict", secure=False)
    response.delete_cookie(key="SESSION_ID", path="/", httponly=True, samesite="strict")

    response.status_code = HTTPStatus.OK

    return response


@authentication_router.post("/session-set")
async def session_set(request: Request, key: str = Query(...), object_: Any = Body(...)):
    session_id_ = request.cookies.get("SESSION_ID")
    print(key, object_, session_id_)

    if session_id_ is not None:
        outcome_ = session_manager_instance.session_add(session_id_, key, json.dumps(object_))
    else:
        return {"status": "NO_SESSION"}

    return {"status": "SUCCESS" if outcome_ else "FAILURE"}


@authentication_router.get("/session-get")
async def session_get(request: Request, key: str = Query(...)) -> Any:
    session_id_ = request.cookies.get("SESSION_ID")
    print(session_id_, key)

    if session_id_ is not None:
        value_str_ = session_manager_instance.session_get(session_id_, key)

        if value_str_ is not None:
            return json.loads(value_str_)
        else:
            return None
    else:
        return None
