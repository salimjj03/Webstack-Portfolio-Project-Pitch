#!/usr/bin/python3
"""
"""

from views import app_view
from flask import Flask, render_template, make_response, request
from flask import session, redirect, url_for, abort, jsonify
from models import storage
from models.utill import Utill
from models.tenant import Tenant


@app_view.route("/tenant", strict_slashes=False)
def tenant():
    """
    """

    tenant = storage.find_obj_by_key(
            "Tenant",
            email=session.get("email")
            )

    active_ren = tenant.active_rent()

    return render_template("tenant.html", user=tenant, houses=active_ren)

@app_view.route("/tenant/available_house", strict_slashes=False)
def available_house():
    """
    """

    tenant = storage.find_obj_by_key(
            "Tenant",
            email=session.get("email")
            )

    houses = storage.find_many_by_key("House", occufied_id=None)
    return render_template(
            "available_house.html",
            user=tenant,
            houses=houses
            )

@app_view.route(
        "/tenant/reserve_house/<house_id>",
        strict_slashes=False
        )
def reserve_house(house_id):
    """
    """

    tenant = storage.find_obj_by_key(
            "Tenant",
            email=session.get("email")
            )

    occ_house = tenant.reserve_house(house_id)
    if occ_house is False:
        return ("Sorry, you cannot make another reservation.You have pending payment. Please make the payment soyou can reserve more. Thank you")
    
    occ_house.save()
    return redirect(url_for("app_view.house", house_id=house_id))

@app_view.route(
        "/tenant/cancel_reservation/<occupied_id>",
        strict_slashes=False
        )
def cancel_reservation(occupied_id):
    """
    """

    tenant = storage.find_obj_by_key(
            "Tenant",
            email=session.get("email")
            )

    status = tenant.cancel_reservation(occupied_id)
    if status == True:
        return redirect(url_for("app_view.tenant"))
    return status


@app_view.route(
        "/tenant/roll_over/<occupied_id>",
        strict_slashes=False
        )
def roll_over(occupied_id):
    """
    """

    tenant = storage.find_obj_by_key(
            "Tenant",
            email=session.get("email")
            )

    roll = tenant.roll_over(occupied_id)
    if roll is True:
        return redirect(url_for("app_view.tenant"))
    return roll


@app_view.route(
        "/add_tenant",
        methods=["GET", "POST"],
        strict_slashes=False)
def add_tenant():
    """
    """

    if request.method == "GET":
        return render_template("add_tenant.html")

    elif request.method == "POST":
        data = request.form

        status = Utill.is_key_exist(**data)
        if status is not False:
            return render_template("add_tenant.html", f_status=status)

        tenant = Tenant(**data)
        tenant.role = 3
        tenant.save()
        return redirect(url_for("app_view.login"))

