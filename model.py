from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


# Base
class DogBase(SQLModel):
    name: str
    size: str
    dangerous: bool
    sterilized: bool
    breed: str


# Para crear
class DogCreate(DogBase):
    pass


# Para leer
class DogRead(DogBase):
    id: int
    created: datetime


# Modelo de tabla
class Dog(DogBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created: datetime = Field(default_factory=datetime.now)