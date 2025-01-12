from enum import Enum
from typing import Dict, Tuple, List

from core.dependency.dependency import Resolver, Injectable


class Entity(str, Enum):
    COUNTRY_CURRENCY = "country_currency"
    EXCHANGE = "exchange"
    TICKER = "ticker"


SEED_ENTITIES: Dict[Entity, Tuple[bool, List[Entity]]] = {
    Entity.COUNTRY_CURRENCY: (True, []),
    Entity.EXCHANGE: (True, [Entity.COUNTRY_CURRENCY]),
    Entity.TICKER: (True, [Entity.EXCHANGE])
}


def compile_seed_resolver() -> Resolver:
    resolver_: Resolver = Resolver()

    for entry_ in SEED_ENTITIES:
        injectable_ = Injectable(name=entry_.value, enabled=SEED_ENTITIES[entry_][0], dependencies=[],
                                 callback=None)
        resolver_.add_injectable(injectable_)
        resolver_.add_dependencies(entry_.value, map(lambda entity_: resolver_.injectable_by_name(entity_.value),
                                                     SEED_ENTITIES[entry_][1]))

    return resolver_
