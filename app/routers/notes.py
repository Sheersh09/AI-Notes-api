from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query
from pydantic import BaseModel
from pydantic import Field

# Create a router so note endpoints can be grouped in a separate module.
router = APIRouter(prefix="/notes", tags=["notes"])


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


class NoteUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


notes: list[dict[str, int | str]] = []


def find_note(note_id: int) -> dict[str, int | str]:
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@router.get("/{id}")
def read_note(id: int) -> dict[str, int | str]:
    return find_note(id)


@router.get("")
def list_notes(limit: int = Query(default=5, ge=1)) -> dict[str, object]:
    return {
        "limit": limit,
        "count": len(notes[:limit]),
        "notes": notes[:limit],
    }


@router.post("", status_code=201)
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


@router.put("/{id}")
def update_note(id: int, note_update: NoteUpdate) -> dict[str, object]:
    existing_note = find_note(id)
    existing_note["title"] = note_update.title
    existing_note["content"] = note_update.content
    return {
        "message": "Note updated successfully",
        "note": existing_note,
    }


@router.delete("/{id}")
def delete_note(id: int) -> dict[str, str]:
    existing_note = find_note(id)
    notes.remove(existing_note)
    return {"message": "Note deleted successfully"}
