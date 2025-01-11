from os import sep
from os.path import abspath
from typing import List

PROJECT_NAME: str = "finance-fastapi-sqlmodel"


def project_root() -> str:
    path_elements_ = abspath(__file__).split(sep)
    project_root_index_ = path_elements_.index(PROJECT_NAME)

    return sep.join(path_elements_[:project_root_index_ + 1])


DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"

EODHD_DEMO: bool = False

EODHD_EXCHANGES: List[str] = ["XETRA", "F"]
EODHD_OVERRIDE_TICKERS = [("AAPL", "NASDAQ"), ("AMZN", "NASDAQ"), ("MSFT", "NASDAQ"), ("TSLA", "NASDAQ")]

if __name__ == "__main__":
    print(project_root())
