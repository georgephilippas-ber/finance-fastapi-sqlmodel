from typing import Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session
from sqlmodel import select

from abstract.manager.manager import Manager
from manager.exchange.exchange_manager import ExchangeManager
from model.ticker.ticker import Ticker
from schema.ticker.ticker import TickerSchema, InstrumentType

from random import sample


class TickerManager(Manager):
    _exchange_manager: ExchangeManager

    def __init__(self, session: Session, exchange_manager: ExchangeManager):
        super().__init__(session)

        self._exchange_manager = exchange_manager

    def by_id(self, id_: int) -> Optional[Ticker]:
        query_ = select(Ticker).where(Ticker.id == id_)

        return self._session.exec(query_).first()

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

    def all(self, sample_size: Optional[int] = None) -> list[Tuple[str, str, int]]:
        try:
            query_ = select(Ticker)

            population_ = [(ticker_.code, ticker_.exchange.code, ticker_.id) for ticker_ in
                           self._session.exec(query_).all()]

            if sample_size is not None and sample_size < len(population_):
                return sample(population_, sample_size)
            else:
                return population_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return []


if __name__ == '__main__':
    pass
