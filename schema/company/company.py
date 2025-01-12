from pydantic import BaseModel


class CompanySchema(BaseModel):
    name: str
    isin: str
    address: str
    primary_ticker: str
    homepage: str
    logo_url: str
    employees: int
    description: str
    fiscal_year_end: str
