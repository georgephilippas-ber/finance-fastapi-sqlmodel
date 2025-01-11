from typing import Optional

from sqlmodel import SQLModel, Field


class Exchange(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    code: str = Field(index=True, nullable=False, unique=True)
    name: str = Field(nullable=False)
