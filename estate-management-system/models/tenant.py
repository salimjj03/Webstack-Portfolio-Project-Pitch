#!/usr/bin/python3
"""
"""

from datetime import datetime, timedelta
from models.user import User
from models.agent import Agent
from models.house import House
from models.base import base_db
from models.occufied_house import Occufied_house


class Tenant(User, base_db):
    """
    """

    __tablename__ = "tenants"

    def reserve_house(self, house_id):
        """
        """

        from models import storage

        expire_date = datetime.now() + timedelta(days=7)
        dic = {
                "house_id": house_id,
                "tenant_id": self.id,
                "occufied_status": 1,
                "payment_status": 0,
                "expire_date": expire_date
                }
        
        house = storage.find_obj_by_key(House, id=house_id)
        if house is None:
            print("invalid house id")
            return False
        if house.occufied_id is not None:
            print("House is currently occupied")
            return(False)
        reserve = Occufied_house(**dic)
        reserve.save()
        house.update(occufied_id=reserve.id)
        print("House reserve successifull")
        return True

    def roll_over(self, occupied_id):
        """
        """
            
        from models import storage

        occupied_house = storage.find_obj_by_key(
                Occufied_house,
                id=occupied_id
                )

        expire_date = occupied_house.expire_date + timedelta(days=360)

        dic = {
                "house_id": occupied_house.house_id,
                "tenant_id": self.id,
                "occufied_status": 1,
                "payment_status": 0,
                "expire_date": expire_date
                }
        
        house = storage.find_obj_by_key(
                House,
                id=occupied_house.house_id
                )

        re_occupied = Occufied_house(**dic)
        re_occupied.save()
        occupied_house.update(occufied_status=0)
        house.update(occufied_id=re_occupied.id)
        print("roll over successifull")
        return(True)
