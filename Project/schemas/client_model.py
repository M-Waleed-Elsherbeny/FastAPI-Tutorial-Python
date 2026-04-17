from pydantic import BaseModel


class ClientRequest(BaseModel):
    id: int | None = None
    name: str
    post_url: str
    price: float
    day_number: int
    is_finished: bool


class ClientResponse(BaseModel):
    client: list[ClientRequest]