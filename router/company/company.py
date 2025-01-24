from collections.abc import Callable
from typing import List, Optional

from fastapi import APIRouter, Query, Depends, Body
from sqlmodel import Session

from instance.dependency.dependency import get_company_service, api_security, \
    get_end_of_day_change_overview_orchestrator, get_company_overview_search_service, get_session, \
    get_company_details_orchestrator
from model.end_of_day_change_overview.end_of_day_change_overview import EndOfDayChangeOverview
from orchestrator.company_details_orchestrator.company_details_orchestrator import CompanyDetailsOrchestrator
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator
from schema.company.company import CompanyOverviewSchema, CompanyDetailsSchema
from schema.company.company_search.company_search_sql import Criterion
from service.company.company_overview_search_service import CompanyOverviewSearchService
from service.company.company_service import CompanyService

company_router = APIRouter(prefix="/company")


@company_router.get("/overview")
async def get_company_overview(company_ids: str = Query(...),
                               company_service: CompanyService = Depends(get_company_service),
                               session: Session = Depends(get_session),
                               security: Callable = Depends(api_security)) -> List[CompanyOverviewSchema]:
    return_ = company_service.company_overview(list(map(lambda id_: int(id_), company_ids.split(','))))
    session.close()

    return return_


@company_router.get("/details")
async def get_company_details(company_id: int = Query(...), session: Session = Depends(get_session),
                              company_details_orchestrator: CompanyDetailsOrchestrator = Depends(
                                  get_company_details_orchestrator),
                              security: Callable = Depends(api_security)) -> Optional[CompanyDetailsSchema]:
    return_ = await company_details_orchestrator.by_company_id(company_id)
    session.close()

    return return_


@company_router.get("/end-of-day-change-overview")
async def get_end_of_day_change_overview(ticker_id: int = Query(...),
                                         end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator = Depends(
                                             get_end_of_day_change_overview_orchestrator),
                                         security: Callable = Depends(api_security),
                                         session: Session = Depends(get_session)) -> EndOfDayChangeOverview:
    return_ = await end_of_day_change_overview_orchestrator.by_ticker_id(ticker_id)
    session.close()

    return return_


@company_router.post("/search")
async def search(query: Optional[str] = Query(default=None), criteria: Optional[List[Criterion]] = Body(default=None),
                 company_overview_search_service: CompanyOverviewSearchService = Depends(
                     get_company_overview_search_service), session: Session = Depends(get_session),
                 security: Callable = Depends(api_security)):  #
    return_ = company_overview_search_service.search(query=query, criteria=criteria)
    session.close()

    return return_
