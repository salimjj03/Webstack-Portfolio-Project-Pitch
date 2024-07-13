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

        quary = {
                "payment_status": 0,
                "tenant_id": self.id,
                "occufied_status": 1
                }
        pending_reserve = storage.find_obj_by_key(
                "Occufied_house",
                **quary
                )

        if pending_reserve:
            return False

        reserve = Occufied_house(**dic)
        reserve.save()
        house.update(occufied_id=reserve.id)
        print("House reserve successifull")
        return reserve

    def active_rent(self):
        """
        """
        
        from models import storage

        
        dic = {"occufied_status": 1, "tenant_id": self.id}
        active_r = storage.find_many_by_key(
                "Occufied_house",
                **dic
                )

        return active_r

    def previous_rent(self):
        """
        """

        from models import storage

        dic = {
                "occufied_status": 0,
                "tenant_id": self.id,
                "payment_status": 1
                }

        prev_rent = storage.find_many_by_key(
                "Occufied_house",
                **dic
                )

        return prev_rent


    def roll_over(self, occupied_id):
        """
        """
            
        from models import storage

        occupied_house = storage.find_obj_by_key(
                Occufied_house,
                id=occupied_id
                )
        if occupied_house == None:
            print("invalid occupied_id")
            return False

        if occupied_house.tenant_id != self.id:
            print("house is not occupied by the current tenant")
            return False

        if occupied_house.occufied_status != 1:
            print("this occufied house is not active")
            return False

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
        #re_occupied.created_at = house.expire_date
        re_occupied.save()
        print("roll over successifull")
        return(True)

    def cancel_reservation(self, occufied_id):
        """
        """

        from models import storage

        house = storage.find_obj_by_key(Occufied_house, id=occufied_id)
        if house and house.tenant_id == self.id:
            if house.payment_status == 0 and house.occufied_status == 1:
                occupied_house = storage.find_obj_by_key(House, id=house.house_id)
                house.update(occufied_status=0)
                if house.id == occupied_house.occufied_id:
                    occupied_house.update(occufied_id=None)
                print("reservation cancel")
                return True
            return ("This reservation can not be cancel")
        return("invalid occufied_id")
