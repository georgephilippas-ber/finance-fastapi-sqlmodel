from client.meilisearch.meilisearch_client import MeilisearchClient
from database.database import Database
from seeder.meilisearch.company_seeder import MeilisearchCompanySeeder
from service.company.company_service import CompanyService
from sqlmodel import Session

import asyncio


async def seed_meilisearch(session: Session):
    with session:
        company_service_ = CompanyService(session)
        meilisearch_client_ = MeilisearchClient()

        await MeilisearchCompanySeeder(meilisearch_client_, company_service_).seed()


if __name__ == "__main__":
    async def execute_async():
        database_ = Database()

        session_ = database_.create_session()

        asyncio.run(seed_meilisearch(session_))
