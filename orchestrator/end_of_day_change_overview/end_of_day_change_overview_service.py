from client.eodhd.eodhd_client import EODHDClient
from manager.end_of_day_change_overview.end_of_day_change_overview_manager import EndOfDayChangeOverviewManager


class EndOfDayChangeOverviewOrchestrator:
    _eodhd_client: EODHDClient
    _end_of_day_change_overview_manager: EndOfDayChangeOverviewManager

    def __init__(self, eodhd_client: EODHDClient, end_of_day_change_overview_manager: EndOfDayChangeOverviewManager):
        self._eodhd_client = eodhd_client
        self._end_of_day_change_overview_manager = end_of_day_change_overview_manager

