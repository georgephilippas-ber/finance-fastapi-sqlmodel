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


MetricsDictionaryType: TypeAlias = Dict[MetricType, Tuple[str, str]]

MetricsDictionary: MetricsDictionaryType = {
    MetricType.MARKET_CAPITALIZATION: ("companysnapshotmetrics", "market_capitalization"),
    MetricType.RETURN_ON_ASSETS: ("companysnapshotmetrics", "return_on_assets")
}


class CriterionType(Enum):
    metric: MetricType
    groups: List[Tuple[GroupType, float]]


class CompanySearchSQLProducer:
    def __init__(self):
        pass

    def sql(self, metric: MetricType, ) -> List[int]:
        pass
