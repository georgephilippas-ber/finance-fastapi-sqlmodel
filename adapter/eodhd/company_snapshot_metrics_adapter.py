from typing import List, Dict, Optional

from decimal import Decimal
from pydantic import ValidationError

from abstract.adapter.adapter import Adapter
from schema.company.company import CompanySnapshotMetricsSchema


def net_invested_capital(json_: Dict) -> Optional[Decimal]:
    balance_sheet_ = json_['Financials']['Balance_Sheet']['yearly']

    return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["netInvestedCapital"])


def operating_income(json_: Dict) -> Optional[Decimal]:
    income_statement_ = json_['Financials']['Income_Statement']['yearly']

    return Decimal(income_statement_[list(income_statement_.keys())[0]]["operatingIncome"])


def total_debt(json_: Dict) -> Optional[Decimal]:
    balance_sheet_ = json_['Financials']['Balance_Sheet']['yearly']

    return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["netDebt"])


def total_assets(json_: Dict) -> Optional[Decimal]:
    balance_sheet_ = json_['Financials']['Balance_Sheet']['yearly']

    return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["totalAssets"])


def total_liabilities(json_: Dict) -> Optional[Decimal]:
    balance_sheet_ = json_['Financials']['Balance_Sheet']['yearly']

    return Decimal(balance_sheet_[list(balance_sheet_.keys())[0]]["totalLiab"])


def total_equity(json_: Dict) -> Optional[Decimal]:
    return total_assets(json_) - total_liabilities(json_)


def free_cash_flow(json_: Dict) -> Optional[Decimal]:
    cash_flow_statement_ = json_['Financials']['Cash_Flow']['yearly']

    return Decimal(cash_flow_statement_[list(cash_flow_statement_.keys())[0]]["freeCashFlow"])


def return_on_invested_capital(json_: Dict) -> Optional[float]:
    try:
        return_on_invested_capital_ = float(operating_income(json_) / net_invested_capital(json_))

        return return_on_invested_capital_
    except Exception as e:
        print(e)
        return None


def debt_to_equity(json_: Dict) -> Optional[float]:
    try:
        return float(total_debt(json_) / total_equity(json_))
    except Exception as e:
        print(e)
        return None


def free_cash_flow_return_on_invested_capital(json_: Dict) -> Optional[float]:
    try:
        return float(free_cash_flow(json_) / net_invested_capital(json_))
    except Exception:
        return None


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
                    return_on_invested_capital=return_on_invested_capital(json_),
                    debt_to_equity_ratio=debt_to_equity(json_),
                    free_cash_flow_return_on_invested_capital=free_cash_flow_return_on_invested_capital(json_)
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
