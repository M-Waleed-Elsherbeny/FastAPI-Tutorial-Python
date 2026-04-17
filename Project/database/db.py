from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session
import os

class Base(DeclarativeBase):
    pass

class DB:
    BASE_DIR = os.path.dirname("./")
    connect = "sqlite:///" + os.path.join(BASE_DIR, "clients.db")
    engine = None

    def connect_db(self):
        self.engine = create_engine(self.connect, echo=True )
        Base.metadata.create_all(self.engine)
    
    def create_session(self):
        return Session(bind=self.engine)

class Client(Base):
    __tablename__ = "client"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable= False)
    post_url: Mapped[str] = mapped_column(String(100), nullable= False)
    price: Mapped[float] = mapped_column(nullable= False)
    day_number: Mapped[int] = mapped_column(nullable= False)
    is_finished: Mapped[bool] = mapped_column(nullable= False)

    def __repr__(self) -> str:
        return f"Client(id={self.id!r}, name={self.name!r}, post_url={self.post_url!r}, price={self.price!r}, day_number={self.day_number!r}, is_finished={self.is_finished!r})"
    


db = DB()
connect = db.connect_db()
session = db.create_session()



