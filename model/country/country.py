from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from model.link.country_continent.country_continent import CountryContinent
from model.link.currency_country.currency_country import CurrencyCountry


class Country(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    common_name: str = Field(nullable=False, unique=True)
    official_name: str = Field(nullable=False, unique=True)

    cca2: str = Field(nullable=False, unique=True)
    cca3: str = Field(nullable=False, unique=True)

    latitude: Optional[float] = Field(nullable=True)
    longitude: Optional[float] = Field(nullable=True)

    capital: Optional[str] = Field(nullable=True)
    population: int = Field(nullable=False)
    flag_url: str = Field(nullable=False)

    continent_list: List["Continent"] = Relationship(back_populates="country_list", link_model=CountryContinent)
    currency_list: List["Currency"] = Relationship(back_populates="country_list", link_model=CurrencyCountry)
