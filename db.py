import os

from sqlmodel import Session, create_engine, SQLModel
from fastapi import FastAPI, Depends
from typing import Annotated
from dotenv import load_dotenv



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True
)


def create_all_tables(app: FastAPI):
    if os.getenv("ENV") == "dev":
        SQLModel.metadata.create_all(engine)
    yield


def get_session() -> Session:
    with Session(engine) as session:
        yield


SessionDep = Annotated[Session, Depends(get_session)]