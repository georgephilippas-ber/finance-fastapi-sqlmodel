from typing import List

from core.search.meilisearch.meilisearch_client import MeilisearchClient
from schema.company.company import CompanyOverviewSchema
from service.company.company_service import CompanyService


class CompanyOverviewSearchService:
    _meilisearch_client: MeilisearchClient
    _company_service: CompanyService

    _index_name: str

    def __init__(self, meilisearch_client: MeilisearchClient, company_service: CompanyService,
                 index_name: str = "company"):
        self._meilisearch_client = meilisearch_client
        self._company_service = company_service

        self._index_name = index_name

    def company_overview_query(self, query: str) -> List[CompanyOverviewSchema]:
        return list(
            map(lambda document: CompanyOverviewSchema(**document),
                self._meilisearch_client.search(self._index_name, query)))
