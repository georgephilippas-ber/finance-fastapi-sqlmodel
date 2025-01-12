from typing import Optional

from pydantic import BaseModel, Field


class GICSSchema(BaseModel):
    sector_id: Optional[int] = Field(default=None)
    sector: str

    industry_group_id: Optional[int] = Field(default=None)
    industry_group: str

    industry_id: Optional[int] = Field(default=None)
    industry: str

    sub_industry_id: Optional[int] = Field(default=None)
    sub_industry: str
