from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from model.country.country import Country


class Exchange(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    code: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)

    country_id: int = Field(foreign_key="country.id")
    country: Country = Relationship(back_populates="exchange_list")
