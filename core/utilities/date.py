from datetime import date, timedelta


def day_before(date_: date) -> date:
    return date_ - timedelta(days=1)


def beginning_of_month(date_: date) -> date:
    return date_.replace(day=1)
