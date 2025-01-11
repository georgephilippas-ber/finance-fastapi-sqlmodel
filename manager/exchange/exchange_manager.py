from sqlalchemy.ext.asyncio import AsyncSession

from abstract.manager.manager import Manager


class ExchangeManager(Manager):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
