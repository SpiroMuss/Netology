from datetime import datetime
from fastapi import FastAPI, Request
from sqlalchemy import select
from schema import (
    CreateAdvertisementRequest, IdResponse, GetAdvertisementResponse, SearchAdvertisementResponse,
    UpdateAdvertisementRequest
)
from lifespan import lifespan
from dependency import SessionDependency
from crud import get_item_by_id, add_item, delete_item
from models import Advertisement

app = FastAPI(
    title="Trade API",
    terms_of_service="",
    description="buy/sell advertisements",
    lifespan=lifespan,
)


@app.post("/advertisements/", response_model=IdResponse)
async def create_advertisement(session: SessionDependency, item: CreateAdvertisementRequest):
    adv = Advertisement(
        title=item.title,
        comment=item.comment,
        price=item.price,
        owner=item.owner,
    )
    await add_item(session=session, item=adv)
    return adv.id_json


@app.patch("/advertisements/{adv_id}", response_model=IdResponse)
async def update_advertisement(session: SessionDependency, adv_id: int, item: UpdateAdvertisementRequest):
    adv = await get_item_by_id(session, Advertisement, adv_id)
    print(item)
    update_payload = item.model_dump(exclude_unset=True)
    for key, value in update_payload.items():
        setattr(adv, key, value)
    await add_item(session=session, item=adv)
    return adv.id_json


@app.delete("/advertisements/{adv_id}", response_model=IdResponse)
async def delete_advertisement(session: SessionDependency, adv_id: int):
    adv = await get_item_by_id(session, Advertisement, adv_id)
    await delete_item(session=session, item=adv)
    return {"id": adv_id}


@app.get("/advertisements/{adv_id}", response_model=GetAdvertisementResponse)
async def get_advertisement(session: SessionDependency, adv_id: int):
    adv = await get_item_by_id(session, Advertisement, adv_id)
    return adv.json


@app.get("/advertisements?{query_string}", response_model=SearchAdvertisementResponse)
async def search_advertisement(session: SessionDependency, price: float):
    query = select(Advertisement).where(
        Advertisement.price == price
    ).limit(1000)
    advs = await session.scalars(query)
    return {"advertisements": [adv.id for adv in advs]}