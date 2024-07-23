#!/usr/bin/python3
"""
test module
"""

from models import storage
from models.user import User
from models.admin import Admin
from models.agent import Agent
from models.house import House
from models.tenant import Tenant
from models.occufied_house import Occufied_house

dic = {
        'full_name': 'admin admin',
        'user_name': 'admin',
        'email': "admin@gmail.com",
        'phone_no': '080000000',
        'password': "admin"
        }

admin = Admin(**dic)
admin.save()
print(admin.to_dict())
