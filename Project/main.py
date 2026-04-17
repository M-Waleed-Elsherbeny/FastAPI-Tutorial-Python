from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session

from schemas.client_model import ClientRequest, ClientResponse
from database import Client
from dependencies import get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/api/get-clients", response_model=ClientResponse)
async def get_clients(db: Session = Depends(get_db)):
    clients = db.query(Client).all()
    return {"client": clients}


@app.post("/api/add-client")
async def new_client(client: ClientRequest, db: Session = Depends(get_db)):
    new_client = Client(
        name=client.name,
        post_url=client.post_url,
        price=client.price,
        day_number=client.day_number,
        is_finished=client.is_finished
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return {"msg": "Client added successfully", "new_client": new_client}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)