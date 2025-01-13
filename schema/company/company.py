from typing import Optional

from pydantic import BaseModel, Field


class CompanySchema(BaseModel):
    name: str
    isin: str
    address: str
    primary_ticker: Optional[str] = Field(default=None)
    homepage: str
    logo_url: str
    employees: int
    description: str
    fiscal_year_end: str
