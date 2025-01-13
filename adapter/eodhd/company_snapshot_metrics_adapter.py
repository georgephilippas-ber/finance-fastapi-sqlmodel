from typing import List, Dict, Optional

from abstract.adapter.adapter import Adapter
from schema.company.company import CompanySnapshotMetricsSchema


class CompanySnapshotMetricsAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[CompanySnapshotMetricsSchema]:
        try:
            if json_.get('General', {}).get('Type') == 'Common Stock':
                return CompanySnapshotMetricsSchema(
                    market_capitalization=json_['Highlights']['MarketCapitalization'],
                    enterprise_value=json_['Valuation']['EnterpriseValue'],
                    return_on_assets=json_['Highlights']['ReturnOnAssetsTTM'],
                    operating_profit_margin=json_['Highlights']['OperatingMarginTTM'],
                    net_profit_margin=json_['Highlights']['ProfitMargin'],
                    updated_at=json_['General']['UpdatedAt']
                )
        except KeyError as e:
            print(e)

            return None
        else:
            return None

    def adapt_many(self, json_list_: List[Dict]) -> List[CompanySnapshotMetricsSchema]:
        return [self.adapt(json_) for json_ in json_list_]
