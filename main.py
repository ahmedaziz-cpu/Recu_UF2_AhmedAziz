from fastapi import FastAPI
from services.user import (
    delete_user
)

app = FastAPI()



@app.delete("/users/{user_id}", response_model=dict)
async def delete_user_endpoint(user_id: int):

    success = delete_user(user_id)
    if not success:
        print("no s'ha trobat")
    return {"deleted": True}



