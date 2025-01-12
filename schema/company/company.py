from pydantic import BaseModel


class GICSSchema(BaseModel):
    sector_id: int
    sector: str

    industry_group_id: int
    industry_group: str

    industry_id: int
    industry: str

    sub_industry_id: int
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
