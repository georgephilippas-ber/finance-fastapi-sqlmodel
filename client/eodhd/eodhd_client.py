import asyncio
import json
from http import HTTPStatus
from os import environ
from os.path import join
from typing import Optional, List, Dict
from urllib.parse import urljoin
from datetime import date
from logging import warning

import httpx

from abstract.client.client import Client
from configuration.client.eodhd import EODHD_DEMO
from core.client.eodhd import to_eodhd_exchange_code
from core.environment.environment import load_environment
from core.utilities.date import day_before, beginning_of_month
from core.utilities.root import project_root

load_environment()

API_TOKEN: Optional[str] = environ.get('API_TOKEN') if not EODHD_DEMO else 'demo'

if API_TOKEN is None:
    warning("EODHD API security token is missing. The data being used may be cached or simulated.")

BASE_URL: str = 'https://eodhd.com'


class EODHDClient(Client):
    _api_token: str

    def __init__(self, base_url: str = BASE_URL, api_token: str = API_TOKEN):
        super().__init__(base_url)

        self._api_token = api_token

    async def exchanges_list(self, prefer_cached: bool = True) -> Optional[List[Dict]]:
        url_ = urljoin(self._base_url, '/api/exchanges-list')
        cache_file_path_ = join(project_root(), "client", "cache", "eodhd", "exchanges", "exchanges.json")

        if prefer_cached:
            try:
                with open(cache_file_path_, 'r') as cache_file:
                    return json.load(cache_file)
            except FileNotFoundError:
                pass

        if API_TOKEN is None:
            return None

        async with httpx.AsyncClient() as client:
            response_ = await client.get(url_, params={'api_token': self._api_token, 'fmt': 'json'})

            if response_.status_code == HTTPStatus.OK:
                with open(cache_file_path_, 'w') as cache_file:
                    json.dump(response_.json(), cache_file, indent=4)

                return response_.json()
            else:
                return None

    async def exchange_symbol_list(self, eodhd_exchange_code: str, *, prefer_cached: bool = True) -> Optional[
        List[Dict]]:
        url_ = urljoin(self._base_url, f'/api/exchange-symbol-list/{eodhd_exchange_code.upper()}')
        cache_file_path_ = join(project_root(), "client", "cache", "eodhd", "exchange_symbols",
                                f"{eodhd_exchange_code.upper()}.json")

        if prefer_cached:
            try:
                with open(cache_file_path_, 'r') as cache_file:
                    return json.load(cache_file)
            except FileNotFoundError:
                pass

        if API_TOKEN is None:
            return None

        async with httpx.AsyncClient() as client:
            response_ = await client.get(url_, params={'api_token': self._api_token, 'fmt': 'json'})

            if response_.status_code == HTTPStatus.OK:
                with open(cache_file_path_, 'w') as cache_file:
                    json.dump(response_.json(), cache_file, indent=4)

                return response_.json()
            else:
                return None

    async def exchange_symbol_list_many(self, eodhd_exchange_code_list: List[str], *, prefer_cached: bool = True) -> \
            Optional[
                List[Dict]]:
        list_ = []

        for exchange_code_ in eodhd_exchange_code_list:
            list_.extend(await self.exchange_symbol_list(exchange_code_, prefer_cached=prefer_cached))

        return list(filter(lambda element: element is not None, list_))

    async def _fundamentals(self, symbol: str, eodhd_exchange: str, *, prefer_cached: bool = True,
                            debug: bool = False) -> Optional[Dict]:
        if debug:
            print(symbol.upper(), eodhd_exchange.upper())

        url_ = urljoin(self._base_url, f'/api/fundamentals/{symbol.upper()}.{eodhd_exchange.upper()}')
        cache_file_path_ = join(project_root(), "client", "cache", "eodhd", "fundamentals",
                                f"{symbol.upper()}-{eodhd_exchange.upper()}.json")

        if prefer_cached:
            try:
                with open(cache_file_path_, 'r') as cache_file:
                    return json.load(cache_file)
            except FileNotFoundError:
                pass

        if API_TOKEN is None:
            return None

        async with httpx.AsyncClient() as client:
            response_ = await client.get(url_, params={'api_token': self._api_token, 'fmt': 'json'})

            if response_.status_code == HTTPStatus.OK:
                with open(cache_file_path_, 'w') as cache_file:
                    json.dump(response_.json(), cache_file, indent=4)

                return response_.json()
            else:
                return None

    async def fundamentals(self, symbol: str, exchange_code: str, *, prefer_cached: bool = True, debug: bool = False) -> \
            Optional[Dict]:
        return await self._fundamentals(symbol, to_eodhd_exchange_code(exchange_code), prefer_cached=prefer_cached,
                                        debug=debug)

    async def eod(self, symbol: str, exchange_code: str, date_: Optional[date] = None, *, prefer_cached: bool = True,
                  debug: bool = False) -> Optional[List[Dict]]:
        if date_ is None:
            date_ = date.today()

        url_ = urljoin(self._base_url, f'/api/eod/{symbol.upper()}.{to_eodhd_exchange_code(exchange_code.upper())}')
        cache_file_path_ = join(project_root(), "client", "cache", "eodhd", "end-of-day",
                                f"{symbol.upper()}-{exchange_code.upper()}_{date.today()}.json")

        if prefer_cached:
            try:
                with open(cache_file_path_, 'r') as cache_file:
                    return json.load(cache_file)
            except FileNotFoundError:
                pass

        if API_TOKEN is None:
            return None

        async with httpx.AsyncClient() as client:
            yesterday_ = day_before(date_)
            beginning_of_month_ = beginning_of_month(yesterday_)

            response_ = await client.get(url_,
                                         params={'api_token': self._api_token, 'fmt': 'json', 'period': 'd',
                                                 'from': beginning_of_month_.isoformat(), 'to': yesterday_.isoformat()})

            if debug:
                print(response_.status_code)

            if response_.status_code == HTTPStatus.OK:
                with open(cache_file_path_, 'w') as cache_file:
                    json.dump(response_.json(), cache_file, indent=4)

                return response_.json()
            else:
                return None


if __name__ == '__main__':
    pass
