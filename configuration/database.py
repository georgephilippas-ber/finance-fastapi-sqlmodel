from core.utilities.root import project_root
from os.path import join

from configuration.environment import ENVIRONMENT
from configuration.project import PROJECT_NAME
from core.utilities.root import project_root

DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"

# DATABASE_URL: str = f"sqlite:///{join(project_root(), "database", "files", f"{PROJECT_NAME}-{ENVIRONMENT.value}-sqlite.db")}"

# DATABASE_URL: str = f"duckdb:///{join(project_root(), "database", "files", f"{PROJECT_NAME}-{ENVIRONMENT.value}-duckdb.db")}"

# DATABASE_URL: str = f"duckdb:///:memory:"
