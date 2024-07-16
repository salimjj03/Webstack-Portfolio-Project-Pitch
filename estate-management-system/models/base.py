#!/usr/bin/python3
"""
this is the base class model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer, DateTime
import uuid
from datetime import datetime
from sqlalchemy.orm import sessionmaker
        

base_db = declarative_base()


class Base:
    """
    this is the base class model
    """

    id = Column(String(45), primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self, **kwarg):
        """
        the custructor class
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwarg != None:
            for key, value in kwarg.items():
                setattr(self, key, value)

    def all(self):
        """
        """
        
        from models import storage

        cls = self.__class__.__name__
        return (storage.all(cls))

    def to_dict(self):
        """
        This method return the dictionary representation
        of object
        """

        dic = self.__dict__.copy()
        dic["class_name"] = self.__class__.__name__
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic

    def save(self):
        """
        add obj to the database
        """
        
        from models import storage

        storage.session()
        storage.save(self)
        print("{} added successifully".format(self.__class__.__name__))

    def update(self, **kwarg):
        """
        this update the object
        """

        from models import storage

        return storage.update(self.__class__.__name__, self.id, **kwarg)

    def delete(self):
        """
        """

        from models import storage

        return storage.delete_obj(self)
