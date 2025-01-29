from enum import Enum, auto
from os.path import join

from configuration.environment import ENVIRONMENT
from configuration.project import PROJECT_NAME
from core.utilities.root import project_root


class DBMSType(Enum):
    DUCKDB_FILE = auto()
    DUCKDB_MEMORY = auto()
    MYSQL = auto()
    POSTGRESQL = auto()


DBMS: DBMSType = DBMSType.DUCKDB_MEMORY

if DBMS == DBMSType.MYSQL:
    DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"
elif DBMS == DBMSType.POSTGRESQL:
    DATABASE_URL: str = f"postgresql+psycopg2://root:development@localhost:5432/${PROJECT_NAME.replace('-', '_')}"
elif DBMS == DBMSType.DUCKDB_FILE:
    DATABASE_URL: str = f"duckdb:///{join(project_root(), "database", "files", f"{PROJECT_NAME}-{ENVIRONMENT.value}-duckdb.db")}"
elif DBMS == DBMSType.DUCKDB_MEMORY:
    DATABASE_URL: str = f"duckdb:///:memory:"

SESSION_DATABASE_FILENAME: str = join(project_root(), "database", "files", "session.db")
