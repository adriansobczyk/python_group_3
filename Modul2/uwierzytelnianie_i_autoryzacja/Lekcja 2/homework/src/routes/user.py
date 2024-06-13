from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.schemas import User, UserCreate
from src.database.db import get_db
from src.repository import user as repository

router = APIRouter()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    pass

@router.post("/token", response_model=dict)
async def login_for_access_token(user: UserCreate, db: Session = Depends(get_db)):
    pass
