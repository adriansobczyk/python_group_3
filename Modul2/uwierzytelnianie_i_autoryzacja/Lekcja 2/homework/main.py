import uvicorn
from fastapi import FastAPI
from src.database import db
from src.database.models import Base
from src.routes import contact, user

app = FastAPI()

Base.metadata.create_all(bind=db.engine)

app.include_router(contact.router, prefix="/contacts", tags=["contacts"])
app.include_router(user.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Witaj w aplikacji kontaktowej!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)