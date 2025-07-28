

"""
Used for initializing the database schema during development or prototyping.

Why this is important:
- Base.metadata.create_all() reads from registered models
- All models must be imported (indirectly via base.py)
- This setup avoids having to list every model manually here
"""

from app.db.base import Base  # This also imports all models via base.py
from app.db.session import engine  # DB engine that connects to PostgreSQL/MySQL/SQLite

def init_db() -> None:
    """
    Creates database tables based on all registered models.
    Call this once during prototyping or local development.
    """
    Base.metadata.create_all(bind=engine)
