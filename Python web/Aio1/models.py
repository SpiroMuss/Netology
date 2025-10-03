import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, MappedColumn
from sqlalchemy import Integer, String


POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'Polygon')

PG_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(PG_DSN)
DbSession = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class SWCharacter(Base):
    __tablename__ = 'swcharacters'

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    birth_year: MappedColumn[str] = mapped_column(String, nullable=True)
    eye_color: MappedColumn[str] = mapped_column(String, nullable=True)
    gender: MappedColumn[str] = mapped_column(String, nullable=True)
    hair_color: MappedColumn[str] = mapped_column(String, nullable=True)
    homeworld: MappedColumn[str] = mapped_column(String, nullable=True)
    mass: MappedColumn[str] = mapped_column(String, nullable=True)
    name: MappedColumn[str] = mapped_column(String, nullable=True)
    skin_color: MappedColumn[str] = mapped_column(String, nullable=True)


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def close_orm():
    await engine.dispose()