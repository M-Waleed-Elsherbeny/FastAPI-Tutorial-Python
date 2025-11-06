from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


class Item(BaseModel):
    name: str = Field(..., title="Item Name")
    description: str | None = None
    price: float = Field(..., gt=0, title="Item Price", description="The Price Of Item")

@app.put("/item/{item_id}")
async def update_item(
        item_id: int,
        item: Item
    ):
    return {"item_id": item_id, "item": item}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)