from fastapi import FastAPI
import uvicorn

from database import connect, session, User

# def add_user_to_db():
#     with session as s:
#         user1 = User(
#             name = "Mohammed",
#             age = 35
#         )
#         user2 = User(
#             name = "Nesma",
#             age = 30
#         )
#         s.add_all([user1, user2])
#         s.commit()

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/api/users", tags=["User"])
def get_all_users():
    # add_user_to_db()
    session.query(User).all()


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)