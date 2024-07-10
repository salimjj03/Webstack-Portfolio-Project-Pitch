#!/usr/bin/python3
"""
"""

from views import app_view
from flask import render_template, session, jsonify
from flask import redirect, url_for, request
from models import storage
from models.admin import Admin
from models.agent import Agent
from models.utill import Utill


@app_view.route("/admin", strict_slashes=False)
def admin():
    """
    """

    if session.get("role") != "Admin":
        return redirect(url_for("app_view.login")) 
    user = storage.find_obj_by_key("Admin", email=session["email"])
    return render_template("admin.html", user=user)


@app_view.route(
        "/admin/add_agent",
        methods=["GET", "POST"],
        strict_slashes=False
        )
def add_agent():
    """
    """
    
    user = storage.find_obj_by_key(
                "Admin",
                email=session["email"]
                )

    if request.method == "GET":
        return render_template("add_agent.html", user=user)

    if request.method == "POST":
        data = request.form

        status = Utill.is_key_exist(**data)
        if status is not False:
            return render_template(
                    "add_agent.html",
                    user=user, f_status=status
                    )
        if data["role"] == "1":
            admin = Admin(**data)
            admin.save()
            status = "{} added successufully".format(admin.full_name)
            return render_template(
                    "add_agent.html",
                    user=user, s_status=status
                    )
        elif data["role"] == "2":
            agent = Agent(**data)
            agent.save()
            status = "{} added successufully".format(agent.full_name)
            return render_template(
                    "add_agent.html",
                    user=user, s_status=status
                    )
