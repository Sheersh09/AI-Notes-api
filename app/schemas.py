from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


class NoteUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    favorite: bool = Field(default=False)


# Allow Pydantic to read data directly from SQLAlchemy model attributes.
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    favorite: bool

    model_config = ConfigDict(from_attributes=True)
