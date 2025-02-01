from collections.abc import Callable
from typing import List, Optional

from fastapi import APIRouter, Query, Depends, Body
from sqlmodel import Session

from instance.dependency.dependency import get_company_service, api_security, \
    get_company_overview_search_service, get_session, \
    get_company_details_orchestrator, get_fundamental_time_series_service
from orchestrator.company_details_orchestrator.company_details_orchestrator import CompanyDetailsOrchestrator
from schema.company.company import CompanyOverviewSchema, CompanyDetailsSchema
from schema.company.company_search.company_search_sql import Criterion
from service.company.company_overview_search_service import CompanyOverviewSearchService
from service.company.company_service import CompanyService
from service.company.fundamental_time_series_service import FundamentalTimeSeriesService

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
    print(return_)
    session.close()

    return return_


@company_router.get("/fundamental-time-series")
async def get_fundamental_time_series(company_id: int = Query(...), session: Session = Depends(get_session),
                                      fundamental_time_series_service: FundamentalTimeSeriesService = Depends(
                                          get_fundamental_time_series_service)):
    return_ = fundamental_time_series_service.fundamental_time_series(company_id=company_id)
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
