from typing import List, Optional

from sqlalchemy import Engine, text

from core.search.meilisearch.meilisearch_client import MeilisearchClient
from database.database import Database
from schema.company.company import CompanyOverviewSchema
from service.company.company_service import CompanyService


class CompanyOverviewSearchService:
    _meilisearch_client: Optional[MeilisearchClient]
    _index_name: str

    _company_service: CompanyService

    def __init__(self, *, sql_engine: Optional[Engine] = None, meilisearch_client: Optional[MeilisearchClient] = None,
                 company_service: CompanyService,
                 meilisearch_index_name: str = "company"):
        self._sql_engine = sql_engine
        self._meilisearch_client = meilisearch_client

        self._company_service = company_service

        self._index_name = meilisearch_index_name

    def meilisearch_query(self, query: str) -> Optional[List[CompanyOverviewSchema]]:
        if self._meilisearch_client:
            return list(
                map(lambda document: CompanyOverviewSchema(**document),
                    self._meilisearch_client.search(self._index_name, query)))
        else:
            print("!MeilisearchClient")

            return None

    def sql_query(self, company_id_list: List[int]) -> Optional[List[CompanyOverviewSchema]]:
        return self._company_service.company_overview(company_id_list)


if __name__ == "__main__":
    db = Database()

    with db.create_session() as session:
        cs = CompanyService(session=session)
        co = CompanyOverviewSearchService(sql_engine=db.get_engine(), company_service=cs)

        print(co.sql_query([10, 20]))
