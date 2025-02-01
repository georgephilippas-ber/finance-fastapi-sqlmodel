from typing import Callable

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from instance.dependency.dependency import get_end_of_day_change_overview_orchestrator, api_security, get_session
from model.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverview
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator

company_router = APIRouter(prefix="/ticker")


@company_router.get("/end-of-day-change-overview")
async def get_end_of_day_change_overview(ticker_id: int = Query(...),
                                         end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator = Depends(
                                             get_end_of_day_change_overview_orchestrator),
                                         security: Callable = Depends(api_security),
                                         session: Session = Depends(get_session)) -> EndOfDayChangeOverview:
    return_ = await end_of_day_change_overview_orchestrator.by_ticker_id(ticker_id)
    session.close()

    return return_
