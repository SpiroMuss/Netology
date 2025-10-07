from pydantic import BaseModel
from datetime import datetime


class IdResponse(BaseModel):
    id: int


class CreateAdvertisementRequest(BaseModel):
    title: str
    comment: str
    price: float
    owner: str


# class SearchAdvertisementRequest(BaseModel):
#     title: str | None
#     price: float | None
#     owner: str | None


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
    title: str | None = None
    comment: str | None = None
    price: float | None = None