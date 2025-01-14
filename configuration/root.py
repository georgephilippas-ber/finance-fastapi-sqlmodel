from os import sep
from os.path import abspath

from enum import Enum

PROJECT_NAME: str = "finance-fastapi-sqlmodel"


class EnvironmentType(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


def project_root() -> str:
    path_elements_ = abspath(__file__).split(sep)
    project_root_index_ = path_elements_.index(PROJECT_NAME)

    return sep.join(path_elements_[:project_root_index_ + 1])


DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"
ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT

if __name__ == "__main__":
    print(project_root())
