from decimal import Decimal
from pathlib import Path
from typing import Optional

from sqlalchemy import Numeric
from sqlmodel import SQLModel, Field, Column, Sequence, Integer, Relationship

from model.company.company import Company


class FundamentalTimeSeries(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(Path(__file__).stem), primary_key=True))

    assets: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    liabilities: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    cash: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    net_debt: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    net_working_capital: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    capital_expenditure: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    net_invested_capital: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    free_cash_flow: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    net_income: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))

    equity: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    return_on_equity: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    free_cash_flow_return_on_assets: Optional[Decimal] = Field(
        sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))
    debt_to_equity_ratio: Optional[Decimal] = Field(sa_column=Column(nullable=True, default=None, type_=Numeric(26, 2)))

    company_id: int = Field(foreign_key="company.id")
    company: Company = Relationship(back_populates="fundamental_time_series")
