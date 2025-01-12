from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, select

from abstract.manager.manager import Manager
from model.exchange.exchange import Exchange
from schema.exchange.exchange import ExchangeSchema


class ExchangeManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def by_code(self, code: str) -> Optional[Exchange]:
        query_ = select(Exchange).where(Exchange.code == code)

        return self._session.exec(query_).first()

    def retrieve_unique(self, schema: ExchangeSchema) -> Optional[Exchange]:
        query_ = select(Exchange).where(Exchange.code == schema.code)

        return self._session.exec(query_).first()

    def persist(self, schema: ExchangeSchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[Exchange]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.name = schema.name
            existing_.code = schema.code
            existing_.country_id = foreign_keys['country_id']
            existing_.currency_id = foreign_keys['currency_id']

            self._session.flush()
            return existing_

        exchange_ = Exchange(name=schema.name, code=schema.code, country_id=foreign_keys['country_id'],
                             currency_id=foreign_keys['currency_id'])

        try:
            self._session.add(exchange_)

            self._session.flush()

            return existing_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
