from pydantic import BaseModel


class GICSSchema(BaseModel):
    sector: str
    industry_group: str
    industry: str
    sub_industry: str


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
