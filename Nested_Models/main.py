from fastapi import FastAPI
import uvicorn
from models.product_model import Product


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-to-product")
async def add_product(product: Product):
    result = {"product": product}
    return [result]

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)