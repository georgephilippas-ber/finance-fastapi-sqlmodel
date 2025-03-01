from typing import Any, List
from abc import ABC, abstractmethod


class Adapter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def adapt(self, json_: Any) -> Any:
        pass

    def _preprocess_many(self, json_list_: List[Any]) -> List[Any]:
        return json_list_

    @abstractmethod
    def adapt_many(self, json_list_: List[Any]) -> List[Any]:
        pass
