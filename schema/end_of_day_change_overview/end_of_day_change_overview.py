from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class EndOfDayChangeOverviewSchema(BaseModel):
    latest: Optional[float] = Field(default=None)
    latest_date: Optional[date] = Field(default=None)

    latest_adjusted: Optional[float] = Field(default=None)
    beginning_of_month_adjusted: Optional[float] = Field(default=None)
    beginning_of_year_adjusted: Optional[float] = Field(default=None)
