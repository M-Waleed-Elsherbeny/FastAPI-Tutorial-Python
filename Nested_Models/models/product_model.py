from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    image: HttpUrl
    description: str | None = None
    

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    image: list[Image]



class Product(BaseModel):
    item: Item


