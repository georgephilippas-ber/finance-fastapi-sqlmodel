from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


class GICSSector(SQLModel, table=True):
    __tablename__ = 'GICSSector'
    id: Optional[str] = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)

    industry_groups: List["GICSIndustryGroup"] = Relationship(back_populates="sector")
    industries: List["GICSIndustry"] = Relationship(back_populates="sector")
    sub_industries: List["GICSSubIndustry"] = Relationship(back_populates="sector")

    companies: List["Company"] = Relationship(back_populates="gics_sector")


class GICSIndustryGroup(SQLModel, table=True):
    __tablename__ = 'GICSIndustryGroup'

    id: Optional[str] = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)

    sector_id: str = Field(foreign_key="GICSSector.id")
    sector: GICSSector = Relationship(back_populates="industry_groups")

    industries: List["GICSIndustry"] = Relationship(back_populates="industry_group")
    sub_industries: List["GICSSubIndustry"] = Relationship(back_populates="industry_group")

    companies: List["Company"] = Relationship(back_populates="gics_industry_group")


class GICSIndustry(SQLModel, table=True):
    __tablename__ = 'GICSIndustry'

    id: Optional[str] = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)

    sector_id: str = Field(foreign_key="GICSSector.id")
    sector: GICSSector = Relationship(back_populates="industries")

    industry_group_id: str = Field(foreign_key="GICSIndustryGroup.id")
    industry_group: GICSIndustryGroup = Relationship(back_populates="industries")

    sub_industries: List["GICSSubIndustry"] = Relationship(back_populates="industry")

    companies: List["Company"] = Relationship(back_populates="gics_industry")


class GICSSubIndustry(SQLModel, table=True):
    __tablename__ = 'GICSSubIndustry'

    id: Optional[str] = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)

    sector_id: str = Field(foreign_key="GICSSector.id")
    sector: GICSSector = Relationship(back_populates="sub_industries")

    industry_group_id: str = Field(foreign_key="GICSIndustryGroup.id")
    industry_group: GICSIndustryGroup = Relationship(back_populates="sub_industries")

    industry_id: str = Field(foreign_key="GICSIndustry.id")
    industry: GICSIndustry = Relationship(back_populates="sub_industries")

    companies: List["Company"] = Relationship(back_populates="gics_subindustry")
