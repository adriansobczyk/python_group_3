from fastapi import FastAPI, Path, Query

app = FastAPI()

'''
Komenda do uruchomienia aplikacji:
uvicorn basics:app --host localhost --port 8000 --reload
'''

# @app.get("/api/healthchecker")
# def root():
#     return {"message": "Welcome to FastAPI!"}

# 1/
# @app.get("/notes/{note_id}")
# async def read_note(note_id: int):
#     return {"note": note_id}

# 2.
# @app.get("/notes/{note_id}")
# async def read_note(note_id: int):
#     return {"note": note_id}

# @app.get("/notes/new")
# async def read_new_notes():
#     return {"message": "Return new notes"}

# 3. 
# @app.get("/note/new")
# async def read_new_notes():
#     return {"message": "Return new notes"}

# @app.get("/notes/{note_id}")
# async def read_note(note_id: int):
#     return {"note": note_id}

# 4.
# @app.get("/notes/{note_id}")
# async def read_note(note_id: int = Path(description="The ID of the note to get", gt=0, le=10)):
#     return {"note": note_id}

# 5.
# @app.get("/notes")
# async def read_notes(skip: int = 0, limit: int = 10):
#     return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}

# 6.
# @app.get("/notes")
# async def read_notes(skip: int = 0, limit: int = 10, q: str | None = None):
#     return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}

# # 7.
# @app.get("/notes")
# async def read_notes(skip: int = 0, limit: int = Query(default=10, le=100, ge=10)):
#     return {"message": f"Return all notes: skip: {skip}, limit: {limit}"}
