#!/usr/bin/python3
"""
user module
"""

from models.base import base_db, Base
from sqlalchemy import Column, String, Integer


class User(Base):
    """
    user class which will be inherited by
    all type of users
    """

    full_name = Column(String(45), nullable=False)
    user_name = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=False, unique=True)
    role = Column(Integer, default=2)
    phone_no = Column(String(45), nullable=False, unique=True)
    address = Column(String(60))
    password = Column(String(40), nullable=False)
