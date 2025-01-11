from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from configuration.configuration import DATABASE_URL


class Database:
    _connection_string: str
    _async_engine: AsyncEngine

    def __init__(self, connection_string: str = DATABASE_URL):
        self._connection_string = connection_string

        self._async_engine = create_async_engine(connection_string)

    def get_async_engine(self) -> AsyncEngine:
        return self._async_engine

    async def create_tables(self, *, drop_all: bool = False):
        async with self._async_engine.begin() as connection:
            if drop_all:
                await connection.run_sync(SQLModel.metadata.drop_all)
            await connection.run_sync(SQLModel.metadata.create_all)
