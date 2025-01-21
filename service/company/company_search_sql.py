import re
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple, List, Literal, Optional

from sqlalchemy import text, Engine

from database.database import Database
from model.GICS.GICS import GICSIndustry
from model.company.company_snapshot_metrics import CompanySnapshotMetrics
from model.continent.continent import Continent
from model.country.country import Country


class MetricType(Enum):
    MARKET_CAPITALIZATION = 'market_capitalization'
    RETURN_ON_ASSETS = 'return_on_assets'
    OPERATING_PROFIT_MARGIN = 'operating_profit_margin'


class GroupType(Enum):
    GICS_INDUSTRY = GICSIndustry.__tablename__
    COUNTRY = Country.__tablename__
    CONTINENT = Continent.__tablename__


metrics_dictionary: Dict[MetricType, Tuple[str, str]] = {
    MetricType.MARKET_CAPITALIZATION: (CompanySnapshotMetrics.__tablename__, "market_capitalization"),
    MetricType.RETURN_ON_ASSETS: (CompanySnapshotMetrics.__tablename__, "return_on_assets"),
    MetricType.OPERATING_PROFIT_MARGIN: (CompanySnapshotMetrics.__tablename__, "operating_profit_margin"),
}

groups_dictionary = {
    GroupType.GICS_INDUSTRY: ("gics_industry_id", GICSIndustry.__tablename__)
    # (table name, foreign_key in company table)
}


@dataclass
class CriterionType:
    metric: MetricType
    groups: List[Tuple[GroupType, float]]


example: List[CriterionType] = [
    CriterionType(MetricType.MARKET_CAPITALIZATION, [(GroupType.GICS_INDUSTRY, 0.0001)]),
    # CriterionType(MetricType.RETURN_ON_ASSETS, [(GroupType.GICS_INDUSTRY, 0.5)]),
    # CriterionType(MetricType.OPERATING_PROFIT_MARGIN, [(GroupType.GICS_INDUSTRY, 0.1)])
]


class CompanySearchSQL:
    _session: Engine

    def __init__(self, engine: Engine):
        self._engine = engine

    def sql(self, criteria_list: List[CriterionType], operator: Literal["AND", "OR"]) -> List[int]:
        query_list_: List[str] = []

        for criterion_ in criteria_list:
            metric_ = criterion_.metric
            for group_ in criterion_.groups:
                query_list_.append("(" + query(metric_, group_[0], group_[1]) + ")")

        if operator == "OR":
            query_: str = ' UNION '.join(query_list_)
            print(query_)
        elif operator == "AND":
            pass

        with self._engine.connect() as connection:
            query_results_ = connection.execute(text(query_)).all()

            return [query_result_[0] for query_result_ in query_results_]


if __name__ == '__main__':
    db = Database()

    sql = CompanySearchSQL(db.get_engine())
    print(sql.sql(example, "OR"))
