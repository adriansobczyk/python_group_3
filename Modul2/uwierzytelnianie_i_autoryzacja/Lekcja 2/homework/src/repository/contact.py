from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactCreate

def create_contact(db: Session, contact: ContactCreate, user_id: int):
    pass

def get_contacts(db: Session, user_id: int):
    pass

def get_contact(db: Session, contact_id: int, user_id: int):
    pass

def update_contact(db: Session, contact_id: int, contact: ContactCreate, user_id: int):
    pass

def delete_contact(db: Session, contact_id: int, user_id: int):
    pass

def search_contacts(db: Session, query: str, user_id: int):
    pass

def get_birthdays(db: Session, user_id: int):
    pass
