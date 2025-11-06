from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
Path ==> For Path Parameters
... ==> required
gt ==> greater than
lt ==> less than
ge ==> greater than or equal to
le ==> less than or equal to
"""

#http://127.0.0.1:8000/item/20
@app.get("/item/{item_id}")
async def get_item(
    item_id: float = Path(..., 
                        ge=1, le=100, 
                        title="Item ID", 
                        description="The ID of the item to get Must be From 1 : 100",
                        ),
    ):
    return {"item_id": item_id}

"""
Query ==> For Query Parameters
... ==> required
gt ==> greater than
lt ==> less than
ge ==> greater than or equal to
le ==> less than or equal to
"""


# http://127.0.0.1:8000/items/?item_name=Shose&item_id=10
@app.get("/items/", tags=["Items"], description="Get an Item")
async def get_items(
    item_id: float = Query(..., 
                        ge=1, le=100, 
                        title="Item ID", 
                        description="The ID of the item to get Must be From 1 : 100",
                        ),
    item_name: str = Query(..., 
                        min_length=3, 
                        max_length=50, 
                        regex=r"^[a-zA-Z\s]+$", 
                        title="Item Name", 
                        description="The name of the item to get",
                        ),):
    return {"item_id": item_id, "item_name": item_name}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)