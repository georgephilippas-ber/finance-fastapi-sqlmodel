import asyncio

from core.search.meilisearch.meilisearch_client import MeilisearchClient
from database.database import Database
from service.company.company_overview_search_service import CompanyOverviewSearchService
from service.company.company_service import CompanyService

if __name__ == '__main__':
    async def exec():
        db = Database()

        mclient_ = MeilisearchClient()
        with db.create_session() as session:
            c_service = CompanyService(session)

        coss = CompanyOverviewSearchService(mclient_, c_service)

        print(coss.company_overview_query("consumer"))


    asyncio.run(exec())
