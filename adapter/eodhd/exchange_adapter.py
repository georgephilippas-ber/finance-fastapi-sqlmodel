from typing import Dict, List

from abstract.adapter.adapter import Adapter
from schema.exchange.exchange import ExchangeSchema


class ExchangeAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> ExchangeSchema:
        return ExchangeSchema(name=json_['Name'], code=json_['Code'], country=json_['Country'],
                              currency=json_['Currency'], country_iso2=json_['CountryISO2'],
                              country_iso3=json_['CountryISO3'])

    def adapt_many(self, json_list_: List[Dict]) -> List[ExchangeSchema]:
        return [self.adapt(json_) for json_ in json_list_]
