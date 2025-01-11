import asyncio

from sqlmodel import Session

from adapter.eodhd.exchange_adapter import ExchangeAdapter
from adapter.restcountries.restcountries_adapter import RESTCountriesAdapter
from client.eodhd.eodhd_client import EODHDClient
from client.restcountries.restcountries_client import RESTCountriesClient
from database.database import Database
from manager.continent.continent_manager import ContinentManager
from manager.country.country_manager import CountryManager
from manager.currency.currency_manager import CurrencyManager
from manager.exchange.exchange_manager import ExchangeManager
from seeder.eodhd.eodhd_seeder import EODHDSeeder
from seeder.restcountries.restcountries_seeder import RESTCountriesSeeder


async def seed():
    database_ = Database()
    database_.create_tables(drop_all=True)

    restcountries_client = RESTCountriesClient()
    eodhd_client = EODHDClient()

    restcountries_adapter = RESTCountriesAdapter()
    eodhd_exchange_adapter = ExchangeAdapter()

    with Session(database_.get_engine()) as session:
        country_manager_ = CountryManager(session)
        currency_manager_ = CurrencyManager(session)
        continent_manager_ = ContinentManager(session)
        exchange_manager_ = ExchangeManager(session)

        restcountries_seeder_ = RESTCountriesSeeder(restcountries_client, restcountries_adapter, country_manager_,
                                                    currency_manager_,
                                                    continent_manager_)

        eodhd_seeder_ = EODHDSeeder(eodhd_client, eodhd_exchange_adapter, country_manager_, currency_manager_,
                                    exchange_manager_)

        await restcountries_seeder_.seed_many()
        await eodhd_seeder_.seed_exchange()

        session.commit()


if __name__ == '__main__':
    asyncio.run(seed())
