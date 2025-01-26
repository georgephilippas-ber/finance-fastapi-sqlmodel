from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Optional

from sqlalchemy import Column, Numeric, Integer, Sequence
from sqlmodel import SQLModel, Field, Relationship

from model.company.company import Company


class CompanySnapshotMetrics(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(Path(__file__).stem), primary_key=True))

    market_capitalization: Decimal = Field(sa_column=Column(Numeric(26, 2)))
    enterprise_value: Decimal = Field(sa_column=Column(Numeric(26, 2)))

    return_on_assets: float = Field(nullable=False)

    operating_profit_margin: float = Field(nullable=False)
    net_profit_margin: float = Field(nullable=False)

    price_earnings_ratio: Optional[float] = Field(nullable=True, default=None)
    book_price_per_share: float = Field(nullable=False)

    revenue: Decimal = Field(sa_column=Column(Numeric(26, 2)))
    gross_profit: Decimal = Field(sa_column=Column(Numeric(26, 2)))

    diluted_eps: Optional[float] = Field(nullable=True, default=None)

    price_to_book_ratio: float = Field(nullable=False)

    shares_outstanding: Decimal = Field(sa_column=Column(Numeric(26, 2)))
    shares_float: Decimal = Field(sa_column=Column(Numeric(26, 2)))

    beta: Optional[float] = Field(nullable=True, default=None)

    fifty_two_week_high: float
    fifty_two_week_low: float

    return_on_invested_capital: Optional[float] = Field(nullable=True, default=None)
    free_cash_flow_return_on_invested_capital: Optional[float] = Field(nullable=True, default=None)
    debt_to_equity_ratio: Optional[float] = Field(nullable=True, default=None)

    updated_at: date = Field(nullable=False)

    company_id: int = Field(foreign_key="company.id")
    company: Company = Relationship(back_populates="company_snapshot_metrics")
