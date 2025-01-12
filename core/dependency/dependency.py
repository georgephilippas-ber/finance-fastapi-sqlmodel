from __future__ import annotations

from dataclasses import dataclass
from typing import List, Callable, Set, Optional


@dataclass
class Injectable:
    name: str
    enabled: bool
    callback: Callable[[str], None]
    dependencies: List[Injectable]


class CircularDependencyError(Exception):
    pass


class Resolver:
    _resolved_set: Set[str]
    _currently_processing_set: Set[str]

    _entry_list: List[Injectable]

    _debug: bool

    def __init__(self, entry_list: Optional[List[Injectable]] = None, *, debug: bool = False):
        self._resolved_set = set()
        self._currently_processing_set = set()

        self._entry_list = entry_list or []

        self._debug = debug

    def _clear(self):
        self._resolved_set.clear()
        self._currently_processing_set.clear()

    def _resolve(self, item: Injectable):
        if item.name in self._resolved_set:
            return

        if item.name in self._currently_processing_set:
            raise CircularDependencyError

        self._currently_processing_set.add(item.name)

        for dependency in item.dependencies:
            self._resolve(dependency)

        if item.enabled:
            if self._debug:
                print(f"executing {item.name}")
            item.callback(item.name)

        self._resolved_set.add(item.name)

        self._currently_processing_set.remove(item.name)

    def process(self):
        for item in self._entry_list:
            self._resolve(item)


def print_name(s):
    print(s)


if __name__ == '__main__':
    pass
