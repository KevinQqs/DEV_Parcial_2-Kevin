from typing import List

from fastapi import FastAPI
from sqlmodel import select

from db import SessionDep, create_all_tables
from models import Dog


app = FastAPI(
    lifespan=create_all_tables
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/dogs", response_model=Dog)
def create_dog(dog: Dog, session: SessionDep):

    session.add(dog)
    session.commit()
    session.refresh(dog)

    return dog


@app.get("/dogs", response_model=List[Dog])
def get_dogs(session: SessionDep):

    dogs = session.exec(
        select(Dog)
    ).all()

    return dogs


@app.get("/dogs/{dog_id}", response_model=Dog)
def get_dog(dog_id: int, session: SessionDep):

    dog = session.get(Dog, dog_id)

    return dog