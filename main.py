from fastapi import FastAPI
from services.user import (create_user)

app = FastAPI()


@app.post("/users", response_model=dict)
async def create_user_endpoint(
    nom: str, email: str, cognom: str, descripcio: str, curs: str, ano: int, calle: str, cp: int, password: str
):
    new_user = create_user(nom, email, cognom, descripcio, curs, ano, calle, cp, password)
    return new_user


