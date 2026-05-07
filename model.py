from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


# BASE
class DogBase(SQLModel):
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str


# CREATE
class DogCreate(DogBase):
    pass


# UPDATE
class DogUpdate(SQLModel):
    name: Optional[str] = None
    size: Optional[str] = None
    dangerous: Optional[bool] = None
    sterilized: Optional[bool] = None
    breed: Optional[str] = None


# READ
class DogRead(DogBase):
    id: int
    created: datetime


# TABLE
class Dog(DogBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)