from fastapi import FastAPI
import uvicorn

from database import connect, session


app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)