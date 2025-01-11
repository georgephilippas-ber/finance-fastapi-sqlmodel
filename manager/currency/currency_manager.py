from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from abstract.manager.manager import Manager
from model.currency.currency import Currency
from schema.currency.currency import CurrencySchema


class CurrencyManager(Manager):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def retrieve_unique(self, schema: CurrencySchema) -> Optional[Currency]:
        query_ = Currency.select().where(Currency.code == schema.code)

        return (await self._session.exec(query_)).first()

    async def persist(self, schema: CurrencySchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[
        Currency]:
        existing_ = await self.retrieve_unique(schema)

        if existing_ is not None:
            return existing_

        currency_ = Currency(name=schema.name, code=schema.code, symbol=schema.symbol)

        try:
            self._session.add(currency_)

            await self._session.commit()

            return currency_
        except SQLAlchemyError as e:
            print(e)
            await self._session.rollback()

            return None

    async def by_code(self, code: str) -> Optional[Currency]:
        query_ = select(Currency).where(Currency.code == code)

        return (await self._session.exec(query_)).first()
