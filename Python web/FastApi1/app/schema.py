from pydantic import BaseModel
from datetime import datetime


class IdResponse(BaseModel):
    id: int


class CreateAdvertisementRequest(BaseModel):
    title: str
    comment: str
    price: float
    owner: str


class GetAdvertisementResponse(BaseModel):
    id: int
    title: str
    comment: str
    price: float
    owner: str
    created_at: datetime


class SearchAdvertisementResponse(BaseModel):
        advertisements: list[int]


class UpdateAdvertisementRequest(BaseModel):
    title: str | None
    comment: str | None
    price: float | None