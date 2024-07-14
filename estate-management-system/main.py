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



#print(storage.occufied())


dic = {
        'full_name': 'salim aliyu',
        'user_name': 'jj',
        'email': "salemaliyu1992@gmail.com",
        'phone_no': '08055760736',
        'password': "1234"
        #'agent_id': 'e65b91f1-7f1c-4ff4-9d80-e369511f6462',
        #'tenant_id': '0851e408-48b2-487a-b9dc-87c2dea104a4',
        #'house_id': 'a9e40b26-7dee-430f-9919-21de7a5951a3'
        }

agen = Admin(**dic)
agen.save()
#print(agen.to_dict())
#ten = Tenant(**dic)
#ten.save()
#print(ten.to_dict())
"""
hos = {
        'price': '80,000',
        'location': "fagoji oppsite sauki clinic dutse, jigawa",
        "house_type": "2 bed Room plat"
        #"agent_id": "a31ad593-a3ea-4f2d-ac82-2faaf9791c5a",
        #"tenant_id": "74441f75-e0ef-4f2a-8788-f90fa2d4f937"
        }
"""

#ad = storage.find_obj_by_key(Agent, id="415fa77f-ad8d-4cb0-afd9-47c3951bb2d3")
#te = storage.find_obj_by_key(Tenant, id="88c03360-6949-4ad9-9563-f43b863021bb")

#print(te.active_rent())
#print(te.roll_over("3083949a-b785-459d-ae2a-56333c219b10"))
#te.cancel_reservation("9ce9b397-3175-4813-bcb5-da50a62fcaa8")
#print(ad.occufied())


#obj = House(**hos)
#pass_w = {"password": "ss"}
#obj.save()
#print(obj.to_dict())


#print(ad.un_occufied())

#ad.update(Agent, "a31ad593-a3ea-4f2d-ac82-2faaf9791c5a", phone_no="9999999")

#ad.add_house(**hos)
#print(ad.reserve_house(house_id="f71959f3-5da6-4b5f-929a-35b4f8f39ab6"))

##print(obj.all())
##print(obj.update(**pass_w))
##print(obj.to_dict())

