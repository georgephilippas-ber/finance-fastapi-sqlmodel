from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple, List, Literal, Optional

from sqlalchemy import text, Engine

from database.database import Database
from model.GICS.GICS import GICSIndustry
from model.company.company_snapshot_metrics import CompanySnapshotMetrics
from model.country.country import Country


class MetricDirection(Enum):
    HIGH_IS_BEST = 'DESC'
    LOW_IS_BEST = 'ASC'


class MetricType(Enum):
    MARKET_CAPITALIZATION = 'market_capitalization'
    RETURN_ON_ASSETS = 'return_on_assets'
    OPERATING_PROFIT_MARGIN = 'operating_profit_margin'


class GroupType(Enum):
    GICS_INDUSTRY = GICSIndustry.__tablename__
    COUNTRY = Country.__tablename__


metrics_dictionary: Dict[MetricType, Tuple[str, str]] = {
    MetricType.MARKET_CAPITALIZATION: (CompanySnapshotMetrics.__tablename__, "market_capitalization"),
    MetricType.RETURN_ON_ASSETS: (CompanySnapshotMetrics.__tablename__, "return_on_assets"),
    MetricType.OPERATING_PROFIT_MARGIN: (CompanySnapshotMetrics.__tablename__, "operating_profit_margin"),
}

groups_dictionary = {
    GroupType.GICS_INDUSTRY: ("gics_industry_id", GICSIndustry.__tablename__),
    GroupType.COUNTRY: ("country_id", Country.__tablename__),
}


@dataclass
class CriterionType:
    metric: MetricType
    metric_direction: MetricDirection
    groups: List[Tuple[Optional[GroupType], float]]


example: List[CriterionType] = [
    CriterionType(MetricType.MARKET_CAPITALIZATION, MetricDirection.HIGH_IS_BEST, [(GroupType.COUNTRY, 0.20)]),
    # CriterionType(MetricType.RETURN_ON_ASSETS, [(GroupType.GICS_INDUSTRY, 1)]),
    # CriterionType(MetricType.OPERATING_PROFIT_MARGIN, [(GroupType.GICS_INDUSTRY, 1)])
]


def get_partition(group: Optional[GroupType]):
    return f"PARTITION BY company.{groups_dictionary[group][0]}" if group is not None else ""


def query(metric: MetricType, metric_direction: MetricDirection, group_and_percentile: Tuple[GroupType, float]) -> str:
    query_ = f"""
        WITH ranking_table AS (
            SELECT
                company.id AS company_id,
                {metrics_dictionary[metric][0]}.{metrics_dictionary[metric][1]} AS {metrics_dictionary[metric][1]},
                PERCENT_RANK() OVER 
                (
                    {get_partition(group_and_percentile[0])} ORDER BY {metrics_dictionary[metric][0]}.{metrics_dictionary[metric][1]} {metric_direction.value} 
                ) AS company_percentile
            FROM
                {metrics_dictionary[metric][0]}
            JOIN
                company ON {metrics_dictionary[metric][0]}.company_id = company.id
        )
        SELECT company_id, company_percentile FROM ranking_table WHERE company_percentile <= {group_and_percentile[1]}
    """

    return query_


class CompanySearchSQL:
    _session: Engine

    def __init__(self, engine: Engine):
        self._engine = engine

    def sql(self, criteria_list: List[CriterionType], operator: Literal["AND", "OR"]) -> List[int]:
        query_list_: List[str] = []

        for criterion_ in criteria_list:
            metric_ = criterion_.metric
            metric_direction_ = criterion_.metric_direction
            for group_ in criterion_.groups:
                query_list_.append(query(metric_, metric_direction_, group_))

        match operator:
            case "AND":
                query_ = ' INTERSECT '.join(map(lambda subquery: f"({subquery})", query_list_))
            case "OR":
                query_ = ' UNION '.join(map(lambda subquery: f"({subquery})", query_list_))
            case _:
                query_ = None

        with self._engine.connect() as connection:
            query_results_ = connection.execute(text(query_)).all()

            return [query_result_[0] for query_result_ in query_results_]


if __name__ == '__main__':
    db = Database()

    sql = CompanySearchSQL(db.get_engine())
    print(sql.sql(example, "AND"))
