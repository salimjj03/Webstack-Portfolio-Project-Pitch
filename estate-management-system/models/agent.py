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

    def approve_payment(self, occupied_id):
        """
        """

        from models import storage


        occ_house = storage.find_obj_by_key(
                "Occufied_house",
                id=occupied_id
                )

        if occ_house is None:
            return "invalid occufied_id"

        house = storage.find_obj_by_key(
                "House",
                id=occ_house.house_id
                )

        if house.agent_id != self.id:
            return "Agent is not the owner of House"

        if occ_house.occufied_status == 1:
            occ_house.update(payment_status=1)
            return True
        return "House is not occupied"



    def roll_over(self):
        """
        """

        pass
