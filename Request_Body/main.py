from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str                          # Required but can't be null
    discretion: str | None             # Required but can be pass string or null
    price: float                       # Required but can't be null
    tax: float | None = None           # Optional with default value = null

@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + (item.price * item.tax)
        item_dict.update({"total_price": price_with_tax})
    return item_dict







if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)