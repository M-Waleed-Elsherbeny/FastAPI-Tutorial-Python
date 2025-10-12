from fastapi import FastAPI
import uvicorn

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