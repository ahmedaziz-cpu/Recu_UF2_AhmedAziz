from fastapi import FastAPI
from services.user import (
    delete_user,
    create_user,
    get_user_by_id,
    update_user
)

app = FastAPI()



@app.delete("/users/{user_id}", response_model=dict)
async def delete_user_endpoint(user_id: int):

    success = delete_user(user_id)
    if not success:
        print("no s'ha trobat")
    return {"deleted": True}



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

@app.put("/users/{user_id}", response_model=dict)
async def update_user_endpoint(user_id: int, name: str, email: str):

    updated = update_user(user_id, name, email)
    return updated



