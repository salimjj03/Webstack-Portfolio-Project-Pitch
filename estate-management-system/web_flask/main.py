#!/usr/bin/env python3
"""
test module
"""

from models import storage
from models.user import User

dic = {
        'f_name': 'salim',
        'l_name': 'aliyu',
        'email': "salemaliyu1992@gmail.com",
        'phone_no': '08033176562',
        'password': "jj"
        }


obj = User(**dic)
print(obj.id)
print(obj.to_dict())
storage.save(obj)

