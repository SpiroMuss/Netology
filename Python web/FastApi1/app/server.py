from fastapi import FastAPI, Request
from pydantic import BaseModel
from lifespan import lifespan

app = FastAPI(
    title="Trade API",
    terms_of_service="",
    description="buy/sell advertisements",
    lifespan=lifespan,
)


class _Request(BaseModel):
    pass


class _Response(BaseModel):
    pass


@app.get("/", response_model=_Response)
async def view(item:_Request, request: Request):
    return {}