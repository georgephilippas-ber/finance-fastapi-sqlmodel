from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from enum import Enum


class InstrumentType(str, Enum):
    COMMON_STOCK = "Common Stock"
    ETF = "ETF"

    @staticmethod
    def from_str(value: str) -> Optional[InstrumentType]:
        match value:
            case "Common Stock":
                return InstrumentType.COMMON_STOCK
            case "ETF":
                return InstrumentType.ETF
            case _:
                return None


class TickerSchema(BaseModel):
    code: str
    name: str
    type: str
    isin: str
