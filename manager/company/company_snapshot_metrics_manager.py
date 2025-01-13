from typing import Optional, Tuple

from sqlmodel import Session, select

from abstract.manager.manager import Manager
from manager.company.company_manager import CompanyManager
from model.company.company_snapshot_metrics import CompanySnapshotMetrics
from schema.company.company import CompanySchema, CompanySnapshotMetricsSchema
from sqlalchemy import and_


class CompanySnapshotMetricsManager(Manager):
    _company_manager: CompanyManager

    def __init__(self, session: Session, company_manager: CompanyManager):
        super().__init__(session)

        self._company_manager = company_manager

    def retrieve_unique(self, schema_tuple: Tuple[CompanySchema, CompanySnapshotMetricsSchema]) -> Optional[
        CompanySnapshotMetrics]:
        company_schema_, company_snapshot_metrics_schema_ = schema_tuple

        existing_company_ = self._company_manager.by_isin(company_schema_.isin)

        if existing_company_ is not None:
            query_ = select(CompanySnapshotMetrics).where(
                (and_(CompanySnapshotMetrics.company_id == existing_company_.id,
                      CompanySnapshotMetrics.updated_at == company_snapshot_metrics_schema_.date)))

            return self._session.exec(query_).first()
        else:
            return None

    def persist(self, schema_tuple: Tuple[CompanySchema, CompanySnapshotMetricsSchema],
                foreign_keys: Optional[dict] = None) -> Optional[CompanySnapshotMetrics]:
        pass
