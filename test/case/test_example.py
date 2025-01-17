import asyncio

import model.comprehensive

from adapter.eodhd.end_of_day_change_overview_adapter import EndOfDayChangeOverviewAdapter
from client.eodhd.eodhd_client import EODHDClient
from database.database import Database
from manager.end_of_day_change_overview.end_of_day_change_overview_manager import EndOfDayChangeOverviewManager
from manager.exchange.exchange_manager import ExchangeManager
from manager.ticker.ticker_manager import TickerManager
from orchestrator.end_of_day_change_overview.end_of_day_change_overview_orchestrator import \
    EndOfDayChangeOverviewOrchestrator

import pytest


@pytest.mark.asyncio
async def test_case():
    database_ = Database()

    database_.create_tables(drop_all=False)

    with database_.create_session() as session:
        client = EODHDClient()
        adapter = EndOfDayChangeOverviewAdapter()

        overview_manager_ = EndOfDayChangeOverviewManager(session)
        exchange_manager = ExchangeManager(session)
        ticker_manager = TickerManager(session, exchange_manager)

        orchestrator_ = EndOfDayChangeOverviewOrchestrator(
            client,
            adapter,
            overview_manager_,
            ticker_manager,
            exchange_manager
        )

        assert await orchestrator_.by_ticker_id(1) is not None


if __name__ == '__main__':
    asyncio.run(test_case())
