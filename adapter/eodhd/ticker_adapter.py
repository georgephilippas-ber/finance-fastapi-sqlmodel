from typing import Dict, List, Tuple, Optional

from abstract.adapter.adapter import Adapter
from schema.country.country import CountryISOCodeSchema
from schema.currency.currency import CurrencySchema
from schema.exchange.exchange import ExchangeSchema
from schema.ticker.ticker import TickerSchema


class TickerAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[Tuple[TickerSchema, ExchangeSchema, CurrencySchema]]:
        ticker_schema_ = TickerSchema(code=json_['Code'], name=json_['Name'], isin=json_['Isin'], type=json_['Type'])

        exchange_schema_ = ExchangeSchema(code=json_['Exchange'])

    def adapt_many(self, json_list_: List[Dict]) -> List[ExchangeSchema]:
        pass
