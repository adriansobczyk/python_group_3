from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

...

class Note(BaseModel):
    name: str
    description: str
    done: bool

@app.post("/notes")
async def create_note(note: Note):
    return {"name": note.name, "description": note.description, "status": note.done}

@app.delete("/notes/delete")
async def create_note(note: Note):
    return {"name": note.name, "description": note.description, "status": note.done}