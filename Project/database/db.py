from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped, Session
import os

class Base(DeclarativeBase):
    pass

class DB:
    BASE_DIR = os.path.dirname("./Project")
    connect = "sqlite:///" + os.path.join(BASE_DIR, "users.db")
    engine = None

    def connect_db(self):
        self.engine = create_engine(self.connect, echo=True )
        Base.metadata.create_all(self.engine)
    
    def create_session(self):
        return Session(bind=self.engine)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable= False)
    age: Mapped[int] = mapped_column(Integer, nullable= True)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, age={self.age!r})"
    


db = DB()
connect = db.connect_db()
session = db.create_session()



