from enum import Enum, auto
from typing import Dict, Tuple, List

from typing import TypeAlias

from model.GICS.GICS import GICSIndustry
from model.continent.continent import Continent
from model.country.country import Country


class MetricType(Enum):
    MARKET_CAPITALIZATION = 'market_capitalization'
    RETURN_ON_ASSETS = 'return_on_assets'


class GroupType(Enum):
    GICS_INDUSTRY = GICSIndustry.__tablename__
    COUNTRY = Country.__tablename__
    CONTINENT = Continent.__tablename__


MetricsDictionary: Dict[MetricType, Tuple[str, str]] = {
    MetricType.MARKET_CAPITALIZATION: ("companysnapshotmetrics", "market_capitalization"),
    MetricType.RETURN_ON_ASSETS: ("companysnapshotmetrics", "return_on_assets")
}

GroupsDictionary = {
    GroupType.GICS_INDUSTRY: ("gicsindustry", "gics_industry_id")  # (table name, foreign_key in company table)
}


class CriterionType(Enum):
    metric: MetricType
    groups: List[Tuple[GroupType, float]]


class CompanySearchSQL:
    def __init__(self):
        pass

    def sql(self, metric: MetricType, ) -> List[int]:
        pass
