from typing import List, Optional

from sqlalchemy import Engine

from client.search.meilisearch.meilisearch_client import MeilisearchClient
from database.database import Database
from schema.company.company import CompanyOverviewSchema
from schema.company.company_search.company_search_sql import Criterion
from service.company.company_search_sql_service import CompanySearchSQLService
from service.company.company_service import CompanyService


class CompanyOverviewSearchService:
    _engine: Engine

    _meilisearch_client: Optional[MeilisearchClient]
    _index_name: str

    _company_search_sql_service: Optional[CompanySearchSQLService]

    _company_service: CompanyService

    def __init__(self, *, engine: Engine, meilisearch_client: Optional[MeilisearchClient] = None,
                 company_search_sql_service: Optional[CompanySearchSQLService],
                 company_service: CompanyService,
                 meilisearch_index_name: str = "company"):
        self._meilisearch_client = meilisearch_client
        self._index_name = meilisearch_index_name

        self._company_service = company_service
        self._company_search_sql_service = company_search_sql_service

        self._engine = engine

    def _meilisearch_search_with_criteria(self, query: str) -> Optional[List[int]]:
        if self._meilisearch_client:
            return list(
                map(lambda document: CompanyOverviewSchema(**document).company_id,
                    self._meilisearch_client.search(self._index_name, query)))
        else:
            print("!MeilisearchClient")

            return None

    def _sql_search_with_criteria(self, criteria: List[Criterion]) -> Optional[List[int]]:
        if self._company_search_sql_service:
            self._company_search_sql_service.get_company_ids(criteria)
        else:
            return None

    def _get_company_overview(self, company_id_list: List[int]) -> Optional[List[CompanyOverviewSchema]]:
        return self._company_service.company_overview(company_id_list)

    def search(self, query: str, criteria: List[Criterion]) -> Optional[List[CompanyOverviewSchema]]:
        meilisearch_query_results_: List[int] = self._meilisearch_search_with_criteria(query) or []
        sql_query_results_: List[int] = self._sql_search_with_criteria(criteria) or []

        return self._get_company_overview(
            [company_id for company_id in meilisearch_query_results_ if company_id in sql_query_results_])


if __name__ == "__main__":
    db = Database()

    with db.create_session() as session:
        cs = CompanyService(session=session)
        co = CompanyOverviewSearchService(engine=db.get_engine(), company_service=cs)

        print(co._get_company_overview([10, 20]))
