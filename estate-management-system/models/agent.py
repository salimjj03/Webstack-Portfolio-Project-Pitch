#!/usr/bin/python3
"""
"""

from models.user import User
from models.base import base_db


class Agent(User, base_db):
    """
    """

    __tablename__ = "agents"


    def occufied(self):
        """
        this method return the occufied houses
        """

        from models import storage

        result = storage.occufied(self.id)
        return result

    def un_occufied(self, agent_id=None):
        """
        this method return the occufied houses
        """

        from models import storage

        result = storage.un_occufied(self.id)
        return result

    def roll_over(self):
        """
        """

        pass
