from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from model.GICS.GICS import GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry
from model.ticker.ticker import Ticker


class Company(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    name: str = Field(nullable=False)
    isin: str = Field(nullable=False, unique=True)
    address: str = Field(nullable=False)
    primary_ticker: str = Field(nullable=False, unique=True)
    homepage: Optional[str] = Field(nullable=True)
    logo_url: Optional[str] = Field(nullable=True)
    employees: Optional[int] = Field(nullable=True)
    description: str = Field(nullable=False)
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
