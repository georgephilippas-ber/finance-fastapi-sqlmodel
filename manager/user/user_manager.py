from typing import Optional, Literal, Tuple, List

from sqlalchemy import or_, and_
from sqlmodel import Session, select

from abstract.manager.manager import Manager
from core.encryption.encryption import hash_password
from model.user.user import User
from schema.user.user import UserSchema


class UserManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def verify_and_retrieve(self, identifier: str, password: str) -> Optional[User]:
        query_ = select(User).where(
            or_(User.username == identifier, User.email == identifier)
        )

        user_ = self._session.exec(query_).first()

        return user_ if user_ is not None and hash_password(password) == user_.password else None

    def retrieve_unique(self, schema: UserSchema) -> Optional[
        Tuple[User, Literal["exists_by_username", "exists_by_email"]]]:
        query_ = select(User).where(
            or_(User.username == schema.username, User.email == schema.email)
        )

        query_result_ = self._session.exec(query_).first()

        if query_result_ is not None:
            if query_result_.username == schema.username:
                return query_result_, "exists_by_username"
            elif query_result_.email == schema.email:
                return query_result_, "exists_by_email"

        return None

    def all(self) -> List[User]:
        return list(self._session.exec(select(User)).all())

    def persist(self, schema: UserSchema, foreign_keys: Optional[dict] = None) -> Tuple[
        Optional[User], Optional[Literal["exists_by_username", "exists_by_email", "other_error"]]]:
        existing_and_criteria_ = self.retrieve_unique(schema)

        if existing_and_criteria_ is not None:
            return None, existing_and_criteria_[1]
        else:
            user_ = User(username=schema.username, email=schema.email, password=hash_password(schema.password))

            try:
                self._session.add(user_)
                self._session.commit()
                self._session.refresh(user_)

                return user_, None
            except Exception as e:
                print(e)
                self._session.rollback()

                return None, "other_error"
