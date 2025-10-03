from datetime import datetime
import os
import atexit
from sqlalchemy import create_engine, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, relationship

POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'Polygon')

PG_DSN = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
DbSession = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = "user"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     name: Mapped[str] = mapped_column(String, unique=True)
#
#     @property
#     def id_json(self):
#         return {
#             'id': self.id,
#         }
#
#     @property
#     def json(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#         }


class Advertisement(Base):
    __tablename__ = "advertisement"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    header: Mapped[str] = mapped_column(String)
    comment: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    owner: Mapped[str] = mapped_column(String)

    @property
    def id_json(self):
        return {
            'id': self.id,
        }

    @property
    def json(self):
        return {
            'id': self.id,
            'header': self.header,
            'comment': self.comment,
            'created_at': self.created_at.isoformat(),
            'owner': self.owner,
        }


Base.metadata.create_all(engine)

atexit.register(engine.dispose)