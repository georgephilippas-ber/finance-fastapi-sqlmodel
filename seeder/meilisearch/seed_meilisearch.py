from client.search.meilisearch.meilisearch_client import MeilisearchClient
from database.database import Database
from seeder.meilisearch.company_seeder import MeilisearchCompanySeeder
from service.company.company_service import CompanyService

if __name__ == "__main__":
    database_ = Database()

    with database_.create_session() as session:
        company_service_ = CompanyService(session)
        meilisearch_client_ = MeilisearchClient()

        MeilisearchCompanySeeder(meilisearch_client_, company_service_).seed()
