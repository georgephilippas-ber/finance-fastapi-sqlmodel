from enum import Enum
from typing import Dict, Tuple, List, Any

from core.dependency.dependency import Resolver, Injectable


def compile_resolver(entities_dict: Dict[Enum, Tuple[bool, List[Any]]], debug: bool = True) -> Resolver:
    resolver_: Resolver = Resolver(debug=debug)

    for entry_ in entities_dict:
        injectable_ = Injectable(name=entry_.value, enabled=entities_dict[entry_][0], dependencies=[],
                                 callback=None)
        resolver_.add_injectable(injectable_)
        resolver_.add_dependencies(entry_.value, map(lambda entity_: resolver_.injectable_by_name(entity_.value),
                                                     entities_dict[entry_][1]))

    return resolver_
