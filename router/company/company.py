from collections.abc import Callable
from typing import List

from fastapi import APIRouter, Query, Depends, Body

from instance.dependency.dependency import get_company_service, api_security, \
    get_end_of_day_change_overview_orchestrator
from model.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverview
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator
from schema.company.company import CompanyOverviewSchema
from schema.company.company_search.company_search_sql import Criterion
from service.company.company_service import CompanyService

company_router = APIRouter(prefix="/company")


@company_router.get("/overview")
async def get_company_overview(company_ids: str = Query(...),
                               company_service: CompanyService = Depends(get_company_service),
                               security: Callable = Depends(api_security)) -> List[CompanyOverviewSchema]:
    return company_service.company_overview(list(map(lambda id_: int(id_), company_ids.split(','))))


@company_router.get("/end-of-day-change-overview")
async def get_end_of_day_change_overview(ticker_id: int = Query(...),
                                         end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator = Depends(
                                             get_end_of_day_change_overview_orchestrator),
                                         security: Callable = Depends(api_security)) -> EndOfDayChangeOverview:
    return await end_of_day_change_overview_orchestrator.by_ticker_id(ticker_id)


@company_router.post("/search")
async def search(query: str = Query(...), criteria: List[Criterion] = Body(...)):
    pass
