from typing import Optional

from pydantic import BaseModel, Field


class ExchangeSchema(BaseModel):
    code: str
    name: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    currency: Optional[str] = Field(default=None)
    country_iso2: Optional[str] = Field(default=None)
    country_iso3: Optional[str] = Field(default=None)
