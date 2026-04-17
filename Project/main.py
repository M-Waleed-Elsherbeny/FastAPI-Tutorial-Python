from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session

from database import session, Client
from dependencies import get_db

# def add_user_to_db():
#     with session as s:
#         user1 = User(
#             name = "Mohammed",
#             age = 35
#         )
#         user2 = User(
#             name = "Akram",
#             age = 30
#         )
#         s.add_all([user1, user2])
#         s.commit()

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/api/users", tags=["User"])
async def  get_all_users():
    # await add_user_to_db()
    return session.query(Client).all()




@app.get("/api/users/{id}", tags=["Depends"])
async def  get_all_users(id: int, db: Session = Depends(get_db)):
    return db.query(Client).filter(Client.id == id).first()

@app.post("/api/add-user", tags=["Add User"])
async def  add_user(user: Client, db: Session = Depends(get_db)):
    await db.add(user)        
    return user


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)