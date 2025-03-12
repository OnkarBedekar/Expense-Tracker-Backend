from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional

# User schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None

class PasswordUpdate(BaseModel):
    current_password: str
    new_password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

# Expense schemas
class ExpenseCreate(BaseModel):
    amount: float
    description: Optional[str] = None
    date: date
    category: Optional[str] = None

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    description: Optional[str] = None
    date: date
    category: Optional[str] = None
    user_id: int

    class Config:
        orm_mode = True
