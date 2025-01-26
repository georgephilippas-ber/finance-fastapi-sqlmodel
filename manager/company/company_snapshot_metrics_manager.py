from typing import Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError
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

    def by_company_id_latest(self, company_id: int) -> Optional[CompanySnapshotMetrics]:
        query_ = select(CompanySnapshotMetrics).where(CompanySnapshotMetrics.company_id == company_id).order_by(
            CompanySnapshotMetrics.updated_at.desc()).limit(1)

        return self._session.exec(query_).first()

    def retrieve_unique(self, schema_tuple: Tuple[CompanySchema, CompanySnapshotMetricsSchema], **kwargs) -> Optional[
        CompanySnapshotMetrics]:
        company_schema_, company_snapshot_metrics_schema_ = schema_tuple

        existing_company_ = self._company_manager.by_isin(company_schema_.isin)

        if existing_company_ is not None:
            query_ = select(CompanySnapshotMetrics).where(
                (and_(CompanySnapshotMetrics.company_id == existing_company_.id,
                      CompanySnapshotMetrics.updated_at == company_snapshot_metrics_schema_.updated_at)))

            return self._session.exec(query_).first()
        else:
            return None

    def persist(self, schema_tuple: Tuple[CompanySchema, CompanySnapshotMetricsSchema],
                foreign_keys: Optional[dict] = None) -> Optional[CompanySnapshotMetrics]:
        existing_ = self.retrieve_unique(schema_tuple)

        if existing_ is not None:
            self._session.flush()
            return existing_

        company_schema_, company_snapshot_metrics_schema_ = schema_tuple

        company_snapshot_metrics_ = CompanySnapshotMetrics(
            updated_at=company_snapshot_metrics_schema_.updated_at,
            company_id=foreign_keys['company_id'],
            market_capitalization=company_snapshot_metrics_schema_.market_capitalization,
            enterprise_value=company_snapshot_metrics_schema_.enterprise_value,
            return_on_assets=company_snapshot_metrics_schema_.return_on_assets,
            operating_profit_margin=company_snapshot_metrics_schema_.operating_profit_margin,
            net_profit_margin=company_snapshot_metrics_schema_.net_profit_margin,
            price_to_book_ratio=company_snapshot_metrics_schema_.price_to_book_ratio,
            fifty_two_week_high=company_snapshot_metrics_schema_.fifty_two_week_high,
            fifty_two_week_low=company_snapshot_metrics_schema_.fifty_two_week_low,
            price_earnings_ratio=company_snapshot_metrics_schema_.price_earnings_ratio,
            book_price_per_share=company_snapshot_metrics_schema_.book_price_per_share,
            diluted_eps=company_snapshot_metrics_schema_.diluted_eps,
            revenue=company_snapshot_metrics_schema_.revenue,
            gross_profit=company_snapshot_metrics_schema_.gross_profit,
            beta=company_snapshot_metrics_schema_.beta,
            shares_outstanding=company_snapshot_metrics_schema_.shares_outstanding,
            shares_float=company_snapshot_metrics_schema_.shares_float,
            debt_to_equity_ratio=company_snapshot_metrics_schema_.debt_to_equity_ratio,
            return_on_invested_capital=company_snapshot_metrics_schema_.return_on_invested_capital,
            free_cash_flow_return_on_invested_capital=company_snapshot_metrics_schema_.free_cash_flow_return_on_invested_capital,
        )

        try:
            self._session.add(company_snapshot_metrics_)

            self._session.flush()

            return company_snapshot_metrics_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
