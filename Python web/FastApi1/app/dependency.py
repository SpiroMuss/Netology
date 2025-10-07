from models import DbSession
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncSession:
    async with DbSession() as session:
        yield session


SessionDependency = Annotated[AsyncSession, Depends(get_session)]