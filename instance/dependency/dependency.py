from fastapi import Depends
from sqlmodel import Session

from database.database import Database
from instance.shared import database_instance
from manager.user.user_manager import UserManager
from service.company.company_service import CompanyService


def get_session(database_: Database = Depends(lambda: database_instance)) -> Session:
    return database_.create_session()


def get_user_manager(session: Session = Depends(get_session)) -> UserManager:
    return UserManager(session)


def get_company_service(session: Session = Depends(get_session)) -> CompanyService:
    return CompanyService(session)
