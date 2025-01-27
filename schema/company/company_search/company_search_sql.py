from enum import Enum
from typing import List, Tuple, Optional, Dict

from pydantic import BaseModel

from model.GICS.GICS import GICSIndustry, GICSSector
from model.company.company_snapshot_metrics import CompanySnapshotMetrics
from model.country.country import Country


class MetricDirectionType(Enum):
    HIGH_IS_BEST = 'DESC'
    LOW_IS_BEST = 'ASC'


class MetricType(Enum):
    MARKET_CAPITALIZATION = 'market_capitalization'
    RETURN_ON_ASSETS = 'return_on_assets'
    OPERATING_PROFIT_MARGIN = 'operating_profit_margin'


class GroupType(Enum):
    GICS_INDUSTRY = GICSIndustry.__tablename__
    GICS_SECTOR = GICSSector.__tablename__
    COUNTRY = Country.__tablename__


class Criterion(BaseModel):
    metric: MetricType
    metric_direction: MetricDirectionType
    groups: List[Tuple[Optional[GroupType], float]]


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
