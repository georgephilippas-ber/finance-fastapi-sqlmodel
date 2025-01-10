from typing import Dict, List

from schema.country.country import CountrySchema, CountryNameSchema, CountryISOCodeSchema, CurrencySchema, \
    LocationSchema


class RESTCountriesAdapter:
    def __init__(self):
        pass

    @staticmethod
    def adapt_country(self, country_dict: Dict) -> CountrySchema:
        country_name_ = CountryNameSchema(common=country_dict['name']['common'],
                                          official=country_dict['name']['official'])

        country_iso_code_ = CountryISOCodeSchema(cca2=country_dict['cca2'], cca3=country_dict['cca3'])

        currency_list_: List[CurrencySchema] = []

        for currency_code_ in country_dict['currencies']:
            currency_list_.append(
                CurrencySchema(code=currency_code_, name=country_dict['currencies'][currency_code_]['name'],
                               symbol=country_dict['currencies'][currency_code_]['symbol']))

        location_ = LocationSchema(latitude=country_dict['latlng'][0], longitude=country_dict['latlng'][1])

        capital_ = country_dict['capital']
        population_ = country_dict['population']
        continents_ = country_dict['continents']

        flag_url_ = country_dict['flags']['svg']

        return CountrySchema(name=country_name_, iso_code=country_iso_code_, currency_list=currency_list_,
                             location=location_, capital=capital_, population=population_, continents=continents_,
                             flag_url=flag_url_)
