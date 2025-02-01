from typing import List

from manager.time_series.fundamental_time_series_manager import FundamentalTimeSeriesManager
from model.time_series.fundamental_time_series import FundamentalTimeSeries


class FundamentalTimeSeriesService:
    _fundamental_time_series_manager: FundamentalTimeSeriesManager

    def __init__(self, fundamental_time_series_manager: FundamentalTimeSeriesManager):
        self._fundamental_time_series_manager = fundamental_time_series_manager

    def fundamental_time_series(self, company_id: int) -> List[FundamentalTimeSeries]:
        return self._fundamental_time_series_manager.by_company_id(company_id)
