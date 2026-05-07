from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class DogBase(SQLModel):
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str


class DogCreate(DogBase):
    pass


class DogUpdate(SQLModel):
    name: Optional[str] = None
    size: Optional[str] = None
    dangerous: Optional[bool] = None
    sterilized: Optional[bool] = None
    breed: Optional[str] = None


class DogRead(DogBase):
    id: int
    created: datetime


class Dog(DogBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)