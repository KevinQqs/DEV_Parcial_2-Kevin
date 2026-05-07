from typing import List

from fastapi import FastAPI, HTTPException, status
from sqlmodel import select

from db import SessionDep, create_all_tables

from model import (
    Dog,
    DogCreate,
    DogRead,
    DogUpdate
)

app = FastAPI(
    lifespan=create_all_tables
)


@app.get(
    "/",
    status_code=status.HTTP_200_OK
)
def root():
    return {"message": "API funcionando"}


@app.get(
    "/dogs",
    response_model=List[DogRead],
    status_code=status.HTTP_200_OK
)
def get_dogs(session: SessionDep):

    dogs = session.exec(
        select(Dog)
    ).all()

    return dogs


@app.get(
    "/dogs/{dog_id}",
    response_model=DogRead,
    status_code=status.HTTP_200_OK
)
def get_dog(
        dog_id: int,
        session: SessionDep
):

    dog = session.get(Dog, dog_id)

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perro no encontrado"
        )

    return dog


@app.post(
    "/dogs",
    response_model=DogRead,
    status_code=status.HTTP_201_CREATED
)
def create_dog(
        dog: DogCreate,
        session: SessionDep
):

    db_dog = Dog.model_validate(dog)

    session.add(db_dog)
    session.commit()
    session.refresh(db_dog)

    return db_dog


@app.put(
    "/dogs/{dog_id}",
    response_model=DogRead,
    status_code=status.HTTP_200_OK
)
def update_dog(
        dog_id: int,
        dog_update: DogUpdate,
        session: SessionDep
):

    db_dog = session.get(Dog, dog_id)

    if not db_dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perro no encontrado"
        )

    dog_data = dog_update.model_dump(
        exclude_unset=True
    )

    for key, value in dog_data.items():
        setattr(db_dog, key, value)

    session.add(db_dog)
    session.commit()
    session.refresh(db_dog)

    return db_dog

@app.delete(
    "/dogs/{dog_id}",
    status_code=status.HTTP_200_OK
)
def delete_dog(
        dog_id: int,
        session: SessionDep
):

    dog = session.get(Dog, dog_id)

    if not dog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Perro no encontrado"
        )

    session.delete(dog)
    session.commit()

    return {
        "message": "Perro eliminado correctamente"
    }