from pydantic import BaseModel


class ContinentSchema(BaseModel):
    name: str
