from typing import Dict, List, Optional, Tuple, Iterable

from pydantic import ValidationError

from abstract.adapter.adapter import Adapter
from schema.GICS.gics import GICSSchema
from schema.company.company import CompanySchema
from schema.currency.currency import CurrencySchema


class CompanyAdapter(Adapter):
    def __init__(self, ):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[Tuple[CompanySchema, GICSSchema, CurrencySchema]]:
        try:
            if json_.get('General', {}).get('Type') == 'Common Stock':
                return CompanySchema(
                    name=json_['General']['Name'],
                    isin=json_['General']['ISIN'],
                    address=json_['General']['Address'],
                    primary_ticker=json_['General']['PrimaryTicker'],
                    homepage=json_['General']['WebURL'],
                    logo_url=json_['General']['LogoURL'],
                    employees=json_['General']['FullTimeEmployees'],
                    description=json_['General']['Description'],
                    fiscal_year_end=json_['General']['FiscalYearEnd'],
                ), GICSSchema(sector=json_['General']['GicSector'], industry=json_['General']['GicIndustry'],
                              industry_group=json_['General']['GicGroup'],
                              sub_industry=json_['General']['GicSubIndustry']), CurrencySchema(
                    code=json_['General']['CurrencyCode'])
        except (KeyError, ValidationError) as e:
            print(e)

            return None
        else:
            return None

    def adapt_many(self, json_list_: List[Dict]) -> Iterable[Tuple[CompanySchema, GICSSchema, CurrencySchema]]:
        return filter(lambda schema_tuple_: schema_tuple_ is not None, [self.adapt(json_) for json_ in json_list_])
