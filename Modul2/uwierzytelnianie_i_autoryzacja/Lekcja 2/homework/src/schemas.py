from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    birth_date: Optional[date] = None
    additional_info: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    contacts: List[Contact] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str

class TokenData(BaseModel):
    email: Optional[EmailStr] = None
