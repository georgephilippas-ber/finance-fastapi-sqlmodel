from typing import Optional
from datetime import date
from pydantic import BaseModel, Field, EmailStr, HttpUrl, field_validator
from pydantic_core.core_schema import ValidationInfo

import re

from configuration.security import PASSWORD_MINIMUM_LENGTH, PASSWORD_MAXIMUM_LENGTH


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    password: str = Field(min_length=PASSWORD_MINIMUM_LENGTH, max_length=PASSWORD_MAXIMUM_LENGTH)
    password_confirm: Optional[str] = Field(default=None)
    email: EmailStr()

    first_name: Optional[str] = Field(default=None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(default=None, min_length=1, max_length=50)
    birthdate: Optional[date] = Field(default=None)

    avatar_url: Optional[HttpUrl] = Field(default=None)

    @field_validator("password", mode="after")
    @classmethod
    def password_strength(cls, value: str) -> str:
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{PASSWORD_MINIMUM_LENGTH,PASSWORD_MAXIMUM_LENGTH}$".replace(
            'PASSWORD_MINIMUM_LENGTH', str(PASSWORD_MINIMUM_LENGTH)).replace('PASSWORD_MAXIMUM_LENGTH',
                                                                             str(PASSWORD_MAXIMUM_LENGTH))
        if not re.match(pattern, value):
            raise ValueError(
                f"Password must be {PASSWORD_MINIMUM_LENGTH}-{PASSWORD_MAXIMUM_LENGTH} characters long and contain at least one uppercase letter one lowercase letter, one number, and one special character (@, $, !, %, *, ?, &, or #).")
        return value

    @field_validator("password_confirm", mode="after")
    @classmethod
    def password_match(cls, value: Optional[str], info: ValidationInfo) -> Optional[str]:
        if value is not None and "password" in info.data and value != info.data["password"]:
            raise ValueError("Passwords do not match")
        else:
            return value
