from pydantic import BaseModel
from typing import List


class CountryNameSchema(BaseModel):
    common: str
    official: str


class CountryISOCodeSchema(BaseModel):
    cca2: str
    cca3: str


class LocationSchema(BaseModel):
    latitude: float
    longitude: float


class CountrySchema(BaseModel):
    name: CountryNameSchema
    iso_code: CountryISOCodeSchema
    location: LocationSchema

    capital: str
    population: int
    flag_url: str
