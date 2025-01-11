from sqlmodel import SQLModel, Field


class CountryContinent(SQLModel, table=True):
    country_id: int = Field(foreign_key="country.id", primary_key=True)
    continent_id: int = Field(foreign_key="continent.id", primary_key=True)
