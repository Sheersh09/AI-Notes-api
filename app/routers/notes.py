from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from pydantic import BaseModel
from pydantic import Field
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Note

router = APIRouter(prefix="/notes", tags=["notes"])


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    favorite: bool = Field(default=False)


class NoteUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    favorite: bool = Field(default=False)


# Convert ORM note objects into plain dictionaries for JSON responses.
def serialize_note(note: Note):
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
        "favorite": note.favorite,
    }


# Reuse one database lookup path so missing-note handling stays consistent.
def find_note(note_id: int, db: Session) -> Note:
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/{id}")
def read_note(id: int, db: Session = Depends(get_db)) -> dict[str, int | str | bool]:
    note = find_note(id, db)
    return serialize_note(note)


@router.get("")
def list_notes(
    limit: int = Query(default=5, ge=1),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    note_records = db.query(Note).limit(limit).all()
    return {
        "limit": limit,
        "count": len(note_records),
        "notes": [serialize_note(note) for note in note_records],
    }


@router.post("", status_code=201)
def create_note(note: NoteCreate, db: Session = Depends(get_db)) -> dict[str, object]:
    # Build an ORM object so SQLAlchemy can insert it into the notes table.
    new_note = Note(
        title=note.title,
        content=note.content,
        favorite=note.favorite,
    )
    db.add(new_note)
    db.commit()
    # Refresh the object so generated values like the database ID are available.
    db.refresh(new_note)
    return {
        "message": "Note created successfully",
        "note": serialize_note(new_note),
    }


@router.put("/{id}")
def update_note(
    id: int,
    note_update: NoteUpdate,
    db: Session = Depends(get_db),
) -> dict[str, object]:
    existing_note = find_note(id, db)
    existing_note.title = note_update.title # type: ignore
    existing_note.content = note_update.content # type: ignore
    existing_note.favorite = note_update.favorite # type: ignore
    db.commit()
    db.refresh(existing_note)
    return {
        "message": "Note updated successfully",
        "note": serialize_note(existing_note),
    }


@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    existing_note = find_note(id, db)
    db.delete(existing_note)
    db.commit()
    return {"message": "Note deleted successfully"}
