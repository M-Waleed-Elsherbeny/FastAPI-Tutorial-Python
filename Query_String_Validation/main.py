from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# http://127.0.0.1:8000/validate?name=Mohammed
@app.get('/validate')
def get_item(name: str = Query(default = ..., max_length=50, min_length=3, regex="^[a-zA-Z\s]+$")):
    return {"name": name} # default = ... ==> this field is required

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)