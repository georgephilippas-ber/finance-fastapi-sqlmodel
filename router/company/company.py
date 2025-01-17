from fastapi import APIRouter, Query, Depends

from instance.dependency.dependency import get_company_service, api_security
from service.company.company_service import CompanyService

company_router = APIRouter(prefix="/company")


@company_router.get("/overview")
async def get_company(ids: str = Query(...), company_service: CompanyService = Depends(get_company_service),
                      security=Depends(api_security)):
    return company_service.get_company_overview(list(map(lambda id_: int(id_), ids.split(','))))
