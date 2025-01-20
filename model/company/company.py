from typing import Optional, Annotated
from uuid import uuid4

from sqlalchemy import String, Column, Integer, Sequence
from sqlmodel import SQLModel, Field, Relationship
from model.GICS.GICS import GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry
from model.currency.currency import Currency
from model.ticker.ticker import Ticker
from model.country.country import Country


class Company(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(uuid4().hex), primary_key=True))

    name: str = Field(nullable=False)
    isin: str = Field(nullable=False, unique=True)
    address: str = Field(nullable=False)
    primary_ticker: Optional[str] = Field(nullable=True, unique=True)
    homepage: Optional[str] = Field(nullable=True)
    logo_url: Optional[str] = Field(nullable=True)
    employees: Optional[int] = Field(nullable=True)
    description: str = Field(sa_column=Column(String(length=0x1000), nullable=False))
    fiscal_year_end: str = Field(nullable=False)

    ticker_id: Optional[int] = Field(foreign_key="ticker.id")
    ticker: Optional[Ticker] = Relationship(back_populates="company")

    gics_sector_id: Optional[int] = Field(foreign_key="GICSSector.id")
    gics_sector: Optional[GICSSector] = Relationship(back_populates="companies")

    gics_industry_group_id: Optional[int] = Field(foreign_key="GICSIndustryGroup.id")
    gics_industry_group: Optional[GICSIndustryGroup] = Relationship(back_populates="companies")

    gics_industry_id: Optional[int] = Field(foreign_key="GICSIndustry.id")
    gics_industry: Optional[GICSIndustry] = Relationship(back_populates="companies")

    gics_subindustry_id: Optional[int] = Field(foreign_key="GICSSubIndustry.id")
    gics_subindustry: Optional[GICSSubIndustry] = Relationship(back_populates="companies")

    currency_id: Optional[int] = Field(foreign_key="currency.id")
    currency: Optional[Currency] = Relationship(back_populates="company_list")

    company_snapshot_metrics: "CompanySnapshotMetrics" = Relationship(back_populates="company")

    country_id: int = Field(foreign_key="country.id")
    country: Country = Relationship(back_populates="company_list")
