from fastapi import FastAPI
import uvicorn
from enum import Enum
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post-data")
async def post_data():
    return {"message": "this is a post request"}
@app.post("/post-data", deprecated=True)
async def post_data_deprecated():
    return {"message": "this is a post request"}

@app.put("/put-data", description="this is a put request")
async def put_data():
    return {"message": "this is a put request"}



@app.get("/users", tags=["Users"])
async def list_of_users():
    return {"message": "list of users"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)