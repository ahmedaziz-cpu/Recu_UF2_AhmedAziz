from fastapi import FastAPI
from services.user import (
    update_user
)

app = FastAPI()


@app.put("/users/{user_id}", response_model=dict)
async def update_user_endpoint(user_id: int, name: str, email: str):

    updated = update_user(user_id, name, email)
    return updated

