from abc import ABC

from sqlmodel.ext.asyncio.session import AsyncSession


class Manager(ABC):
    _session: AsyncSession

    def __init__(self, session: AsyncSession):
        self._session = session
