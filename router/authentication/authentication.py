from http import HTTPStatus
from typing import Any

from fastapi import Depends, HTTPException, APIRouter, Response, Body
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

    if user_ is not None:
        token_ = json_web_token_instance.encode(user_.model_dump(exclude={"password", "id"}))

        response.set_cookie(key="Authorization",
                            value=token_,
                            httponly=True,
                            samesite="strict",
                            max_age=JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES * 60)

        response.set_cookie(key="SESSION_ID", value=generate_session_id(), httponly=True, samesite="strict",
                            max_age=JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES * 60)

        return {
            "access_token": token_
        }
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Incorrect user identifier or password")


@authentication_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="Authorization")
    response.delete_cookie(key="SESSION_ID")

    response.status_code = HTTPStatus.OK

    return response


@authentication_router.post("/session-set")
async def session_set(object_: Any = Body(...)):
    session_manager_instance.set(object_)
