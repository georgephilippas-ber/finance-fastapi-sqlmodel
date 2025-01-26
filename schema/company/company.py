from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from decimal import Decimal

from schema.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverviewSchema


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
    updated_at: Optional[date] = Field(default=None)

    market_capitalization: Decimal
    enterprise_value: Decimal

    return_on_assets: float

    operating_profit_margin: float
    net_profit_margin: float

    price_earnings_ratio: Optional[float] = Field(default=None)
    book_price_per_share: float

    revenue: Decimal
    gross_profit: Decimal

    diluted_eps: float

    price_to_book_ratio: float

    shares_outstanding: Decimal
    shares_float: Decimal

    beta: Optional[float] = Field(default=None)

    fifty_two_week_high: float
    fifty_two_week_low: float

    return_on_invested_capital: Optional[float] = Field(default=None)
    free_cash_flow_return_on_invested_capital: Optional[float] = Field(default=None)
    debt_to_equity_ratio: Optional[float] = Field(default=None)


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
    country_common_name: str
    country_official_name: str
    country_cca2: str
    country_cca3: str
    continents: str


class CompanyDetailsSchema(BaseModel):
    company_overview: CompanyOverviewSchema
    company_snapshot_metrics: CompanySnapshotMetricsSchema
    end_of_day_change_overview: Optional[EndOfDayChangeOverviewSchema] = Field(default=None)
