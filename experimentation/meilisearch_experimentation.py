from service.search.meilisearch.meilisearch_client import MeilisearchClient
from seeder.meilisearch.meilisearch_seeder import MeilisearchSeeder
from database.database import Database
from service.company.company_service import CompanyService

from time import sleep

if __name__ == '__main__':
    db = Database()

    mclient_ = MeilisearchClient()
    with db.create_session() as session:
        c_service = CompanyService(session)

        seeder = MeilisearchSeeder(mclient_, c_service)

        print(seeder.seed())

        print(mclient_.all("company"))
        print(mclient_.search("company", "Woodward"))
