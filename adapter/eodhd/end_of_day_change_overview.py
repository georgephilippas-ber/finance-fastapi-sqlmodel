from abstract.adapter.adapter import Adapter
from typing import List, Dict, Optional
from datetime import date, timedelta

from core.utilities.date import closest_past_date_index, beginning_of_month
from schema.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverviewSchema


class EndOfDayChangeOverview(Adapter):
    def __init__(self, ):
        super().__init__()

    def adapt(self, json_: List[Dict], date_: Optional[date] = None) -> Optional[EndOfDayChangeOverviewSchema]:
        if date_ is None:
            date_ = date.today()

        yesterday_ = date_ - timedelta(days=1)
        try:
            earliest_ = json_[0]
            latest_ = json_[-1]
            beginning_of_month_ = json_[
                closest_past_date_index(list(map(lambda entry: date.fromisoformat(entry['date']), json_)),
                                        beginning_of_month(yesterday_))]

            return EndOfDayChangeOverviewSchema(
                latest_date=date.fromisoformat(latest_['date']),
                latest=latest_['close'],
                latest_adjusted=latest_['adjusted_close'],
                beginning_of_month_adjusted=beginning_of_month_['adjusted_close'],
                beginning_of_year_adjusted=earliest_['adjusted_close']
            )
        except (KeyError, IndexError) as e:
            print(e)

            return None

    def adapt_many(self, json_list_: List[List[Dict]], date_: Optional[date] = None) -> List[
        EndOfDayChangeOverviewSchema]:

        return list(filter(lambda value: value is not None, [self.adapt(json_, date_) for json_ in json_list_]))
