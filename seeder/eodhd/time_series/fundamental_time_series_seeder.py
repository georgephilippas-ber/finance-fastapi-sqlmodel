from adapter.eodhd.fundamental_time_series_adapter import FundamentalTimeSeriesAdapter
from client.eodhd.eodhd_client import EODHDClient
from manager.company.company_manager import CompanyManager
from manager.ticker.ticker_manager import TickerManager
from manager.time_series.fundamental_time_series_manager import FundamentalTimeSeriesManager


class FundamentalTimeSeriesSeeder:
    _company_manager: CompanyManager
    _fundamental_time_series_manager: FundamentalTimeSeriesManager
    _eodhd_client: EODHDClient
    _eodhd_fundamental_time_series_adapter: FundamentalTimeSeriesAdapter

    def __init__(self,
                 company_manager: CompanyManager,
                 fundamental_time_series_manager: FundamentalTimeSeriesManager,
                 eodhd_client: EODHDClient,
                 eodhd_fundamental_time_series_adapter: FundamentalTimeSeriesAdapter):
        self._company_manager = company_manager
        self._fundamental_time_series_manager = fundamental_time_series_manager
        self._eodhd_client = eodhd_client
        self._eodhd_fundamental_time_series_adapter = eodhd_fundamental_time_series_adapter

    async def seed(self):
        for company_ in self._company_manager.all():
            ticker_code_, exchange_code_ = company_.ticker.code, company_.ticker.exchange.code

            dict_ = await self._eodhd_client.fundamentals(ticker_code_, exchange_code_, debug=False)
            schema_ = self._eodhd_fundamental_time_series_adapter.adapt(dict_)
            self._fundamental_time_series_manager.persist(schema_, {'company_id': company_.id})

