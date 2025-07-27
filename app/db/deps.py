
from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal


# dependency to get a SQLAlchemy DB session per request

def get_db()->[Session, None, None]:
    """
    This function is a dependency that provides a database session.
    It ensures:
      - a fresh session is provided for each request
      - session is closed after request (even on error)
    """

    db = SessionLocal()  # creates session and connects actual db for each request

    try:
        yield db
    
    finally:
        db.close()


# Generator[Session, None, None] 
# is the correct return type here — the function is a generator that yields a Session.