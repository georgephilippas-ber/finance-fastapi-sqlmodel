from typing import Dict, List, Tuple

from abstract.adapter.adapter import Adapter
from schema.continent.continent import ContinentSchema
from schema.country.country import CountrySchema, CountryNameSchema, CountryISOCodeSchema, LocationSchema
from schema.currency.currency import CurrencySchema


class RESTCountriesAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt_many(self, json_list_: List[Dict]) -> List[
        Tuple[CountrySchema, List[CurrencySchema], List[ContinentSchema]]]:
        return [self.adapt(json_) for json_ in json_list_]

    def adapt(self, json_: Dict) -> Tuple[CountrySchema, List[CurrencySchema], List[ContinentSchema]]:
        country_name_ = CountryNameSchema(common=json_['name']['common'],
                                          official=json_['name']['official'])

        country_iso_code_ = CountryISOCodeSchema(cca2=json_['cca2'], cca3=json_['cca3'])

        currency_list_: List[CurrencySchema] = []

        for currency_code_ in json_['currencies']:
            currency_list_.append(
                CurrencySchema(code=currency_code_, name=json_['currencies'][currency_code_]['name'],
                               symbol=json_['currencies'][currency_code_]['symbol']))

        location_ = LocationSchema(latitude=json_['latlng'][0], longitude=json_['latlng'][1])

        capital_ = json_['capital']
        population_ = json_['population']
        continent_list_ = [ContinentSchema(name=continent_name_) for continent_name_ in json_['continents']]

        flag_url_ = json_['flags']['svg']

        return CountrySchema(name=country_name_, iso_code=country_iso_code_, location=location_, capital=capital_,
                             population=population_, flag_url=flag_url_), currency_list_, continent_list_
