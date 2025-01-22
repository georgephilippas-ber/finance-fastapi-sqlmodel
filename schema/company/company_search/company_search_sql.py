from enum import Enum
from typing import List, Tuple, Optional

from pydantic import BaseModel

from model.GICS.GICS import GICSIndustry, GICSSector
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
