from typing import Iterable, Optional, Tuple

from sqlmodel import Session

from abstract.manager.manager import Manager, BaseModelBound, SQLModelBound
from model.time_series.fundamental_time_series import FundamentalTimeSeries
from schema.time_frame.time_frame import TimeFrame


class FundamentalTimeSeriesManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def retrieve_unique(self, schema: BaseModelBound | Iterable[BaseModelBound], **kwargs) -> Optional[
        SQLModelBound]:
        pass

    def persist(self, schema: TimeFrame, foreign_keys: Optional[dict] = None) -> Optional[Tuple[int, int]]:
        for date_ in schema.get_dates():
            try:
                fundamental_time_series_ = FundamentalTimeSeries(
                    assets=schema.get_value(date_, 'assets'),
                    debt_to_equity_ratio=schema.get_value(date_, 'debt_to_equity_ratio'),
                    return_on_equity=schema.get_value(date_, 'return_on_equity'),
                    cash=schema.get_value(date_, 'cash'),
                    net_invested_capital=schema.get_value(date_, 'net_invested_capital'),
                    free_cash_flow_return_on_assets=schema.get_value(date_, 'free_cash_flow_return_on_assets'),
                    capital_expenditure=schema.get_value(date_, 'capital_expenditure'),
                    net_working_capital=schema.get_value(date_, 'net_working_capital'),
                    equity=schema.get_value(date_, 'equity'),
                    liabilities=schema.get_value(date_, 'liabilities'),
                    net_debt=schema.get_value(date_, 'net_debt'),
                    net_income=schema.get_value(date_, 'net_income'),
                    free_cash_flow=schema.get_value(date_, 'free_cash_flow'),
                    record_date=date_,
                    company_id=foreign_keys['company_id'],
                )

                self._session.add(fundamental_time_series_)
                self._session.commit()
            except Exception as e:
                print(e)
                pass
