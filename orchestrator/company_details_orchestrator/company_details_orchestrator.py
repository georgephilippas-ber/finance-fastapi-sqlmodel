from pydantic import BaseModel

from manager.company.company_snapshot_metrics_manager import CompanySnapshotMetricsManager
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator
from schema.company.company import CompanySnapshotMetricsSchema, CompanyOverviewSchema
from schema.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverviewSchema
from service.company.company_service import CompanyService


class CompanyDetailsSchema(BaseModel):
    company_snapshot_metrics: CompanySnapshotMetricsSchema
    company_overview: CompanyOverviewSchema
    end_of_day_change_overview: EndOfDayChangeOverviewSchema


class CompanyDetailsOrchestrator:
    _end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator
    _company_service: CompanyService
    _company_snapshot_metrics_manager: CompanySnapshotMetricsManager

    def __init__(self, end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator,
                 company_service: CompanyService, company_snapshot_metrics_manager: CompanySnapshotMetricsManager):
        self._end_of_day_change_overview_orchestrator = end_of_day_change_overview_orchestrator
        self._company_service = company_service
        self._company_snapshot_metrics_manager = company_snapshot_metrics_manager
