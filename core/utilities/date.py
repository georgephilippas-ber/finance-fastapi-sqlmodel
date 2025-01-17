from datetime import date, timedelta
from typing import List, Optional


def day_before(date_: date) -> date:
    return date_ - timedelta(days=1)


def beginning_of_month(date_: date) -> date:
    return date_.replace(day=1)


def closest_past_date_index(date_list: List[date], date_: date) -> Optional[int]:
    before_date_ = [(i, d) for i, d in enumerate(date_list) if d <= date_]

    return max(before_date_, key=lambda x: x[1])[0] if before_date_ else 0
