from typing import Optional, List
from uuid import uuid4

from sqlalchemy import Integer, Column, Sequence
from sqlmodel import SQLModel, Field, Relationship

from model.link.country_continent.country_continent import CountryContinent
from model.link.currency_country.currency_country import CurrencyCountry
from pathlib import Path


class Country(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(Path(__file__).stem), primary_key=True))

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

    exchange_list: List["Exchange"] = Relationship(back_populates="country")

    company_list: List["Company"] = Relationship(back_populates="country")
