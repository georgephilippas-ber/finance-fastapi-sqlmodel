from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class CountryNameSchema(BaseModel):
    common: str
    official: str


class CountryISOCodeSchema(BaseModel):
    cca2: Optional[str] = Field(default=None)
    cca3: Optional[str] = Field(default=None)


class LocationSchema(BaseModel):
    latitude: float
    longitude: float


class CountrySchema(BaseModel):
    name: Optional[CountryNameSchema] = Field(default=None)
    iso_code: CountryISOCodeSchema
    location: Optional[LocationSchema] = Field(default=None)

    capital: Optional[str] = Field(default=None)
    population: Optional[int] = Field(default=None)
    flag_url: Optional[str] = Field(default=None)
