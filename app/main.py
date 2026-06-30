from fastapi import FastAPI

# Import the notes router so notes-related endpoints live in their own module.
from app.routers import notes

app = FastAPI()

# Attach all note routes from the router module to the main app.
app.include_router(notes.router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the AI Notes API"}


@app.get("/about")
def read_about() -> dict[str, str]:
    return {
        "project": "AI Notes API",
        "phase": "Phase 4 - Project Structure",
        "description": "This phase organizes note routes using APIRouter and modular structure.",
    }
