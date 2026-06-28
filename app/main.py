# Import FastAPI so we can create the API application.
from fastapi import FastAPI
# Import HTTPException so we can return a 404 error when a note is missing.
from fastapi import HTTPException
# Import Query so we can validate query parameters like limit.
from fastapi import Query
# Import BaseModel so we can define a request body schema with Pydantic.
from pydantic import BaseModel
# Import Field so we can add validation rules to each request body field.
from pydantic import Field

# Create the FastAPI app instance that handles incoming requests.
app = FastAPI()


# Define a Pydantic model for the data that a user sends when creating a note.
class NoteCreate(BaseModel):
    # Require a title string with at least 1 character.
    title: str = Field(..., min_length=1)
    # Require a content string with at least 1 character.
    content: str = Field(..., min_length=1)


# Create an empty list to store notes in memory while the app is running.
notes_storage: list[dict[str, int | str]] = []


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
        # Show the project name.
        "project": "AI Notes API",
        # Show the active learning phase.
        "phase": "Phase 2 - Request Validation",
        # Explain what this phase is teaching.
        "description": "This phase uses Pydantic models to validate request bodies.",
    }


# Register a GET endpoint for the "/notes/{id}" URL path.
@app.get("/notes/{id}")
# Define the function that runs when a note ID is sent in the URL.
def read_note(id: int) -> dict[str, int | str]:
    # Loop through each stored note to find the matching ID.
    for note in notes_storage:
        # Check whether the current note has the requested ID.
        if note["id"] == id:
            # Return the matching note as a JSON response.
            return note
    # Raise a 404 error if no note with that ID exists.
    raise HTTPException(status_code=404, detail="Note not found")


# Register a GET endpoint for the "/notes" URL path.
@app.get("/notes")
# Define the function that runs when the notes endpoint is requested.
def list_notes(limit: int = Query(default=5, ge=1)) -> dict[str, object]:
    # Return the stored notes up to the requested limit.
    return {
        # Show the limit value received from the query string.
        "limit": limit,
        # Show how many notes are being returned.
        "count": len(notes_storage[:limit]),
        # Return the notes list up to the selected limit.
        "notes": notes_storage[:limit],
    }


# Register a POST endpoint for the "/notes" URL path.
@app.post("/notes", status_code=201)
# Define the function that runs when a new note is sent in the request body.
def create_note(note: NoteCreate) -> dict[str, object]:
    # Create a dictionary for the new note using the validated request data.
    new_note = {
        # Generate a simple ID based on the current number of stored notes.
        "id": len(notes_storage) + 1,
        # Copy the validated title from the request body.
        "title": note.title,
        # Copy the validated content from the request body.
        "content": note.content,
    }
    # Add the new note to the in-memory list.
    notes_storage.append(new_note)
    # Return a success message and the created note as JSON.
    return {
        # Confirm that the note was created successfully.
        "message": "Note created successfully",
        # Return the new note data.
        "note": new_note,
    }
