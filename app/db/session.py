# session factory setup

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 1. Build the actual DB URL (loaded from .env via settings)

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# 2. Create engine - handles DB connection pool internally

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create reusable session factory to manage db transactions in routes/services
# bind is used to bind the engine to sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)