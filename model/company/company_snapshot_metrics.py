from typing import Optional

from sqlalchemy import Column, Numeric
from sqlmodel import SQLModel, Field, Relationship

from decimal import Decimal
from datetime import date

from model.company.company import Company


class CompanySnapshotMetrics(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    market_capitalization: Decimal = Field(sa_column=Column(Numeric(26, 2)))
    enterprise_value: Decimal = Field(sa_column=Column(Numeric(26, 2)))

    return_on_assets: float = Field(nullable=False)

    operating_profit_margin: float = Field(nullable=False)
    net_profit_margin: float = Field(nullable=False)

    updated_at: date = Field(nullable=False)

    company_id: int = Field(foreign_key="company.id")
    company: Company = Relationship(back_populates="company_snapshot_metrics")
