#!/usr/bin/python3
"""
"""

from models.base import base_db, Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime


class Occufied_house(Base, base_db):
    """
    """

    __tablename__ = "occufied_houses"

    tenant_id = Column(
            String(45),
            ForeignKey("tenants.id", ondelete="SET NULL"),
            nullable=True
            )

    house_id = Column(
            String(45),
            ForeignKey("houses.id", ondelete="SET NULL"),
            nullable=True
            )

    occufied_status = Column(Integer, default=1)
    payment_status = Column(Integer, default=0)
    expire_date = Column(DateTime)
