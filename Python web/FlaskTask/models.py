import os

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = 'advertisments'

    id
    header
    comment
    created_at
    owner