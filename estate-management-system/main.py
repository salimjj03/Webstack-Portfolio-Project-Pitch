#!/usr/bin/python3
"""
test module
"""

from models import storage
from models.user import User
from models.agent import Agent
from models.house import House
from models.tenant import Tenant
from models.occufied_house import Occufied_house


dic = {
        'full_name': 'sssssalim',
        'user_name': 'sssssliyu',
        'email': "sssalmsssaliyu1992@gmail.com",
        'phone_no': 's8s0sss33176562',
        'password': "555",
        'agent_id': 'e65b91f1-7f1c-4ff4-9d80-e369511f6462',
        'tenant_id': '0851e408-48b2-487a-b9dc-87c2dea104a4',
        'house_id': 'a9e40b26-7dee-430f-9919-21de7a5951a3'
        }


obj = Occufied_house(**dic)
pass_w = {"password": "ss"}
obj.save()
print(obj.all())
print(obj.update(**pass_w))
print(obj.to_dict())

