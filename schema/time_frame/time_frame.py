from datetime import date
from typing import List, Dict, Callable, Tuple, Optional

from decimal import Decimal
from pydantic import BaseModel, Field


class TimeFrame(BaseModel):
    column_names: List[str] = Field(default_factory=list)
    frame: Dict[date, List[Decimal]] = Field(default_factory=dict)

    def __len__(self):
        return len(self.frame.keys())

    def get_frame(self) -> Dict[date, List[Decimal]]:
        return self.frame

    def get_value(self, record_date: date, column_name: str) -> Optional[Decimal]:
        index_ = self.column_names.index(column_name)

        return self.frame[record_date][index_]

    def get_column(self, column_name: str) -> Optional[List[Decimal]]:
        index_ = self.column_names.index(column_name)

        return [row_[index_] for row_ in self.frame.values()]

    def get_dates(self) -> List[date]:
        return list(self.frame.keys())

    def _add_column(self, column_name: str, values: List[Decimal]):
        self.column_names.append(column_name)

        for date_key, value in zip(self.frame.keys(), values):
            self.frame[date_key].append(value)

    def _binary_operator(self, column_names: Tuple[str, str], operation: Callable[[Decimal, Decimal], Decimal]) -> List[
        Decimal]:
        index_ = self.column_names.index(column_names[0]), self.column_names.index(column_names[1])

        values_ = []
        for row_ in self.frame.values():
            if row_[index_[0]] is not None and row_[index_[1]] is not None:
                values_.append(operation(row_[index_[0]], row_[index_[1]]))
            else:
                values_.append(None)

        return values_

    def calculate(self, new_column_name: str, columns: Tuple[str, str],
                  operation: Callable[[Decimal, Decimal], Decimal]):
        self._add_column(new_column_name, self._binary_operator(columns, operation))

    def columns(self) -> List[str]:
        return self.column_names
