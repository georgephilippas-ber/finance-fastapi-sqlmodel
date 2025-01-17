from http import HTTPStatus
from typing import Optional

from fastapi import Depends, Request, HTTPException
from sqlmodel import Session

from configuration.security import API_SECURITY_ENABLED
from database.database import Database
from instance.shared import database_instance, json_web_token_instance
from manager.user.user_manager import UserManager
from service.company.company_service import CompanyService


def get_json_web_token(request: Request) -> Optional[str]:
    return request.cookies.get("Authorization")


def verify_json_web_token_cookie(token: Optional[str] = Depends(get_json_web_token)) -> None:
    if token and json_web_token_instance.verify_token(token):
        return
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)


def bypass_security() -> None:
    pass


api_security = verify_json_web_token_cookie if API_SECURITY_ENABLED else bypass_security


def get_session(database_: Database = Depends(lambda: database_instance)) -> Session:
    return database_.create_session()


def get_user_manager(session: Session = Depends(get_session)) -> UserManager:
    return UserManager(session)


def get_company_service(session: Session = Depends(get_session)) -> CompanyService:
    return CompanyService(session)
