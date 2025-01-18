from typing import Optional, Dict, Any

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select, Session

from abstract.manager.manager import Manager
from model.country.country import Country
from schema.country.country import CountrySchema


class CountryManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def by_cca2(self, cca2: str) -> Optional[Country]:
        query_ = select(Country).where(Country.cca2 == cca2.upper())

        return (self._session.exec(query_)).first()

    def by_cca3(self, cca3: str) -> Optional[Country]:
        query_ = select(Country).where(Country.cca3 == cca3.upper())

        return (self._session.exec(query_)).first()

    def retrieve_unique(self, schema: CountrySchema, **kwargs) -> Optional[Country]:
        query_ = select(Country).where(Country.cca2 == schema.iso_code.cca2)

        return (self._session.exec(query_)).first()

    def persist(self, schema: CountrySchema, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[Country]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.common_name = schema.name.common
            existing_.official_name = schema.name.official
            existing_.cca2 = schema.iso_code.cca2
            existing_.cca3 = schema.iso_code.cca3
            existing_.latitude = schema.location.latitude
            existing_.longitude = schema.location.longitude
            existing_.capital = schema.capital
            existing_.population = schema.population
            existing_.flag_url = schema.flag_url

            self._session.flush()
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

            self._session.flush()

            return country_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
