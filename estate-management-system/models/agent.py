#!/usr/bin/python3
"""
"""

from models.user import User
from models.base import base_db


class Agent(User, base_db):
    """
    """

    __tablename__ = "agents"
