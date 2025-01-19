from http import HTTPStatus
from typing import Optional, Tuple

from fastapi import Depends, Request, HTTPException
from sqlmodel import Session

from configuration.security import API_SECURITY_ENABLED
from database.database import Database
from instance.shared import database_instance, json_web_token_instance, eodhd_client_instance, \
    eodhd_end_of_day_change_overview_adapter_instance, meilisearch_client_instance
from manager.end_of_day_change_overview.end_of_day_change_overview_manager import EndOfDayChangeOverviewManager
from manager.exchange.exchange_manager import ExchangeManager
from manager.ticker.ticker_manager import TickerManager
from manager.user.user_manager import UserManager
from orchestrator.eodhd.end_of_day_change_overview_orchestrator import EndOfDayChangeOverviewOrchestrator
from service.company.company_overview_search_service import CompanyOverviewSearchService
from service.company.company_service import CompanyService


def get_json_web_token(request: Request) -> Optional[str]:
    return request.cookies.get("Authorization")


def verify_json_web_token_cookie(token: Optional[str] = Depends(get_json_web_token)) -> None:
    if token and json_web_token_instance.verify_token(token):
        return
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED)


def bypass_security() -> None:
    pass


api_security = verify_json_web_token_cookie if API_SECURITY_ENABLED else bypass_security


def get_session(database_: Database = Depends(lambda: database_instance)) -> Session:
    return database_.create_session()


def get_user_manager(session: Session = Depends(get_session)) -> UserManager:
    return UserManager(session)


def get_company_service(session: Session = Depends(get_session)) -> CompanyService:
    return CompanyService(session)


def get_end_of_day_change_overview_orchestrator_dependencies(session: Session = Depends(get_session)) -> (
        EndOfDayChangeOverviewManager, TickerManager, ExchangeManager):
    end_of_day_change_overview_manager = EndOfDayChangeOverviewManager(session)
    ticker_manager = TickerManager(session, ExchangeManager(session))
    exchange_manager = ExchangeManager(session)

    return end_of_day_change_overview_manager, ticker_manager, exchange_manager


def get_end_of_day_change_overview_orchestrator(
        dependencies: Tuple[EndOfDayChangeOverviewManager, TickerManager, ExchangeManager] = Depends(
            get_end_of_day_change_overview_orchestrator_dependencies)) -> EndOfDayChangeOverviewOrchestrator:
    return EndOfDayChangeOverviewOrchestrator(eodhd_client_instance, eodhd_end_of_day_change_overview_adapter_instance,
                                              dependencies[0], dependencies[1], dependencies[2])


def get_company_overview_search_service(company_service: CompanyService = Depends(get_company_service)):
    return CompanyOverviewSearchService(meilisearch_client_instance, company_service)
