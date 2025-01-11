from typing import Optional

from sqlmodel import SQLModel, Field


class Currency(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    name: str = Field(nullable=False, unique=True)
    code: str = Field(index=True, nullable=False, unique=True)
    symbol: str = Field(nullable=False)
