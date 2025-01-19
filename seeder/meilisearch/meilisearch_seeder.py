from core.meilisearch.meilisearch_client import MeilisearchClient
from service.company.company_service import CompanyService


class MeilisearchSeeder:
    _meilisearch_client: MeilisearchClient
    _company_service: CompanyService

    def __init__(self, meilisearch_client: MeilisearchClient, company_service: CompanyService):
        self._meilisearch_client = meilisearch_client
        self._company_service = company_service

    def seed(self):
        pass
