from pydantic import BaseModel, EmailStr  # restrict input type and format returns
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    """
    This post schema comes from Pydantic. This defines how's our Postman Body(JSON) input data types。
    It defines the structure of a request & response.
    """
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # change sqlalchemy model to pydantic model
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
