from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Dict

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
    async def persist(self, schema: BaseModelBound, keys: Optional[Dict] = None) -> Optional[SQLModelBound]:
        pass
