from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Dict, Any

from poetry.console.commands import self
from pydantic import BaseModel
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

BaseModelBound = TypeVar("BaseModelBound", bound=BaseModel)
SQLModelBound = TypeVar("SQLModelBound", bound=SQLModel)


class Manager(ABC):
    _session: AsyncSession

    def __init__(self, session: AsyncSession):
        self._session = session

    @abstractmethod
    async def retrieve_unique(self, schema: BaseModelBound) -> Optional[SQLModelBound]:
        return None

    @abstractmethod
    async def persist(self, schema: BaseModelBound, foreign_keys: Optional[Dict[str, Any]] = None) -> Optional[
        SQLModelBound]:
        pass
