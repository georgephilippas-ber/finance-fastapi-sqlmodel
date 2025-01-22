from typing import List

from sqlalchemy import Engine
from sqlalchemy.sql.ddl import CreateTable
from sqlmodel import create_engine, SQLModel, Session
from configuration.database import DATABASE_URL

import model.comprehensive


class Database:
    _connection_string: str
    _engine: Engine

    def __init__(self, connection_string: str = DATABASE_URL):
        self._connection_string = connection_string

        self._engine = create_engine(connection_string, echo=False)

    def get_engine(self) -> Engine:
        print(self._engine.pool.status())
        return self._engine

    def create_tables(self, *, drop_all: bool = False):
        if drop_all:
            SQLModel.metadata.drop_all(self._engine)

        SQLModel.metadata.create_all(self._engine)

    def create_session(self) -> Session:
        return Session(self._engine)

    def get_create_tables_sql_query(self) -> str:
        models_ = SQLModel.metadata.tables.values()

        statements_: List[str] = []

        for model_ in models_:
            model_create_sql_statement_ = str(CreateTable(model_).compile(self.get_engine())).replace("\n", "").replace(
                "\t", "").strip()
            statements_.append(model_create_sql_statement_)

        return "; ".join(statements_)


if __name__ == '__main__':
    pass
