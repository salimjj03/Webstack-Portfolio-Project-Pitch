#!/usr/bin/python3
"""
"""

from views import app_view
from models import storage
from flask import redirect, url_for, render_template
from flask import session


@app_view.route("/house/<house_id>", strict_slashes=False)
def house(house_id):
    """
    """

    house = storage.find_obj_by_key("House", id=house_id)
    if house is None:
        return "None"

    agent = None
    tenant = None
    occ_house = None
    status = "Un occupied"
    path = session.get("role")

    if path == "Admin":
        path = "/admin"
    elif path == "Tenant":
        path = "/tenant"
    elif path == "Agent":
        path = "/agent"

    agent = storage.find_obj_by_key(
                "Agent",
                id=house.agent_id
                )
    if house.occufied_id is not None:
        occ_house = storage.find_obj_by_key(
                "Occufied_house",
                id=house.occufied_id
                )
        status = "Occupied"

        tenant = storage.find_obj_by_key(
                "Tenant",
                id=occ_house.tenant_id
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
