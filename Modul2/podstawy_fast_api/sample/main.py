from fastapi import FastAPI, Path, Query, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text # SQLAlchemy wymaga aby zapytania były w formie tekstu

from db import get_db, Note

app = FastAPI()

@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).fetchone()
    if result is None:
        raise HTTPException(status_code=500, detail="Database is not configured correctly")
    return {"message": "Welcome to FastAPI!"}


class NoteModel(BaseModel):
    name: str
    description: str
    done: bool

@app.post("/notes")
async def create_note(note: NoteModel, db: Session = Depends(get_db)):
    new_note = Note(name=note.name, description=note.description, done=note.done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
