#!/usr/bin/python3
"""
house module
"""

from models.base import base_db, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class House(Base, base_db):
    """
    house class which inherit from Base class and
    sqlalchemy declarative base
    """

    __tablename__ = "houses"

    agent_id = Column(
            String(45),
            ForeignKey("agents.id", ondelete="SET NULL")
            )
    occufied_id = Column(
            String(45),
            ForeignKey("occufied_houses.id", ondelete="SET NULL")
            )
    price = Column(String(45), nullable=False)
    location = Column(String(60), nullable=False)
    house_type = Column(String(60), nullable=False)
    discription = Column(String(60))
