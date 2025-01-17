from datetime import date, timedelta
from typing import List, Optional

def day_before(date_: date) -> date:
    return date_ - timedelta(days=1)


def beginning_of_month(date_: date) -> date:
    return date_.replace(day=1)

def closest_past_date_index(dates: List[date], target_date: date) -> Optional[int]:
    past_dates = [(i, d) for i, d in enumerate(dates) if d <= target_date]
    return max(past_dates, key=lambda x: x[1])[0] if past_dates else None