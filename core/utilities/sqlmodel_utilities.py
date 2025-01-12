from typing import TypeVar, List

from sqlmodel import SQLModel

SQLModelBound = TypeVar("SQLModelBound", bound=SQLModel)


def distinct_items(list_a: List[SQLModelBound], list_b: List[SQLModelBound]) -> List[T]:
    unique_dict_ = {
        item.id: item for item in list_a + list_b if item.id is not None
    }

    return list(unique_dict_.values())
