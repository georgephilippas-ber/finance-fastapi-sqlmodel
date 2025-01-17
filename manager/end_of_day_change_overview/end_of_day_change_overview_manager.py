from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import Session, select

from abstract.manager.manager import Manager
from model.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverview
from schema.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverviewSchema
from datetime import date
from sqlalchemy import and_


class EndOfDayChangeOverviewManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def by_ticker_id_and_date(self, ticker_id: int, date_: date) -> Optional[EndOfDayChangeOverview]:
        query_ = select(EndOfDayChangeOverview).where(
            and_(EndOfDayChangeOverview.ticker_id == ticker_id, EndOfDayChangeOverview.latest_date == date_)).where()

        return self._session.exec(query_).first()

    def retrieve_unique(self, schema: EndOfDayChangeOverviewSchema) -> Optional[EndOfDayChangeOverview]:
        query_ = select(EndOfDayChangeOverview).where(EndOfDayChangeOverview.latest_date == schema.latest_date)

        return self._session.exec(query_).first()

    def persist(self, schema: EndOfDayChangeOverviewSchema, foreign_keys: Optional[dict] = None) -> Optional[
        EndOfDayChangeOverview]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.latest_date = schema.latest_date

            existing_.latest = schema.latest
            existing_.latest_adjusted = schema.latest_adjusted

            existing_.beginning_of_month_adjusted = schema.beginning_of_month_adjusted
            existing_.beginning_of_year_adjusted = schema.beginning_of_year_adjusted

            self._session.commit()
            return existing_

        end_of_day_change_overview_ = EndOfDayChangeOverview(
            latest_date=schema.latest_date,
            latest=schema.latest,
            latest_adjusted=schema.latest_adjusted,
            beginning_of_month_adjusted=schema.beginning_of_month_adjusted,
            beginning_of_year_adjusted=schema.beginning_of_year_adjusted,
            ticker_id=foreign_keys['ticker_id']
        )

        try:
            self._session.add(end_of_day_change_overview_)

            self._session.commit()

            return existing_
        except SQLAlchemyError as e:
            print(e)
            self._session.rollback()

            return None
