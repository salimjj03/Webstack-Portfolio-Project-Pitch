#!/usr/bin/python3
"""
Rent  history module
"""


from models.base import Base, base_db
from sqlalchemy import Column, String, ForeignKey, DateTime


class Rent_history(Base, base_db):
    """
    The Rent histor class that will keep
    the record of tenant reservation
    """

    __tablename__ = "rent_histories"

    tenant_id = Column(
            String(50),
            ForeignKey("tenants.id", ondelete="SET NULL")
            )

    agent_id = Column(
            String(50),
            ForeignKey("agents.id", ondelete="SET NULL")
            )

    house_id = Column(
            String(50),
            ForeignKey("houses.id", ondelete="SET NULL")
            )
    
    price = Column(
            String(20)
            )

    expire_date = Column(
            DateTime
            )
