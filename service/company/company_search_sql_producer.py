from enum import Enum, auto
from typing import Dict, Tuple

from typing import TypeAlias


class MetricType(Enum):
    MARKET_CAPITALIZATION = auto()
    RETURN_ON_ASSETS = auto()


MetricsDictionaryType: TypeAlias = Dict[MetricType, Tuple[str, str]]

MetricsDictionary: MetricsDictionaryType = {
    MetricType.MARKET_CAPITALIZATION: ("companysnapshotmetrics", "market_capitalization"),
    MetricType.RETURN_ON_ASSETS: ("companysnapshotmetrics", "return_on_assets")
}


class CompanySearchSQLProducer:
    def __init__(self):
        pass
