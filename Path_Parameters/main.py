from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()

# include_in_schema=False ===> hide from docs
@app.get("/users/1", include_in_schema=False)
async def admin_user():
    return {"message": "The Admin User"}



@app.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users-name/{user_name}", tags=["Users"])
async def get_user_name(user_name: str):
    return {"message": f"Hello {user_name}"} 

@app.get("/items/{item_id}", tags=["Items"])
async def read_user_item(item_id: str):
    return { "item_id": item_id}


class ModelName(str, Enum):
    admin = 1
    manager = 2
    user = 3


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name.name}


if __name__ == "__main__":
    uvicorn.run("Path_Parameters/main:app", reload=True)