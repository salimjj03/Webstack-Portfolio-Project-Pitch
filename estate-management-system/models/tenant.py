#!/usr/bin/python3
"""
"""

from models.user import User
from models.agent import Agent
from models.base import base_db
#from sqlalchemy import Column, String, Forein_key


class Tenant(User, base_db):
    """
    """

    __tablename__ = "tenants"

#    agent_id = Column(string(45), )
