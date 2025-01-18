from typing import List

from sqlmodel import select, Session

from configuration.client.eodhd import EODHD_BASE_URL
from model.GICS.GICS import GICSSector, GICSIndustry
from model.company.company import Company
from model.country.country import Country
from model.currency.currency import Currency
from model.exchange.exchange import Exchange
from model.ticker.ticker import Ticker
from schema.company.company import CompanyOverviewSchema
from urllib.parse import urljoin


class CompanyService:
    _session: Session
    _company_logo_base_url: str

    def __init__(self, session: Session, company_logo_base_url: str = EODHD_BASE_URL):
        self._session = session

        self._company_logo_base_url = company_logo_base_url

    def company_overview(self, company_id_list: List[int]) -> List[CompanyOverviewSchema]:
        query_ = select(
            Company.id, Company.name, Ticker.code, Exchange.code, Currency.symbol,
            GICSSector.name, GICSIndustry.name,
            Company.logo_url, Country.flag_url, Ticker.id).select_from(
            Company).join(Country,
                          Company.country_id == Country.id).join(
            Currency, Currency.id == Company.currency_id).join(GICSSector,
                                                               GICSSector.id == Company.gics_sector_id).join(
            GICSIndustry,
            GICSIndustry.id == Company.gics_industry_id).join(Ticker, Ticker.id == Company.ticker_id).join(Exchange,
                                                                                                           Ticker.exchange_id == Exchange.id).where(
            Company.id.in_(company_id_list))

        query_result_list_ = self._session.exec(query_).all()

        return [
            CompanyOverviewSchema(company_id=query_result_[0], company_name=query_result_[1],
                                  ticker_code=query_result_[2], exchange_code=query_result_[3],
                                  currency_symbol=query_result_[4], gics_sector_name=query_result_[5],
                                  gics_industry_name=query_result_[6],
                                  company_logo_url=urljoin(self._company_logo_base_url, query_result_[7]),
                                  country_flag_url=query_result_[8], ticker_id=query_result_[9])
            for query_result_ in query_result_list_]


if __name__ == '__main__':
    pass
