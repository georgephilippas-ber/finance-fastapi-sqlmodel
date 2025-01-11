from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from abstract.manager.manager import Manager, SQLModelBound
from model.country.country import Country
from schema.country.country import CountrySchema


class CountryManager(Manager):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def by_cca2(self, cca2: str) -> Optional[Country]:
        query_ = select(Country).where(Country.cca2 == cca2.upper())

        return (await self._session.exec(query_)).first()

    async def by_cca3(self, cca3: str) -> Optional[Country]:
        query_ = select(Country).where(Country.cca3 == cca3.upper())

        return (await self._session.exec(query_)).first()

    async def retrieve_unique(self, schema: CountrySchema) -> Optional[Country]:
        query_ = select(Country).where(Country.cca2 == schema.iso_code.cca2)

        return (await self._session.exec(query_)).first()

    async def persist(self, schema: CountrySchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[Country]:
        existing_ = await self.retrieve_unique(schema)

        if existing_ is not None:
            return existing_

        country_ = Country(common_name=schema.name.common,
                           official_name=schema.name.official,
                           cca2=schema.iso_code.cca2,
                           cca3=schema.iso_code.cca3,
                           latitude=schema.location.latitude,
                           longitude=schema.location.longitude,
                           capital=schema.capital,
                           population=schema.population,
                           flag_url=schema.flag_url)

        try:
            self._session.add(country_)

            await self._session.commit()

            return country_
        except SQLAlchemyError as e:
            print(e)
            await self._session.rollback()

            return None
