from database.database import Database
from seeder.meilisearch.meilisearch_seeder import MeilisearchSeeder
from service.company.company_service import CompanyService
from service.search.meilisearch.meilisearch_client import MeilisearchClient

if __name__ == '__main__':
    db = Database()

    mclient_ = MeilisearchClient()
    with db.create_session() as session:
        c_service = CompanyService(session)

        seeder = MeilisearchSeeder(mclient_, c_service)

        print(seeder.seed())
        print(len(mclient_.search("company", "retail")))
