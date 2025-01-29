import asyncio

from sqlmodel import Session

from adapter.eodhd.company_adapter import CompanyAdapter
from adapter.eodhd.company_snapshot_metrics_adapter import CompanySnapshotMetricsAdapter
from adapter.eodhd.exchange_adapter import ExchangeAdapter
from adapter.eodhd.ticker_adapter import TickerAdapter
from adapter.kaggle.gics_adapter import GICSAdapter
from adapter.restcountries.restcountries_adapter import RESTCountriesAdapter
from client.eodhd.eodhd_client import EODHDClient
from client.restcountries.restcountries_client import RESTCountriesClient
from configuration.seed import SEED_ENTITIES_SPECIFICATION, ModelSliceEnum, DROP_ALL_TABLES_BEFORE_SEEDING, \
    SeedSpecificationDict
from database.database import Database
from manager.GICS.GICS_manager import GICSSectorManager, GICSIndustryGroupManager, GICSIndustryManager, \
    GICSSubIndustryManager
from manager.company.company_manager import CompanyManager
from manager.company.company_snapshot_metrics_manager import CompanySnapshotMetricsManager
from manager.continent.continent_manager import ContinentManager
from manager.country.country_manager import CountryManager
from manager.currency.currency_manager import CurrencyManager
from manager.exchange.exchange_manager import ExchangeManager
from manager.ticker.ticker_manager import TickerManager
from manager.user.user_manager import UserManager
from seeder.eodhd.eodhd_seeder import EODHDSeeder
from seeder.kaggle.kaggle_seeder import KaggleSeeder
from seeder.local.user_seeder import UserSeeder
from seeder.meilisearch.company_seeder import MeilisearchCompanySeeder
from seeder.restcountries.restcountries_seeder import RESTCountriesSeeder
from service.company.company_service import CompanyService
from core.dependency.dependency import Resolver
from core.dependency.resolvers.compile import compile_resolver
from client.meilisearch.meilisearch_client import MeilisearchClient


async def seed(seed_specification: SeedSpecificationDict, drop_all: bool = False, debug: bool = True):
    database_ = Database()
    database_.create_tables(drop_all=drop_all)

    restcountries_client = RESTCountriesClient()
    eodhd_client = EODHDClient()

    restcountries_adapter_ = RESTCountriesAdapter()
    eodhd_exchange_adapter_ = ExchangeAdapter()
    eodhd_ticker_adapter_ = TickerAdapter()
    eodhd_company_adapter_ = CompanyAdapter()
    eodhd_company_snapshot_metrics_adapter_ = CompanySnapshotMetricsAdapter()

    meilisearch_client = MeilisearchClient()

    with Session(database_.get_engine()) as session:
        country_manager_ = CountryManager(session)
        currency_manager_ = CurrencyManager(session)
        continent_manager_ = ContinentManager(session)
        exchange_manager_ = ExchangeManager(session)
        ticker_manager_ = TickerManager(session, exchange_manager_)

        company_manager_ = CompanyManager(session)
        company_snapshot_metrics_manager_ = CompanySnapshotMetricsManager(session, company_manager_)

        user_manager_ = UserManager(session)

        gics_sector_manager_ = GICSSectorManager(session)
        gics_industry_group_manager_ = GICSIndustryGroupManager(session, gics_sector_manager_)
        gics_industry_manager_ = GICSIndustryManager(session, gics_sector_manager_, gics_industry_group_manager_)
        gics_sub_industry_manager = GICSSubIndustryManager(session, gics_sector_manager_,
                                                           gics_industry_group_manager_, gics_industry_manager_)

        company_service_ = CompanyService(session)

        restcountries_seeder_ = RESTCountriesSeeder(restcountries_client, restcountries_adapter_, country_manager_,
                                                    currency_manager_,
                                                    continent_manager_)

        eodhd_seeder_ = EODHDSeeder(eodhd_client, eodhd_exchange_adapter_, eodhd_ticker_adapter_,
                                    eodhd_company_adapter_, eodhd_company_snapshot_metrics_adapter_,
                                    country_manager_,
                                    currency_manager_,
                                    exchange_manager_, ticker_manager_, company_manager_,
                                    company_snapshot_metrics_manager_,
                                    gics_sector_manager_, gics_industry_group_manager_, gics_industry_manager_,
                                    gics_sub_industry_manager, session=session)

        kaggle_gics_adapter_ = GICSAdapter()

        gics_sector_manager_ = GICSSectorManager(session)
        gics_industry_group_manager_ = GICSIndustryGroupManager(session, gics_sector_manager_)
        gics_industry_manager_ = GICSIndustryManager(session, gics_sector_manager_, gics_industry_group_manager_)
        gics_sub_industry_manager = GICSSubIndustryManager(session, gics_sector_manager_, gics_industry_group_manager_,
                                                           gics_industry_manager_)

        kaggle_seeder_ = KaggleSeeder(
            kaggle_gics_adapter_,
            gics_sector_manager_,
            gics_industry_group_manager_, gics_industry_manager_, gics_sub_industry_manager)

        user_seeder_ = UserSeeder(user_manager_)

        meilisearch_company_seeder_ = MeilisearchCompanySeeder(meilisearch_client, company_service_)

        resolver_: Resolver = compile_resolver(seed_specification, debug=debug)

        resolver_.add_callback(ModelSliceEnum.COUNTRY_CURRENCY.value, restcountries_seeder_.seed)
        resolver_.add_callback(ModelSliceEnum.GICS, kaggle_seeder_.seed_gics)
        resolver_.add_callback(ModelSliceEnum.EXCHANGE.value, eodhd_seeder_.seed_exchange)
        resolver_.add_callback(ModelSliceEnum.TICKER.value, eodhd_seeder_.seed_ticker)
        resolver_.add_callback(ModelSliceEnum.COMPANY_AND_COMPANY_SNAPSHOT_METRICS.value,
                               eodhd_seeder_.seed_company_and_company_snapshot_metrics)
        resolver_.add_callback(ModelSliceEnum.USER.value, user_seeder_.seed)
        resolver_.add_callback(ModelSliceEnum.MEILISEARCH_COMPANY_SEEDER, meilisearch_company_seeder_.seed)

        await resolver_.process()

        session.commit()


if __name__ == '__main__':
    asyncio.run(seed(SEED_ENTITIES_SPECIFICATION, drop_all=DROP_ALL_TABLES_BEFORE_SEEDING, debug=True))
