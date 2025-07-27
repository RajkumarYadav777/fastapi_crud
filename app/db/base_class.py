# this is the declarative base class
# each model must inherit this base

from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

# Modern base for SQLAlchemy 2.0+ (instead of as_declarative)
class Base(DeclarativeBase):
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

