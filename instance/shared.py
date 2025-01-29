from adapter.eodhd.end_of_day_change_overview_adapter import EndOfDayChangeOverviewAdapter
from client.eodhd.eodhd_client import EODHDClient
from client.meilisearch.meilisearch_client import MeilisearchClient
from core.security.jsonwebtoken.jsonwebtoken import JSONWebToken
from database.database import Database
from manager.session.session_manager import SessionManager
from service.company.company_search_sql_service import CompanySearchSQLService

json_web_token_instance = JSONWebToken()

database_instance = Database()

session_manager_instance = SessionManager()

eodhd_client_instance = EODHDClient()
eodhd_end_of_day_change_overview_adapter_instance = EndOfDayChangeOverviewAdapter()

meilisearch_client_instance = MeilisearchClient()

company_search_sql_service_instance = CompanySearchSQLService(database_instance.get_engine())
