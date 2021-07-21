from datetime import datetime, date
from enum import Enum
from pydantic import BaseModel, validator


class SideEnum(Enum):
    BUY = "buy"
    SELL = "sell"


class Order(BaseModel):
    isin: str
    limit_price: float
    side: SideEnum
    valid_until: int
    quantity: int

    @validator("isin")
    def isin_validate(cls, v):
        if len(v) != 12:
            raise ValueError("isin must be 12 characters")
        return v

    @validator("limit_price")
    def limit_price_validate(cls, v):
        if v <= 0:
            raise ValueError("Limit price must be greater than zero")
        return v

    @validator("quantity")
    def quantity_validate(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be greater than zero")
        return v
