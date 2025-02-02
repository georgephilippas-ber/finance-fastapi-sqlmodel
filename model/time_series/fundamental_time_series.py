from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Optional

from sqlalchemy import Numeric, UniqueConstraint
from sqlmodel import SQLModel, Field, Column, Sequence, Integer, Relationship

from model.company.company import Company


class FundamentalTimeSeries(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(Path(__file__).stem), primary_key=True, default=None))

    record_date: date = Field(nullable=False)

    # EXTRACTED
    assets: Optional[float] = Field(nullable=True, default=None)
    liabilities: Optional[float] = Field(nullable=True, default=None)
    cash: Optional[float] = Field(nullable=True, default=None)
    net_debt: Optional[float] = Field(nullable=True, default=None)
    net_working_capital: Optional[float] = Field(nullable=True, default=None)
    capital_expenditure: Optional[float] = Field(nullable=True, default=None)
    net_invested_capital: Optional[float] = Field(nullable=True, default=None)
    free_cash_flow: Optional[float] = Field(nullable=True, default=None)
    net_income: Optional[float] = Field(nullable=True, default=None)

    # COMPUTED
    equity: Optional[float] = Field(nullable=True, default=None)
    return_on_equity: Optional[float] = Field(nullable=True, default=None)
    free_cash_flow_return_on_assets: Optional[float] =Field(nullable=True, default=None)
    debt_to_equity_ratio: Optional[float] = Field(nullable=True, default=None)

    company_id: int = Field(foreign_key="company.id")
    company: Company = Relationship(back_populates="fundamental_time_series")

    __table_args__ = (
        UniqueConstraint("record_date", "company_id"),
    )
