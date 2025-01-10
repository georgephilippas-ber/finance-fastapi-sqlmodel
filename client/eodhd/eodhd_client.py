import json
from http import HTTPStatus
from os import environ
from os.path import join
from typing import Optional, List
from urllib.parse import urljoin

import httpx

from abstract.client.client import Client
from configuration.configuration import EODHD_DEMO, project_root
from core.environment.environment import load_environment
from exception.exception import APISecurityException

load_environment()

API_TOKEN: Optional[str] = environ.get('API_TOKEN') if not EODHD_DEMO else 'demo'

if API_TOKEN is None:
    raise APISecurityException

BASE_URL: str = 'https://eodhd.com'


class EODHDClient(Client):
    _api_token: str

    def __init__(self, base_url: str = BASE_URL, api_token: str = API_TOKEN):
        super().__init__(base_url)

        self._api_token = api_token

    async def exchanges_list(self, prefer_cached: bool = True) -> Optional[List[str]]:
        url_ = urljoin(self._base_url, '/api/exchanges-list')
        cache_file_path_ = join(project_root(), "client", "cache", "eodhd", "exchanges", "exchanges.json")

        if prefer_cached:
            try:
                with open(cache_file_path_, 'r') as cache_file:
                    return json.load(cache_file)
            except FileNotFoundError:
                pass

        async with httpx.AsyncClient() as client:
            response_ = await client.get(url_, params={'api_token': self._api_token, 'fmt': 'json'})

            if response_.status_code == HTTPStatus.OK:
                with open(cache_file_path_, 'w') as cache_file:
                    json.dump(response_.json(), cache_file, indent=4)

                return response_.json()
            else:
                return None


if __name__ == '__main__':
    pass
