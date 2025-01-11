from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel.ext.asyncio.session import AsyncSession

from abstract.manager.manager import Manager, BaseModelBound, SQLModelBound
from model.continent.continent import Continent
from schema.continent.continent import ContinentSchema

from sqlmodel import select


class ContinentManager(Manager):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def retrieve_unique(self, schema: ContinentSchema) -> Optional[Continent]:
        query_ = select(Continent).where(Continent.name == schema.name)

        return (await self._session.exec(query_)).first()

    async def persist(self, schema: ContinentSchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[
        Continent]:

        existing_ = await self.retrieve_unique(schema)

        if existing_ is not None:
            return existing_

        continent_ = Continent(name=schema.name)

        try:
            self._session.add(continent_)

            await self._session.commit()

            return continent_
        except SQLAlchemyError as e:
            print(e)
            await self._session.rollback()

            return None
