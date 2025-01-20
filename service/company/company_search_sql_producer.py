from enum import Enum
from typing import Dict, Tuple

from typing import TypeAlias


class MetricType(Enum):
    MARKET_CAPITALIZATION = 1


MetricD: TypeAlias = Dict[MetricType, Tuple[str, str]]

a: MetricD = {MetricType.MARKET_CAPITALIZATION: ("", "")}


class CompanySearchSQLProducer:
    def __init__(self):
        pass
