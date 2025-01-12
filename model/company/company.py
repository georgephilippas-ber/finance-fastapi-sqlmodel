from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from model.GICS.GICS import GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry


class Company(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    gics_sector_id: Optional[int] = Field(foreign_key="GICSSector.id")
    gics_sector: Optional[GICSSector] = Relationship(back_populates="companies")

    gics_industry_group_id: Optional[int] = Field(foreign_key="GICSIndustryGroup.id")
    gics_industry_group: Optional[GICSIndustryGroup] = Relationship(back_populates="companies")

    gics_industry_id: Optional[int] = Field(foreign_key="GICSIndustry.id")
    gics_industry: Optional[GICSIndustry] = Relationship(back_populates="companies")

    gics_subindustry_id: Optional[int] = Field(foreign_key="GICSSubIndustry.id")
    gics_subindustry: Optional[GICSSubIndustry] = Relationship(back_populates="companies")
