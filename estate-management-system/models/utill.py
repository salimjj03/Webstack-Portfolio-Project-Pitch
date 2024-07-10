#!/usr/bin/python3
"""
"""

from models import storage

class Utill():
    """
    """
    
    @classmethod
    def is_valid_user(cls, email, password):
        """
        """

        if email is not None and password is not None:
            user = storage.find_obj_by_key("Admin", email=email)
            if user is None:
                user = storage.find_obj_by_key("Agent", email=email)
                if user is None:
                    user = storage.find_obj_by_key("Tenant", email=email)
                    if user is None:
                        return None

            if user.password == password:
                return user
        return None

    @classmethod
    def is_key_exist(cls, **kwarg):
        """
        """
        
        ls = ["email", "phone_no", "user_name"]
        for key in ls:
            if key not in kwarg:
                continue
            dic = {key: kwarg.get(key)}
            user = storage.find_obj_by_key("Admin", **dic)
            if user is not None:
                return "{} exist".format(key)
            user = storage.find_obj_by_key("Agent", **dic)
            if user is not None:
                return "{} exist".format(key)
            user = storage.find_obj_by_key(
                            "Tenant",
                            **dic
                            )
            if user is not None:
                return "{} exist".format(key)

        return False


