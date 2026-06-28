from fastapi import FastAPI
from fastapi import Query

app = FastAPI()

# Register a GET endpoint for the root URL path "/".
@app.get("/")
# Define the function that runs when the root endpoint is requested.
def read_root() -> dict[str, str]:
    # Return a welcome message as a JSON response.
    return {"message": "Welcome to the AI Notes API"}


# Register a GET endpoint for the "/about" URL path.
@app.get("/about")
# Define the function that runs when the about endpoint is requested.
def read_about() -> dict[str, str]:
    # Return basic information about the current learning phase.
    return {
        # Describe the project name.
        "project": "AI Notes API",
        # Describe the active learning phase.
        "phase": "Phase 1 - API Fundamentals",
        # Explain what this phase is focused on.
        "description": "This phase is focused on FastAPI routing basics.",
    }


# Register a GET endpoint for the "/notes/{id}" URL path.
@app.get("/notes/{id}")
# Define the function that runs when a note ID is sent in the URL.
def read_note(id: int) -> dict[str, object]:
    # Return a sample response showing how a path parameter works.
    return {
        # Echo the note ID that came from the path.
        "note_id": id,
        # Explain that this is only a routing example for now.
        "message": "This is a sample note route using a path parameter.",
    }


# Register a GET endpoint for the "/notes" URL path.
@app.get("/notes")
# Define the function that runs when the notes endpoint is requested.
def list_notes(limit: int = Query(default=5, ge=1)) -> dict[str, object]:
    # Return a sample response showing how a query parameter works.
    return {
        # Echo the limit value that came from the query string.
        "limit": limit,
        # Explain that there is no real notes data yet.
        "message": "This is a sample notes route using a query parameter.",
        # Return placeholder note names to demonstrate JSON output.
        "notes": [
            # Add a sample note title.
            "Sample Note 1",
            # Add another sample note title.
            "Sample Note 2",
            # Add a third sample note title.
            "Sample Note 3",
        ][:limit],
    }
