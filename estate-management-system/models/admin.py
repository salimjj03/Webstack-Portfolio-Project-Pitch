#!/usr/bin/python3
"""
admin class
"""

from models.user import User
from models.house import House
from models.base import base_db


class Admin(User, base_db):
    """
    admin class
    """

    __tablename__ = "admins"


    def add_house(self, **kwarg):
        """
        this method is only availabel in the admin
        and it can be used to add house in the db
        """

        if kwarg.get('price') is None:
            print('missing price')
            return False

        if kwarg.get('location') is None:
            print('missing location')
            return False

        if kwarg.get('house_type') is None:
            print('missing house_type')
            return False

        new_house = House(**kwarg)
        new_house.save()
        print("new hous with id: {} addad successuflly".format(new_house.id))
        return (True)

    def occufied(self):
        """
        return list of occufied houses
        """

        from models import storage

        return storage.occufied()


    def un_occufied(self):
        """
        return list of un_occufied houses
        """

        from models import storage

        return storage.un_occufied()
