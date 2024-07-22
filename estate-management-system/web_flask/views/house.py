#!/usr/bin/python3
"""
"""

from views import app_view
from models import storage
from flask import redirect, url_for, render_template
from flask import session


@app_view.route("/house", strict_slashes=False)
@app_view.route("/house/<house_id>", strict_slashes=False)
def house(house_id=None):
    """
    """
    
    if house_id == None:
        return "ok"

    agent = None
    tenant = None
    occ_house = None
    status = "Unoccupied"


    path = session.get("role")

    if path == "Admin":
        path = "/admin"
    elif path == "Tenant":
        path = "/tenant"
    elif path == "Agent":
        path = "/agent"


    house = storage.find_obj_by_key("House", id=house_id)
    if house is None:
        occ_house = storage.find_obj_by_key("Occufied_house", id=house_id)
        if occ_house is None:
            occ_house = storage.find_obj_by_key("Rent_history", id=house_id)
        if occ_house is None:
            return "None"
        else:
            house = storage.find_obj_by_key("House", id=occ_house.house_id)

    else:
        if house.occufied_id is not None:
            occ_house = storage.find_obj_by_key(
                    "Occufied_house",
                    id=house.occufied_id
                    )

    if occ_house is not None:
        tenant = storage.find_obj_by_key(
            "Tenant",
            id=occ_house.tenant_id
            )
        if occ_house.__class__.__name__ == "Rent_history":
            status = "Expired"
        else:
            status = "Occupied"

    agent = storage.find_obj_by_key(
                "Agent",
                id=house.agent_id
                )

    if session.get("role") == "Tenant":
        return render_template(
        "tenant_house.html",
        house=house,
        tenant=tenant,
        status=status,
        agent=agent,
        occ_house=occ_house,
        path=path
        )

    return render_template(
            "house.html",
            house=house,
            tenant=tenant,
            status=status,
            agent=agent,
            occ_house=occ_house,
            path=path
            )
