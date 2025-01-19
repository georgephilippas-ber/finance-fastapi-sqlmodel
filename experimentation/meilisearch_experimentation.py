import asyncio
from typing import List

from database.database import Database
from schema.company.company import CompanyOverviewSchema
from seeder.meilisearch.company_seeder import MeilisearchCompanySeeder
from service.company.company_service import CompanyService
from core.search.meilisearch.meilisearch_client import MeilisearchClient


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


if __name__ == '__main__':
    async def exec():
        db = Database()

        mclient_ = MeilisearchClient()
        with db.create_session() as session:
            c_service = CompanyService(session)

        coss = CompanyOverviewSearchService(mclient_, c_service)

        print(coss.company_overview_query("consumer"))


    asyncio.run(exec())
