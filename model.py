from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Dog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str
    created: datetime = Field(default_factory=datetime.now)

