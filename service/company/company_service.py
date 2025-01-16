from typing import Optional, Any

from pydantic import BaseModel
from sqlmodel import select, Session

from database.database import Database
from model.company.company import Company
from model.country.country import Country


class CompanyOverviewSchema(BaseModel):
    country_flag_url: str


class CompanyService:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def get_company_overview(self, id_: int) -> Optional[Any]:
        query_ = select(Company.id, Company.name, Company.logo_url).select_from(Company).join(Country,
                                                                                              Company.country_id == Country.id).where(
            Company.id == id_)

        return self._session.exec(query_).first()


if __name__ == '__main__':
    import model.comprehensive

    db = Database()
    db.create_tables(drop_all=False)

    with db.create_session() as session:
        cs = CompanyService(session)

        print(cs.get_company_overview(1))
