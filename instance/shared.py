from adapter.eodhd.end_of_day_change_overview_adapter import EndOfDayChangeOverviewAdapter
from client.eodhd.eodhd_client import EODHDClient
from core.jsonwebtoken.jsonwebtoken import JSONWebToken
from database.database import Database

json_web_token_instance = JSONWebToken()

database_instance = Database()

eodhd_client_instance = EODHDClient()
eodhd_end_of_day_change_overview_adapter_instance = EndOfDayChangeOverviewAdapter()
