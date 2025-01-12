from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session
from sqlmodel import select

from abstract.manager.manager import Manager
from model.ticker.ticker import Ticker
from schema.ticker.ticker import TickerSchema, InstrumentType


class TickerManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def retrieve_unique(self, schema: TickerSchema) -> Optional[Ticker]:
        query_ = select(Ticker).where(Ticker.isin == schema.isin)

        return (self._session.exec(query_)).first()

    def persist(self, schema: TickerSchema, foreign_keys: Optional[dict] = None) -> Optional[Ticker]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.code = schema.code
            existing_.isin = schema.isin
            existing_.name = schema.name
            existing_.currency_id = foreign_keys['currency_id']
            existing_.exchange_id = foreign_keys['exchange_id']
            existing_.instrument_type = InstrumentType.from_str(schema.type)

            self._session.flush()
            return existing_

        ticker_ = Ticker(code=schema.code, exchange_id=foreign_keys['exchange_id'], isin=schema.isin, name=schema.name,
                         currency_id=foreign_keys['currency_id'], instrument_type=InstrumentType.from_str(schema.type))

        try:
            self._session.add(ticker_)

            self._session.flush()

            return existing_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
