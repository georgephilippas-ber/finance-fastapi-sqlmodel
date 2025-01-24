from datetime import date
from typing import Optional
from uuid import uuid4

from sqlalchemy import Column, Integer, Sequence
from sqlmodel import SQLModel, Field

from pathlib import Path


class User(SQLModel, table=True):
    id: Optional[int] = Field(sa_column=Column(Integer, Sequence(Path(__file__).stem), primary_key=True))

    username: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    avatar_url: Optional[str] = Field(nullable=True)

    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    birthdate: Optional[date] = Field(default=None)
