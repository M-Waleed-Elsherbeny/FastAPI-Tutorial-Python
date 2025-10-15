from fastapi import FastAPI
import uvicorn
from enum import Enum

app = FastAPI()

items = [
    {
        "id": 1,
        "name": "book",
        "price": 100,
        "stock": True
    }, {
        "id": 2,
        "name": "shoes",
        "price": 200,
        "stock": True
    }, {
        "id": 3,
        "name": "laptop",
        "price": 1500,
        "stock": True
    }, {
        "id": 4,
        "name": "tv",
        "price": 2000,
        "stock": False
        },
    {
        "id": 5,
        "name": "phone",
        "price": 1000,
        "stock": True
    },
    {
        "id": 6,
        "name": "mouse",
        "price": 50,
        "stock": False
    }]


# /items?id=5
# /items?name=mouse
@app.get("/items")
async def list_items(
    start: int = 0, 
    end: int = 10,
    name: str = None,
    id: int = None,
    ):
    if id:
        item = next((item for item in items if item['id'] == id), None)
        if item:
            return item
        else:
            return {"message": f"id ({id}) not Not found"}
    if name:
        item = next((item for item in items if item['name'] == name), None)
        if not item:
            return {"message": f"Name ({name}) not found"}
        return item
    return items[start:end]


# /items/price?range=100
@app.get("/items/price")
async def get_price(range: int = None):
    sorted_items = sorted(items, key=lambda x:x["price"], reverse=True)
    if range:
        filter_items = [item for item in items if item['price'] <= range]
        return filter_items
    return sorted_items


# /items/stock?stock=false
@app.get("/items/stock")
async def in_stock(stock: bool = True):
    if not stock:
        return [item for item in items if item["stock"] == False ]
    else:
        return [item for item in items if item["stock"] == True ]
        
    



if __name__ == "__main__":
    uvicorn.run("Query_Parameters/main:app", reload=True)