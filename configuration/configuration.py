from os import sep
from os.path import abspath

PROJECT_NAME: str = "finance-fastapi-sqlmodel"


def project_root() -> str:
    path_elements_ = abspath(__file__).split(sep)
    project_root_index_ = path_elements_.index(PROJECT_NAME)

    return sep.join(path_elements_[:project_root_index_ + 1])


DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"

COMPANY_SAMPLE_SIZE: int = 10

if __name__ == "__main__":
    print(project_root())
