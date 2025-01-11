from typing import Optional

from pydantic import BaseModel, Field


class CurrencySchema(BaseModel):
    code: str
    name: Optional[str] = Field(default=None)
    symbol: Optional[str] = Field(default=None)
