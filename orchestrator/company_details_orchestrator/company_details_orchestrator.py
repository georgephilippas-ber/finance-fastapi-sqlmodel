from typing import Optional

from manager.company.company_manager import CompanyManager
from manager.company.company_snapshot_metrics_manager import CompanySnapshotMetricsManager
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator
from schema.company.company import CompanySnapshotMetricsSchema, CompanyDetailsSchema
from schema.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverviewSchema
from service.company.company_service import CompanyService


class CompanyDetailsOrchestrator:
    _end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator
    _company_service: CompanyService
    _company_snapshot_metrics_manager: CompanySnapshotMetricsManager
    _company_manager: CompanyManager

    def __init__(self,
                 end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator,
                 company_service: CompanyService,
                 company_snapshot_metrics_manager: CompanySnapshotMetricsManager,
                 company_manager: CompanyManager):
        self._end_of_day_change_overview_orchestrator = end_of_day_change_overview_orchestrator
        self._company_service = company_service
        self._company_snapshot_metrics_manager = company_snapshot_metrics_manager
        self._company_manager = company_manager

    async def by_company_id(self, company_id: int) -> Optional[CompanyDetailsSchema]:
        try:
            company_overview_schema_, = self._company_service.company_overview([company_id])

            ticker_id_: Optional[int] = self._company_manager.ticker_id(company_id)

            try:
                end_of_day_change_overview_ = await self._end_of_day_change_overview_orchestrator.by_ticker_id(
                    ticker_id_)
                print("EOCO", end_of_day_change_overview_)
            except Exception as e:
                end_of_day_change_overview_ = None

            company_snapshot_metrics_ = self._company_snapshot_metrics_manager.by_company_id_latest(company_id)

            company_snapshot_metrics_schema_ = CompanySnapshotMetricsSchema(
                **company_snapshot_metrics_.model_dump()
            )

            if end_of_day_change_overview_ is not None:
                end_of_day_change_overview_schema_ = EndOfDayChangeOverviewSchema(
                    **end_of_day_change_overview_.model_dump()
                )
            else:
                end_of_day_change_overview_schema_ = None

            if company_snapshot_metrics_ is not None and company_overview_schema_ is not None:
                return CompanyDetailsSchema(
                    company_snapshot_metrics=company_snapshot_metrics_schema_,
                    company_overview=company_overview_schema_,
                    end_of_day_change_overview=end_of_day_change_overview_schema_)
            else:
                return None
        except Exception as e:
            return None


if __name__ == "__main__":
    pass
