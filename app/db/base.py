"""
This file exists to ensure all models are imported once so they get
registered with SQLAlchemy’s metadata system.

Why this is important:
- SQLAlchemy uses Base.metadata to create tables.
- If you don’t import models, they won’t be registered.
"""
from app.db.base_class import Base

from app.models.user import User