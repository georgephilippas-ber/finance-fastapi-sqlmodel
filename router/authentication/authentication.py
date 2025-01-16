from fastapi import Depends, HTTPException, APIRouter, Response
from http import HTTPStatus

from pydantic import BaseModel

from configuration.security import JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES
from instances.dependencies.dependencies import get_user_manager
from instances.shared import json_web_token
from manager.user.user_manager import UserManager

from schema.user.user import UserSchema

authentication_router = APIRouter(prefix="/authentication")


class UserLoginSchema(BaseModel):
    identifier: str
    password: str


@authentication_router.post("/login")
async def login(user_schema: UserLoginSchema, response: Response,
                user_manager: UserManager = Depends(get_user_manager)):
    user_ = user_manager.verify_and_retrieve(user_schema.identifier, user_schema.password)

    if user_ is not None:
        token_ = json_web_token.encode(user_.model_dump(exclude={"password", "id"}))

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
