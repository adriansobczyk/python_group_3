from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas import Contact, ContactCreate
from src.database.db import get_db
from src.repository import contact as repository
from src.services.auth import Auth

router = APIRouter()

@router.post("/create", response_model=Contact, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass

@router.get("/read_contacts", response_model=List[Contact])
def read_contacts(db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass

@router.get("/read_contact/{contact_id}", response_model=Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass

@router.put("/update_contact/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass

@router.delete("/delete_contact/{contact_id}", response_model=Contact)
def delete_contact(contact_id: int, db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass

@router.get("/search/", response_model=List[Contact])
def search_contacts(query: str, db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass

@router.get("/birthdays/", response_model=List[Contact])
def get_birthdays(db: Session = Depends(get_db), current_user: int = Depends(Auth.get_current_user)):
    pass
