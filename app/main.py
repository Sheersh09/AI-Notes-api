from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import notes

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(notes.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the AI Notes API"}


@app.get("/about")
def read_about() -> dict[str, str]:
    return {
        "project": "AI Notes API",
        "phase": "Phase 5 - Database",
        "description": "This phase stores notes in SQLite using SQLAlchemy ORM and sessions.",
    }
