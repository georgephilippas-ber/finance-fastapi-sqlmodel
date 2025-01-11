from sqlalchemy import Engine
from sqlmodel import create_engine, SQLModel
from configuration.configuration import DATABASE_URL


class Database:
    _connection_string: str
    _engine: Engine

    def __init__(self, connection_string: str = DATABASE_URL):
        self._connection_string = connection_string

        self._engine = create_engine(connection_string, echo=False)

    def get_engine(self) -> Engine:
        return self._engine

    def create_tables(self, *, drop_all: bool = False):
        if drop_all:
            SQLModel.metadata.drop_all(self._engine)

        SQLModel.metadata.create_all(self._engine)
