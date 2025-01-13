from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from model.link.currency_country.currency_country import CurrencyCountry


class Currency(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    name: str = Field(nullable=False, unique=True)
    code: str = Field(index=True, nullable=False, unique=True)
    symbol: str = Field(nullable=False)

    country_list: List["Country"] = Relationship(back_populates="currency_list", link_model=CurrencyCountry)

    exchange_list: List["Exchange"] = Relationship(back_populates="currency")
    ticker_list: list["Ticker"] = Relationship(back_populates="currency")

    company_list: list["Company"] = Relationship(back_populates="currency")
