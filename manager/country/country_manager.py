from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from abstract.manager.manager import Manager
from model.country.country import Country
from schema.country.country import CountrySchema

from sqlmodel import select


class CountryManager(Manager):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def by_cca2(self, cca2: str) -> Optional[Country]:
        query_ = select(Country).where(Country.cca2 == cca2.upper())

        return (await self._session.exec(query_)).first()

    async def by_cca3(self, cca2: str) -> Optional[Country]:
        query_ = select(Country).where(Country.cca3 == cca2.upper())

        return (await self._session.exec(query_)).first()

    async def persist(self, country_schema: CountrySchema) -> Optional[Country]:
        country_ = Country(common_name=country_schema.name.common,
                           official_name=country_schema.name.official,
                           cca2=country_schema.iso_code.cca2,
                           cca3=country_schema.iso_code.cca3,
                           latitude=country_schema.location.latitude,
                           longitude=country_schema.location.longitude,
                           capital=country_schema.capital,
                           population=country_schema.population,
                           flag_url=country_schema.flag_url)

        try:
            self._session.add(country_)

            await self._session.commit()
        except SQLAlchemyError as e:
            print(e)
            await self._session.rollback()

            return None
