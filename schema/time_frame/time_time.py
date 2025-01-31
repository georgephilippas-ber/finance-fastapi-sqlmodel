from datetime import date
from typing import List, Dict

from pydantic import BaseModel, Field


class TimeFrame(BaseModel):
    column_names: List[str] = Field(default_factory=list)
    frame: Dict[date, List[float]] = Field(default_factory=dict)

    def data_points(self) -> int:
        return len(self.frame.keys())
