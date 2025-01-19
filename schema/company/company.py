from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from decimal import Decimal


class CompanySchema(BaseModel):
    name: str
    isin: str
    address: str
    primary_ticker: Optional[str] = Field(default=None)
    homepage: str
    logo_url: str
    employees: int
    description: str
    fiscal_year_end: str


class CompanySnapshotMetricsSchema(BaseModel):
    market_capitalization: Decimal
    enterprise_value: Decimal

    return_on_assets: float

    operating_profit_margin: float
    net_profit_margin: float

    updated_at: date


class CompanyOverviewSchema(BaseModel):
    company_id: int
    ticker_id: int
    company_name: str
    ticker_code: str
    exchange_code: str
    currency_symbol: str
    currency_code: str
    gics_sector_name: str
    gics_industry_name: str
    company_logo_url: str
    country_flag_url: str
    description: str
