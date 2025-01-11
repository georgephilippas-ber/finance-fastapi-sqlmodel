from typing import Dict, List

from abstract.adapter.adapter import Adapter
from schema.exchange.exchange import ExchangeSchema

UNITED_STATES_EXCHANGE_LIST = [
    {
        "Name": "New York Stock Exchange",
        "Code": "NYSE",
        "OperatingMIC": "XNYS",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "NASDAQ Stock Exchange",
        "Code": "NASDAQ",
        "OperatingMIC": "XNAS",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "Chicago Board Options Exchange",
        "Code": "CBOE",
        "OperatingMIC": "XCBO",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "Chicago Stock Exchange",
        "Code": "CHX",
        "OperatingMIC": "XCHI",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    },
    {
        "Name": "Investors Exchange",
        "Code": "IEX",
        "OperatingMIC": "IEXG",
        "Country": "United States",
        "Currency": "USD",
        "CountryISO2": "US",
        "CountryISO3": "USA"
    }
]


class ExchangeAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> ExchangeSchema:
        return ExchangeSchema(name=json_['Name'], code=json_['Code'], country=json_['Country'],
                              currency=json_['Currency'], country_iso2=json_['CountryISO2'],
                              country_iso3=json_['CountryISO3'])

    def adapt_many(self, json_list_: List[Dict]) -> List[ExchangeSchema]:
        return [self.adapt(json_) for json_ in self._preprocess_many(json_list_)]

    def _preprocess_many(self, json_list_: List[Dict]) -> List[Dict]:
        exchange_list_ = list(filter(lambda json_: json_['CountryISO2'] != 'US', json_list_))

        exchange_list_.extend(UNITED_STATES_EXCHANGE_LIST)

        return exchange_list_
