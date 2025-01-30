from typing import Dict, List, Set, Optional

from pydantic import BaseModel, Field
from datetime import date

from dataclasses import dataclass

from abstract.adapter.adapter import Adapter
from core.utilities.quickjson import read
from core.utilities.root import project_root


class TimeFrame(BaseModel):
    column_names: List[str] = Field(default_factory=list)
    frame: Dict[date, List[float]] = Field(default_factory=dict)


@dataclass
class EODHDFinancialTimeSeriesColumn:
    statement: str
    key: str
    name: str


TIME_SERIES_COLUMNS: List[EODHDFinancialTimeSeriesColumn] = [
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='totalAssets', name='assets'),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='totalLiab', name='liabilities'),
]


class TimeSeriesAdapter(Adapter):
    _columns: List[EODHDFinancialTimeSeriesColumn]

    def __init__(self, columns: List[EODHDFinancialTimeSeriesColumn]):
        super().__init__()

        self._columns = columns

    def adapt(self, json_: Dict) -> Optional[TimeFrame]:
        date_key_set_: Set[date] = set()

        for column_ in self._columns:
            for date_key_ in json_["Financials"][column_.statement]["yearly"].keys():
                date_key_set_.add(date.fromisoformat(date_key_))

        timeframe_: TimeFrame = TimeFrame(frame={})

        frame_: Dict[date, List[float]] = {}
        for date_key_ in date_key_set_:
            values_ = [json_["Financials"][column_.statement]["yearly"][date_key_.isoformat()][column_.key] for column_
                       in
                       self._columns]

            frame_[date_key_] = values_

        timeframe_.column_names = [column_.name for column_ in self._columns]
        timeframe_.frame = frame_

        return timeframe_

    def adapt_many(self, json_list_: List[Dict]) -> List[TimeFrame]:
        return [self.adapt(json_list_[0])]


if __name__ == '__main__':
    a = read([project_root(), "client", "cache", "eodhd", "fundamentals", "MSFT-US.json"])

    ad = TimeSeriesAdapter(TIME_SERIES_COLUMNS)

    print(ad.adapt(a))
