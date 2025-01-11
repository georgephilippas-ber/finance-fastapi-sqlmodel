from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select, Session

from abstract.manager.manager import Manager
from model.currency.currency import Currency
from schema.currency.currency import CurrencySchema


class CurrencyManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def retrieve_unique(self, schema: CurrencySchema) -> Optional[Currency]:
        query_ = select(Currency).where(Currency.code == schema.code)

        return (self._session.exec(query_)).first()

    def persist(self, schema: CurrencySchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[
        Currency]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            return existing_

        currency_ = Currency(name=schema.name, code=schema.code, symbol=schema.symbol)

        try:
            self._session.add(currency_)

            self._session.flush()

            return currency_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None

    def by_code(self, code: str) -> Optional[Currency]:
        query_ = select(Currency).where(Currency.code == code)

        return (self._session.exec(query_)).first()
