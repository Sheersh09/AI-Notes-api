from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from pydantic import BaseModel
from pydantic import Field

app = FastAPI()


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


# Reuse the same validation rules when a note is fully updated.
class NoteUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


notes: list[dict[str, int | str]] = []


# Centralize note lookup so read, update, and delete use the same logic.
def find_note(note_id: int) -> dict[str, int | str]:
    # Check each stored note until the matching ID is found.
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the AI Notes API"}


@app.get("/about")
def read_about() -> dict[str, str]:
    return {
        "project": "AI Notes API",
        "phase": "Phase 3 - CRUD in Memory",
        "description": "This phase builds full CRUD operations using an in-memory list.",
    }


@app.get("/notes/{id}")
def read_note(id: int) -> dict[str, int | str]:
    return find_note(id)


@app.get("/notes")
def list_notes(limit: int = Query(default=5, ge=1)) -> dict[str, object]:
    return {
        "limit": limit,
        "count": len(notes[:limit]),
        "notes": notes[:limit],
    }


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate) -> dict[str, object]:
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
    }
    notes.append(new_note)
    return {
        "message": "Note created successfully",
        "note": new_note,
    }


# Add a PUT route so an existing note can be replaced with new data.
@app.put("/notes/{id}")
# Accept the note ID from the path and the validated update data from the body.
def update_note(id: int, note_update: NoteUpdate) -> dict[str, object]:
    # Find the existing note first so we can update its fields in place.
    existing_note = find_note(id)
    # Replace the old title with the new validated title.
    existing_note["title"] = note_update.title
    # Replace the old content with the new validated content.
    existing_note["content"] = note_update.content
    return {
        "message": "Note updated successfully",
        "note": existing_note,
    }


# Add a DELETE route so notes can be removed from the in-memory list.
@app.delete("/notes/{id}")
# Use the note ID from the path to locate and remove the note.
def delete_note(id: int) -> dict[str, str]:
    # Find the existing note before trying to remove it.
    existing_note = find_note(id)
    # Remove the matched note from the shared notes list.
    notes.remove(existing_note)
    return {"message": "Note deleted successfully"}
