from pydantic import BaseModel


class TickerSchema(BaseModel):
    code: str
    name: str
    type: str
    isin: str
