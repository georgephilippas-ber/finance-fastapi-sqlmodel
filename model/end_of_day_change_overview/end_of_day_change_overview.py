from typing import Optional
from datetime import date
from uuid import uuid4

from sqlalchemy import Column, Integer, Sequence
from sqlmodel import SQLModel, Field, Relationship

from model.ticker.ticker import Ticker


class EndOfDayChangeOverview(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(uuid4().hex), primary_key=True))

    latest_date: date = Field(nullable=False)
    latest: Optional[float] = Field(default=None)

    latest_adjusted: Optional[float] = Field(default=None)
    beginning_of_month_adjusted: Optional[float] = Field(default=None)
    beginning_of_year_adjusted: Optional[float] = Field(default=None)

    ticker_id: int = Field(foreign_key="ticker.id")
    ticker: Ticker = Relationship()

    def calculate_month_to_date_change(self) -> Optional[float]:
        if (self.beginning_of_month_adjusted is not None) and (self.latest_adjusted is not None):
            return self.latest_adjusted - self.beginning_of_month_adjusted
        else:
            return None

    def calculate_year_to_date_change(self) -> Optional[float]:
        if (self.beginning_of_year_adjusted is not None) and (self.latest_adjusted is not None):
            return self.latest_adjusted - self.beginning_of_year_adjusted
        else:
            return None
