from typing import Dict, List

from pydantic import BaseModel
from datetime import date

from dataclasses import dataclass

from abstract.adapter.adapter import Adapter


class TimeSeries(BaseModel):
    name: str
    series: Dict[date, float]


class TimeFrame(BaseModel):
    frame: Dict[date, List[TimeSeries]]


@dataclass
class EODHDFinancialTimeSeriesColumn:
    statement: str
    key: str
    name: str


TIME_SERIES_COLUMNS: List[EODHDFinancialTimeSeriesColumn] = [
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='totalAssets', name='assets'),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='totalLiabilities', name='liabilities'),
]


class TimeSeriesAdapter(Adapter):
    _columns: List[EODHDFinancialTimeSeriesColumn]

    def __init__(self, columns: List[EODHDFinancialTimeSeriesColumn]):
        super().__init__()

        self._columns = columns

    def adapt(self, json_: Dict) -> TimeFrame:
        pass

    def adapt_many(self, json_list_: List[Dict]) -> List[TimeFrame]:
        return [self.adapt(json_list_[0])]
