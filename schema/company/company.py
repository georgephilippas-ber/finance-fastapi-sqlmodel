from pydantic import BaseModel


class GICSSchema(BaseModel):
    sector_id: str
    sector: str

    industry_group_id: str
    industry_group: str

    industry_id: str
    industry: str

    sub_industry_id: str
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
