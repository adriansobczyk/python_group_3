from sqlalchemy.orm import Session
from src.schemas import UserCreate

async def get_user_by_email(email: str, db: Session):
    pass

async def create_user(db: Session, user: UserCreate):
    pass
