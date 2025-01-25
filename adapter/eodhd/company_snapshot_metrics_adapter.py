from typing import List, Dict, Optional

from pydantic import ValidationError

from abstract.adapter.adapter import Adapter
from schema.company.company import CompanySnapshotMetricsSchema


def get_return_on_invested_capital(json_: Dict) -> Optional[float]:
    return json_['Financials']['BalanceSheet']['yearly']


class CompanySnapshotMetricsAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[CompanySnapshotMetricsSchema]:
        try:
            if json_.get('General', {}).get('Type') == 'Common Stock':
                return CompanySnapshotMetricsSchema(
                    updated_at=json_['General']['UpdatedAt'],
                    market_capitalization=json_['Highlights']['MarketCapitalization'],
                    enterprise_value=json_['Valuation']['EnterpriseValue'],
                    return_on_assets=json_['Highlights']['ReturnOnAssetsTTM'],
                    operating_profit_margin=json_['Highlights']['OperatingMarginTTM'],
                    net_profit_margin=json_['Highlights']['ProfitMargin'],
                    price_earnings_ratio=json_['Highlights']['PERatio'],
                    book_price_per_share=json_['Highlights']['BookValue'],
                    revenue=json_['Highlights']['RevenueTTM'],
                    gross_profit=json_['Highlights']['GrossProfitTTM'],
                    diluted_eps=json_['Highlights']['DilutedEpsTTM'],
                    shares_outstanding=json_['SharesStats']['SharesOutstanding'],
                    shares_float=json_['SharesStats']['SharesFloat'],
                    beta=json_['Technicals']['Beta'],
                    fifty_two_week_high=json_['Technicals']['52WeekHigh'],
                    fifty_two_week_low=json_['Technicals']['52WeekLow'],
                    price_to_book_ratio=json_['Valuation']['PriceBookMRQ'],
                )
        except (KeyError, ValidationError) as e:
            print(e)

            return None
        else:
            return None

    def adapt_many(self, json_list_: List[Dict]) -> List[CompanySnapshotMetricsSchema]:
        return [self.adapt(json_) for json_ in json_list_]
