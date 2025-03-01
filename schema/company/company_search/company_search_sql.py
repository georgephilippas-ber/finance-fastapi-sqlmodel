from enum import Enum
from typing import List, Tuple, Optional, Dict

from pydantic import BaseModel

from model.GICS.GICS import GICSIndustry, GICSSector, GICSIndustryGroup, GICSSubIndustry
from model.company.company_snapshot_metrics import CompanySnapshotMetrics
from model.country.country import Country


class MetricDirectionType(Enum):
    HIGH_IS_BEST = 'DESC'
    LOW_IS_BEST = 'ASC'


class MetricType(Enum):
    MARKET_CAPITALIZATION = 'market_capitalization'
    ENTERPRISE_VALUE = 'enterprise_value'
    REVENUE = 'revenue'
    RETURN_ON_ASSETS = 'return_on_assets'
    RETURN_ON_INVESTED_CAPITAL = 'return_on_invested_capital'
    FREE_CASH_FLOW_RETURN_ON_INVESTED_CAPITAL = 'free_cash_flow_return_on_invested_capital'
    RETURN_ON_EQUITY = 'return_on_equity'
    OPERATING_PROFIT_MARGIN = 'operating_profit_margin'
    NET_PROFIT_MARGIN = 'net_profit_margin'
    PRICE_EARNINGS_RATIO = 'price_earnings_ratio'
    PRICE_TO_BOOK_RATIO = 'price_to_book_ratio'
    BETA = 'beta'
    DEBT_TO_EQUITY_RATIO = 'debt_to_equity_ratio'


class GroupType(Enum):
    GICS_SECTOR = GICSSector.__tablename__
    GICS_INDUSTRY = GICSIndustry.__tablename__
    GICS_INDUSTRY_GROUP = GICSIndustryGroup.__tablename__
    GICS_SUB_INDUSTRY = GICSSubIndustry.__tablename__
    COUNTRY = Country.__tablename__


class Criterion(BaseModel):
    metric: MetricType
    metric_direction: MetricDirectionType
    groups: List[Tuple[Optional[GroupType], float]]


# table_name: column name
METRICS_DICTIONARY: Dict[MetricType, Tuple[str, str]] = {
    MetricType.MARKET_CAPITALIZATION: (CompanySnapshotMetrics.__tablename__, "market_capitalization"),
    MetricType.ENTERPRISE_VALUE: (CompanySnapshotMetrics.__tablename__, "enterprise_value"),
    MetricType.REVENUE: (CompanySnapshotMetrics.__tablename__, "revenue"),
    MetricType.RETURN_ON_ASSETS: (CompanySnapshotMetrics.__tablename__, "return_on_assets"),
    MetricType.RETURN_ON_INVESTED_CAPITAL: (CompanySnapshotMetrics.__tablename__, "return_on_invested_capital"),
    MetricType.FREE_CASH_FLOW_RETURN_ON_INVESTED_CAPITAL: (
        CompanySnapshotMetrics.__tablename__, "free_cash_flow_return_on_invested_capital"),
    MetricType.RETURN_ON_EQUITY: (CompanySnapshotMetrics.__tablename__, "return_on_equity"),
    MetricType.OPERATING_PROFIT_MARGIN: (CompanySnapshotMetrics.__tablename__, "operating_profit_margin"),
    MetricType.NET_PROFIT_MARGIN: (CompanySnapshotMetrics.__tablename__, "net_profit_margin"),
    MetricType.PRICE_EARNINGS_RATIO: (CompanySnapshotMetrics.__tablename__, "price_earnings_ratio"),
    MetricType.PRICE_TO_BOOK_RATIO: (CompanySnapshotMetrics.__tablename__, "price_to_book_ratio"),
    MetricType.BETA: (CompanySnapshotMetrics.__tablename__, "beta"),
    MetricType.DEBT_TO_EQUITY_RATIO: (CompanySnapshotMetrics.__tablename__, "debt_to_equity_ratio"),
}

# foreign keys in 'company' table
GROUPS_DICTIONARY = {
    GroupType.GICS_SECTOR: ("gics_sector_id", GICSSector.__tablename__),
    GroupType.GICS_INDUSTRY_GROUP: ("gics_industry_group_id", GICSIndustryGroup.__tablename__),
    GroupType.GICS_INDUSTRY: ("gics_industry_id", GICSIndustry.__tablename__),
    GroupType.GICS_SUB_INDUSTRY: ("gics_subindustry_id", GICSSubIndustry.__tablename__),
    GroupType.COUNTRY: ("country_id", Country.__tablename__),
}
