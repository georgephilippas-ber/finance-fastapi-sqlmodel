from typing import Dict, List, Set, Optional

from datetime import date

from dataclasses import dataclass

from abstract.adapter.adapter import Adapter
from core.utilities.quickjson import read
from core.utilities.root import project_root
from schema.time_frame.time_frame import TimeFrame

from decimal import Decimal


@dataclass
class EODHDFinancialTimeSeriesColumn:
    scale: int
    statement: str
    key: str
    column_name: str


TIME_SERIES_COLUMNS: List[EODHDFinancialTimeSeriesColumn] = [
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='totalAssets', column_name='assets', scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='totalLiab', column_name='liabilities',
                                   scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='cash', column_name='cash', scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='netDebt', column_name='net_debt', scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='netWorkingCapital',
                                   column_name='net_working_capital', scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Cash_Flow', key='capitalExpenditures', column_name='capital_expenditure',
                                   scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Balance_Sheet', key='netInvestedCapital',
                                   column_name='net_invested_capital', scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Cash_Flow', key='freeCashFlow', column_name='free_cash_flow',
                                   scale=int(1.e6)),
    EODHDFinancialTimeSeriesColumn(statement='Income_Statement', key='netIncome', column_name='net_income',
                                   scale=int(1.e6)),
]


class TimeSeriesAdapter(Adapter):
    _columns: List[EODHDFinancialTimeSeriesColumn]

    def __init__(self, columns: List[EODHDFinancialTimeSeriesColumn]):
        super().__init__()

        self._columns = columns

    def adapt(self, json_: Dict) -> Optional[TimeFrame]:
        dates_in_columns_: List[List[str]] = []
        for column_ in self._columns:
            dates_in_columns_.append(
                [date_key_ for date_key_ in json_["Financials"][column_.statement]["yearly"].keys()])

        if dates_in_columns_:
            date_key_set_: Set[str] = set(dates_in_columns_[0])

            for list_ in dates_in_columns_[1:]:
                date_key_set_ = date_key_set_.intersection(set(list_))
        else:
            date_key_set_ = set()

        timeframe_: TimeFrame = TimeFrame(frame={})

        frame_: Dict[date, List[Decimal]] = {}
        for date_key_ in date_key_set_:
            values_ = []
            for column_ in self._columns:
                try:
                    value_candidate_ = Decimal(json_["Financials"][column_.statement]["yearly"][date_key_][column_.key])
                except Exception as e:
                    value_candidate_ = None

                if value_candidate_ is not None:
                    values_.append(value_candidate_ / column_.scale)
                else:
                    values_.append(None)

            frame_[date.fromisoformat(date_key_)] = values_

        timeframe_.column_names = [column_.column_name for column_ in self._columns]
        timeframe_.frame = frame_

        return timeframe_

    def postprocess(self, time_frame: TimeFrame) -> TimeFrame:
        pass

    def adapt_many(self, json_list_: List[Dict]) -> List[TimeFrame]:
        return [self.adapt(json_list_[0])]


if __name__ == '__main__':
    a = read([project_root(), "client", "cache", "eodhd", "fundamentals", "MSFT-US.json"])

    ad = TimeSeriesAdapter(TIME_SERIES_COLUMNS)

    f = ad.adapt(a)

    f.calculate("equity", ("assets", "liabilities"), lambda x, y: x - y)
    f.calculate("return_on_equity", ("net_income", "equity"), lambda x, y: x / y)
    f.calculate("free_cash_flow_return_on_investment", ("free_cash_flow", "assets"), lambda x, y: x / y)

    print(f.get_column("free_cash_flow_return_on_investment"))
    print(f.get_column("return_on_equity"))

    print(len(f))
