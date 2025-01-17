from http import HTTPStatus

from fastapi import Depends, HTTPException, APIRouter, Response
from pydantic import BaseModel

from configuration.security import JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES
from instance.dependency.dependency import get_user_manager
from instance.shared import json_web_token_instance
from manager.user.user_manager import UserManager

authentication_router = APIRouter(prefix="/authentication")


class UserLoginSchema(BaseModel):
    identifier: str
    password: str


@authentication_router.post("/login")
async def login(user_login_schema: UserLoginSchema, response: Response,
                user_manager: UserManager = Depends(get_user_manager)):
    user_ = user_manager.verify_and_retrieve(user_login_schema.identifier, user_login_schema.password)

    if user_ is not None:
        token_ = json_web_token_instance.encode(user_.model_dump(exclude={"password", "id"}))

        response.set_cookie(key="Authorization",
                            value=token_,
                            httponly=True,
                            max_age=JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES * 60)

        return {
            "access_token": token_
        }
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Incorrect user identifier or password")


@authentication_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="Authorization")
    response.status_code = HTTPStatus.OK

    return response
