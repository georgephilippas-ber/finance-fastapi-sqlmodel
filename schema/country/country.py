from pydantic import BaseModel
from typing import List


class CountryNameSchema(BaseModel):
    common: str
    official: str


class CountryISOCodeSchema(BaseModel):
    cca2: str
    cca3: str


class CurrencySchema(BaseModel):
    code: str
    name: str
    symbol: str


class LocationSchema(BaseModel):
    latitude: float
    longitude: float


class CountrySchema(BaseModel):
    name: CountryNameSchema
    iso_code: CountryISOCodeSchema
    currency_list: List[CurrencySchema]
    location: LocationSchema

    capital: str
    population: int
    continents: List[str]
    flag_url: str