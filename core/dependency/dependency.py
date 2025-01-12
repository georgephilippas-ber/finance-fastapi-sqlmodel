from __future__ import annotations

import inspect
from dataclasses import dataclass
from typing import List, Callable, Set, Optional, Never, Awaitable


@dataclass
class Injectable:
    name: str
    enabled: bool
    callback: Optional[Callable[[], Awaitable[None]]]
    dependencies: List[Injectable]


class CircularDependencyError(Exception):
    pass


class DependencyNotFoundError(Exception):
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

    async def _resolve(self, item: Injectable):
        if item.name in self._resolved_set:
            return

        if item.name in self._currently_processing_set:
            raise CircularDependencyError

        self._currently_processing_set.add(item.name)

        for dependency in item.dependencies:
            await self._resolve(dependency)

        if item.enabled:
            if self._debug:
                print(f"executing {item.name}")
            if inspect.iscoroutinefunction(item.callback):
                await item.callback()
            else:
                item.callback()

        self._resolved_set.add(item.name)

        self._currently_processing_set.remove(item.name)

    def add_callback(self, name: str, callback: Callable[[], Awaitable[None]]):
        for entry_ in self._entry_list:
            if entry_.name == name:
                entry_.callback = callback
                return

        raise DependencyNotFoundError

    async def process(self):
        for item in self._entry_list:
            await self._resolve(item)


def print_name(s):
    print(s)


if __name__ == '__main__':
    pass
