from typing import List, Dict, Optional

from configuration.meilisearch import MEILISEARCH_MASTER_KEY, MEILISEARCH_SERVER_URL
from meilisearch import Client


class MeilisearchClient:
    _connection_url: str
    _master_key: str

    _client: Client

    def __init__(self, connection_url: str = MEILISEARCH_SERVER_URL, master_key: str = MEILISEARCH_MASTER_KEY):
        self._connection_url = connection_url
        self._master_key = master_key

        self._client = Client(connection_url, master_key)

    def get_client(self) -> Client:
        return self._client

    def seed_index(self, index_name: str, data: List[Dict]) -> bool:
        try:
            self._client.wait_for_task(self._client.create_index(index_name).task_uid)
        except Exception as e:
            pass

        index_ = self._client.index(index_name)

        try:
            self._client.wait_for_task(index_.add_documents(data).task_uid)

            return True
        except Exception as e:
            return False

    def search_with_highlight(self, index_name: str, field_name: str, query_text: str) -> Optional[List[Dict]]:
        try:
            index_ = self._client.index(index_name)

            search_result_ = index_.search(
                query_text,
                {
                    "attributesToHighlight": [field_name],
                    "highlightPreTag": "<mark>",
                    "highlightPostTag": "</mark>"
                }
            )

            return search_result_.get("hits")
        except Exception as e:
            print(e)

            return None
