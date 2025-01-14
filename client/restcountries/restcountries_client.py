import asyncio
import json
from http import HTTPStatus
from os.path import join
from urllib.parse import urljoin

import httpx

from abstract.client.client import Client
from typing import List, Dict, Optional

from core.utilities.root import project_root

BASE_URL: str = 'https://restcountries.com'

FIELDS: List[str] = ['name', 'cca2', 'cca3', 'currencies', 'capital', 'latlng', 'area' 'maps', 'population',
                     'continents', 'flags']


class RESTCountriesClient(Client):
    def __init__(self, base_url: str = BASE_URL):
        super().__init__(base_url)

    async def get_all(self, prefer_cached: bool = True) -> Optional[List[Dict]]:
        url_ = urljoin(self._base_url, '/v3.1/all')

        cache_file_path_ = join(project_root(), "client", "cache", "restcountries", "all", "all.json")

        if prefer_cached:
            try:
                with open(cache_file_path_, 'r') as cache_file:
                    return json.load(cache_file)
            except FileNotFoundError:
                pass

        async with httpx.AsyncClient() as client:
            response_ = await client.get(url_, params={'fields': ','.join(FIELDS)})

            if response_.status_code == HTTPStatus.OK:
                with open(cache_file_path_, 'w') as cache_file:
                    json.dump(response_.json(), cache_file, indent=4)

                return response_.json()
            else:
                return None


if __name__ == '__main__':
    asyncio.run(RESTCountriesClient().get_all())
