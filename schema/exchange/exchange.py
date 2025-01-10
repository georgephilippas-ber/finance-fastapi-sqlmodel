from pydantic import BaseModel


class ExchangeSchema(BaseModel):
    code: str
    name: str
    country: str
    currency: str
    country_iso2: str
    country_iso3: str
