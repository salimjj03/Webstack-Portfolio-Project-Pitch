#!/usr/bin/python3
"""
this is the storage engine
"""

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base import base_db
from models.admin import Admin
from models.user import User
from models.house import House
from models.agent import Agent
from models.tenant import Tenant
from models.rent_history import Rent_history
from models.occufied_house import Occufied_house
from models.rent_history import Rent_history
from datetime import datetime

classes = [
        User,
        Agent,
        Tenant,
        House,
        Occufied_house,
        Admin,
        Rent_history
        ]

class Db():
    """
    this is the storage engine
    """

    __engine = None
    __session = None


    def __init__(self):
        """
        this method create the database engine
        """

        Db.__engine = create_engine(
            "mysql+mysqldb://salem:root@localhost/estate", echo=False
            )

        base_db.metadata.create_all(Db.__engine)

    def is_valid_cls(self, cls):
        """
        this method return true if class is a valid one
        else False
        """

        if isinstance(cls, str):
            try:
                cls = globals()[cls]
            except Exception:
                return False

        if cls in classes:
            return cls

        return False

    def all(self, cls=None):
        """
        this method return the dict of all obj of same cls
        if the cls is valid
        """
        
        cls = self.is_valid_cls(cls)
        if cls:
            dic = {}
            result = self.__session.query(cls).all()
            return result
        return None

    def find_obj_by_key(self, cls, **kwarg):
        """
        this method return cls obj base on the key value
        if it exist else error
        """

        cls = self.is_valid_cls(cls)
        if cls is False:
            return None

        if len(kwarg) >= 2:
            filters = []

            for key, value in kwarg.items():
                filters.append(getattr(cls, key) == value)

            result = self.__session.query(cls).filter(
                    *filters
                    ).first()
        elif len(kwarg) == 1:

            key = next(iter(kwarg))
            value = kwarg.get(key)
            result = self.__session.query(
                    cls
                    ).filter(getattr(cls, key) == value).first()

        else:
            ressult = []

        return result

    def find_many_by_key(self, cls, **kwarg):
        """
        this method return cls obj base on the key value
        if it exist else error
        """
        
        
        cls = self.is_valid_cls(cls)
        if cls is False:
            return None

        if len(kwarg) >= 2:
            filters = []

            for key, value in kwarg.items():
                filters.append(getattr(cls, key) == value)

            result = self.__session.query(cls).filter(
                    *filters
                    ).all()
        elif len(kwarg) == 1:

            key = next(iter(kwarg))
            value = kwarg.get(key)
            result = self.__session.query(
                    cls
                    ).filter(getattr(cls, key) == value).all()

        else:
            ressult = []

        return result

    def occufied(self, agent_id=None):
        """
        this method return the occufied houses
        """
        
        if agent_id == None:
            result = self.__session.query(House).filter(
                    House.agent_id != None,
                    House.occufied_id != None
                    ).all()

            return result

        else:
            result = self.__session.query(House).filter(
                    House.agent_id == agent_id,
                    House.occufied_id != None
                    ).all()

            return result

    def un_occufied(self, agent_id=None):
        """
        this method return the unoccufied houses
        """

        if agent_id == None:
            result = self.__session.query(House).filter(
                    House.occufied_id == None
                    ).all()

            return result

        else:
            result = self.__session.query(House).filter(
                    House.agent_id == agent_id,
                    House.occufied_id == None
                    ).all()

            return result

    def save(self, obj):
        """
        this method save obj to database
        """

        self.__session.add(obj)
        self.__session.commit()
    

    def update_obj(self, obj, **kwarg):
        """
        """

        if obj:
            for key, value in kwarg.items():
                if key in obj.to_dict():
                    setattr(obj, key, value)
                    obj.updated_at = datetime.utcnow()
                    print("{} updated successifully".format(key))
                else:
                    print("invalid key {}".format(key))
            self.__session.commit()
            print("record updated successifully")
            return True
        return False


    def update(self, cls, id, **kwarg):
        """
        this method update obj if it exist
        """

        obj = self.find_obj_by_key(cls, id=id)
        if obj:
            for key, value in kwarg.items():
                if key in obj.to_dict():
                    if value is None or value == "":
                        continue
                    setattr(obj, key, value)
                    obj.updated_at = datetime.utcnow()
                    print("{} updated successifully".format(key))
                else:
                    print("invalid key {}".format(key))
            self.__session.commit()
            print("record updated successifully")
            return True
        print("obj not found")
        return("obj not found")
    

    def delete_obj(self, obj):
        """
        """

        self.__session.merge(obj)
        self.__session.delete(obj)
        self.__session.commit()
        print("obj deleted successufully")
        return True

    def delete(self, cls, id):
        """
        this method delete obj if exist
        """

        obj = self.find_obj_by_key(cls, id=id)
        if obj:
            self.__session.delete(obj)
            self.__session.commit()
            print("obj deleted successufully")
            return True
        print ("obj not found")
        return ("obj not found")

    def session(self):

        Session = scoped_session(
                sessionmaker(
                    bind=self.__engine,
                    expire_on_commit=False
                    )
                )
        self.__session = Session


    def close(self):
        """
        this method close the database session
        """

        if self.__session != None:
            self.__session.remove()


    def expire_rent(self):
        """
        """

        now = datetime.now()

        expire_rents = self.__session.query(Occufied_house).filter(
                Occufied_house.expire_date < now,
                Occufied_house.payment_status == 1,
                Occufied_house.occufied_status == 1
                ).all()

        for expire in expire_rents:
            house = self.find_obj_by_key(
                    House,
                    id=expire.house_id
                    )
            print("expired_rent: {}".format(house.id))
            dic = {
                    "tenant_id": expire.tenant_id,
                    "agent_id": house.agent_id,
                    "house_id": house.id,
                    "expire_date": expire.expire_date,
                    "price": house.price
                    }

            house.occufied_id = None
            expire.occufied_status = 0
            house.updated_at = now
            rent_history = Rent_history(**dic)
            self.__session.add(rent_history)
            self.__session.delete(expire)
        self.__session.commit()
        print("checking expired rent")


    def expire_reservation(self):
        """
        """

        now = datetime.now()

        expire_rents = self.__session.query(Occufied_house).filter(
                Occufied_house.expire_date < now,
                Occufied_house.payment_status == 0
                ).all()

        for expire in expire_rents:
            house = self.find_obj_by_key(
                    House,
                    id=expire.house_id
                    )
            house.occufied_id = None
            print("expired_reservation: {}".format(house.id))
            self.__session.delete(expire)
            house.updated_at = now
        self.__session.commit()
        print("checking expired reservation")

