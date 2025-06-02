from fastapi import FastAPI
from services.user import (
    create_user,
    get_user_by_id
)


app = FastAPI()


@app.get("/users/{user_id}", response_model=dict)
async def read_user(user_id: int):
    user = get_user_by_id(user_id)

    return user

@app.post("/users", response_model=dict)
async def create_user_endpoint(
    nom: str, email: str, cognom: str, descripcio: str, curs: str, ano: int, calle: str, cp: int, password: str
):
    new_user = create_user(nom, email, cognom, descripcio, curs, ano, calle, cp, password)
    return new_user


