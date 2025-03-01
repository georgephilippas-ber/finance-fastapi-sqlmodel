from typing import List, Optional

from sqlalchemy import Engine

from client.meilisearch.meilisearch_client import MeilisearchClient
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

    def _meilisearch_search_with_criteria(self, query: Optional[str]) -> Optional[List[int]]:
        if self._meilisearch_client and query is not None:
            return list(
                map(lambda document: CompanyOverviewSchema(**document).company_id,
                    self._meilisearch_client.search(self._index_name, query) or []))
        else:
            if self._meilisearch_client is None:
                print("!MeilisearchClient")

            return None

    def _sql_search_with_criteria(self, criteria: Optional[List[Criterion]]) -> Optional[List[int]]:
        if self._company_search_sql_service is not None and criteria is not None:
            return self._company_search_sql_service.get_company_ids(criteria)
        else:
            return None

    def _get_company_overview(self, company_id_list: List[int]) -> Optional[List[CompanyOverviewSchema]]:
        return self._company_service.company_overview(company_id_list)

    def search(self, *, query: Optional[str] = None, criteria: Optional[List[Criterion]] = None) -> Optional[
        List[CompanyOverviewSchema]]:
        meilisearch_query_results_: Optional[List[int]] = self._meilisearch_search_with_criteria(
            query) if query else None
        sql_query_results_: Optional[List[int]] = self._sql_search_with_criteria(
            criteria) if criteria is not None else None

        if meilisearch_query_results_ is None:
            return_ = sql_query_results_ or []
        elif sql_query_results_ is None:
            return_ = meilisearch_query_results_ or []
        else:
            return_ = [company_id for company_id in meilisearch_query_results_ if company_id in sql_query_results_]

        return self._get_company_overview(return_)


if __name__ == "__main__":
    pass
