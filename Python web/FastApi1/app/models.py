from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column
from sqlalchemy import Integer, String, DateTime, func, Float
from datetime import datetime

from config import PG_DSN

engine=create_async_engine(PG_DSN)
DbSession = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase, AsyncAttrs):

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)

    @property
    def id_json(self):
        return {"id": self.id}


class Advertisement(Base):

    __tablename__ = "advertisement"

    header: MappedColumn[str] = mapped_column(String)
    comment: MappedColumn[str] = mapped_column(String, nullable=True)
    price: MappedColumn[float] = mapped_column(Float)
    owner: MappedColumn[str] = mapped_column(String)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, server_default=func.now())

    @property
    def json(self):
        return {
            "id": self.id,
            "header": self.header,
            "comment": self.comment,
            "price": self.price,
            "owner": self.owner,
            "created_at": self.created_at,
        }


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_orm():
    await engine.dispose()


ORM_OBJ = Advertisement
ORM_CLS = type[Advertisement]