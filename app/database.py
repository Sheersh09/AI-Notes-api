from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Point SQLAlchemy at a local SQLite file so note data persists between runs.
DATABASE_URL = "sqlite:///./notes.db"

# Disable SQLite's same-thread check so FastAPI request handling can share the engine safely.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Build session objects that each request can use for database work.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class that all SQLAlchemy models will inherit from.
Base = declarative_base()


# Open a session for each request and close it automatically afterward.
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
