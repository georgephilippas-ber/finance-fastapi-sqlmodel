from typing import Optional

from adapter.eodhd.end_of_day_change_overview_adapter import EndOfDayChangeOverviewAdapter
from client.eodhd.eodhd_client import EODHDClient
from manager.end_of_day_change_overview.end_of_day_change_overview_manager import EndOfDayChangeOverviewManager
from manager.exchange.exchange_manager import ExchangeManager
from manager.ticker.ticker_manager import TickerManager

from datetime import date

from model.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverview
from model.exchange.exchange import Exchange
from model.ticker.ticker import Ticker


class EndOfDayChangeOverviewOrchestrator:
    _eodhd_client: EODHDClient
    _end_of_day_change_overview_adapter: EndOfDayChangeOverviewAdapter
    _end_of_day_change_overview_manager: EndOfDayChangeOverviewManager
    _ticker_manager: TickerManager
    _exchange_manager: ExchangeManager

    def __init__(self, eodhd_client: EODHDClient,
                 eodhd_end_of_day_change_overview_adapter: EndOfDayChangeOverviewAdapter,
                 end_of_day_change_overview_manager: EndOfDayChangeOverviewManager,
                 ticker_manager: TickerManager, exchange_manager: ExchangeManager):
        self._eodhd_client = eodhd_client
        self._end_of_day_change_overview_adapter = eodhd_end_of_day_change_overview_adapter
        self._end_of_day_change_overview_manager = end_of_day_change_overview_manager
        self._ticker_manager = ticker_manager
        self._exchange_manager = exchange_manager

    async def by_ticker_id(self, ticker_id: int, date_: Optional[date] = None, retries_left: int = 5) -> Optional[
        EndOfDayChangeOverview]:
        if date_ is None:
            date_ = date.today()

        if retries_left <= 0:
            return None

        existing_optional_ = self._end_of_day_change_overview_manager.by_ticker_id_and_date(ticker_id, date_)

        if existing_optional_ is not None:
            return existing_optional_
        else:
            ticker_: Optional[Ticker] = self._ticker_manager.by_id(ticker_id)

            if ticker_ is not None:
                exchange_: Optional[Exchange] = self._exchange_manager.by_id(ticker_.exchange_id)

                if exchange_ is not None:
                    list_ = await self._eodhd_client.eod(ticker_.code, exchange_.code, date_)

                    if list_ is not None:
                        adapted_ = self._end_of_day_change_overview_adapter.adapt(list_)

                        self._end_of_day_change_overview_manager.persist(adapted_, {'ticker_id': ticker_id})
                    else:
                        pass

                    return await self.by_ticker_id(ticker_id, date_, retries_left=retries_left - 1)
                else:
                    return None
            else:
                return None
