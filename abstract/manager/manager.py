from abc import ABC, abstractmethod
from typing import Optional, TypeVar, TypedDict, Dict, Any, Iterable

from pydantic import BaseModel
from sqlmodel import SQLModel, Session

BaseModelBound = TypeVar("BaseModelBound", bound=BaseModel)
SQLModelBound = TypeVar("SQLModelBound", bound=SQLModel)


class Manager(ABC):
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    @abstractmethod
    async def retrieve_unique(self, schema: BaseModelBound | Iterable[BaseModelBound]) -> Optional[SQLModelBound]:
        return None

    @abstractmethod
    async def persist(self, schema: BaseModelBound, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[
        SQLModelBound]:
        pass
