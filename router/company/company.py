from fastapi import APIRouter, Query, Depends

from instance.dependency.dependency import get_company_service, api_security, \
    get_end_of_day_change_overview_orchestrator
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator
from service.company.company_service import CompanyService

company_router = APIRouter(prefix="/company")


@company_router.get("/overview")
async def get_company(ids: str = Query(...), company_service: CompanyService = Depends(get_company_service),
                      security=Depends(api_security)):
    return company_service.company_overview(list(map(lambda id_: int(id_), ids.split(','))))


@company_router.get("/end-of-day-change-overview")
async def get_end_of_day_change_overview(ticker_id: int = Query(...),
                                         end_of_day_change_overview_orchestrator: EndOfDayChangeOverviewOrchestrator = Depends(
                                             get_end_of_day_change_overview_orchestrator),
                                         security=Depends(api_security)):
    return await end_of_day_change_overview_orchestrator.by_ticker_id(ticker_id)
