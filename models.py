from typing import Text
from pymysql import Date
from sqlalchemy import DATE, TEXT, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(TEXT)
    created_at = Column(DATE)
    updated_at = Column(DATE)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(DATE)
    updated_at = Column(DATE)
