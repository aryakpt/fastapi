import email
from typing import Optional
from datetime import date
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True
