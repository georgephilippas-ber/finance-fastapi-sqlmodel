from sqlmodel import Session

from adapter.eodhd.company_adapter import CompanyAdapter
from adapter.eodhd.exchange_adapter import ExchangeAdapter
from adapter.eodhd.ticker_adapter import TickerAdapter
from client.eodhd.eodhd_client import EODHDClient
from configuration.configuration import COMPANY_SAMPLE_SIZE
from configuration.eodhd.eodhd import EODHD_EXCHANGES
from manager.GICS.GICS_manager import GICSSectorManager, GICSIndustryGroupManager, GICSIndustryManager, \
    GICSSubIndustryManager
from manager.company.company_manager import CompanyManager
from manager.country.country_manager import CountryManager
from manager.currency.currency_manager import CurrencyManager
from manager.exchange.exchange_manager import ExchangeManager
from manager.ticker.ticker_manager import TickerManager


class EODHDSeeder:
    _eodhd_client: EODHDClient

    _eodhd_exchange_adapter: ExchangeAdapter
    _eodhd_ticker_adapter: TickerAdapter
    _eodhd_company_adapter: CompanyAdapter

    _country_manager: CountryManager
    _currency_manager: CurrencyManager
    _exchange_manager: ExchangeManager
    _ticker_manager: TickerManager
    _company_manager: CompanyManager

    _gics_sector_manager: GICSSectorManager
    _gics_industry_group_manager: GICSIndustryGroupManager
    _gics_industry_manager: GICSIndustryManager
    _gics_sub_industry_manager: GICSSubIndustryManager

    _session: Session
    _prefer_cached: bool = True

    def __init__(self, eodhd_client: EODHDClient, eodhd_exchange_adapter: ExchangeAdapter,
                 eodhd_ticker_adapter: TickerAdapter, eodhd_company_adapter: CompanyAdapter,
                 country_manager: CountryManager, currency_manager: CurrencyManager,
                 exchange_manager: ExchangeManager, ticker_manager: TickerManager, company_manager: CompanyManager,
                 gics_sector_manager: GICSSectorManager, gics_industry_group_manager: GICSIndustryGroupManager,
                 gics_industry_manager: GICSIndustryManager, gics_sub_industry_manager: GICSSubIndustryManager, *,
                 session: Session,
                 prefer_cached: bool = True):
        self._eodhd_client = eodhd_client

        self._eodhd_exchange_adapter = eodhd_exchange_adapter
        self._eodhd_ticker_adapter = eodhd_ticker_adapter
        self._eodhd_company_adapter = eodhd_company_adapter

        self._country_manager = country_manager
        self._currency_manager = currency_manager
        self._exchange_manager = exchange_manager
        self._ticker_manager = ticker_manager
        self._company_manager = company_manager

        self._gics_sector_manager = gics_sector_manager
        self._gics_industry_group_manager = gics_industry_group_manager
        self._gics_industry_manager = gics_industry_manager
        self._gics_sub_industry_manager = gics_sub_industry_manager

        self._session = session
        self._prefer_cached = prefer_cached

    async def seed_exchange(self):
        print("SEEDING - Exchange", end='')

        dict_list_ = await self._eodhd_client.exchanges_list()
        schema_list_ = self._eodhd_exchange_adapter.adapt_many(dict_list_)

        for exchange_schema_ in schema_list_:
            country_ = self._country_manager.by_cca2(exchange_schema_.country_iso2)
            currency_ = self._currency_manager.by_code(exchange_schema_.currency)

            if country_ is not None and currency_ is not None:
                exchange_model_ = self._exchange_manager.persist(exchange_schema_, {'country_id': country_.id,
                                                                                    'currency_id': currency_.id})
        self._session.commit()
        print(' - Done')

    async def seed_ticker(self):
        print("SEEDING - Ticker", end='')

        dict_list_ = await self._eodhd_client.exchange_symbol_list_many(EODHD_EXCHANGES)
        schema_list_ = self._eodhd_ticker_adapter.adapt_many(dict_list_)

        for ticker_schema_, exchange_schema_, currency_schema_ in schema_list_:
            exchange_ = self._exchange_manager.by_code(exchange_schema_.code)
            currency_ = self._currency_manager.by_code(currency_schema_.code)

            self._ticker_manager.persist(ticker_schema_, {'exchange_id': exchange_.id, 'currency_id': currency_.id})
        self._session.commit()
        print(' - Done')

    async def seed_company(self):
        print("SEEDING - Company", end='')

        for symbol_, exchange_code_, ticker_id_ in self._ticker_manager.all(COMPANY_SAMPLE_SIZE):
            dict_ = await self._eodhd_client.fundamentals(symbol_, exchange_code_, debug=False)
            company_and_gics_schema_ = self._eodhd_company_adapter.adapt(dict_)

            if company_and_gics_schema_ is not None:
                sector_ = self._gics_sector_manager.by_name(company_and_gics_schema_[1].sector)
                industry_group_ = self._gics_industry_group_manager.by_name(company_and_gics_schema_[1].industry_group)
                industry_ = self._gics_industry_manager.by_name(company_and_gics_schema_[1].industry)
                sub_industry_ = self._gics_sub_industry_manager.by_name(company_and_gics_schema_[1].sub_industry)

                self._company_manager.persist(company_and_gics_schema_[0],
                                              {'gics_sector_id': sector_.id, 'ticker_id': ticker_id_,
                                               'gics_industry_group_id': industry_group_.id,
                                               'gics_industry_id': industry_.id,
                                               'gics_subindustry_id': sub_industry_.id})
        self._session.commit()
        print(' - Done')
