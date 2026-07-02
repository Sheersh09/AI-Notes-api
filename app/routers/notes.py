from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Note
from app.schemas import NoteCreate
from app.schemas import NoteResponse
from app.schemas import NoteUpdate

router = APIRouter(prefix="/notes", tags=["notes"])
def find_note(note_id: int, db: Session) -> Note:
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/{id}", response_model=NoteResponse)
def read_note(id: int, db: Session = Depends(get_db)) -> Note:
    return find_note(id, db)


@router.get("", response_model=list[NoteResponse])
def list_notes(
    limit: int = Query(default=5, ge=1),
    db: Session = Depends(get_db),
) -> list[Note]:
    return db.query(Note).limit(limit).all()


@router.post("", status_code=201, response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)) -> Note:
    # New notes start as not favorited because that field is not part of NoteCreate.
    new_note = Note(
        title=note.title,
        content=note.content,
        favorite=False,
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


@router.put("/{id}", response_model=NoteResponse)
def update_note(
    id: int,
    note_update: NoteUpdate,
    db: Session = Depends(get_db),) -> Note:
    existing_note = find_note(id, db)
    existing_note.title = note_update.title # type: ignore
    existing_note.content = note_update.content # type: ignore
    existing_note.favorite = note_update.favorite # pyright: ignore[reportAttributeAccessIssue]
    db.commit()
    db.refresh(existing_note)
    return existing_note


@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    existing_note = find_note(id, db)
    db.delete(existing_note)
    db.commit()
    return {"message": "Note deleted successfully"}
