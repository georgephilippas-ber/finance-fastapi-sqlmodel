from typing import Optional
from uuid import uuid4

from sqlalchemy import Column, Integer, Sequence
from sqlmodel import SQLModel, Field, Relationship

from model.country.country import Country
from model.currency.currency import Currency


class Exchange(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(uuid4().hex), primary_key=True))

    code: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)

    country_id: int = Field(foreign_key="country.id")
    country: Country = Relationship(back_populates="exchange_list")

    currency_id: int = Field(foreign_key="currency.id")
    currency: Currency = Relationship(back_populates="exchange_list")

    ticker_list: list["Ticker"] = Relationship(back_populates="exchange")
