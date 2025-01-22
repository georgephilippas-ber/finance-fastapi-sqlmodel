from meilisearch import Client
from typing import List, Dict, Optional
from configuration.meilisearch import MEILISEARCH_MASTER_KEY, MEILISEARCH_SERVER_URL

import nltk


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

    @staticmethod
    def get_stopwords() -> List[str]:
        try:
            nltk.download('stopwords', quiet=True, raise_on_error=True)

            return nltk.corpus.stopwords.words('english')
        except Exception as e:
            print(e)

            return []

    def seed_index(self, index_name: str, documents: List[Dict], *, primary_key: str) -> bool:
        try:
            self._client.wait_for_task(self._client.delete_index(index_name).task_uid)
        except Exception as e:
            print(e)
            self._client.wait_for_task(
                self._client.create_index(index_name, {"stopWords": MeilisearchClient.get_stopwords()}).task_uid)

        index_ = self._client.index(index_name)

        try:
            self._client.wait_for_task(index_.add_documents(documents, primary_key=primary_key).task_uid)

            return True
        except Exception as e:
            print(e)
            return False

    def search(self, index_name: str, query_text: str) -> Optional[List[Dict]]:
        try:
            index_ = self._client.index(index_name)

            search_result_ = index_.search(query_text)

            return search_result_.get("hits")
        except Exception as e:
            print(e)

            return None

    def all(self, index_name: str) -> Optional[List[Dict]]:
        try:
            index_ = self._client.index(index_name)
            return [dict(f) for f in index_.get_documents().results]
        except Exception as e:
            print(e)

            return None


if __name__ == '__main__':
    nltk.download('stopwords')

    english_stopwords = nltk.corpus.stopwords.words('english')
    german_stopwords = nltk.corpus.stopwords.words('german')
    print(english_stopwords)
    print(german_stopwords)
