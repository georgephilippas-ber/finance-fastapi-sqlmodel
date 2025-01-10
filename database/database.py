from sqlmodel import create_engine
from sqlalchemy.engine.base import Engine

from configuration.configuration import DATABASE_URL


class Database:
    _connection_string: str
    _engine: Engine

    def __init__(self, connection_string: str = DATABASE_URL):
        self._connection_string = connection_string

        self._engine = create_engine(connection_string)

    def get_engine(self) -> Engine:
        return self._engine
