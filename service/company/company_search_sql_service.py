from typing import Tuple, List, Literal, Optional

from sqlalchemy import text, Engine

from configuration.search.company.company_search_sql import METRICS_DICTIONARY, GROUPS_DICTIONARY
from database.database import Database
from schema.company.company_search.company_search_sql import MetricDirectionType, MetricType, GroupType, Criterion


class CompanySearchSQLService:
    _session: Engine

    def __init__(self, engine: Engine):
        self._engine = engine

    @staticmethod
    def _get_partition(group: Optional[GroupType]):
        return f"PARTITION BY company.{GROUPS_DICTIONARY[group][0]}" if group is not None else ""

    @staticmethod
    def _query(metric: MetricType, metric_direction: MetricDirectionType,
               group_and_percentile: Tuple[GroupType, float]) -> str:
        query_ = f"""
            WITH ranking_table AS (
                SELECT
                    company.id AS company_id,
                    {METRICS_DICTIONARY[metric][0]}.{METRICS_DICTIONARY[metric][1]} AS {METRICS_DICTIONARY[metric][1]},
                    PERCENT_RANK() OVER 
                    (
                        {CompanySearchSQLService._get_partition(group_and_percentile[0])} ORDER BY {METRICS_DICTIONARY[metric][0]}.{METRICS_DICTIONARY[metric][1]} {metric_direction.value} 
                    ) AS company_percentile
                FROM
                    {METRICS_DICTIONARY[metric][0]}
                JOIN
                    company ON {METRICS_DICTIONARY[metric][0]}.company_id = company.id
            )
            SELECT company_id, company_percentile FROM ranking_table WHERE company_percentile <= {group_and_percentile[1]}
        """

        return query_

    def get_company_ids(self, criteria_list: List[Criterion], operator: Literal["AND", "OR"] = "AND") -> List[int]:
        query_list_: List[str] = []

        for criterion_ in criteria_list:
            metric_ = criterion_.metric
            metric_direction_ = criterion_.metric_direction
            for group_ in criterion_.groups:
                query_list_.append(CompanySearchSQLService._query(metric_, metric_direction_, group_))

        match operator:
            case "AND":
                query_ = ' INTERSECT '.join(map(lambda subquery: f"({subquery})", query_list_))
            case "OR":
                query_ = ' UNION '.join(map(lambda subquery: f"({subquery})", query_list_))
            case _:
                query_ = None

        if query_:
            with self._engine.connect() as connection:
                query_results_ = connection.execute(text(query_)).all()

                return [query_result_[0] for query_result_ in query_results_]
        else:
            return []


if __name__ == '__main__':
    pass
