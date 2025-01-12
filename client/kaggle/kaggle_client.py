from typing import List, Dict, Any, Literal

from pandas import DataFrame, read_csv
from os.path import join

from configuration.configuration import project_root


class KaggleGICSClient:
    __dataframe: DataFrame
    __version: Literal['2018', '2023']

    def __init__(self, version: Literal['2018', '2023'] = '2023'):
        self.__version = version
        self.__dataframe = self.read_gics()

    def read_gics(self) -> DataFrame:
        return read_csv(
            join(project_root(), "resources", "GICS", f"gics-map-{self.__version}.csv"))

    def columns(self) -> List[str]:
        return list(self.__dataframe.columns)

    def get_dataframe(self) -> DataFrame:
        return self.__dataframe

    def get_records(self) -> List[Dict[str, Any]]:
        return self.__dataframe.to_dict(orient="records")


if __name__ == "__main__":
    pass
