from typing import List, Optional

from sqlalchemy import Engine, text
from sqlmodel import Session

from core.search.meilisearch.meilisearch_client import MeilisearchClient
from schema.company.company import CompanyOverviewSchema


class CompanyOverviewSearchService:
    _meilisearch_client: Optional[MeilisearchClient]
    _sql_engine: Optional[Engine]

    _index_name: str

    def __init__(self, *, sql_engine: Optional[Engine] = None, meilisearch_client: Optional[MeilisearchClient] = None,
                 meilisearch_index_name: str = "company"):
        self._sql_engine = sql_engine
        self._meilisearch_client = meilisearch_client

        self._index_name = meilisearch_index_name

    def company_overview_meilisearch_query(self, query: str) -> Optional[List[CompanyOverviewSchema]]:
        if self._meilisearch_client:
            return list(
                map(lambda document: CompanyOverviewSchema(**document),
                    self._meilisearch_client.search(self._index_name, query)))
        else:
            print("!MeilisearchClient")

            return None

    def sql_query_by_company_id(self, company_id_list: List[int]):
        if self._sql_engine:
            with self._sql_engine.connect() as connection_:
                connection_.execute(
                    text("select * from company where id in :company_id_list", {"company_id_list": company_id_list}),
                    {}).all()
        else:
            print("!Engine")

            return None


if __name__ == "__main__":
    pass
