import asyncio
from typing import Dict, List, Optional

from sqlmodel import Session

from adapter.restcountries.restcountries_adapter import RESTCountriesAdapter
from client.restcountries.restcountries_client import RESTCountriesClient
from database.database import Database
from manager.continent.continent_manager import ContinentManager
from manager.country.country_manager import CountryManager
from manager.currency.currency_manager import CurrencyManager


class RESTCountriesSeeder:
    _restcountries_client: RESTCountriesClient
    _restcountries_adapter: RESTCountriesAdapter

    _country_manager: CountryManager
    _currency_manager: CurrencyManager
    _continent_manager: ContinentManager

    _prefer_cached: bool

    def __init__(self, restcountries_client: RESTCountriesClient,
                 restcountries_adapter: RESTCountriesAdapter,
                 country_manager: CountryManager, currency_manager: CurrencyManager,
                 continent_manager: ContinentManager, *, prefer_cached: bool = True):

        self._restcountries_client = restcountries_client
        self._restcountries_adapter = restcountries_adapter

        self._country_manager = country_manager
        self._currency_manager = currency_manager
        self._continent_manager = continent_manager

        self._prefer_cached = prefer_cached

    async def seed(self):
        dict_list_: Optional[List[Dict]] = await self._restcountries_client.get_all()

        if dict_list_ is not None:
            schema_list_ = self._restcountries_adapter.adapt_many(dict_list_)

            for country_schema_, currency_schema_list_, continent_schema_list_ in schema_list_:
                country_model_ = self._country_manager.persist(country_schema_)

                currency_model_list_ = [self._currency_manager.persist(currency_schema_) for currency_schema_ in
                                        currency_schema_list_]

                country_model_.currency_list.extend(currency_model_list_)

                continent_model_list_ = [self._continent_manager.persist(continent_schema_) for continent_schema_
                                         in continent_schema_list_]

                country_model_.continent_list.extend(continent_model_list_)


if __name__ == '__main__':
    pass
