from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select

from abstract.manager.manager import Manager, BaseModelBound, SQLModelBound
from model.company.company import Company
from schema.company.company import CompanySchema


class CompanyManager(Manager):
    def __init__(self):
        super().__init__()

    def retrieve_unique(self, schema: CompanySchema) -> Optional[Company]:
        query_ = select(Company).where(Company.isin == schema.isin)

        return (self._session.exec(query_)).first()

    def persist(self, schema: CompanySchema, foreign_keys: Optional[dict] = None) -> Optional[Company]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.isin = schema.isin
            existing_.name = schema.name

            self._session.flush()
            return existing_

        company_ = Company(isin=schema.isin, name=schema.name, address=schema.address,
                           primary_ticker=schema.primary_ticker,
                           homepage=schema.homepage, logo_url=schema.logo_url, employees=schema.employees,
                           description=schema.description,
                           fiscal_year_end=schema.fiscal_year_end,
                           gics_sector_id=foreign_keys['gics_sector_id'],
                           gics_industry_group_id=foreign_keys['gics_industry_group_id'],
                           gics_industry_id=foreign_keys['gics_industry_id'],
                           gics_subindustry_id=foreign_keys['gics_subindustry_id'])

        try:
            self._session.add(company_)

            self._session.flush()

            return company_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
