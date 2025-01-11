from typing import Dict, List, Tuple, Optional, TypeAlias

from abstract.adapter.adapter import Adapter
from schema.currency.currency import CurrencySchema
from schema.exchange.exchange import ExchangeSchema
from schema.ticker.ticker import TickerSchema

TickerType: TypeAlias = Tuple[TickerSchema, ExchangeSchema, CurrencySchema]


class TickerAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[TickerType]:
        if json_['Type'] in ['Common Stock', 'ETF']:
            ticker_schema_ = TickerSchema(code=json_['Code'], name=json_['Name'], isin=json_['Isin'],
                                          type=json_['Type'])

            exchange_schema_ = ExchangeSchema(code=json_['Exchange'])

            currency_schema_ = CurrencySchema(code=json_['Currency'])

            return ticker_schema_, exchange_schema_, currency_schema_
        else:
            return None

    def adapt_many(self, json_list_: List[Dict]) -> List[TickerType]:
        return [self.adapt(json_) for json_ in json_list_]
