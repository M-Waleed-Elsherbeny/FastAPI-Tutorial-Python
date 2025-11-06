from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

# http://127.0.0.1:8000/items/25?q=hello
@app.put("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(..., gt=0, le=100, title="Item Id", description="This is item id"),
    q: str = Query(..., min_length=3, max_length=50, title="Query", description="The description to search for."),
    item: Item | None = None,
    user: User | None,
    age: float = Body(...)
    ):
    result: dict = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item :
        result.update({"item": [item]})
    if user:
        result.update({"user": [user]})
    if age:
        result.update({"age": age})
    return result


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)