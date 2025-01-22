from typing import Tuple, Dict

from model.GICS.GICS import GICSIndustry, GICSSector
from model.company.company_snapshot_metrics import CompanySnapshotMetrics
from model.country.country import Country
from schema.company.company_search.company_search_sql import MetricType, GroupType

METRICS_DICTIONARY: Dict[MetricType, Tuple[str, str]] = {
    MetricType.MARKET_CAPITALIZATION: (CompanySnapshotMetrics.__tablename__, "market_capitalization"),
    MetricType.RETURN_ON_ASSETS: (CompanySnapshotMetrics.__tablename__, "return_on_assets"),
    MetricType.OPERATING_PROFIT_MARGIN: (CompanySnapshotMetrics.__tablename__, "operating_profit_margin"),
}

GROUPS_DICTIONARY = {
    GroupType.GICS_INDUSTRY: ("gics_industry_id", GICSIndustry.__tablename__),
    GroupType.COUNTRY: ("country_id", Country.__tablename__),
    GroupType.GICS_SECTOR: ("gics_sector_id", GICSSector.__tablename__),
}
