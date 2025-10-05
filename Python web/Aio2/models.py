from datetime import datetime
import os
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, MappedColumn
from dotenv import load_dotenv
load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'Polygon')

PG_DSN = (f"postgresql+asyncpg://"
          f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
          f"{POSTGRES_HOST}:{POSTGRES_PORT}/"
          f"{POSTGRES_DB}")

engine = create_async_engine(PG_DSN)
DbSession = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)

    @property
    def id_json(self):
        return {
            'id': self.id,
        }


class Advertisement(Base):
    __tablename__ = "advertisement"

    header: MappedColumn[str] = mapped_column(String)
    comment: MappedColumn[str] = mapped_column(String)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, server_default=func.now())
    owner: MappedColumn[str] = mapped_column(String)

    @property
    def json(self):
        return {
            'id': self.id,
            'header': self.header,
            'comment': self.comment,
            'created_at': int(self.created_at.timestamp()),
            'owner': self.owner,
        }


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_orm():
    await engine.dispose()