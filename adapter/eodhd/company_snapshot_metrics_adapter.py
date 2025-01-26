from typing import List, Dict, Optional

from decimal import Decimal
from pydantic import ValidationError

from abstract.adapter.adapter import Adapter
from schema.company.company import CompanySnapshotMetricsSchema


class EODHDFundamentalsPreprocessor:
    _json: Dict

    def __init__(self, json_: Dict):
        self._json = json_

    def net_invested_capital(self) -> Optional[Decimal]:
        balance_sheet_ = self._json['Financials']['Balance_Sheet']['yearly']

        return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["netInvestedCapital"])

    def operating_income(self) -> Optional[Decimal]:
        income_statement_ = self._json['Financials']['Income_Statement']['yearly']

        return Decimal(income_statement_[list(income_statement_.keys())[0]]["operatingIncome"])

    def total_debt(self) -> Optional[Decimal]:
        balance_sheet_ = self._json['Financials']['Balance_Sheet']['yearly']

        return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["netDebt"])

    def total_assets(self) -> Optional[Decimal]:
        balance_sheet_ = self._json['Financials']['Balance_Sheet']['yearly']

        return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["totalAssets"])

    def total_liabilities(self) -> Optional[Decimal]:
        balance_sheet_ = self._json['Financials']['Balance_Sheet']['yearly']

        return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["totalLiab"])

    def total_equity(self) -> Optional[Decimal]:
        return self.total_assets() - self.total_liabilities()

    def free_cash_flow(self) -> Optional[Decimal]:
        cash_flow_statement_ = json_['Financials']['Cash_Flow']['yearly']

        return Decimal(cash_flow_statement_[list(cash_flow_statement_.keys())[0]]["freeCashFlow"])

    def return_on_invested_capital(self) -> Optional[float]:
        try:
            return_on_invested_capital_ = float(self.operating_income() / self.net_invested_capital())

            return return_on_invested_capital_
        except Exception as e:
            print(e)
            return None

    def debt_to_equity(self) -> Optional[float]:
        try:
            return float(self.total_debt() / self.total_equity())
        except Exception as e:
            print(e)
            return None

    def free_cash_flow_return_on_invested_capital(self) -> Optional[float]:
        try:
            return float(self.free_cash_flow() / self.net_invested_capital())
        except Exception:
            return None


class CompanySnapshotMetricsAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[CompanySnapshotMetricsSchema]:
        preprocessor_ = EODHDFundamentalsPreprocessor(json_)

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
                    return_on_invested_capital=preprocessor_.return_on_invested_capital(),
                    debt_to_equity_ratio=preprocessor_.debt_to_equity(),
                    free_cash_flow_return_on_invested_capital=preprocessor_.free_cash_flow_return_on_invested_capital()
                )
        except (KeyError, ValidationError) as e:
            print(e)

            return None
        else:
            return None

    def adapt_many(self, json_list_: List[Dict]) -> List[CompanySnapshotMetricsSchema]:
        return [self.adapt(json_) for json_ in json_list_]


if __name__ == '__main__':
    from json import load
    from os.path import join
    from core.utilities.root import project_root

    with open(join(project_root(), "client", "cache", "eodhd", "fundamentals", "4MD-F.json"), "r") as file:
        json_ = load(file)

        print(free_cash_flow_return_on_invested_capital(json_))
        print(return_on_invested_capital(json_))
        print(debt_to_equity(json_))
