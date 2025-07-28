
# create pydantic schema used for incoming and outgoing data
# validation and serialization/deserialization


from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# shared model fields
class UserBase(BaseModel):
    name: str = Field(..., max_length=50)
    email: EmailStr


# create user data
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)

# update user ; all are optinal data like for PATCH

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    is_active: Optional[bool] = None

# sending response to client
class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# Internal DB schema need for using inside services

class UserInDB(UserRead):
    hashed_password: str

