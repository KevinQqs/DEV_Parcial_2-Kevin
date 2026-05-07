from typing import List

from fastapi import FastAPI
from sqlmodel import select

from db import SessionDep, create_all_tables
from model import Dog, DogCreate, DogRead


app = FastAPI(
    lifespan=create_all_tables
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Crear perro
@app.post("/dogs", response_model=DogRead)
def create_dog(dog: DogCreate, session: SessionDep):

    db_dog = Dog.model_validate(dog)

    session.add(db_dog)
    session.commit()
    session.refresh(db_dog)

    return db_dog


# Obtener todos
@app.get("/dogs", response_model=List[DogRead])
def get_dogs(session: SessionDep):

    dogs = session.exec(
        select(Dog)
    ).all()

    return dogs


# Obtener por id
@app.get("/dogs/{dog_id}", response_model=DogRead)
def get_dog(dog_id: int, session: SessionDep):

    dog = session.get(Dog, dog_id)

    return dog