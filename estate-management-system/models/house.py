#!/usr/bin/python3
"""
"""

from models.base import base_db, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class House(Base, base_db):
    """
    """

    __tablename__ = "houses"

    agent_id = Column(
            String(45),
            ForeignKey("agents.id", ondelete="CASCADE")
            )
    occufied_id = Column(
            String(45),
            ForeignKey("occufied_houses.id", ondelete="CASCADE")
            )
    price = Column(String(45), default="0.00", nullable=False)
    location = Column(String(60), default="jigawa", nullable=False)
    house_type = Column(String(60), default="2 bed-room", nullable=False)
    discription = Column(String(60))
