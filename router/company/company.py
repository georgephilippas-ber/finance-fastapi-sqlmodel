from typing import List

from fastapi import APIRouter, Query, Depends

from instance.dependency.dependency import get_company_service
from service.company.company_service import CompanyService

company_router = APIRouter(prefix="/company")


@company_router.get("/overview")
async def get_company(id_param: List[int] = Query(...), company_service: CompanyService = Depends(get_company_service)):
    return company_service.get_company_overview(id_param)
