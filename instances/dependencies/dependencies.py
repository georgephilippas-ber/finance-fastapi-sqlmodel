from fastapi import Depends
from sqlmodel import Session

from database.database import Database
from instances.shared import database
from manager.user.user_manager import UserManager


def get_session(database_: Database = Depends(lambda: database)) -> Session:
    return database_.create_session()


def get_user_manager(session: Session = Depends(get_session)) -> UserManager:
    return UserManager(session)
