from fastapi import Depends, HTTPException
from http import HTTPStatus

from instances.dependencies.dependencies import get_user_manager
from instances.shared import json_web_token
from manager.user.user_manager import UserManager
from router.router import authentication_router
from schema.user.user import UserSchema


@authentication_router.post("/login")
async def login(user_schema: UserSchema, user_manager: UserManager = Depends(get_user_manager)):
    user_ = user_manager.verify_and_retrieve(user_schema.username, user_schema.password)

    if user_ is not None:
        return {
            "access_token": json_web_token.encode(user_.model_dump(exclude={"password"})),
        }
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Incorrect user identifier or password")
