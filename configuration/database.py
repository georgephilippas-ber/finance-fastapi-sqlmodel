from enum import Enum, auto
from os.path import join

from configuration.environment import ENVIRONMENT
from configuration.project import PROJECT_NAME
from core.environment.environment import is_running_in_docker
from core.utilities.root import project_root


class DBMSType(Enum):
    DUCKDB = auto()
    MYSQL = auto()
    POSTGRESQL = auto()


DBMS: DBMSType = DBMSType.MYSQL

if is_running_in_docker():
    DBMS: DBMSType = DBMSType.DUCKDB

if DBMS == DBMSType.MYSQL:
    DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"
elif DBMS == DBMSType.POSTGRESQL:
    DATABASE_URL: str = f"postgresql+psycopg2://root:development@localhost:5432/${PROJECT_NAME.replace('-', '_')}"
elif DBMS == DBMSType.DUCKDB:
    DATABASE_URL: str = f"duckdb:///{join(project_root(), "database", "files", f"{PROJECT_NAME}-{ENVIRONMENT.value}-duckdb.db")}"

SESSION_DATABASE_FILENAME: str = join(project_root(), "database", "files", "session.db")
