from typing import Optional
from sqlmodel import SQLModel, Field

from decimal import Decimal
from datetime import date


class CompanySnapshotMetrics(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    market_capitalization: Decimal = Field(nullable=False)
    enterprise_value: Decimal = Field(nullable=False)

    return_on_assets: float = Field(nullable=False)

    operating_profit_margin: float = Field(nullable=False)
    net_profit_margin: float = Field(nullable=False)

    updated_at: date = Field(nullable=False)
