from sqlmodel import SQLModel, Field


class Exchange(SQLModel, table=True):
    code: str = Field(primary_key=True)

    name: str
