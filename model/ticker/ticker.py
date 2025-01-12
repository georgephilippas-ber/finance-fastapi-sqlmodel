from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from model.currency.currency import Currency
from model.exchange.exchange import Exchange
from schema.ticker.ticker import InstrumentType


class Ticker(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    isin: Optional[str] = Field(nullable=True, unique=True)

    code: str = Field(nullable=False)
    name: str = Field(nullable=False)

    exchange_id: int = Field(foreign_key="exchange.id")
    exchange: Exchange = Relationship(back_populates="ticker_list")

    currency_id: int = Field(foreign_key="currency.id")
    currency: Currency = Relationship(back_populates="ticker_list")

    instrument_type: InstrumentType = Field(nullable=False)
