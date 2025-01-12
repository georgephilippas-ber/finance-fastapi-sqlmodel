from enum import Enum
from typing import Dict

from core.dependency.dependency import Resolver, Injectable


class Entity(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    EXCHANGE = "exchange"
    TICKER = "ticker"


SEED_ENTITIES: Dict[Entity, bool] = {
    Entity.COUNTRY_CURRENCY: True,
    Entity.EXCHANGE: True,
    Entity.TICKER: True
}


def compile_seed_resolver() -> Resolver:
    country_currency_injectable_ = Injectable(name=Entity.COUNTRY_CURRENCY.value,
                                              enabled=SEED_ENTITIES[Entity.COUNTRY_CURRENCY], dependencies=[],
                                              callback=None)

    exchange_injectable_ = Injectable(name=Entity.EXCHANGE.value, enabled=SEED_ENTITIES[Entity.EXCHANGE],
                                      dependencies=[country_currency_injectable_], callback=None)

    ticker_injectable_ = Injectable(name=Entity.TICKER.value, enabled=SEED_ENTITIES[Entity.TICKER],
                                    dependencies=[exchange_injectable_], callback=None)

    return Resolver([country_currency_injectable_, exchange_injectable_, ticker_injectable_])
