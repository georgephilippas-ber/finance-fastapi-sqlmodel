from service.search.meilisearch.meilisearch_client import MeilisearchClient
from service.company.company_service import CompanyService


class MeilisearchSeeder:
    _meilisearch_client: MeilisearchClient
    _company_service: CompanyService

    _index_name: str

    def __init__(self, meilisearch_client: MeilisearchClient, company_service: CompanyService,
                 index_name: str = "company"):
        self._meilisearch_client = meilisearch_client
        self._company_service = company_service

        self._index_name = index_name

    def seed(self) -> bool:
        return self._meilisearch_client.seed_index(self._index_name,
                                                   [company_overview_.model_dump() for company_overview_ in
                                                    self._company_service.company_overview()],
                                                   primary_key='_'.join([self._index_name, "id"]))
