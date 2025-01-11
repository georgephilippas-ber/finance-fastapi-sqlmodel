from sqlmodel import SQLModel, Field


class CurrencyCountry(SQLModel, table=True):
    currency_id: int = Field(foreign_key="currency.id", primary_key=True)
    country_id: int = Field(foreign_key="country.id", primary_key=True)
