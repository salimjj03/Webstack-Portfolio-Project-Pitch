#!/usr/bin/python3
"""
"""

from views import app_view
from flask import render_template, session, jsonify
from flask import redirect, url_for
from models import storage


@app_view.route("/agent", strict_slashes=False)
def agent():
    """
    this route return the agent dashboard
    """
    
    if session.get("role") != "Agent":
        return redirect(url_for("app_view.login"))
    user = storage.find_obj_by_key("Agent", email=session["email"])
    return render_template("agent.html", user=user)

@app_view.route(
        "/agent/approve_payment/<occupied_id>",
        strict_slashes=False
        )
def approve_payment(occupied_id):
    """
    this route is used to approve payment
    """

    agent = storage.find_obj_by_key("Agent", email=session["email"])
    status = agent.approve_payment(occupied_id)
    if status == True:
        house = storage.find_obj_by_key(
                "House",
                occufied_id=occupied_id
                )
        return redirect(url_for("app_view.house", house_id=house.id))
    return status

@app_view.route(
        "/agent/cancel_payment/<occupied_id>",
        strict_slashes=False
        )
def cancel_payment(occupied_id):
    """
    this route is used to cancel payment
    """

    agent = storage.find_obj_by_key("Agent", email=session["email"])
    status = agent.cancel_payment(occupied_id)
    if status == True:
        house = storage.find_obj_by_key(
                "House",
                occufied_id=occupied_id
                )
        return redirect(url_for("app_view.house", house_id=house.id))
    return status

