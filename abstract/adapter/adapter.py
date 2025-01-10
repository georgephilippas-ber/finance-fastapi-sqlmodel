from typing import Any, List
from abc import ABC, abstractmethod


class Adapter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def adapt(self, json_: Any) -> Any:
        pass

    @abstractmethod
    def adapt_many(self, json_list_: List[Any]) -> List[Any]:
        pass
