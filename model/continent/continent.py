from typing import List

from typing import Optional
from uuid import uuid4

from sqlalchemy import Column, Integer, Sequence
from sqlmodel import SQLModel, Field, Relationship

from model.link.country_continent.country_continent import CountryContinent


class Continent(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(uuid4().hex), primary_key=True))

    name: str = Field(nullable=False, unique=True)

    country_list: List["Country"] = Relationship(back_populates="continent_list", link_model=CountryContinent)
