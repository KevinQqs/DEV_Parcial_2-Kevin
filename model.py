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

class Dog(SQLModel, table = True):
    __tablename__ = "Dogs"

    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )

