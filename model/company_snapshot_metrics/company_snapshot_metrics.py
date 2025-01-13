from typing import Optional
from sqlmodel import SQLModel, Field
from decimal import Decimal


class CompanySnapshotMetrics(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    market_capitalization: Decimal = Field(nullable=False)
    enterprise_value: Decimal = Field(nullable=False)
