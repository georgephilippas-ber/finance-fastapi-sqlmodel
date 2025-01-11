from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select, Session

from abstract.manager.manager import Manager
from model.continent.continent import Continent
from schema.continent.continent import ContinentSchema


class ContinentManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def retrieve_unique(self, schema: ContinentSchema) -> Optional[Continent]:
        query_ = select(Continent).where(Continent.name == schema.name)

        return (self._session.exec(query_)).first()

    def persist(self, schema: ContinentSchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[
        Continent]:

        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            return existing_

        continent_ = Continent(name=schema.name)

        try:
            self._session.add(continent_)

            self._session.flush()

            return continent_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
