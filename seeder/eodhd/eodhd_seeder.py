from adapter.eodhd.exchange_adapter import ExchangeAdapter
from client.eodhd.eodhd_client import EODHDClient
from manager.country.country_manager import CountryManager
from manager.currency.currency_manager import CurrencyManager
from manager.exchange.exchange_manager import ExchangeManager


class EODHDSeeder:
    _eodhd_client: EODHDClient
    _eodhd_exchange_adapter: ExchangeAdapter
    _country_manager: CountryManager
    _currency_manager: CurrencyManager
    _exchange_manager: ExchangeManager

    _prefer_cached: bool = True

    def __init__(self, eodhd_client: EODHDClient, eodhd_exchange_adapter: ExchangeAdapter,
                 country_manager: CountryManager, currency_manager: CurrencyManager,
                 exchange_manager: ExchangeManager, *, prefer_cached: bool = True):
        self._eodhd_client = eodhd_client
        self._eodhd_exchange_adapter = eodhd_exchange_adapter
        self._country_manager = country_manager
        self._currency_manager = currency_manager
        self._exchange_manager = exchange_manager

        self._prefer_cached = prefer_cached

    async def seed_exchange(self):
        dict_list_ = await self._eodhd_client.exchanges_list()
        schema_list_ = self._eodhd_exchange_adapter.adapt_many(dict_list_)

        for exchange_schema_ in schema_list_:
            country_ = self._country_manager.by_cca2(exchange_schema_.country_iso2)
            currency_ = self._currency_manager.by_code(exchange_schema_.currency)

            if country_ is not None and currency_ is not None:
                exchange_model_ = self._exchange_manager.persist(exchange_schema_, {'country_id': country_.id,
                                                                                    'currency_id': currency_.id})
